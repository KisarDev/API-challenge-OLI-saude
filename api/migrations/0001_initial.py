# Generated by Django 4.2.6 on 2023-10-24 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemsHealth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_problem', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1)),
                ('date_create', models.DateTimeField()),
                ('data_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('problem_health', models.ManyToManyField(related_name='problem', to='api.problemshealth')),
            ],
        ),
    ]