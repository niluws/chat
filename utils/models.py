from uuid import uuid4

from django.db import models
from django.utils import timezone


class AbstracId(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid4)
    create_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
