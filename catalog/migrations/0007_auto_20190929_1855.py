# Generated by Django 2.2.5 on 2019-09-29 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190929_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaderboardmodel',
            old_name='other_points',
            new_name='rd1_bonus',
        ),
        migrations.RenameField(
            model_name='leaderboardmodel',
            old_name='rd1_points',
            new_name='rd1_ctpld',
        ),
        migrations.RenameField(
            model_name='leaderboardmodel',
            old_name='rd2_points',
            new_name='rd1_golf',
        ),
        migrations.RenameField(
            model_name='leaderboardmodel',
            old_name='rd3_points',
            new_name='rd1_total',
        ),
        migrations.AlterField(
            model_name='evententrymodel',
            name='category',
            field=models.CharField(blank=True, choices=[('Round1Golf', 'Round1Golf'), ('Round2Golf', 'Round2Golf'), ('Round3Golf', 'Round3Golf'), ('OtherPoints', 'OtherPoints')], max_length=30, null=True),
        ),
    ]
