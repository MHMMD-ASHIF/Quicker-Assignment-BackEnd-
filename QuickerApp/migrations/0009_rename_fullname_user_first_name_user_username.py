# Generated by Django 4.1.1 on 2023-01-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickerApp', '0008_alter_user_fullname_alter_user_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='FullName',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
