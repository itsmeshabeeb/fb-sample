# Generated by Django 3.2.7 on 2021-12-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=20)),
                ('email_phone', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=5)),
            ],
        ),
    ]
