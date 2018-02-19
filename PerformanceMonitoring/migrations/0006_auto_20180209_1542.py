# Generated by Django 2.0.1 on 2018-02-09 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PerformanceMonitoring', '0005_auto_20180203_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='id',
        ),
        migrations.AlterField(
            model_name='job',
            name='job_name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='job_rank',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_ranks', to='PerformanceMonitoring.Job'),
        ),
        migrations.AlterField(
            model_name='timer',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timers', to='PerformanceMonitoring.ClimateModel'),
        ),
        migrations.AlterField(
            model_name='timing',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timings', to='PerformanceMonitoring.Job'),
        ),
        migrations.AlterField(
            model_name='timing',
            name='timer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timings', to='PerformanceMonitoring.timer'),
        ),
    ]