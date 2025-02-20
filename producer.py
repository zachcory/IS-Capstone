from google.cloud import pubsub_v1
from config import Config

# Initialize the Publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(Config.GOOGLE_CLOUD_PROJECT, Config.PUBSUB_TOPIC)

def publish_message(message: str):
    data = message.encode("utf-8")
    future = publisher.publish(topic_path, data=data)
    print(f"Published message ID: {future.result()}")

if __name__ == '__main__':
    # Example usage: publish a test message
    message = "Hello, Pub/Sub from Producer!"
    publish_message(message)