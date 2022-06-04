from user import get_user_menu, set_user_menu, set_used_photos
from vk import vk, upload_photos
from menus import MainMenu
from vk_api.longpoll import VkLongPoll, VkEventType
from keyboard import bake_keyboard, button


upload_photos()


def process_event(event):
    if event.type != VkEventType.MESSAGE_NEW or not event.to_me:
        return
    msg = event.text.lower()
    user_id = str(event.user_id)
    menu = get_user_menu(user_id)
    if menu is None:
        menu = MainMenu(user_id)
        set_user_menu(user_id, menu)
        set_used_photos(user_id)
    else:
        menu.on_message(msg=msg)


while True:
    for event in VkLongPoll(vk).check():
        process_event(event)
