# Generated by Django 4.1.2 on 2022-10-12 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("partner_records", "0002_environmentfactor_medicalimage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="partnerrecord",
            name="medical_images",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="medical_images",
                to="partner_records.medicalimage",
            ),
            preserve_default=False,
        ),
    ]