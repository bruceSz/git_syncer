
import os
import sys

possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                        os.pardir,
                                       os.pardir,
                                       os.pardir))

if os.path.exists(os.path.join(possible_topdir,"gsyncer", "__init__.py")):
        sys.path.insert(0, possible_topdir)



import gsyncer.agent.gsyncer as gsyncer

if __name__ == '__main__':

    gscer = gsyncer.Gsyncer('/fedora_home/brucesz/work/scripts-ccs','origin','development','origin','development')
    gscer.sync()
