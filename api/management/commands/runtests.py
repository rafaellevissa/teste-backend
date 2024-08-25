from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Apply migrations and then run tests"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Applying migrations..."))
        call_command("migrate", verbosity=1, interactive=False)

        self.stdout.write(self.style.SUCCESS("Running tests..."))
        call_command("test")
