from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User

from managers import TagManager, TaggedItemManager


try:
    _DEFAULT_MIN_WEIGHT = settings.TAGS_DEFAULT_MIN_WEIGHT
except AttributeError:
    _DEFAULT_MIN_WEIGHT = 1.2


class Tag(models.Model):
    slug = models.SlugField(_('tag slug'), max_length=50, \
        unique=True, db_index=True)
    name = models.CharField(_('tag name'), max_length=50, \
        unique=True, db_index=True)

    # system tag have special meaning for system
    # (e.g. 'featured post' or more generally 'selected item')
    # and this tag does NOT display to visitors
    is_system = models.BooleanField(_('is system tag'), default=False)

    # this tag is not set directly to content but
    # generalizes other tags instead
    is_super = models.BooleanField(_('is super tag'), default=False)

    # minimal requested weight (i.e. minimal count of users
    min_weight = models.FloatField( \
        _('minimal required weight of tag to publish'), null=True, blank=True)

    objects = TagManager(restrict_date=True)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
        permissions = (
            ("can_add_tag", "Can add tag"),
            ("can_add_system_tag", "Can add system tag"),
            ("can_remove_tag", "Can remove tag"),
            ("can_remove_system_tag", "Can remove system tag"),
        )

    def __unicode__(self):
        return u'%s' % (self.display_name, )

    @property
    def display_name(self):
        return self.name or self.slug


class TaggedItem(models.Model):
    """
    Holds the relationship between a tag and the item being tagged.
    """
    tag = models.ForeignKey(Tag, verbose_name=_('tag'), related_name='items')
    content_type = models.ForeignKey(ContentType, \
        verbose_name=_('content type'))
    object_id = models.PositiveIntegerField(_('object id'), db_index=True)
    object = generic.GenericForeignKey('content_type', 'object_id')

    # sum of UserTaggedItem weights
    weight = models.FloatField(_('weight of tag'), default=1.0)

    # this fields are applied on system tags, where this values make sense
    valid_from = models.DateTimeField(_('valid from date'), \
        blank=True, null=True)
    valid_to = models.DateTimeField(_('valid to date'), \
        blank=True, null=True)

    objects = TaggedItemManager()

    class Meta:
        unique_together = (('tag', 'content_type', 'object_id'), )
        verbose_name = _('tagged item')
        verbose_name_plural = _('tagged items')

    def __unicode__(self):
        return u'%s [%s]' % (self.object, self.tag)


class UserTaggedItem(models.Model):
    """
    Holds information about user who tagged item
    """
    taggeditem = models.ForeignKey(TaggedItem, verbose_name=_('tagged item'))
    user = models.ForeignKey(User, verbose_name=_('user that set tag'))
    weight = models.FloatField(_('weight of vote'), default=1.0)
