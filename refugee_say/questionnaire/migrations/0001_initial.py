# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-07 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ranking_question', '0001_initial'),
        ('radio_question', '0001_initial'),
        ('selection_question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Last updated time')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(default=1, verbose_name='Question order')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='questionnaire.Questionnaire')),
                ('radio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='radio_question.RadioQuestion')),
                ('rank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ranking_question.RankingQuestion')),
                ('selection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='selection_question.SelectionQuestion')),
            ],
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='radios',
            field=models.ManyToManyField(through='questionnaire.QuestionOrder', to='radio_question.RadioQuestion'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='ranks',
            field=models.ManyToManyField(through='questionnaire.QuestionOrder', to='ranking_question.RankingQuestion'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='selections',
            field=models.ManyToManyField(through='questionnaire.QuestionOrder', to='selection_question.SelectionQuestion'),
        ),
    ]
