# Generated by Django 3.1.1 on 2020-09-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20200910_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]