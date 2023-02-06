# Generated by Django 2.2.5 on 2020-04-26 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheerjoy', '0007_auto_20200426_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='catprofile',
            name='father',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='impregnated', to='sheerjoy.CatProfile'),
        ),
        migrations.AddField(
            model_name='catprofile',
            name='mother',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='born', to='sheerjoy.CatProfile'),
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='birth',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name='Litters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('birth', models.DateField(blank=True, default=None, null=True)),
                ('father', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sheerjoy.CatProfile')),
                ('mother', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sheerjoy.CatProfile')),
            ],
        ),
        migrations.AddField(
            model_name='catprofile',
            name='litter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='family', to='sheerjoy.Litters'),
        ),
    ]