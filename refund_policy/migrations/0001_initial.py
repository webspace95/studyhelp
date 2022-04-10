# Generated by Django 3.0.4 on 2022-02-15 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoubleCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderCancelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RefundPolicyIntroduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Introduction', max_length=50)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RevisionDeadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShortageOfWriter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
            ],
        ),
    ]
