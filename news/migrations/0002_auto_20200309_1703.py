# Generated by Django 3.0.4 on 2020-03-09 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='LanguageDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_content', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Language')),
            ],
        ),
    ]
