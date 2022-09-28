from firebase_admin import messaging, initialize_app


default_app = initialize_app() # requires that the `GOOGLE_APPLICATION_CREDENTIALS` env var has been set

# These registration tokens come from the client FCM SDKs.

def subscribe_tokens(tokens, topic):
    response = messaging.subscribe_to_topic(tokens, topic)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    print(response.success_count, 'tokens were subscribed successfully')

def send_notification_to_topic(topic):
    message = messaging.Message(
        topic=topic,
        notification=messaging.Notification(
            title="Some Test Message", body="Lorem Ipsum Dolor Sit Doloris Sit."
        ),
        data={},
    )

    response = messaging.send(message=message, app=default_app)
    print("Response: ", response)


if __name__ == "__main__":
    # This registration token comes from the client FCM SDKs.
    # ideally to be gotten from DB 
    registration_tokens = [
        # TODO: Add client tokens here
    ]
    topic = "test-topic"
    subscribe_tokens(registration_tokens)
    send_notification_to_topic(topic)
