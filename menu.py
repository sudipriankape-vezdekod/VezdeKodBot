from vk import send_message

menus = {}


def register_menu(menu):
    menus[menu.__name__] = menu
    return menu


def serialize_menu(menu):
    return {
        "menu": menu.__class__.__name__,
        "state": menu.save_state()
    }


def deserialize_menu(serialized, user_id):
    menu_class = menus[serialized["menu"]]
    state = serialized["state"]
    menu = menu_class.__new__(menu_class)
    Menu.__init__(menu, user_id)
    menu.load_state(state)
    return menu


class Menu:
    def __init__(self, user_id):
        self.user_id = user_id
        self.used_photos = []

    def on_message(self, _):
        send_message(self.user_id, "Неизвестная команда")

    def load_state(self, state):
        for k, v in state.items():
            self.__setattr__(k, v)

    def save_state(self):
        dict = self.__dict__.copy()
        if 'timer' in dict:
            dict.pop('timer')
        return dict
