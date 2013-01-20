# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Philosophy'
        db.create_table('home_philosophy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('home', ['Philosophy'])

        # Adding model 'Description'
        db.create_table('home_description', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('home', ['Description'])

        # Adding model 'TechnicalSkill'
        db.create_table('home_technicalskill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('home', ['TechnicalSkill'])


    def backwards(self, orm):
        # Deleting model 'Philosophy'
        db.delete_table('home_philosophy')

        # Deleting model 'Description'
        db.delete_table('home_description')

        # Deleting model 'TechnicalSkill'
        db.delete_table('home_technicalskill')


    models = {
        'home.description': {
            'Meta': {'object_name': 'Description'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'home.philosophy': {
            'Meta': {'object_name': 'Philosophy'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'home.technicalskill': {
            'Meta': {'object_name': 'TechnicalSkill'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['home']