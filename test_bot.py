import requests


class Bot:

    def __init__(self, user_id):
        self._USER_ID = user_id
        self._COMMANDS = ["привет", "пока"]

    def reply_message(self, message):

        #  привет
        if message.lower() == self._COMMANDS[0]:
            return "Приветствую!"
        #  пока
        elif message.lower() == self._COMMANDS[1]:
            return "Пока-пока~"
        else:
            return "Ничего непонятно, но очень интересно..."
