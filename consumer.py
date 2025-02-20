from google.cloud import pubsub_v1
from config import Config

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(Config.GOOGLE_CLOUD_PROJECT, Config.PUBSUB_SUBSCRIPTION)

def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    # Process the message here (e.g., update the database, trigger a workflow, etc.)
    message.ack()

def listen_for_messages():
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}...")
    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()

if __name__ == '__main__':
    listen_for_messages()