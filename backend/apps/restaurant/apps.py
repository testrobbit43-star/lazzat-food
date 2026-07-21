from django.apps import AppConfig

class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.restaurant'
    verbose_name = 'Restaurant Management'
    
    def ready(self):
        import apps.restaurant.signals  # noqa
