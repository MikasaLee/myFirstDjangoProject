# Generated by Django 3.1.2 on 2020-10-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoId', models.IntegerField(unique=True)),
                ('photoName', models.CharField(max_length=128)),
                ('userId', models.IntegerField(default=-1)),
                ('dateCreate', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=128)),
                ('result', models.FloatField()),
                ('info', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'photo',
            },
        ),
    ]