import json
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from autho.models import User
from autho.serializers import UserSerializer

from core.redis_client import r


def publish_user_event(event_type, payload):
    r.publish("users", json.dumps({"event_type": event_type, "payload": payload}))


@receiver(post_save, sender=User)
def handle_user_create_or_update(sender, instance, *args, **kwargs):
    user = instance
    serializer = UserSerializer(instance=user)
    publish_user_event("user-create-or-update", (serializer.data))


@receiver(post_delete, sender=User)
def handle_user_deletion(sender, instance, *args, **kwargs):
    user = instance
    publish_user_event("account-deletion", user.idx)
