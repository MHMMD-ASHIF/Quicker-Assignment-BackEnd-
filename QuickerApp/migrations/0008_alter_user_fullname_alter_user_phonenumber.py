# Generated by Django 4.1.1 on 2023-01-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickerApp', '0007_user_auth_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='FullName',
            field=models.CharField(blank=True, max_length=240),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
