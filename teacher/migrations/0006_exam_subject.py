# Generated by Django 4.1.7 on 2023-04-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_alter_questionpaper_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='Subject',
            field=models.CharField(default='Computer Science', max_length=100, null=True),
        ),
    ]
