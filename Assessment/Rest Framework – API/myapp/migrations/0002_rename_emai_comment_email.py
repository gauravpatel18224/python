# Generated by Django 5.0.6 on 2024-06-17 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='emai',
            new_name='email',
        ),
    ]
