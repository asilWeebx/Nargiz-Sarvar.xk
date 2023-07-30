# Generated by Django 4.2.3 on 2023-07-30 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_hujjatlar_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='hujjatlar',
            name='another_file_type',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hujjatlar',
            name='file_type',
            field=models.CharField(choices=[('PDF', 'PDF'), ('XLS', 'XLS'), ('DOC', 'DOC'), ('JPG', 'JPG')], default='Boshqa file', max_length=10),
        ),
    ]