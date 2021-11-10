# Generated by Django 3.2.9 on 2021-11-09 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('embeds', '0002_auto_20211109_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embed',
            name='last_modification_by',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_editor', to=settings.AUTH_USER_MODEL),
        ),
    ]
