##git_syncer
==========

git_syncer will watch one git repositories and syn with another. Hope i can be easy to be used.

#Usage:
------

* on git repositories node.
    git syncer agent run in background
    it will listen to the rabbitmq-server: topic:sync
    upon receiving the sync message,syncer agent will 
    first pull configure repositories then push configured
    repositories.

* on one node  repositories hooks server will be started.
    if found there is a commit to watched repositories
    sync message related to that repository will be send.


