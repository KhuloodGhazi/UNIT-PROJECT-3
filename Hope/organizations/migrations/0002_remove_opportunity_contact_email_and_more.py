# Generated by Django 5.1.3 on 2024-11-30 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='contact_phone',
        ),
    ]
