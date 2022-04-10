from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    name = 'payments'

    def ready(self):
        # import signal handlers
        import payments.signals
