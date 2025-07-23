import logging
import unittest
from zensols.propbankdb import Roleset, Database, ApplicationFactory


if 0:
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)


class TestEmbedding(unittest.TestCase):
    def test_embedding(self):
        db: Database = ApplicationFactory.get_database()
        rs: Roleset = db.roleset_stash['indurate.01']
        self.assertTrue(isinstance(rs, Roleset))
        emb = rs.embedding
        self.assertTrue(emb is not None)
        self.assertEqual(768, emb.size(0))
