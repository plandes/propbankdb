import logging
import unittest
import sys
from io import StringIO
from zensols.cli import CliHarness
from zensols.propbankdb import Function, Database
from zensols.propbankdb.load import FramesetParser

if 0:
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)


class TestDb(unittest.TestCase):
    def setUp(self):
        harness = CliHarness(
            app_factory_class='zensols.propbankdb.ApplicationFactory',
            app_config_resource='deploy-resources/app.conf')
        self.fac = harness.get_config_factory('-c test-resources/test.conf --level err')
        self.maxDiff = sys.maxsize
        loader = self.fac('pbdb_db_loader')
        self.fs_limit: int = 10
        if not loader.db.conn_manager.db_file.is_file():
            loader.frameset_limit = self.fs_limit
            loader()

    def test_fuction(self):
        persister = self.fac('pbdb_function_persister')
        func = persister.get_by_label('PAG')
        self.assertEqual(Function, type(func))
        self.assertEqual('PAG', func.label)
        self.assertEqual('default', func.group)

        func2 = Function(
            label=func.label,
            description=func.description,
            group=func.group)
        self.assertEqual(func, func2)
        self.assertEqual(hash(func), hash(func2))

        func2.label = 'different'
        self.assertNotEqual(func, func2)
        self.assertNotEqual(hash(func), hash(func2))

        func3 = persister.get_by_label('PAG')
        self.assertEqual(func, func3)
        self.assertEqual(id(func), id(func3))

    def _test_pred_equal(self, pred1, pred2):
        sio1 = StringIO()
        sio2 = StringIO()
        pred1.write(writer=sio1)
        pred2.write(writer=sio2)
        self.assertEqual(sio1.getvalue(), sio2.getvalue())
        self.assertEqual(pred1, pred2)

        pred1.lemma = 'monkey wrench'
        with self.assertRaises(AssertionError):
            self._test_pred_equal(pred1, pred2)

    def test_db_get_predicate(self):
        parser = self.fac('pbdb_parser')
        db = self.fac('pbdb_db')
        fs = parser(1)[0]
        pred1 = fs.predicates[0]
        pred2 = db.get_predicate(pred1.lemma)
        self._test_pred_equal(pred1, pred2)

    def test_db_iterate_framesets(self):
        parser: FramesetParser = self.fac('pbdb_parser')
        db: Database = self.fac('pbdb_db')
        parsed = sorted(parser(self.fs_limit))
        loaded = sorted(db.get_framesets())
        self.assertEqual(len(parsed), len(loaded))
        for fs1, fs2 in zip(parsed, loaded):
            for pred1, pred2 in zip(fs1.predicates, fs2.predicates):
                self._test_pred_equal(pred1, pred2)

    def test_db_get_roleset(self):
        parser = self.fac('pbdb_parser')
        db = self.fac('pbdb_db')
        # important: you must get the stash from the database for correct
        # initialization
        stash = db.roleset_stash
        fs = parser(1)[0]
        rs1 = fs.predicates[0].rolesets[0]
        rs2 = stash[str(rs1.id)]
        sio1 = StringIO()
        sio2 = StringIO()
        rs1.write(writer=sio1)
        rs2.write(writer=sio2)
        self.assertEqual(sio1.getvalue(), sio2.getvalue())
        self.assertEqual(rs1, rs2)

    def test_db_iter_predicate(self):
        db = self.fac('pbdb_db')
        # important: you must get the stash from the database for correct
        # initialization
        stash = db.predicate_stash
        # force all predicates to
        for k, v in stash:
            assert len(k) > 0
