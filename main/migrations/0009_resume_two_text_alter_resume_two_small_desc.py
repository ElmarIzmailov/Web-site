# Generated by Django 4.1.3 on 2023-01-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_alter_home_link1_alter_home_link2_alter_home_link3_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume_two",
            name="text",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="resume_two",
            name="small_desc",
            field=models.CharField(max_length=35),
        ),
    ]
