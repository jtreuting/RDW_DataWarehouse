'''
Created on Mar 31, 2014

@author: ejen
'''
import unittest
from edmigrate.utils.iptables import IptablesController, IptablesChecker
from edmigrate.exceptions import IptablesCommandError
from unittest.mock import patch, MagicMock
from edmigrate.utils.constants import Constants
import socket
from mocket.mocket import MocketSocket
import mocket
import subprocess
from unittest import skip

IPTABLES_SAVE_OUTPUT_INPUT = "\n".join([
    "# Generated by iptables-save v1.4.7 on Tue Apr  1 19:37:18 2014 ",
    "*filter ",
    ":INPUT DROP [22:704] ",
    ":FORWARD ACCEPT [0:0] ",
    ":OUTPUT ACCEPT [5102:452884] ",
    ":EDMIGRATE_PGSQL - [0:0] ",
    "-A INPUT -j EDMIGRATE_PGSQL ",
    "-A INPUT -j EDMIGRATE_PGSQL ",
    "-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT "
    "-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT ",
    "-A INPUT -p tcp -m tcp --dport 5432 -j ACCEPT ",
    "-A EDMIGRATE_PGSQL -p tcp -m tcp --dport 5432 -j REJECT --reject-with icmp-port-unreachable ",
    "COMMIT ",
    "# Completed on Tue Apr  1 19:37:18 2014 "
])

IPTABLES_SAVE_OUTPUT_OUTPUT = "\n".join([
    "# Generated by iptables-save v1.4.7 on Tue Apr  1 19:37:18 2014 ",
    "*filter ",
    ":INPUT DROP [22:704] ",
    ":FORWARD ACCEPT [0:0] ",
    ":OUTPUT ACCEPT [5102:452884] ",
    ":EDMIGRATE_PGSQL - [0:0] ",
    "-A OUTPUT -j EDMIGRATE_PGSQL ",
    "-A OUTPUT -j EDMIGRATE_PGSQL ",
    "-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT "
    "-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT ",
    "-A INPUT -p tcp -m tcp --dport 5432 -j ACCEPT ",
    "-A EDMIGRATE_PGSQL -p tcp -m tcp --dport 5432 -j REJECT --reject-with icmp-port-unreachable ",
    "COMMIT ",
    "# Completed on Tue Apr  1 19:37:18 2014 "
])

IPTABLES_SAVE_OUTPUT_NEITHER = "\n".join([
    "# Generated by iptables-save v1.4.7 on Tue Apr  1 19:37:18 2014 ",
    "*filter ",
    ":INPUT DROP [22:704] ",
    ":FORWARD ACCEPT [0:0] ",
    ":OUTPUT ACCEPT [5102:452884] ",
    ":EDMIGRATE_PGSQL - [0:0] ",
    "-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT "
    "-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT ",
    "-A INPUT -p tcp -m tcp --dport 5432 -j ACCEPT ",
    "-A EDMIGRATE_PGSQL -p tcp -m tcp --dport 5432 -j REJECT --reject-with icmp-port-unreachable ",
    "COMMIT ",
    "# Completed on Tue Apr  1 19:37:18 2014 "
])

IPTABLES_SAVE_OUTPUT_BOTH = "\n".join([
    "# Generated by iptables-save v1.4.7 on Tue Apr  1 19:37:18 2014 ",
    "*filter ",
    ":INPUT DROP [22:704] ",
    ":FORWARD ACCEPT [0:0] ",
    ":OUTPUT ACCEPT [5102:452884] ",
    ":EDMIGRATE_PGSQL - [0:0] ",
    "-A INPUT -j EDMIGRATE_PGSQL ",
    "-A INPUT -j EDMIGRATE_PGSQL ",
    "-A OUTPUT -j EDMIGRATE_PGSQL ",
    "-A OUTPUT -j EDMIGRATE_PGSQL ",
    "-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT "
    "-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT ",
    "-A INPUT -p tcp -m tcp --dport 5432 -j ACCEPT ",
    "-A EDMIGRATE_PGSQL -p tcp -m tcp --dport 5432 -j REJECT --reject-with icmp-port-unreachable ",
    "COMMIT ",
    "# Completed on Tue Apr  1 19:37:18 2014 "
])


