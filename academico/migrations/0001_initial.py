# Generated by Django 4.1.7 on 2023-03-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=55)),
                ('creditos', models.PositiveBigIntegerField()),
            ],
        ),
    ]
