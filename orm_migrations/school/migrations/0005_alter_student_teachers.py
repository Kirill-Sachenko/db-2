# Generated by Django 4.1.1 on 2022-09-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_teacherstudent_alter_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='Учитель', to='school.teacher'),
        ),
    ]
