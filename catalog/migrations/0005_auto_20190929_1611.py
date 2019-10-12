# Generated by Django 2.2.5 on 2019-09-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_evententrymodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboardmodel',
            name='other_points',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='leaderboardmodel',
            name='rd1_points',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='leaderboardmodel',
            name='rd2_points',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='leaderboardmodel',
            name='rd3_points',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
