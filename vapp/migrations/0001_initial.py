# Generated by Django 4.0 on 2022-04-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('cname', models.CharField(max_length=122)),
                ('constituency', models.CharField(max_length=122)),
                ('party', models.CharField(max_length=122)),
                ('vcount', models.IntegerField()),
            ],
        ),
    ]