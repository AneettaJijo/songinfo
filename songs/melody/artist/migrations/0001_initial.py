# Generated by Django 4.1.3 on 2022-11-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('artist', models.TextField()),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='gallery')),

            ],
        ),
    ]