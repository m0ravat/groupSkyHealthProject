# Generated by Django 5.0.6 on 2025-04-12 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deptName', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('Engineer', 'Engineer'), ('teamLeader', 'Team Leader'), ('deptLeader', 'Department Leader'), ('seniorManager', 'Senior Manager')], max_length=50)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('deptName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Led_Departments', to='core.department')),
                ('teamLeader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Led_Teams', to='core.user')),
            ],
            options={
                'db_table': 'Team',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='deptLeader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Led_By', to='core.user'),
        ),
        migrations.AddField(
            model_name='department',
            name='seniorManager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Managed_By', to='core.user'),
        ),
    ]
