# Generated by Django 5.0.6 on 2024-07-04 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="payment_link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="ID сессии"
            ),
        ),
    ]
