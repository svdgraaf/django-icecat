# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('icecat_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(default='', max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('keywords', self.gf('django.db.models.fields.TextField')(default='')),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['icecat.Category'])),
        ))
        db.send_create_signal('icecat', ['Category'])

        # Deleting field 'Product.name'
        db.delete_column('icecat_product', 'name')

        # Adding field 'Product.model_name'
        db.add_column('icecat_product', 'model_name',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2012, 12, 17, 0, 0), max_length=255),
                      keep_default=False)

        # Adding field 'Product.date_added'
        db.add_column('icecat_product', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 12, 17, 0, 0)),
                      keep_default=False)

        # Adding field 'Product.updated'
        db.add_column('icecat_product', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 12, 17, 0, 0)),
                      keep_default=False)

        # Adding field 'Product.supplier'
        db.add_column('icecat_product', 'supplier',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['icecat.Supplier']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('icecat_category')


        # User chose to not deal with backwards NULL issues for 'Product.name'
        raise RuntimeError("Cannot reverse this migration. 'Product.name' and its values cannot be restored.")
        # Deleting field 'Product.model_name'
        db.delete_column('icecat_product', 'model_name')

        # Deleting field 'Product.date_added'
        db.delete_column('icecat_product', 'date_added')

        # Deleting field 'Product.updated'
        db.delete_column('icecat_product', 'updated')

        # Deleting field 'Product.supplier'
        db.delete_column('icecat_product', 'supplier_id')


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
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['icecat.Supplier']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'icecat.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '1024'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['icecat']