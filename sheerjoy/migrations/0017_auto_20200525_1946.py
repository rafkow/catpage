# Generated by Django 2.2.5 on 2020-05-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheerjoy', '0016_auto_20200505_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catprofile',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile/'),
        ),
    ]
