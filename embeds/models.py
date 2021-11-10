from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, URLField
from django.conf import settings
import datetime

# Create your models here.

PLATFORMS = (
    ('YouTube', 'YouTube'),
    ('Vimeo', 'Vimeo'),
)

class Embed(models.Model):
    title = CharField(max_length=200, default="Evento Sin Nombre")
    event_url = URLField(max_length=200)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='creator')
    creation_date = DateTimeField(auto_now_add=True)
    last_modification_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='last_editor')
    last_modification = DateTimeField(auto_now=True)
    platform = CharField(max_length=20, choices=PLATFORMS)

class Modification(models.Model):
    previous_title = models.ForeignKey(Embed, on_delete=CASCADE, related_name='previous_name', null=True)
    new_title = CharField(max_length=200, default="Evento Sin Nombre " + str(datetime.datetime.now()))
    previous_url = URLField(max_length=200)
    new_url = URLField(max_length=200)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='editor')
    modification_date = DateTimeField(auto_now_add=True)