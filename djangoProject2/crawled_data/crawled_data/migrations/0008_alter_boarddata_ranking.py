# Generated by Django 3.2.3 on 2021-05-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawled_data', '0007_rename_boarddata2_boarddata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boarddata',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
    ]
