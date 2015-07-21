# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomePage'
        db.create_table(u'theme_homepage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'theme', ['HomePage'])

        # Adding model 'Porter'
        db.create_table(u'theme_porter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='porter', null=True, to=orm['theme.HomePage'])),
            ('multiport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theme.Portfolio'], null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['Porter'])

        # Adding model 'Slide'
        db.create_table(u'theme_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', to=orm['theme.HomePage'])),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('featured_image', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('main_label', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('sub_label', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['Slide'])

        # Adding model 'Portfolios'
        db.create_table(u'theme_portfolios', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'theme', ['Portfolios'])

        # Adding model 'Portfolio'
        db.create_table(u'theme_portfolio', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('portfolio_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theme.PortfolioItem'], null=True, blank=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['Portfolio'])

        # Adding model 'TempPortfolio'
        db.create_table(u'theme_tempportfolio', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['TempPortfolio'])

        # Adding model 'ItemPorter'
        db.create_table(u'theme_itemporter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('temp_portfolio', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='item_porter', null=True, to=orm['theme.TempPortfolio'])),
            ('portfolio_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theme.PortfolioItem'], null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['ItemPorter'])

        # Adding model 'PortfolioItem'
        db.create_table(u'theme_portfolioitem', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('featured_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('short_description', self.gf('mezzanine.core.fields.RichTextField')(blank=True)),
            ('href', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
        ))
        db.send_create_signal(u'theme', ['PortfolioItem'])

        # Adding M2M table for field categories on 'PortfolioItem'
        m2m_table_name = db.shorten_name(u'theme_portfolioitem_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portfolioitem', models.ForeignKey(orm[u'theme.portfolioitem'], null=False)),
            ('portfolioitemcategory', models.ForeignKey(orm[u'theme.portfolioitemcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['portfolioitem_id', 'portfolioitemcategory_id'])

        # Adding model 'PortfolioItemImage'
        db.create_table(u'theme_portfolioitemimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('portfolioitem', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['theme.PortfolioItem'])),
            ('file', self.gf('mezzanine.core.fields.FileField')(max_length=200)),
        ))
        db.send_create_signal(u'theme', ['PortfolioItemImage'])

        # Adding model 'PortfolioItemCategory'
        db.create_table(u'theme_portfolioitemcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['PortfolioItemCategory'])


    def backwards(self, orm):
        # Deleting model 'HomePage'
        db.delete_table(u'theme_homepage')

        # Deleting model 'Porter'
        db.delete_table(u'theme_porter')

        # Deleting model 'Slide'
        db.delete_table(u'theme_slide')

        # Deleting model 'Portfolios'
        db.delete_table(u'theme_portfolios')

        # Deleting model 'Portfolio'
        db.delete_table(u'theme_portfolio')

        # Deleting model 'TempPortfolio'
        db.delete_table(u'theme_tempportfolio')

        # Deleting model 'ItemPorter'
        db.delete_table(u'theme_itemporter')

        # Deleting model 'PortfolioItem'
        db.delete_table(u'theme_portfolioitem')

        # Removing M2M table for field categories on 'PortfolioItem'
        db.delete_table(db.shorten_name(u'theme_portfolioitem_categories'))

        # Deleting model 'PortfolioItemImage'
        db.delete_table(u'theme_portfolioitemimage')

        # Deleting model 'PortfolioItemCategory'
        db.delete_table(u'theme_portfolioitemcategory')


    models = {
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'theme.homepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'theme.itemporter': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ItemPorter'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portfolio_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['theme.PortfolioItem']", 'null': 'True', 'blank': 'True'}),
            'temp_portfolio': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item_porter'", 'null': 'True', 'to': u"orm['theme.TempPortfolio']"})
        },
        u'theme.porter': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Porter'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'porter'", 'null': 'True', 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiport': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['theme.Portfolio']", 'null': 'True', 'blank': 'True'})
        },
        u'theme.portfolio': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Portfolio', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'portfolio_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['theme.PortfolioItem']", 'null': 'True', 'blank': 'True'})
        },
        u'theme.portfolioitem': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'PortfolioItem', '_ormbases': [u'pages.Page']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'portfolioitems'", 'blank': 'True', 'to': u"orm['theme.PortfolioItemCategory']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'short_description': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'})
        },
        u'theme.portfolioitemcategory': {
            'Meta': {'ordering': "('title',)", 'object_name': 'PortfolioItemCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'theme.portfolioitemimage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'PortfolioItemImage'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portfolioitem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['theme.PortfolioItem']"})
        },
        u'theme.portfolios': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Portfolios', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'theme.slide': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'featured_image': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'main_label': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'sub_label': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'})
        },
        u'theme.tempportfolio': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'TempPortfolio', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['theme']