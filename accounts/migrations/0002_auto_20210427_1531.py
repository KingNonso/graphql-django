# Generated by Django 3.2 on 2021-04-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, help_text='Enter birthday in DD-MM-YYYY format ', null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='Write in international phone no format (+234 or +41)', max_length=255, null=True, unique=True, verbose_name='Phone Number'),
        ),
    ]