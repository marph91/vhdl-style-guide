import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import variable
from vsg import vhdlFile
from vsg.tests import utils


class testFixRuleVariableMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','variable','variable_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(self.lFile)

    def test_fix_rule_001(self):
        oRule = variable.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = variable.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = variable.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = variable.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = variable.rule_006()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = variable.rule_007()
        self.assertFalse(oRule.fixable)

    def test_fix_rule_010(self):
        oRule = variable.rule_010()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
