# Generated by Django 4.0.4 on 2022-05-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0003_auto_20220422_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
