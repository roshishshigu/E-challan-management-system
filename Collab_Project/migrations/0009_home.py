# Generated by Django 3.1.7 on 2021-05-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collab_Project', '0008_help'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('slidingtext', models.TextField()),
            ],
        ),
    ]
