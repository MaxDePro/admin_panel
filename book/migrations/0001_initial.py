# Generated by Django 4.1 on 2022-09-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('name', models.CharField(blank=True, max_length=128)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('count', models.IntegerField(default=10)),
                ('writed', models.DateTimeField(default=None)),
                ('publish', models.DateTimeField(default=None)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]