"""
Admin shell.

Utility to simplify creating remote commands executed via http POST request

Shell has two modes
 - regexp match
 - command parser - uses tokenizer

If command string begins with : or ., use command parser, otherwise try match
with regular expression defined actions.

Tokens:
 - ID - unicode identifier
 - string - unicode string encapsulated in '"' or "'" characters
 - int - integer literal
 - float - floating point integer literal
 - datetime - date and time literal
 - timespan - time span literal
 - reference - reference to model instance (GenericForeignKey)

"""
