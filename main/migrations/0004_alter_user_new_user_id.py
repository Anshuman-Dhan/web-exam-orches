# Generated by Django 4.1.7 on 2023-04-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_new_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_new',
            name='User_ID',
            field=models.CharField(default='f615683565844dd19f974b405df4d334', max_length=100, unique=True),
        ),
    ]