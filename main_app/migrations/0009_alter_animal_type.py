# Generated by Django 3.2.7 on 2021-09-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_newuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='type',
            field=models.CharField(choices=[('DOG', 'Dog'), ('CAT', 'Cat'), ('REPTILE', 'Reptile'), ('BIRD', 'Bird')], default='DOG', max_length=50, verbose_name='Type'),
        ),
    ]