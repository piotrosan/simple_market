from django.db import models


class WorkingSpace(models.Model):
    name = models.CharField(
        max_length=255,
        default='Working Space'
    )
    configuration = models.JSONField()
