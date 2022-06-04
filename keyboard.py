import json


GREEN = "positive"
RED = "negative"


def button(text, color=GREEN):
    return {
        "action": {
            "type": "text",
            "label": text,
            "payload": "",
        },
        "color": color,
    }


def make_keyboard(buttons, one_time=False, inline=False):
    return {
        "buttons": buttons,
        "one_time": one_time,
        "inline": inline
    }


def bake_keyboard(*args, **kwargs):
    return json.dumps(make_keyboard(*args, **kwargs))
