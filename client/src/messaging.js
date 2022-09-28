import { getMessaging, getToken, onMessage } from "firebase/messaging";
import { initializeApp } from "firebase/app";

const firebaseConfig = JSON.parse(process.env.REACT_APP_FIREBASE_CONFIG);

const firebaseApp = initializeApp(firebaseConfig);
const messaging = getMessaging(firebaseApp);

function requestPermission() {
	console.log("Requesting permission...");
	return Notification.requestPermission().then((permission) => {
		if (permission === "granted") {
			console.log("Notification permission granted.");
			return true;
		} else {
			console.log("Notification permission rejected.");
			return false;
		}
	});
}

function getClientToken() {
	console.log(process.env.REACT_APP_VAPID_KEY);
	getToken(messaging, {
		vapidKey: process.env.REACT_APP_VAPID_KEY,
	})
		.then((currentToken) => {
			if (currentToken) {
				// Send the token to your server and update the UI if necessary
				// this token will be used to identify this client when sending messages to it from
				//
				console.log("Current Token", currentToken);
			} else {
				// Show permission request UI
				console.log(
					"No registration token available. Request permission to generate one."
				);
				// ...
			}
		})
		.catch((err) => {
			console.log("An error occurred while retrieving token. ", err);
			// ...
		});
}

requestPermission().then((permitted) => {
	if (permitted) {
		getClientToken();
	}
});

onMessage(messaging, (payload) => {
	console.log("Message received. ", payload);
	// ...
});
