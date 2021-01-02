from django.apps import AppConfig


class NurseryConfig(AppConfig):
    name = 'nursery'
    
    def ready(self):
        import nursery.signals