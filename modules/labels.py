from enum import Enum


class Labels(Enum):
    CALCULATED = "{boy_name} сумісний з {girl_name} на {percent}%"
    UNDEFINED: str = "Невідомий статус ¯\\_(ツ)_/¯"
    GIRL_NAME: str = "Ім'я дівчини"
    BOY_NAME: str = "Ім'я хлопця"

    CALCULATE_LOVE: str = "Розрахувати любов"

    def __str__(self) -> str:
        return self.value
