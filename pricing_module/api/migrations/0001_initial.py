# Generated by Django 4.1 on 2022-08-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DBP', models.IntegerField()),
                ('TBP', models.IntegerField()),
            ],
        ),
    ]
