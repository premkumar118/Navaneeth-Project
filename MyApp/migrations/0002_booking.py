# Generated by Django 3.2.10 on 2024-03-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Train', models.CharField(default='', max_length=50)),
                ('Number', models.CharField(default='', max_length=50)),
                ('Date', models.CharField(default='', max_length=50)),
                ('BookingNumber', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
