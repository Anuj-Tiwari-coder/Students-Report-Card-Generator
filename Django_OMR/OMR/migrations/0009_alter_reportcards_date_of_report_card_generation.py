# Generated by Django 5.1 on 2024-09-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMR', '0008_alter_reportcards_date_of_report_card_generation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcards',
            name='date_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
