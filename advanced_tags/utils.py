"""
Format of added tags
simple example:
    fun, mini comix
advanced examples:
    -1.5x sys new {dummy}Dummy tag [(\d{1,2}.\d{1,2})?]
"""

import re
import unicodedata
from datetime import datetime

from django.utils.encoding import force_unicode

from models import Tag, TaggedItem, UserTaggedItem


def replace_accents(str):
    "Replace accented characters with common ascii chars"
    return u"".join((c for c in unicodedata.normalize('NFD', str) \
        if unicodedata.category(c) != 'Mn'))


def normalize_slug(text, max_length=50):
    "make string usable as slug"
    text = force_unicode(text)
    text = replace_accents(text)
    text = re.sub(r"[^a-zA-Z0-9]+", '-', text).strip("-").lower()
    return text[:max_length]


_date_pattern = re.compile( \
    r'^\s*(?P<day>\d\d?)\.?\s*' + \
    r'(?P<month>\d\d?)\.?\s*' + \
    r'(?P<year>\d{4})?\s*' + \
    r'((?P<hour>\d\d?):(?P<minutes>\d\d?))?\s*$')


def parsedate(str):
    """
    Parse date and time string in format dd.mm.[rrrr] [HH:MM]
    """
    m = _date_pattern.match(str).groupdict()
    if not m:
        raise Exception('Invalid date string')
    return datetime(int(m["year"] or datetime.now().year), \
        int(m["month"]), int(m["day"]), \
        int(m["hour"] or 0), int(m["minutes"] or 0))


def nice_date(date):
    if not date:
        return u""
    fmt = u"%d.%d.%d" % (date.day, date.month, date.year)
    try:
        if date.hour != 0 or date.minute != 0:
            return fmt + (u" %2d:%2d" % (date.hour, date.minute))
    except:
        pass
    return fmt


class TagParser(object):

    _tag_pattern = re.compile( \
        r'(?P<sign>([+]+|[-]+))?' + \
        r'(?P<weight>\d+(\.\d+)?)?[xX]?[:]?' + \
        r'(?P<attribs>(\w*:)*)\s*' + \
        r'(?P<tag>.*)')

    _tag_date_pattern = re.compile( \
        r'\[\s*' + \
        r'(((from|od)\s*)?(?P<from>[0-9:\.tT\s]+)\s*)?' + \
        r'((to|do|-)\s*(?P<to>[0-9:\.tT\s]+))?' + \
        r'\s*\]')

    _slug_pattern = re.compile(r'\{(?P<slug>.*)\}')

    def __init__(self, tag_string, **kwargs):
        self.tag_string = tag_string
        s = self._extract_date(tag_string)
        s = self._extract_slug(s)
        tag_parts = TagParser._tag_pattern.match(s).groupdict()
        self.sign = tag_parts["sign"]
        self.weight = tag_parts["weight"]
        if self.weight:
            self.weight = float(self.weight)
        else:
            self.weight = 1.0
        self.attribs = [x \
            for x in tag_parts["attribs"][:-1].split(':') if x != '']
        self.tagname = tag_parts["tag"]
        if not self.slug:
            self.slug = normalize_slug(self.tagname)

    def _extract_date(self, tag_string):
        match = TagParser._tag_date_pattern.search(tag_string)
        if match:
            self.from_date = match.group("from")
            self.to_date = match.group("to")
            if self.from_date:
                self.from_date = parsedate(self.from_date)
            if self.to_date:
                self.to_date = parsedate(self.to_date)
            return tag_string[:match.start(0)] +':'+ tag_string[match.end(0):]
        else:
            self.from_date = None
            self.to_date = None
            return tag_string

    def _extract_slug(self, tag_string):
        match = TagParser._slug_pattern.search(tag_string)
        if match:
            self.slug = normalize_slug(match.group("slug"))
            return tag_string[:match.start(0)] +':'+ tag_string[match.end(0):]
        else:
            self.slug = None
            return tag_string

    def normalize(self):
        if self.from_date or self.to_date:
            daterange = u''
            if self.from_date:
                daterange = u'%s ' % nice_date(self.from_date)
            if self.to_date:
                daterange += u'to %s' % nice_date(self.to_date)
            daterange = u'[' + daterange.strip() + u']'
        else:
            daterange = u''
        if self.attribs:
            attribs = reduce(lambda a, b: a+':'+b, self.attribs)
        else:
            attribs = u''
        return u"%.1f:%s%s{%s}%s" % \
            (self.weight, attribs, daterange, self.slug, self.tagname)

    def __repr__(self):
        # [2:-1] = strip unicode representation chars - u'...'
        return "<TagParser:%s>" % self.normalize().__repr__()[2:-1]

    def __unicode__(self):
        fmt = u""
        if self.weight:
            fmt += u"%.1f:" % self.weight
        if self.attribs and len(self.attribs) > 0:
            fmt += (u":".join(self.attribs)) + u":"
        ds = u""
        if self.from_date:
            ds += u"from %s " % nice_date(self.from_date)
        if self.to_date:
            ds += u"to %s" % nice_date(self.to_date)
        if self.from_date or self.to_date:
            fmt += u"[%s]" % ds.strip()
        return u"%s{%s}%s" % (fmt, self.slug, self.tagname)


class TagsParser(object):

    def __init__(self, tags_string, **kwargs):
        self.tags = [TagParser(s.strip(), **kwargs) \
            for s in re.split(r'[,;]+', tags_string)]

    def __unicode__(self):
        return u"; ".join(self.tags)
