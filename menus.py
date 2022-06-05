from photos import get_randoms
from keyboard import RED, bake_keyboard, button
from menu import Menu, register_menu
from user import set_user_menu, set_used_photos
from vk import send_message, send_photos
import config


@register_menu
class MainMenu(Menu):
    def __init__(self, user_id):
        super().__init__(user_id)
        buttons = [[button(config.startButton)]]
        keyboard = bake_keyboard(buttons)
        send_message(user_id, config.welcome, keyboard)
        self.user_id = user_id

    def on_message(self, msg):
        if msg == config.startButton.lower():
            print(get_randoms(self.user_id, 5))
            send_photos(self.user_id, get_randoms(self.user_id, 5))
            #set_user_menu(self.user_id, StartMenu(self.user_id))
        else:
            super().on_message(msg)


@register_menu
class BaseMenu(Menu):
    def __init__(self, user_id, msg, keys=[]):
        super().__init__(user_id)
        keyboard = bake_keyboard(keys)
        send_message(user_id, msg, keyboard)

    def on_message(self, msg):
        super().on_message(msg)


@register_menu
class StartMenu(BaseMenu):
    def __init__(self, user_id):
        set_used_photos(user_id, [])
        send_photos(user_id, get_randoms(user_id, 5))
        buttons = [[]]
        super().__init__(user_id, "lol", buttons)

    def on_message(self, msg):
        if msg == feederConfig.checkTrigger:
            set_user_menu(self.user_id, FeederCheckState(self.user_id))
        elif msg == config.settingsTrigger:
            set_user_menu(self.user_id, FeederSettingsMenu(self.user_id))
        elif msg == feederConfig.commandsTrigger:
            set_user_menu(self.user_id, FeederCommandsMenu(self.user_id))
        else:
            super().on_message(msg)
