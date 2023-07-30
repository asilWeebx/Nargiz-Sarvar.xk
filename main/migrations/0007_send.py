# Generated by Django 4.2.3 on 2023-07-30 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_blog_data_alter_blog_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('sending', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.contact')),
            ],
        ),
    ]