def side_effect_no_rules(*args, **kwargs):
    if args == (['/usr/bin/sudo', '/sbin/iptables-save'],):
        return IPTABLES_SAVE_OUTPUT_NEITHER
    else:
        return None


def side_effect_only_input(*args, **kwargs):
    if args == (['/usr/bin/sudo', '/sbin/iptables-save'],):
        return IPTABLES_SAVE_OUTPUT_INPUT
    else:
        return None


def side_effect_only_output(*args, **kwargs):
    if args == (['/usr/bin/sudo', '/sbin/iptables-save'],):
        return IPTABLES_SAVE_OUTPUT_OUTPUT
    else:
        return None


def side_effect_both(*args, **kwargs):
    if args == (['/usr/bin/sudo', '/sbin/iptables-save'],):
        return IPTABLES_SAVE_OUTPUT_BOTH
    else:
        return None


class IptableControllerTest(unittest.TestCase):

    def setUp(self):
        self.iptablesController = IptablesController()
        self.iptablesChcker = IptablesChecker()

    def tearDown(self):
        IptablesController._instances = {}

    @patch('subprocess.check_output')
    def test_block_pgsql_input_1(self, MockSubprocess):
        MockSubprocess.side_effect = side_effect_no_rules
        self.iptablesController.block_pgsql_INPUT()
        self.assertEqual(MockSubprocess.call_count, 2)

    @patch('subprocess.check_output')
    def test_block_pgsql_input_2(self, MockSubprocess):
        MockSubprocess.side_effect = side_effect_only_input
        self.iptablesController.block_pgsql_INPUT()
        self.assertEqual(MockSubprocess.call_count, 1)

    @patch('subprocess.check_output')
    def test_block_pgsql_output_1(self, MockSubprocess):
        MockSubprocess.side_effect = side_effect_no_rules
        self.iptablesController.block_pgsql_OUTPUT()
        self.assertEqual(MockSubprocess.call_count, 2)

    @patch('subprocess.check_output')
    def test_block_pgsql_output_2(self, MockSubprocess):
        MockSubprocess.side_effect = side_effect_only_output
        self.iptablesController.block_pgsql_OUTPUT()
        self.assertEqual(MockSubprocess.call_count, 1)

    @patch('subprocess.check_output')
    def test_unblock_pgsql_input_1(self, MockSubprocess):
        MockSubprocess.side_effect = side_effect_only_input
        self.iptablesController.unblock_pgsql_INPUT()
        self.assertEqual(MockSubprocess.call_count, 2)

    @patch('subprocess.check_output')
    def test_unblock_pgsql_input_2(self, MockSubprocess):
        MockSubprocess.side_effect = side_effect_no_rules
        self.iptablesController.unblock_pgsql_INPUT()
        self.assertEqual(MockSubprocess.call_count, 1)

    @patch('subprocess.check_output')
    def test_unblock_pgsql_output_1(self, MockSubprocess):
        MockSubprocess.side_effect = side_effect_only_output
        self.iptablesController.unblock_pgsql_OUTPUT()
        self.assertEqual(MockSubprocess.call_count, 2)

    @patch('subprocess.check_output')
    def test_unblock_pgsql_output_2(self, MockSubprocess):
        MockSubprocess.side_effect = side_effect_no_rules
        self.iptablesController.unblock_pgsql_OUTPUT()
        self.assertEqual(MockSubprocess.call_count, 1)

    @patch.object(mocket.mocket.MocketSocket, 'close')
    @patch('socket.create_connection')
    def test_check_block_input_non_blocked(self, MockSocket, MockMethod):
        MockSocket.side_effect = None
        MockSocket.return_value = mocket.mocket.MocketSocket(socket.AF_INET, socket.SOCK_STREAM)
        MockMethod.return_value = lambda: None
        block_status = self.iptablesChcker.check_block_input('localhost')
        self.assertTrue(block_status)

    @patch.object(mocket.mocket.MocketSocket, 'close')
    @patch('socket.create_connection')
    def test_check_block_output_non_blocked(self, MockSocket, MockMethod):
        MockSocket.side_effect = None
        MockSocket.return_value = mocket.mocket.MocketSocket(socket.AF_INET, socket.SOCK_STREAM)
        MockMethod.return_value = lambda: None
        block_status = self.iptablesChcker.check_block_output('localhost')
        self.assertTrue(block_status)

    @patch.object(mocket.mocket.MocketSocket, 'close')
    @patch('socket.create_connection')
    def test_check_block_input_blocked(self, MockSocket, MockMethod):
        MockSocket.side_effect = ConnectionRefusedError()
        MockSocket.return_value = mocket.mocket.MocketSocket(socket.AF_INET, socket.SOCK_STREAM)
        MockMethod.return_value = lambda: None
        block_status = self.iptablesChcker.check_block_input('localhost')
        self.assertFalse(block_status)

    @patch.object(mocket.mocket.MocketSocket, 'close')
    @patch('socket.create_connection')
    def test_check_block_output_blocked(self, MockSocket, MockMethod):
        MockSocket.side_effect = ConnectionRefusedError()
        MockSocket.return_value = mocket.mocket.MocketSocket(socket.AF_INET, socket.SOCK_STREAM)
        MockMethod.return_value = lambda: None
        block_status = self.iptablesChcker.check_block_output('localhost')
        self.assertFalse(block_status)

    @patch('subprocess.check_output')
    def test_subprocess_exception(self, MockSubprocess):
        MockSubprocess.side_effect = subprocess.CalledProcessError(-1, 'iptables')
        self.assertRaises(IptablesCommandError, self.iptablesController._modify_rule, Constants.IPTABLES_INSERT, Constants.IPTABLES_INPUT_CHAIN)

    @patch('subprocess.check_output')
    def test_check_rules_INPUT(self, MockSubprocess):
        MockSubprocess.return_value = IPTABLES_SAVE_OUTPUT_INPUT
        found = self.iptablesController._check_rules(Constants.IPTABLES_INPUT_CHAIN)
        self.assertTrue(found)
        found = self.iptablesController._check_rules(Constants.IPTABLES_OUTPUT_CHAIN)
        self.assertFalse(found)

    @patch('subprocess.check_output')
    def test_check_rules_OUTPUT(self, MockSubprocess):
        MockSubprocess.return_value = IPTABLES_SAVE_OUTPUT_OUTPUT
        found = self.iptablesController._check_rules(Constants.IPTABLES_INPUT_CHAIN)
        self.assertFalse(found)
        found = self.iptablesController._check_rules(Constants.IPTABLES_OUTPUT_CHAIN)
        self.assertTrue(found)

    @patch('subprocess.check_output')
    def test_check_rules(self, MockSubprocess):
        MockSubprocess.return_value = IPTABLES_SAVE_OUTPUT_NEITHER
        found = self.iptablesController._check_rules(Constants.IPTABLES_INPUT_CHAIN)
        self.assertFalse(found)
        found = self.iptablesController._check_rules(Constants.IPTABLES_OUTPUT_CHAIN)
        self.assertFalse(found)

    @patch('subprocess.check_output')
    def test_check_rules_both(self, MockSubprocess):
        MockSubprocess.return_value = IPTABLES_SAVE_OUTPUT_BOTH
        found = self.iptablesController._check_rules(Constants.IPTABLES_INPUT_CHAIN)
        self.assertTrue(found)
        found = self.iptablesController._check_rules(Constants.IPTABLES_OUTPUT_CHAIN)
        self.assertTrue(found)
