require('dotenv').config();
const functions = require('firebase-functions');
const admin = require('firebase-admin');
const axios = require('axios');

const config = JSON.parse(process.env.FIREBASE_CONFIG);
admin.initializeApp(config);

const PREPROCESS_ENDPOINT = 'https://master-korean-preprocessor-api-dleunji.endpoint.ainize.ai/preprocess';

// exports.scheduledFunction =
//   functions.pubsub.schedule('0 0 * * *').timeZone('Asia/Seoul').onRun((context) => {
//     console.log('Run it everyday at 00:00');
//     return;
//   });

exports.preprocess = functions.database.ref('raw').onUpdate(async (change, context) => {
  const value = change.after.val();
  const key = Object.keys(value)[0];
  const text = value[key].document;
  const response = await axios.post(
    PREPROCESS_ENDPOINT,
    {
      "text": text,
      "emoticon_normalize": false,
      "repeat_normalize": true,
      "only_hangle": false,
      "only_hangle_number": false,
      "only_text": true,
      "num_repeats1": 2,
      "num_repeats2": 0
    }
  );
  const data = response.data;
  admin.database().ref('preprocessed').update({ [key]: data });
});
