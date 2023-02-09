# Generated by Django 4.1.5 on 2023-02-09 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tackler', '0006_rename_topic_ticket_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assigned_users',
            field=models.ManyToManyField(related_name='assigned_tickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
