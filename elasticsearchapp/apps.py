from django.apps import AppConfig


class ElasticsearchappConfig(AppConfig):
    name = 'elasticsearchapp'

    def ready(self):
        import elasticsearchapp.signals