
import os
import sys
possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                        os.pardir,
                                       os.pardir,
                                       os.pardir))

if os.path.exists(os.path.join(possible_topdir,"gsyncer", "__init__.py")):
        sys.path.insert(0, possible_topdir)

import gsyncer.agent.manager as agent_manager
import gsyncer.rpc.manager as rpc_manager

from gsyncer.common.config import CONF 

def get_manager(module_name='agent'):
    if module_name == 'agent':
        return agent_manager.Manager(CONF)
    else:
        return rpc_manager.Manager(CONF)


if __name__ == '__main__':
    manager = get_manager()
    manager.sync('scripts-ccs')
