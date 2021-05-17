const functions = require('firebase-functions');
const admin = require('firebase-admin');
const sdkJSON = require('./keys/mlops-crawler-firebase.json');
admin.initializeApp(sdkJSON);

exports.scheduledFunction =
  functions.pubsub.schedule('0 0 * * *').timeZone('Asia/Seoul').onRun((context) => {
    console.log('Run it everyday at 00:00');
    return;
  });


exports.addMessage = functions.https.onRequest(async (req, res) => {
  // Grab the text parameter.
  const original = req.query.text;
  // Push the new message into Firestore using the Firebase Admin SDK.
  const writeResult = await admin.firestore().collection('messages').add({ original: original });
  // Send back a message that we've successfully written the message
  res.json({ result: `Message with ID: ${writeResult.id} added.` });
});

exports.preprocess = functions.database.ref('/raw').onCreate(async (snapshot, context) => {
  const value = snapshot.val();
  // TODO: preprocess here
  admin.database().ref('/preprocessed').update(value);
});