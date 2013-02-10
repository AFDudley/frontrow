# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('runway_userprofile', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True, blank=True)),
            ('dt_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow, db_index=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('runway', ['UserProfile'])

        # Adding model 'RunwayCollection'
        db.create_table('runway_runwaycollection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coll_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('designer_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('video_file', self.gf('django.db.models.fields.files.FileField')(max_length=250, null=True, blank=True)),
            ('video_thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=250, null=True, blank=True)),
            ('dt_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
        ))
        db.send_create_signal('runway', ['RunwayCollection'])

        # Adding model 'Look'
        db.create_table('runway_look', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['runway.RunwayCollection'])),
            ('look_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('frame_time', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dt_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
        ))
        db.send_create_signal('runway', ['Look'])

        # Adding model 'Piece'
        db.create_table('runway_piece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('look', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['runway.Look'])),
            ('piece_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=256, null=True, blank=True)),
            ('metadata', self.gf('django.db.models.fields.TextField')()),
            ('dt_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
        ))
        db.send_create_signal('runway', ['Piece'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('runway_userprofile')

        # Deleting model 'RunwayCollection'
        db.delete_table('runway_runwaycollection')

        # Deleting model 'Look'
        db.delete_table('runway_look')

        # Deleting model 'Piece'
        db.delete_table('runway_piece')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'runway.look': {
            'Meta': {'object_name': 'Look'},
            'coll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['runway.RunwayCollection']"}),
            'dt_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'frame_time': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'look_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'runway.piece': {
            'Meta': {'object_name': 'Piece'},
            'dt_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'look': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['runway.Look']"}),
            'metadata': ('django.db.models.fields.TextField', [], {}),
            'piece_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'runway.runwaycollection': {
            'Meta': {'object_name': 'RunwayCollection'},
            'coll_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'designer_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dt_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_file': ('django.db.models.fields.files.FileField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'video_thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'runway.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'dt_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'db_index': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['runway']