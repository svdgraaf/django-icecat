# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Product.updated'
        db.delete_column('icecat_product', 'updated')

        # Deleting field 'Product.date_added'
        db.delete_column('icecat_product', 'date_added')

        # Adding field 'Product.created_at'
        db.add_column('icecat_product', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 12, 17, 0, 0)),
                      keep_default=False)

        # Adding field 'Product.updated_at'
        db.add_column('icecat_product', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 12, 17, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Product.updated'
        raise RuntimeError("Cannot reverse this migration. 'Product.updated' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Product.date_added'
        raise RuntimeError("Cannot reverse this migration. 'Product.date_added' and its values cannot be restored.")
        # Deleting field 'Product.created_at'
        db.delete_column('icecat_product', 'created_at')

        # Deleting field 'Product.updated_at'
        db.delete_column('icecat_product', 'updated_at')


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
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['icecat.Supplier']"}),
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