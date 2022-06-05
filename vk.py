import vk_api
import os
# from dotenv import load_dotenv
from photos import get_all_photos, save_new_img
from img_data import imgs


load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

vk = vk_api.VkApi(token=API_TOKEN)
upload = vk_api.VkUpload(vk)


def send_message(user_id, msg, keyboard=None):
    request = {
        "user_id": int(user_id),
        "message": msg,
        "random_id": 0,
    }
    if keyboard is not None:
        request["keyboard"] = keyboard
    vk.method("messages.send", request)


def send_keyboard(user_id, keyboard=None):
    request = {
        "user_id": int(user_id),
        "message": '',
        "random_id": 0
    }
    if keyboard is not None:
        request["keyboard"] = keyboard
    vk.method("messages.send", request)


def upload_photos():
    for photo_dir in get_all_photos():
        if photo_dir in imgs.keys():
            continue
        print(photo_dir)
        photo = upload.photo_messages(photo_dir)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        save_new_img(photo_dir, attachment)


def send_photos(user_id, imgs):
    attachments = ''
    for img in imgs:
        attachments += img + ','
    request = {
        "user_id": int(user_id),
        "random_id": 0,
        "attachment": attachments
    }
    vk.method("messages.send", request)
