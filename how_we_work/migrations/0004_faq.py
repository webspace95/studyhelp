# Generated by Django 3.0.4 on 2022-02-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('how_we_work', '0003_howweworkchecklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
            ],
        ),
    ]
