import gsyncer

class Manager(object):
    def __init__(self,conf):
        self._conf = conf
        self.agents = {}
        for repo in conf.repos:
            repo_source_url = '%s_source_url'%(repo,)
            repo_dest_url = '%s_dest_url'%(repo,)
            repo_source_branch = '%s_source_branch'%(repo,)
            repo_dest_branch='%s_dest_branch'%(repo,)

            repo_dir = '%s_dir_name'%(repo,)

            repo_dir = getattr(conf,repo_dir)

            repo_source_url = getattr(conf,repo_source_url)
            repo_source_branch = getattr(conf,repo_source_branch)

            repo_dest_url = getattr(conf,repo_dest_url)
            repo_dest_branch = getattr(conf,repo_dest_branch)
            gscer = gsyncer.Gsyncer(repo_dir,
                                    repo_source_url,
                                    repo_source_branch,
                                    repo_dest_url,
                                    repo_dest_branch)


            # note:the manager will not be thread safe,
            # only one thread should run this.
            self.agents[repo] = [(repo_dir,gscer),(repo_source_url,repo_source_branch),(repo_dest_url,repo_dest_branch)]

    def sync(self,repo_name):
        self.agents[repo_name][0][1].sync()
        #print self.agents[repo_name]


