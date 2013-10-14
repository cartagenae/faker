from . import BaseProvider


class Provider(BaseProvider):
    formats = ('###-###-###',)

    @classmethod
    def phone_number(cls):
        return cls.numerify(cls.randomElement(cls.formats))