# Generated by Django 3.2.20 on 2023-10-08 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='next_story',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='story_test.story'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='object_needed',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='choices_available',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='story_test.choice'),
        ),
    ]
