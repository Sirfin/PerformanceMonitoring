# Generated by Django 2.0.1 on 2018-02-01 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PerformanceMonitoring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_mpi_rank', models.SmallIntegerField()),
                ('hostname', models.CharField(max_length=32)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PerformanceMonitoring.Job')),
            ],
        ),
        migrations.CreateModel(
            name='timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timer_name', models.CharField(max_length=32)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PerformanceMonitoring.ClimateModel')),
            ],
        ),
        migrations.CreateModel(
            name='timing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_mpi_rank', models.SmallIntegerField()),
                ('i_omp_thread', models.SmallIntegerField()),
                ('cnum', models.IntegerField()),
                ('tsum', models.FloatField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PerformanceMonitoring.Job')),
                ('timer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PerformanceMonitoring.timer')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='timing',
            unique_together={('job', 'timer', 'i_mpi_rank', 'i_omp_thread')},
        ),
        migrations.AlterUniqueTogether(
            name='timer',
            unique_together={('model', 'timer_name')},
        ),
    ]