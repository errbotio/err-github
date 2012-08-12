import logging
from errbot.botplugin import BotPlugin
from errbot.jabberbot import botcmd
from errbot.builtins.webserver import webhook
from flask import request
"""
Example post from github:
    {u'forced': False, u'compare': u'https://github.com/gbin/test/compare/b3cd9e66e52e...833392a49245', u'pusher': {u'name': u'gbin', u'email': u'gbin@gootz.net'}, u'repository': {u'fork': False, u'has_wiki': True, u'name': u'test', u'has_downloads': True, u'url': u'https://github.com/gbin/test', u'created_at': u'2012-08-12T16:09:43-07:00', u'description': u'ignore this, this is for testing the new err github integration', u'private': False, u'pushed_at': u'2012-08-12T16:42:38-07:00', u'owner': {u'name': u'gbin', u'email': u'gbin@gootz.net'}, u'watchers': 0, u'open_issues': 0, u'has_issues': True, u'forks': 0, u'stargazers': 0, u'size': 128}, u'head_commit': {u'committer': {u'username': u'gbin', u'name': u'Guillaume BINET', u'email': u'gbin@gootz.net'}, u'added': [], u'author': {u'username': u'gbin', u'name': u'Guillaume BINET', u'email': u'gbin@gootz.net'}, u'url': u'https://github.com/gbin/test/commit/833392a492453e6837173d7740c16f51e958e63f', u'timestamp': u'2012-08-12T16:40:27-07:00', u'modified': [u'README.md'], u'distinct': True, u'message': u'this time ?', u'removed': [], u'id': u'833392a492453e6837173d7740c16f51e958e63f'}, u'deleted': False, u'commits': [{u'committer': {u'username': u'gbin', u'name': u'Guillaume BINET', u'email': u'gbin@gootz.net'}, u'added': [], u'author': {u'username': u'gbin', u'name': u'Guillaume BINET', u'email': u'gbin@gootz.net'}, u'url': u'https://github.com/gbin/test/commit/833392a492453e6837173d7740c16f51e958e63f', u'timestamp': u'2012-08-12T16:40:27-07:00', u'modified': [u'README.md'], u'distinct': True, u'message': u'this time ?', u'removed': [], u'id': u'833392a492453e6837173d7740c16f51e958e63f'}], u'after': u'833392a492453e6837173d7740c16f51e958e63f', u'created': False, u'ref': u'refs/heads/master', u'before': u'b3cd9e66e52e4783c1a0b98fbaaad6258669275f'}
"""
class Github(BotPlugin):
    @webhook(r'/github-notifs/', form_param = 'payload')
    def notification(self, incoming_request):
        logging.info(str(incoming_request))

                                                                                                                
