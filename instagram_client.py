from instagrapi import Client
import bot_config

cl = Client()
cl.login(bot_config.INSTAGRAM_USERNAME, bot_config.INSTAGRAM_PASSWORD)

def upload_post(image_path, caption):
    cl.photo_upload(image_path, caption)

def get_followers_count():
    return len(cl.user_followers(cl.user_id))

def get_inactive_users():
    followers = cl.user_followers(cl.user_id)
    return [u.username for u in followers.values() if u.media_count == 0]