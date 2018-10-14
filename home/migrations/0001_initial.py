# Generated by Django 2.1 on 2018-10-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateTimeField(verbose_name='date of birth')),
                ('gender', models.CharField(max_length=200)),
                ('hobbies', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('aimage', models.CharField(max_length=200)),
            ],
        ),
    ]
