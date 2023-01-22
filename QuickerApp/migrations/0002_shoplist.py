# Generated by Django 4.1.1 on 2023-01-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShopName', models.CharField(max_length=100)),
                ('ShopAddress', models.CharField(max_length=350)),
                ('ShopCity', models.CharField(max_length=50)),
                ('ShopPhone', models.CharField(max_length=25)),
                ('ShopImage', models.ImageField(blank=True, upload_to='pictures')),
                ('ShopImageName', models.CharField(max_length=100)),
            ],
        ),
    ]
