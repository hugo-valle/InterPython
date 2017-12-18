from reader.reader import Reader
from reader.compressed.bzipped import opener as bz2_opener
from reader.compressed.gzipped import opener as gzip_opener

# Rules for import *
__all__ = ['bz2_opener', 'gzip_opener']