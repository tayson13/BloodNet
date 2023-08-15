# Generated by Django 4.2.3 on 2023-08-15 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_customuser_thana'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField(max_length=300, null=True)),
                ('thana', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.thana')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=2000)),
                ('contact_no', models.CharField(max_length=40)),
                ('is_published', models.BooleanField(default=True)),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.hospital')),
            ],
        ),
    ]
