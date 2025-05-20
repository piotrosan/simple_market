from django.db import models
from django.utils import timezone


class CreatedUpdatedMixin:
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
