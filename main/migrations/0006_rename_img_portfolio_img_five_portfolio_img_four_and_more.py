# Generated by Django 4.1.3 on 2023-01-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_resume_four_desc"),
    ]

    operations = [
        migrations.RenameField(
            model_name="portfolio",
            old_name="img",
            new_name="img_five",
        ),
        migrations.AddField(
            model_name="portfolio",
            name="img_four",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="portfolio",
            name="img_one",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="portfolio",
            name="img_seven",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="portfolio",
            name="img_six",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="portfolio",
            name="img_three",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="portfolio",
            name="img_two",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
    ]
