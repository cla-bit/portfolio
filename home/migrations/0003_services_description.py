# Generated by Django 4.1 on 2023-01-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_portfolio_git_link_alter_portfolio_github_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
