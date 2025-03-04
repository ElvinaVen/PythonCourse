from datetime import timedelta

from rest_framework.exceptions import ValidationError


class AssociatedWithoutRewardValidator:
    """
    Исключаем одновременный выбор связанной привычки и указания вознаграждения.
    """
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, habit):
        if habit.get('associated_habit') and habit.get('surprise'):
            raise ValidationError(f'В модели не должно быть заполнено одновременно и поле вознаграждения,'
                                  f' и поле связанной привычки. Можно заполнить только одно из двух полей.')


class LeadTimeValidator:
    """
    Время выполнения должно быть не больше 120 секунд.
    """

    duration_time = timedelta(seconds=120)

    def __init__(self, field1):
        self.field1 = field1

    # def __call__(self, habit):
        # if habit.get('time_to_complete') and habit.get('time_to_complete') > 120:
        #     raise ValidationError('Время выполнения должно быть не больше 120 секунд.')
        # if habit.get('time_to_complete') and habit.get('time_to_complete') > self.duration_time.total_seconds():
        #     raise ValidationError('Время выполнения должно быть не больше 120 секунд.')

    def __call__(self, habit):
        time_to_complete = habit.get('time_to_complete')
        print(time_to_complete)

        if time_to_complete is not None:  # Проверяем, что значение не None
            # Преобразуем time_to_complete в секунды
            total_seconds = time_to_complete.hour * 3600 + time_to_complete.minute * 60 + time_to_complete.second

            if total_seconds > self.duration_time.total_seconds():
                raise ValidationError('Время выполнения должно быть не больше 120 секунд.')


class NiceHabitInAssociatedValidator:
    """
    В связанные привычки могут попадать только привычки с признаком приятной привычки.
    """
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, habit):
        if habit.get('associted_habit'):
            if not habit.get('nice_habit'):
                raise ValidationError(f'В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class NiceHabitWithoutValidator:
    """
    У приятной привычки не может быть вознаграждения или связанной привычки.
    """
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, habit):
        if habit.get('nice_habit'):
            if habit.get('surprise') or habit.get('associted_habit'):
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


class PeriodicityValidator:
    """
    Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
    """
    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, habit):
        periodicity = habit.get('periodicity')
        if 7 < periodicity or periodicity < 1:
            raise ValidationError(f'За одну неделю необходимо выполнить привычку хотя бы один раз.')
