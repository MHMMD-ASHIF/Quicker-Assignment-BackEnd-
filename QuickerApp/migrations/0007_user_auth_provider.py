# Generated by Django 4.1.1 on 2023-01-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickerApp', '0006_remove_user_auth_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_provider',
            field=models.CharField(default='email', max_length=255),
        ),
    ]