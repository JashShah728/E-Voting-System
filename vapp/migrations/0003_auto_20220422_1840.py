# Generated by Django 2.2.13 on 2022-04-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0002_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]