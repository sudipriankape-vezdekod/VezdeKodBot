from data import data, save_data
from menu import serialize_menu, deserialize_menu

users = {}


def get_user_menu(user_id):
    if user_id not in users and user_id in data:
        users[user_id] = deserialize_menu(data[user_id], user_id)
    if user_id in users:
        return users[user_id]
    else:
        return None


def get_used_photos(user_id):
    if user_id not in users and user_id in data:
        users[user_id] = deserialize_menu(data[user_id], user_id)
    if user_id in users:
        return users[user_id].used_photos
    else:
        return None


def set_used_photos(user_id, used_photos=[]):
    if user_id not in users and user_id in data:
        users[user_id] = deserialize_menu(data[user_id], user_id)
    if user_id in users:
        users[user_id].used_photos.extend(used_photos)
    save_data()


def set_user_menu(user_id, menu):
    users[user_id] = menu
    data[user_id] = serialize_menu(menu)
    save_data()


def save_user_menu(user_id):
    set_user_menu(user_id, get_user_menu(user_id))
