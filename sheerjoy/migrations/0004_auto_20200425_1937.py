# Generated by Django 2.2.5 on 2020-04-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheerjoy', '0003_auto_20200425_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catprofile',
            name='description',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='weight',
            field=models.SmallIntegerField(default=0),
        ),
    ]
