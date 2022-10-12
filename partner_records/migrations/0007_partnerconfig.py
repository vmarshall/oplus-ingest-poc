# Generated by Django 4.1.2 on 2022-10-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("partner_records", "0006_alter_partnerrecord_doctor_notes_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PartnerConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("partner_name", models.CharField(max_length=200)),
                ("connect_string", models.CharField(max_length=200)),
            ],
        ),
    ]