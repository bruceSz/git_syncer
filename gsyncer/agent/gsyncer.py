import os
import sys


class Gsyncer(object):
    def __init__(self,dir_name,source_url,source_branch,dest_url,dest_branch):
        self.dir_name = dir_name
        self.source_url = source_url
        self.dest_url = dest_url

        # currently, to make it easy,treat two of these branch equal.

        self.source_branch = source_branch
        self.dest_branch = dest_branch
    def sync(self):
        try: 
            os.chdir(self.dir_name)
            # assume the source_url means the source_url_alias,dest_url is the same
        except OSError :
            print >>sys.stderr,"check into dir:",self.dir_name,' error !'
            sys.exit(0)

        pull(self.source_url,self.source_branch)
        push(self.dest_url,self.dest_branch)


def pull(url_alias,branch):
    if os.system('git pull '+url_alias+' '+branch) == 0:
        print >>sys.stdout,'git pull succeed ! '
    else:
        print >>sys.stderr,"git pull error !"

def push(url_alias,branch):
    if os.system('git push '+url_alias+' '+branch) ==0:
        print >>sys.stdout,'git push succeed ! '
    else:
        print >>sys.stderr,"git push error !"

def ls(dir_name):
    if os.system('ls '+dir_name)==0:
        print >>sys.stdout,'ls succeed ! '
    else:
        print >>sys.stderr,"ls error !"


if __name__ == '__main__':
    gsyncer = Gsyncer('/fedora_home/brucesz/work/scripts-ccs','origin','development','origin','development')
    gsyncer.sync()

