# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.on_market'
        db.add_column('icecat_product', 'on_market',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.on_market'
        db.delete_column('icecat_product', 'on_market')


    models = {
        'icecat.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['icecat.Category']"}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '1024'})
        },
        'icecat.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['icecat.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'on_market': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['icecat.Supplier']"}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '1024'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        'icecat.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '1024'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['icecat']