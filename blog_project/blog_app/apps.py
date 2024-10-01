from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'

from django.apps import AppConfig

class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'

    def ready(self):
        import blog_app.signals  # Importa el archivo de señales

from django.apps import AppConfig

class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'

    def ready(self):
        import blog_app.signals  # Importa las señale