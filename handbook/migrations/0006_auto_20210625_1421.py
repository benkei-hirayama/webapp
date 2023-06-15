# Generated by Django 3.1.6 on 2021-06-25 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0005_auto_20210625_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentsrecords',
            name='contents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='record', to='handbook.contents', verbose_name='細目'),
        ),
    ]
