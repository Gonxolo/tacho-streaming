# Generated by Django 3.2.9 on 2021-11-09 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('embeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embed',
            name='last_modification',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='embed',
            name='last_modification_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_editor', to=settings.AUTH_USER_MODEL),
        ),
    ]