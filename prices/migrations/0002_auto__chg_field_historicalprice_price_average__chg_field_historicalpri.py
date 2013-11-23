# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HistoricalPrice.price_average'
        db.alter_column('items_history', 'price_average', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2))

        # Changing field 'HistoricalPrice.price_high'
        db.alter_column('items_history', 'price_high', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2))

        # Changing field 'HistoricalPrice.price_low'
        db.alter_column('items_history', 'price_low', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'HistoricalPrice.price_average'
        db.alter_column('items_history', 'price_average', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))

        # Changing field 'HistoricalPrice.price_high'
        db.alter_column('items_history', 'price_high', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))

        # Changing field 'HistoricalPrice.price_low'
        db.alter_column('items_history', 'price_low', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))

    models = {
        u'prices.historicalprice': {
            'Meta': {'unique_together': "(('region', 'date', 'type'),)", 'object_name': 'HistoricalPrice', 'db_table': "'items_history'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_average': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'price_high': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'price_low': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.BigIntegerField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['static.Region']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['static.Type']"})
        },
        u'static.region': {
            'Meta': {'object_name': 'Region', 'db_table': "'mapRegions'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'regionID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'regionName'"})
        },
        u'static.type': {
            'Meta': {'object_name': 'Type', 'db_table': "'invTypes'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'typeID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'typeName'"}),
            'published': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['prices']