import os
from random import choice
from img_data import img, save_imgs
from user import get_used_photos, set_used_photos

print(os.listdir())
photos_dirs = os.listdir("photos/")
last_photos_dirs = photos_dirs.copy()


def get_all_photos():
    return ["photos/" + x for x in photos_dirs]


def save_new_img(photo, img):
    photo_img = {
        "name": img,
        "keywords": []
    }
    img[photo] = photo_img
    save_imgs()


def get_randoms(user_id, number):
    random_photos = []
    total_last = len(photos_dirs) - len(get_used_photos(user_id))
    if number > total_last:
        number = total_last
    while len(random_photos) != number:
        random_photo = choice(photos_dirs)
        if random_photo in get_used_photos(user_id):
            continue
        random_photos.append(random_photo)
        set_used_photos(user_id, [random_photo])
    return random_photos
