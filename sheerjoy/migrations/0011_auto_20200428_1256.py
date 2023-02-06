# Generated by Django 2.2.5 on 2020-04-28 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheerjoy', '0010_auto_20200426_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='catprofile',
            name='is_with_us',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='culture',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='sheerjoy.Culture'),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='father',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='impregnated', to='sheerjoy.CatProfile'),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='image',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='litter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='family', to='sheerjoy.Litter'),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='mother',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='born', to='sheerjoy.CatProfile'),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='title',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='laureate', to='sheerjoy.Title'),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='weight',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
