from django.apps import AppConfig


class FoodDonerConfig(AppConfig):
    name = 'food_doner'

    def ready(self):
        import food_doner.signals
