"""
Here are doctests for advanced_tags application:


>>> from utils import *
>>> parsedate("1.5")
datetime.datetime(2010, 5, 1, 0, 0)
>>> parsedate("1.5.")
datetime.datetime(2010, 5, 1, 0, 0)
>>> parsedate("1. 5. ")
datetime.datetime(2010, 5, 1, 0, 0)
>>> parsedate("1. 5. 2005")
datetime.datetime(2005, 5, 1, 0, 0)
>>> parsedate("1. 5. 23:0")
datetime.datetime(2010, 5, 1, 23, 0)
>>> parsedate("1. 5. 3:0")
datetime.datetime(2010, 5, 1, 3, 0)
>>> parsedate("1. 5. 23:13")
datetime.datetime(2010, 5, 1, 23, 13)
>>> parsedate("15. 12. 2008 23:13")
datetime.datetime(2008, 12, 15, 23, 13)
>>> parsedate("15.12.2008 23:13")
datetime.datetime(2008, 12, 15, 23, 13)
>>> parsedate("15.12.23:13")
datetime.datetime(2010, 12, 15, 23, 13)
>>> parsedate("15.12.2008 23:13")
datetime.datetime(2008, 12, 15, 23, 13)
>>> parsedate("1512200823:13")
datetime.datetime(2008, 12, 15, 23, 13)
>>> parsedate("0102200823:13")
datetime.datetime(2008, 2, 1, 23, 13)

"""
