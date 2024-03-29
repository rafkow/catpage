# Generated by Django 2.2.5 on 2020-04-26 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheerjoy', '0008_auto_20200426_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cultures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='catprofile',
            name='gender',
        ),
        migrations.AddField(
            model_name='animalcoloration',
            name='short',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='catprofile',
            name='sex',
            field=models.CharField(choices=[('1,0', 'Male'), ('0,1', 'Female')], default=None, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='catprofile',
            name='culture',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='sheerjoy.Cultures'),
        ),
        migrations.AddField(
            model_name='catprofile',
            name='title',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='laureate', to='sheerjoy.Titles'),
        ),
    ]
