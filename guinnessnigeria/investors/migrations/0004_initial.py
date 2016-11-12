# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StockTicker'
        db.create_table(u'investors_stockticker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('current_stock_value', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('previous_stock_value', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('last_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'investors', ['StockTicker'])

        # Adding model 'FinancialDownload'
        db.create_table(u'investors_financialdownload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'investors', ['FinancialDownload'])

        # Adding model 'ShareSummary'
        db.create_table(u'investors_sharesummary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('average_purchase_price', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=4)),
            ('shares', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'investors', ['ShareSummary'])

        # Adding model 'ShareDownload'
        db.create_table(u'investors_sharedownload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'investors', ['ShareDownload'])

        # Adding model 'FinancialReport'
        db.create_table(u'investors_financialreport', (
            (u'financialdownload_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['investors.FinancialDownload'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'investors', ['FinancialReport'])

        # Adding model 'FinancialResult'
        db.create_table(u'investors_financialresult', (
            (u'financialdownload_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['investors.FinancialDownload'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'investors', ['FinancialResult'])


    def backwards(self, orm):
        # Deleting model 'StockTicker'
        db.delete_table(u'investors_stockticker')

        # Deleting model 'FinancialDownload'
        db.delete_table(u'investors_financialdownload')

        # Deleting model 'ShareSummary'
        db.delete_table(u'investors_sharesummary')

        # Deleting model 'ShareDownload'
        db.delete_table(u'investors_sharedownload')

        # Deleting model 'FinancialReport'
        db.delete_table(u'investors_financialreport')

        # Deleting model 'FinancialResult'
        db.delete_table(u'investors_financialresult')


    models = {
        u'investors.financialdownload': {
            'Meta': {'ordering': "['order']", 'object_name': 'FinancialDownload'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'investors.financialreport': {
            'Meta': {'ordering': "['order']", 'object_name': 'FinancialReport', '_ormbases': [u'investors.FinancialDownload']},
            u'financialdownload_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['investors.FinancialDownload']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'investors.financialresult': {
            'Meta': {'ordering': "['order']", 'object_name': 'FinancialResult', '_ormbases': [u'investors.FinancialDownload']},
            u'financialdownload_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['investors.FinancialDownload']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'investors.sharedownload': {
            'Meta': {'ordering': "['order']", 'object_name': 'ShareDownload'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'investors.sharesummary': {
            'Meta': {'ordering': "['date']", 'object_name': 'ShareSummary'},
            'average_purchase_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '4'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shares': ('django.db.models.fields.IntegerField', [], {})
        },
        u'investors.stockticker': {
            'Meta': {'object_name': 'StockTicker'},
            'current_stock_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'previous_stock_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'})
        }
    }

    complete_apps = ['investors']