# Generated by Django 2.2 on 2019-09-29 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='link',
            new_name='slug',
        ),
    ]