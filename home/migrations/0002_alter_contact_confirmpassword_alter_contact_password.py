# Generated by Django 5.1.2 on 2024-11-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='confirmpassword',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='contact',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
