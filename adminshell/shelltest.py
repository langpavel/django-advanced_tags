import antlr3
from ShellLexer import ShellLexer

l = ShellLexer(antlr3.StringStream(u"ident 123 3.141527 .707 'String with [\\']' \"String with [\\\"]\" "))

t = l.nextToken()

