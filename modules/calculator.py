from fuzzywuzzy.fuzz import ratio


class Calculator:
    @classmethod
    def calculate(cls, boy_name: str, girl_name: str) -> float:
        return ratio(boy_name.lower(), girl_name.lower())

