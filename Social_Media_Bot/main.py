import facebook
import tweepy
import os
import schedule
import time
import logging

# Logging setup
logging.basicConfig(filename='social_media_bot.log', level=logging.INFO)

# Facebook API credentials
FACEBOOK_APP_ID = "your_app_id"
FACEBOOK_APP_SECRET = "your_app_secret"
FACEBOOK_ACCESS_TOKEN = "your_access_token"

# Twitter API credentials
TWITTER_CONSUMER_KEY = "your_consumer_key"
TWITTER_CONSUMER_SECRET = "your_consumer_secret"
TWITTER_ACCESS_TOKEN = "your_access_token"
TWITTER_ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Facebook API setup
def setup_facebook():
    try:
        graph = facebook.GraphAPI(FACEBOOK_ACCESS_TOKEN)
        logging.info("Facebook API setup successful")
        return graph
    except Exception as e:
        logging.error(f"Facebook API setup failed: {e}")

# Twitter API setup
def setup_twitter():
    try:
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        logging.info("Twitter API setup successful")
        return api
    except Exception as e:
        logging.error(f"Twitter API setup failed: {e}")

# Post update on Facebook and Twitter
def post_update(graph, api, message):
    try:
        graph.put_object(parent_object="me", connection_name="feed", message=message)
        api.update_status(status=message)
        logging.info("Post update successful")
    except Exception as e:
        logging.error(f"Post update failed: {e}")

# Share image on Facebook and Twitter
def share_image(graph, api, image_path):
    try:
        graph.put_photo(image=open(image_path, "rb"), message="Image")
        api.update_with_media(filename=image_path, status="Image")
        logging.info("Image share successful")
    except Exception as e:
        logging.error(f"Image share failed: {e}")

def main():
    graph = setup_facebook()
    api = setup_twitter()

    # Schedule post
    schedule_post(graph, api, "Hello, world!", "10:00")

    # Post analytics
    post_analytics(graph, "post_id")

    # Twitter thread support
    messages = ["Message 1", "Message 2", "Message 3"]
    tweet_thread(api, messages)

    # Facebook story sharing
    story = "This is a story."
    share_story(graph, story)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()