# Generated by Django 3.1.2 on 2022-10-23 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userdata_user_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='email',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
