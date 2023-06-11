# Generated by Django 3.2.9 on 2022-12-06 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0005_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='stock',
        ),
        migrations.AddField(
            model_name='stock',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='stock_app.account'),
        ),
    ]