# Generated by Django 4.1.1 on 2022-09-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_side', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmanager',
            name='progress',
            field=models.CharField(choices=[('started', 'started'), ('15%', '15%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('completed', 'completed')], default='started', max_length=30),
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
    ]
