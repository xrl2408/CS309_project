# Generated by Django 2.2.7 on 2019-12-24 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anwser1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(default='', max_length=128)),
                ('anwser', models.CharField(default='', max_length=10000)),
                ('anwser_time', models.CharField(default='', max_length=128)),
                ('respondent_level', models.CharField(default='', max_length=128)),
                ('respondent_id', models.CharField(default='', max_length=128)),
                ('star', models.CharField(default='', max_length=128)),
                ('star_guy', models.CharField(default='', max_length=50000)),
            ],
        ),
        migrations.CreateModel(
            name='Question1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questioner', models.CharField(default='', max_length=128)),
                ('title', models.CharField(default='', max_length=10000)),
                ('question', models.CharField(default='', max_length=10000)),
                ('question_time', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Anwser',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
