import os
import sys
possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                        os.pardir,
                                       os.pardir,
                                       os.pardir))

if os.path.exists(os.path.join(possible_topdir,"gsyncer", "__init__.py")):
        sys.path.insert(0, possible_topdir)

print possible_topdir

from gsyncer.common import  config
conf = config.CONF


for attr in dir(conf):
    if not attr.startswith('__'):
        if attr == 'repos':
            assert(isinstance(getattr(conf,attr),list))
        print attr,getattr(conf,attr)
