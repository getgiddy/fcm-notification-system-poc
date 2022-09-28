from firebase_admin import messaging, initialize_app


default_app = initialize_app() # requires that the `GOOGLE_APPLICATION_CREDENTIALS` env var has been set


def send_notification(token):
    message = messaging.Message(
        notification=messaging.Notification(
            title="Some Test Message", body="Lorem Ipsum Dolor Sit Doloris Sit."
        ),
        data={},
        token=token,
    )

    response = messaging.send(message=message, app=default_app)
    print("Response: ", response)


if __name__ == "__main__":
    # This registration token comes from the client FCM SDKs.
    # ideally to be gotten from DB 
    registration_token = "" # TODO: Add client token here
    send_notification(registration_token)
