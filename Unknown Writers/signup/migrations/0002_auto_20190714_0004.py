# Generated by Django 2.1 on 2019-07-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupform',
            name='Email',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='signupform',
            name='Name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='signupform',
            name='Password',
            field=models.CharField(max_length=14),
        ),
    ]