# Generated by Django 3.1.5 on 2021-01-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20210121_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='google_id',
            field=models.TextField(null=True),
        ),
    ]
