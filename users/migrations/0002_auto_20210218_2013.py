# Generated by Django 2.2.12 on 2021-02-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vyasprofile',
            name='Date_ended',
            field=models.DateField(blank=True, null=True),
        ),
    ]
