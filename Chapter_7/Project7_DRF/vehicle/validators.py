import re

from rest_framework.serializers import ValidationError


class TitleValidator(object):
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile("^[a-zA-Z0-9.\- ]+$")
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):  # усли есть знаки,то false. если нет то true
            raise ValidationError("название содержит недопустимые символы")
