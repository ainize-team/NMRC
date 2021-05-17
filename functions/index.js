require('dotenv').config();
const functions = require('firebase-functions');
const admin = require('firebase-admin');

const config = JSON.parse(process.env.FIREBASE_CONFIG);
admin.initializeApp(config);

// exports.scheduledFunction =
//   functions.pubsub.schedule('0 0 * * *').timeZone('Asia/Seoul').onRun((context) => {
//     console.log('Run it everyday at 00:00');
//     return;
//   });

exports.preprocess = functions.database.ref('raw').onUpdate(async (change, context) => {
  const value = change.after.val();
  // TODO: preprocess here
  admin.database().ref('preprocessed').update(value);
});
