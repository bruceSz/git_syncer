import sys
import os

from wsgiref.simple_server import make_server

#from  gsyncer.monitor import monitor

possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                    os.pardir,
                    os.pardir))

if os.path.exists(os.path.join(possible_topdir,"gsyncer","__init__.py")):
    sys.path.insert(0,possible_topdir)

#print possible_topdir
from gsyncer.monitor import app


if __name__ == '__main__':
    httpd = make_server('',8082,app.Monitor(app.urls))
    print 'Serving on port 8082'
    httpd.serve_forever()

