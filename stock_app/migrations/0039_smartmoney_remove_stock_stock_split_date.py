# Generated by Django 4.1.7 on 2023-03-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0038_auto_20230315_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateY', models.DateField(blank=True, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='stock',
            name='stock_split_date',
        ),
    ]