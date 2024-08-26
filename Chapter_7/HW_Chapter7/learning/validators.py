from rest_framework.serializers import ValidationError


def validate_youtube(value):

    if "youtube.com" not in value:
        raise ValidationError("Поле  должно ссылаться только на видео с youtube.com")
