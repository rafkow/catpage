# Generated by Django 3.0.6 on 2020-06-18 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheerjoy', '0017_auto_20200525_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='LitterPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(upload_to='litter/')),
            ],
        ),
        migrations.AddField(
            model_name='catprofile',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='photos', to='sheerjoy.HashTag'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='who_is_in',
            field=models.ManyToManyField(blank=True, related_name='on_picture', to='sheerjoy.CatProfile'),
        ),
        migrations.AlterField(
            model_name='litter',
            name='father',
            field=models.ForeignKey(limit_choices_to={'sex': '1,0'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sheerjoy.CatProfile'),
        ),
        migrations.AlterField(
            model_name='litter',
            name='mother',
            field=models.ForeignKey(limit_choices_to={'sex': '0,1'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sheerjoy.CatProfile'),
        ),
        migrations.CreateModel(
            name='Kitten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, upload_to='kitten/')),
                ('litter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='sheerjoy.Litter')),
            ],
        ),
    ]