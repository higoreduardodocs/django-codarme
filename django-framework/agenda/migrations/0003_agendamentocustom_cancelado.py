# Generated by Django 4.2.4 on 2023-09-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_agendamentocustom'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamentocustom',
            name='cancelado',
            field=models.BooleanField(default=False),
        ),
    ]
