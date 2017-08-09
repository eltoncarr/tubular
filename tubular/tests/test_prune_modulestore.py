"""
Tests for pruning modulestore
"""

from __future__ import absolute_import

import json
import logging
import os
import sys
import unittest

import tubular.scripts.prune_modulestore as pruning_script


class TestModuleStorePruning(unittest.TestCase):
    u"""
    Test basic modulestore pruning
    """

    # output file for post-prune data
    output_file = u"output.json"

    # input file: static dataset
    input_file = u"test_prune_modulestore_data.json"

    def removeOutputFile(self):
        # check if the specified file exists
        file_exists = os.path.isfile(self.output_file)

        assert isinstance(file_exists, object)
        if file_exists:
            # there is residual output
            os.remove(self.output_file)

    def setUp(self):
        # make sure we remove any residual output file
        # this is defensive
        self.removeOutputFile()

    def tearDown(self):
        # make sure we remove any residual output fileimport tubular.jenkins as jenkins
        self.removeOutputFile()

    def testPrune(self):
        # stub
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
