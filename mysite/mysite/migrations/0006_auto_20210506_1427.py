# Generated by Django 3.1.7 on 2021-05-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20210506_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinetakvim',
            name='saat0',
            field=models.TimeField(blank=True, null=True, unique=True, verbose_name='1. Saat '),
        ),
        migrations.AlterField(
            model_name='onlinetakvim',
            name='saat1',
            field=models.TimeField(blank=True, null=True, verbose_name='2. Saat '),
        ),
        migrations.AlterField(
            model_name='onlinetakvim',
            name='saat2',
            field=models.TimeField(blank=True, null=True, verbose_name='3. Saat '),
        ),
        migrations.AlterField(
            model_name='onlinetakvim',
            name='saat3',
            field=models.TimeField(blank=True, null=True, verbose_name='4. Saat '),
        ),
        migrations.AlterField(
            model_name='onlinetakvim',
            name='saat4',
            field=models.TimeField(blank=True, null=True, verbose_name='5. Saat '),
        ),
        migrations.AlterField(
            model_name='onlinetakvim',
            name='saat5',
            field=models.TimeField(blank=True, null=True, verbose_name='6. Saat '),
        ),
        migrations.AlterField(
            model_name='onlinetakvim',
            name='saat6',
            field=models.TimeField(blank=True, null=True, verbose_name='7. Saat '),
        ),
        migrations.AlterField(
            model_name='onlinetakvim',
            name='saat7',
            field=models.TimeField(blank=True, null=True, verbose_name='8. Saat '),
        ),
    ]
