# Generated by Django 3.2.3 on 2021-05-30 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawled_data', '0004_auto_20210530_2009'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BoardData2',
            new_name='BoardData',
        ),
    ]