# Generated by Django 2.1.5 on 2019-10-12 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0010_auto_20191008_2358'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scratch',
            unique_together={('judge', 'team')},
        ),
    ]
