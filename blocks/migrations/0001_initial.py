# Generated by Django 3.1.5 on 2021-01-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=100)),
                ('height', models.BigIntegerField()),
                ('timestamp', models.BigIntegerField()),
                ('miner', models.CharField(max_length=100)),
                ('transactionCount', models.BigIntegerField()),
            ],
        ),
    ]
