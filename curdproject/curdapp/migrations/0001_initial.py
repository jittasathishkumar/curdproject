# Generated by Django 4.2.7 on 2023-12-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('Email', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('Cgpa', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
            ],
        ),
    ]
