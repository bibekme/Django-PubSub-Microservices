from django.core.management import BaseCommand

from autho.models import User

class Command(BaseCommand):
    help = 'Seed a superuser if it does not exist'

    def handle(self, *args, **options):
        user_email = "admin@example.com"
        if not User.objects.filter(email=user_email).exists():
            User.objects.create_superuser(name="Super Admin User", email=user_email, password="password" )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        else:
            self.stdout.write('Superuser already exists.')