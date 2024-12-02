from kivy.app import App
from kivy.uix.widget import Widget
from random import choice
from kivy.properties import ObjectProperty


class Lucky(Widget):
    numbers = ObjectProperty(None)

    def lucky(self):
        result = ""
        pres = list(range(1, 35))
        suffix = list(range(1, 12))
        for _ in range(5):
            lucky_one = choice(pres)
            if lucky_one < 10:
                lucky_one = "0" + str(lucky_one)
            result += str(lucky_one) + "-"
            pres.remove(lucky_one)
        result = result[:-1] + " || "
        for _ in range(2):
            lucky_one = choice(suffix)
            if lucky_one < 10:
                lucky_one = "0" + str(lucky_one)
            result += str(lucky_one) + "-"
            suffix.remove(lucky_one)
        self.numbers.text = result[:-1]


class Money(App):
    def build(self):
        return Lucky()
