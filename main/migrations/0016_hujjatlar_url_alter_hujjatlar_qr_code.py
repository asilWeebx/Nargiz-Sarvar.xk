# Generated by Django 4.2.3 on 2023-07-30 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_hujjatlar_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='hujjatlar',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hujjatlar',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='hujjatlar/'),
        ),
    ]