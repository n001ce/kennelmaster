# Generated by Django 3.2.7 on 2021-09-08 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210908_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.newuser',),
        ),
    ]