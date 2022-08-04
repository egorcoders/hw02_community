# Generated by Django 2.2.9 on 2021-09-26 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210924_1849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['-title'], 'verbose_name': 'Группа статей', 'verbose_name_plural': 'Группы статей'},
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Group', verbose_name='Группа статей'),
        ),
    ]