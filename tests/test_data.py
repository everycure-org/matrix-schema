"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from matrix_schema.datamodel.matrix_schema import MatrixEdgeList, MatrixNodeList, MatrixDiseaseList

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            if "MatrixEdgeList" in path:
                obj = yaml_loader.load(path, target_class=MatrixEdgeList)
            elif "MatrixNodeList" in path:
                obj = yaml_loader.load(path, target_class=MatrixNodeList)
            elif "MatrixDiseaseList" in path:
                obj = yaml_loader.load(path, target_class=MatrixDiseaseList)
            assert obj
