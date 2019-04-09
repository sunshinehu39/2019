# Generated by Django 2.0.4 on 2019-01-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosjh', '0003_auto_20190102_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarydetail',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='dosjh/dairy/audio', verbose_name='语音日记'),
        ),
        migrations.AlterField(
            model_name='diarydetail',
            name='content',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='日记内容'),
        ),
    ]
