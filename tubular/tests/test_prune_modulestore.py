"""
Tests for pruning modulestore. 
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import json
import logging
import os
import sys
import unittest

import ddt

@ddt.ddt
class TestModuleStorePruning(unittest.TestCase):
    u"""
    Test basic modulestore pruning
    """
    def testPrune(self): 
        self.assertEqual((True, True)
    

if __name__ == '__main__':
    unittest.main()

