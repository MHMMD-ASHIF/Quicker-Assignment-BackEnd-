# Generated by Django 4.1.1 on 2023-01-08 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickerApp', '0003_alter_shoplist_shopimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoplist',
            name='ShopImage',
        ),
    ]