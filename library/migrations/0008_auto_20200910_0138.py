# Generated by Django 3.1.1 on 2020-09-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20200910_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='available',
        ),
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
