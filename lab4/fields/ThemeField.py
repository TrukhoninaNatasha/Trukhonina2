from lab4.fields.Field import Field
from lab4.fields.exceptions import FieldValidException

THEME_MIN_LENGTH = 0
THEME_MAX_LENGTH = 128


class ThemeField(Field):
    def __init__(self, theme):
        self.set(theme)

    def set(self, theme):
        if not isinstance(theme, str):
            raise FieldValidException("theme must be string")
        if len(theme) not in range(THEME_MIN_LENGTH, THEME_MAX_LENGTH):
            raise FieldValidException(
                "length theme should be from " + str(THEME_MIN_LENGTH) + " to " + str(THEME_MAX_LENGTH))
        self._theme = theme

    def get(self):
        return self._theme