# Generated by Django 4.2.5 on 2024-01-12 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_question_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('integer', 'Integer'), ('choice', 'Choice'), ('button', 'Button'), ('text', 'Text')], default='button', max_length=100),
        ),
    ]
