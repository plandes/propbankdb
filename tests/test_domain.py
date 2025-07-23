import logging
import unittest
from zensols.propbankdb import RolesetId


if 0:
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)


class TestDomain(unittest.TestCase):
    def test_propbank_id(self):
        pid = RolesetId('see.01')
        self.assertEqual('see.01', pid.label)
        self.assertEqual('see', pid.lemma)
        self.assertEqual(1, pid.index)
        self.assertTrue(pid.is_valid)

        pid = RolesetId('see-01')
        # role set takes canonical form using dot (rather than dashs found in
        # AMR concepts)
        self.assertEqual('see.01', pid.label)
        self.assertEqual('see', pid.lemma)
        self.assertEqual(1, pid.index)
        self.assertTrue(pid.is_valid)

        pid = RolesetId('see')
        self.assertEqual('see', pid.label)
        self.assertEqual(None, pid.lemma)
        self.assertEqual(None, pid.index)
        self.assertFalse(pid.is_valid)

        pid = RolesetId('see@01')
        self.assertEqual('see@01', pid.label)
        self.assertEqual(None, pid.lemma)
        self.assertEqual(None, pid.index)
        self.assertFalse(pid.is_valid)

        self.assertEqual(RolesetId('see.01'), RolesetId('see.01'))
