# FCM Notification System PoC

## Program Flow

- [Client] Get user permission to show notifications using the `Notification.requestPermission()` notification api function
- [Client] Get client token and send to server using `getToken()` function from `firebase/messaging`
- [Client] Listen for messages using the `onMessage()` listener from `firebase/messaging`
- [Server] Take client token and store in database (associating it with a user is best)
- [Server] **Send notification to single user:**
  - create a `firebase_admin.messaging.Message` object passing the `notification`, `token` (client token associated with the user), `data`
  - use the `firebase_admin.messaging.send()` function to send the message
- [Server] **Send notification to multiple users:**
  - subscribe the users (via their associated client tokens) to a specific topic
  - create a `firebase_admin.messaging.Message` object, passing the `topic`
  - use the `firebase_admin.messaging.send()` function to send the message
