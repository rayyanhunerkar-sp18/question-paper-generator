# Generated by Django 4.0.5 on 2022-06-15 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawquestion', '0002_alter_rawquestion_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawquestion',
            name='rawquestionID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
