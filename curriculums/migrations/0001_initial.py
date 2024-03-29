# Generated by Django 2.2.3 on 2019-07-03 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_courses_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('attachment_url', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=64)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Courses')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'curriculums',
            },
        ),
    ]
