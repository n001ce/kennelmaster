# Generated by Django 3.2.7 on 2021-09-07 22:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_date', models.DateField(verbose_name='Employment Start')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('p_num', models.IntegerField()),
                ('emergency_contact', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Task Start')),
                ('end_time', models.TimeField(verbose_name='Task End')),
                ('type', models.CharField(choices=[('K', 'Kennel Cleaning'), ('G', 'Group Play'), ('M', 'Medications'), ('F', 'Feeding')], default='K', max_length=1)),
                ('description', models.TextField(max_length=250)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.IntegerField()),
                ('is_clean', models.BooleanField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('p_num', models.IntegerField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Feeding Date')),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('D', 'Dinner')], default='B', max_length=1)),
                ('food', models.CharField(max_length=50)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.animal')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_name', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='about')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
