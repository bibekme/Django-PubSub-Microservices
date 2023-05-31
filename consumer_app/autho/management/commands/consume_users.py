import json
from django.core.management import BaseCommand

from autho.models import User

from core.redis_client import queue


def consume_user_events():
    queue.subscribe("users")
    print("Consumer Ready. Listening for events...")
    for event in queue.listen():
        data = str(event.get("data") or "")
        data = json.loads(data)
        if isinstance(data, dict):
            if data.get("event_type") == "user-create-or-update":
                KEYS = [
                    "name",
                    "email",
                    "password",
                    "is_obsolete",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "created_on",
                ]
                payload = data.get("payload")
                u = {k: v for k, v in data.get("payload").items() if k in KEYS}
                user, created = User.objects.update_or_create(
                    idx=payload.get("idx"), defaults={**u}
                )
                if created:
                    print(f"User {user} with {user.idx} created successfully")
                else:
                    print(f"User {user} with {user.idx} updated successfully")
            elif data.get("event_type") == "account-deletion":
                user = User.objects.delete(idx=data.get("payload"))
                print(f"User with idx {user.idx} was deleted successfully")


class Command(BaseCommand):
    def handle(self, *args, **options):
        consume_user_events()
