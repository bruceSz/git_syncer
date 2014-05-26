import ConfigParser
import os
import sys
CONF = None

config_name="gsyncer.conf"
#possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
#                                                os.pardir,
#                                                os.pardir))
print possible_topdir
if not os.path.exists(os.path.join(possible_topdir,"etc",config_name)):
    print >> stderr, "config file not found!!!"
    sys.exit(1)

config_path= os.path.join(possible_topdir,"etc")

class Config(object):
    def __init__(self,config_path,config_file):
        cf=ConfigParser.ConfigParser()
        cf.read(config_file)

        scs = cf.sections()
        for sc in scs:
            ops = cf.options(sc)
            for op in ops:
                if op == 'repos':
                    repos = cf.get(sc,op)
                    repos = repos.split(',')
                    self.__dict__[op]=repos
                else:
                    self.__dict__[op] = cf.get(sc,op)


def _init():
    global CONF
    if CONF:
        return CONF
    else:
        CONF = _do_init()
        return CONF

def _do_init():

    #global config_name
    #global possible_topdir 
    #global config_path
    pass

def test_config_parser():
    cf = ConfigParser.ConfigParser()
    cf.read("gsyncer.conf")

    ops = cf.options("default")
    for op in ops:
        print op,cf.get("default",op)


CONF = Config()

