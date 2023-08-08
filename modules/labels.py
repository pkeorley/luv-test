from enum import Enum


class Languages(Enum):
    EN: str = "en"
    UK: str = "uk"

    def __str__(self):
        return self.value


class Labels:
    def __init__(self):
        self.translations = {
            "en": {
                "CALCULATED": "{boy_name} is {percent}% compatible with {girl_name}",
                "UNDEFINED": "Unknown status ¯\\_(ツ)_/¯",
                "GIRL_NAME": "Girl's name",
                "BOY_NAME": "Boy's name"
            },
            "uk": {
                "CALCULATED": "{boy_name} на {percent}% сумісний з {girl_name}",
                "UNDEFINED": "Невідомий статус ¯\\_(ツ)_/¯",
                "GIRL_NAME": "Ім'я дівчини",
                "BOY_NAME": "Ім'я хлопця"
            },
            "es": {
                "CALCULATED": "{boy_name} es {percent}% compatible con {girl_name}",
                "UNDEFINED": "Estado desconocido ¯\_(ツ)_/¯",
                "GIRL_NAME": "Nombre de chica",
                "BOY_NAME": "Nombre de chico"
            }
        }

    @property
    def available_languages(self):
        return list(self.translations.keys())

    def get_translation(self, language: Languages):
        return self.translations.get(str(language), {})

    def get(self, language: Languages, key: str):
        return self.get_translation(language).get(key)
