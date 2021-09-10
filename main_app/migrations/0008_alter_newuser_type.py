# Generated by Django 3.2.7 on 2021-09-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_newuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='type',
            field=models.CharField(choices=[('MANAGER', 'Manager'), ('EMPLOYEE', 'Employee'), ('OWNER', 'Owner')], default='EMPLOYEE', max_length=50, verbose_name='Type'),
        ),
    ]