# Generated by Django 3.1.6 on 2021-06-21 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0003_subject_contents_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='contents_count',
            field=models.IntegerField(verbose_name='細目数'),
        ),
    ]
