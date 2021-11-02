# file: tests/fixtures.py
#
# Pytest fixtures for salt
#

import pytest
import os
import logging
from salt import client
from salt import config
from salt import output
from salt.utils.odict import OrderedDict


class TestCaller(client.Caller):
    '''
    Salt API client Caller for test fixtures
    '''

    def test_state_show_sls(self, state):
        '''
        Run state.show_sls and return true if successful
        '''

        ret = self.cmd('state.show_sls', state)

        if type(ret) == OrderedDict:
            return True
        else:
            self.display_output(ret)
            return False


    def test_state_apply(self, state, mock=False, test=False):
        '''
        Run state apply and return true if successful
        '''

        ret = self.cmd('state.apply', state, mock=mock, test=False)

        if not type(ret) == dict:
            self.display_output(ret)
            return False
        for r_ in ret.values():
            if not r_['result']:
                self.display_output(ret)
                return False
        return True


    def display_output(self, ret):
        '''
        Display output as yaml
        '''
        output.display_output({'local': ret}, out='yaml', opts=self.opts)


@pytest.fixture()
def salt_caller(request, caplog):
    '''
    Return a TestCaller object
    '''

    caplog.set_level(logging.WARNING)
    minion_opts = config.minion_config(os.path.join(str(request.config.rootdir), 'etc', 'salt', 'minion'))
    minion_opts['file_client'] = 'local'
    minion_opts['id'] = 'local-dev'

    caller = TestCaller(mopts=minion_opts)
    return caller
