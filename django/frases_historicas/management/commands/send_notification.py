#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from webpush.models import SubscriptionInfo
from webpush.utils import send_to_subscription

class Command(BaseCommand):
    help = 'Envia uma notificação'

    def add_arguments(self, parser):
        parser.add_argument('mensagem', nargs='+', type=str)

    def handle(self, *args, **options):
        errors = []
        success = []
        subscriptions = SubscriptionInfo.objects.all()
        mensagem = ' '.join(options['mensagem'])

        for subscription in subscriptions:
            try:
                send_to_subscription(subscription, mensagem, 0)
            except Exception as exc:
                errors.append((subscription.pk, str(exc)))
            else:
                success.append(subscription.pk)

        self._show_results(success=success, errors=errors)

    def _show_results(self, success, errors):
        self.stdout.write('\n')
        if success:
            self.stdout.write(self.style.SUCCESS(
                'Notificação enviada para os seguintes subscriptions: %s'
                % str(success)
            ))
        if errors:
            self.stdout.write(self.style.ERROR(
                'Notificação falhou para os seguintes subscriptions: %s'
                % str(errors)
            ))
        self.stdout.write('\n')
