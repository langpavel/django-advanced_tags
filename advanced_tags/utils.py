"""
Format of added tags
<Tags>          ::= <Tags> [,;] <Tag>
                |   <Tag>
<Tag>           ::= <Operators> string
                |   <Operators> '{' url '}' string
<Operators>     ::= <Operator>
<Operator>      ::= [+-]? float 'x:'
                |   'sys:'
                |   'new:'

simple example:
    fun, mini comix
advanced examples:
    -1.5x:sys:new:{dummy}Dummy tag
"""

import re
import unicodedata

from django.utils.encoding import force_unicode

from models import Tag, TaggedItem, UserTaggedItem


_tag_pattern = re.compile( \
    r'(?P<weight>[+-]?\d+(\.\d+)?)?[xX]?[:]?' + \
    r'(?P<attribs>(\w*:)*)\s*' + \
    r'(\{(?P<slug>.*)\}:?)?\s*' + \
    r'(?P<tag>.*)')


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


class TagParser(object):
    """
    >>> u"%s" % TagParser("Tag name")
    u'{tag-name}Tag name'
    """

    def __init__(self, tag_string, **kwargs):
        tag_parts = _tag_pattern.match(tag_string).groupdict()
        self.weight = tag_parts["weight"]
        self.attribs = tag_parts["attribs"][:-1].split(':')
        self.tagname = tag_parts["tag"]
        self.slug = normalize_slug(tag_parts["slug"] or self.tagname)

    def __unicode__(self):
        fmt = u""
        if self.weight:
            fmt += u"%.1f:" % self.weight
        if self.attribs:
            fmt += (u":".join(self.attribs)) + u":"
        return u"%s{%s}%s" % (fmt, self.slug, self.tagname)


class TagsParser(object):

    def __init__(self, tags_string, **kwargs):
        self.tags = [TagParser(s.strip(), **kwargs) \
            for s in re.split(r'[,;]+', tags_string)]

    def __unicode__(self):
        return u"; ".join(self.tags)


# Run doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
