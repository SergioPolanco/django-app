# Generated by Django 2.1.5 on 2019-03-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190318_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(default='unassigned', max_length=50, null=True),
        ),
    ]
