# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Platform'
        db.create_table('projects_platform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('projects', ['Platform'])

        # Adding model 'ProgrammingLanguage'
        db.create_table('projects_programminglanguage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('projects', ['ProgrammingLanguage'])

        # Adding model 'Library'
        db.create_table('projects_library', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['Library'])

        # Adding model 'Tool'
        db.create_table('projects_tool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['Tool'])

        # Adding model 'Screenshot'
        db.create_table('projects_screenshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('large', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('projects', ['Screenshot'])

        # Adding model 'Link'
        db.create_table('projects_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='links', to=orm['projects.Project'])),
        ))
        db.send_create_signal('projects', ['Link'])

        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('source_code', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('title_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding M2M table for field platforms on 'Project'
        m2m_table_name = db.shorten_name('projects_project_platforms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('platform', models.ForeignKey(orm['projects.platform'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'platform_id'])

        # Adding M2M table for field programming_languages on 'Project'
        m2m_table_name = db.shorten_name('projects_project_programming_languages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('programminglanguage', models.ForeignKey(orm['projects.programminglanguage'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'programminglanguage_id'])

        # Adding M2M table for field libraries on 'Project'
        m2m_table_name = db.shorten_name('projects_project_libraries')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('library', models.ForeignKey(orm['projects.library'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'library_id'])

        # Adding M2M table for field tools on 'Project'
        m2m_table_name = db.shorten_name('projects_project_tools')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('tool', models.ForeignKey(orm['projects.tool'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'tool_id'])

        # Adding M2M table for field screenshots on 'Project'
        m2m_table_name = db.shorten_name('projects_project_screenshots')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('screenshot', models.ForeignKey(orm['projects.screenshot'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'screenshot_id'])


    def backwards(self, orm):
        # Deleting model 'Platform'
        db.delete_table('projects_platform')

        # Deleting model 'ProgrammingLanguage'
        db.delete_table('projects_programminglanguage')

        # Deleting model 'Library'
        db.delete_table('projects_library')

        # Deleting model 'Tool'
        db.delete_table('projects_tool')

        # Deleting model 'Screenshot'
        db.delete_table('projects_screenshot')

        # Deleting model 'Link'
        db.delete_table('projects_link')

        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Removing M2M table for field platforms on 'Project'
        db.delete_table(db.shorten_name('projects_project_platforms'))

        # Removing M2M table for field programming_languages on 'Project'
        db.delete_table(db.shorten_name('projects_project_programming_languages'))

        # Removing M2M table for field libraries on 'Project'
        db.delete_table(db.shorten_name('projects_project_libraries'))

        # Removing M2M table for field tools on 'Project'
        db.delete_table(db.shorten_name('projects_project_tools'))

        # Removing M2M table for field screenshots on 'Project'
        db.delete_table(db.shorten_name('projects_project_screenshots'))


    models = {
        'projects.library': {
            'Meta': {'object_name': 'Library'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'projects.link': {
            'Meta': {'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': "orm['projects.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'projects.platform': {
            'Meta': {'object_name': 'Platform'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'projects.programminglanguage': {
            'Meta': {'object_name': 'ProgrammingLanguage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libraries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'blank': 'True', 'to': "orm['projects.Library']"}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'platforms': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['projects.Platform']"}),
            'programming_languages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['projects.ProgrammingLanguage']"}),
            'screenshots': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'blank': 'True', 'to': "orm['projects.Screenshot']"}),
            'source_code': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'blank': 'True', 'to': "orm['projects.Tool']"})
        },
        'projects.screenshot': {
            'Meta': {'object_name': 'Screenshot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'projects.tool': {
            'Meta': {'object_name': 'Tool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['projects']