import unittest

from framework.repo.featureaccess import FeatureAccess
from unittest.mock import patch, Mock


class GetFeaturesTest(unittest.TestCase):
    @patch('framework.athena.repository')
    def test_get_features(self, MockAthena):
        a = MockAthena()
        a.get.return_value = [
            ['part', 'value']
        ]
        feats = FeatureAccess(a).get()
        assert(feats[0][0] == "part")
