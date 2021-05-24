# Generated by Django 3.0 on 2021-05-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hd', '0002_auto_20210520_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('otp', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]