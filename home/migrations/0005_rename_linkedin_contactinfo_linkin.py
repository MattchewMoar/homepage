# Generated by Django 4.1.3 on 2023-01-03 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contactinfo_facebook_alter_bio_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='linkedin',
            new_name='linkin',
        ),
    ]