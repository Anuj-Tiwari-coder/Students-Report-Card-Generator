# Generated by Django 5.1 on 2024-09-21 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OMR', '0006_alter_student_student_contact_reportcards'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reportcards',
            unique_together={('student_rank', 'date_of_report_card_generation')},
        ),
    ]
