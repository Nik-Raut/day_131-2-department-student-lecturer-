# Generated by Django 3.2.7 on 2021-09-13 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(choices=[('mech', 'MECH'), ('civil', 'CIVIL'), ('it', 'IT'), ('computer', 'COMPUTER')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_No', models.IntegerField()),
                ('Stu_name', models.CharField(max_length=50)),
                ('Marks', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InfoApp.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lecturer_name', models.CharField(max_length=30)),
                ('Lecturer_subject', models.CharField(max_length=30)),
                ('department', models.ManyToManyField(to='InfoApp.Department')),
            ],
        ),
    ]
