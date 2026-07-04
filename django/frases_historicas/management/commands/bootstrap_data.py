import os
from pathlib import Path

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction

from frases_historicas.models import FraseHistorica


class Command(BaseCommand):
    help = "Load historical phrases fixture when the database is empty"

    def handle(self, *args, **options):
        if FraseHistorica.objects.exists():
            self.stdout.write(self.style.WARNING("Historical phrases already exist; skipping fixture load."))
            return

        fixture_path = Path(__file__).resolve().parents[2] / "fixtures" / "frases_historicas.json"
        if not fixture_path.exists():
            self.stdout.write(self.style.ERROR(f"Fixture file not found: {fixture_path}"))
            return

        with transaction.atomic():
            call_command("loaddata", str(fixture_path))

        self.stdout.write(self.style.SUCCESS("Historical phrases fixture loaded successfully."))
