# Generated by Django 4.2.6 on 2023-11-19 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tools", "0001_initial"),
        ("stories", "0001_initial"),
        ("choices", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="next_story",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="stories.story",
            ),
        ),
        migrations.AddField(
            model_name="choice",
            name="tools_needed",
            field=models.ManyToManyField(blank=True, to="tools.tool"),
        ),
    ]
