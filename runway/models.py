from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    """
    Any person using the system
    """
    user          = models.OneToOneField(User, primary_key=True)
    full_name     = models.CharField(max_length=100)
    email         = models.EmailField(_('Email'),
                                            max_length=100, null=True, blank=True)
    dt_created    = models.DateTimeField(_('datetime created'),
                                            db_index=True,
                                            default=datetime.utcnow, editable=False)
    is_active     = models.BooleanField(_('is active'),
                                            default=True, editable=True)
    def __unicode__(self):
        return u'%s (%s)' % (self.full_name, self.user.username)

class RunwayCollection(models.Model):
    """
    A video of an entire runway show for one designer.
    """
    coll_name     = models.CharField(max_length=100)
    designer_name = models.CharField(max_length=100)
    video_file    = models.FileField(upload_to='media_items/', 
                                   max_length=250,
                                   null=True, blank=True)
    video_thumb   = models.ImageField(upload_to="media_thumbs/",
                                    max_length=250,
                                    null=True, blank=True)
    dt_created    = models.DateTimeField(default=datetime.utcnow, editable=False)
    def __unicode__(self):
        return u'%s' % self.coll_name

class Look(models.Model):
    """
    An individual look within a collection
    """
    coll       = models.ForeignKey(RunwayCollection)
    look_name  = models.CharField(max_length=100)
    frame_time = models.FloatField(default=0.0)
    dt_created = models.DateTimeField(default=datetime.utcnow, editable=False)
    def __unicode__(self):
        return u'%s' % self.samplepreso_name

class Piece(models.Model):
    """
    An item/article of clothing within a look
    """
    look                   = models.ForeignKey(Look)
    piece_name             = models.CharField(max_length=200, blank=True, null=True)
    url                    = models.URLField(_('url'),
                                            verify_exists=False,
                                            max_length=256,
                                            null=True, blank=True)
    metadata               = models.TextField()
    dt_created             = models.DateTimeField(default=datetime.utcnow, editable=False)
    def __unicode__(self):
        return u'%s' % self.piece_name

    

