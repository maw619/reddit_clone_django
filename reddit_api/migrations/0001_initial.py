# Generated by Django 4.1.7 on 2023-03-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedditAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('author_fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('domain', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
