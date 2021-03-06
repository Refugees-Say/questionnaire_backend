# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-08 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('choice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='radio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='radio_question.RadioQuestion'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='rank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ranking_question.RankingQuestion'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='selection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='selection_question.SelectionQuestion'),
        ),
    ]
