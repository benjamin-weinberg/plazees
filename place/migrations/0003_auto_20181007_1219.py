# Generated by Django 2.1.2 on 2018-10-07 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20181007_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='info',
        ),
        migrations.AddField(
            model_name='point',
            name='pic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='place.Picture'),
            preserve_default=False,
        ),
    ]