# Generated by Django 4.1.3 on 2023-05-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0003_remove_note_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(null=True),
        ),
    ]
