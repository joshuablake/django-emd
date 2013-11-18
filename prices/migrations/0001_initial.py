# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HistoricalPrice'
        db.create_table(u'items_history', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['static.Region'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['static.Type'])),
            ('price_low', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('price_average', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('price_high', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'prices', ['HistoricalPrice'])

        # Adding unique constraint on 'HistoricalPrice', fields ['region', 'date', 'type']
        db.create_unique(u'items_history', ['region_id', 'date', 'type_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'HistoricalPrice', fields ['region', 'date', 'type']
        db.delete_unique(u'items_history', ['region_id', 'date', 'type_id'])

        # Deleting model 'HistoricalPrice'
        db.delete_table(u'items_history')


    models = {
        u'prices.historicalprice': {
            'Meta': {'unique_together': "(('region', 'date', 'type'),)", 'object_name': 'HistoricalPrice'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_average': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'price_high': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'price_low': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'typeName'"}),
            'published': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['prices']
