# Generated by Django 5.1.3 on 2024-12-03 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="accountId",
            new_name="id",
        ),
    ]