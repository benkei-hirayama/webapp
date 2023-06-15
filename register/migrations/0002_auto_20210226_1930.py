# Generated by Django 3.1.6 on 2021-02-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_leader',
            field=models.BooleanField(default=False, help_text='Set whether the user is the leader of the group to which the user belongs.', verbose_name='leader status'),
        ),
        migrations.AddField(
            model_name='user',
            name='team_name',
            field=models.CharField(blank=True, max_length=80, verbose_name='team name'),
        ),
    ]
