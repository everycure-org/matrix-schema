"""Test Pandera schema with PySpark DataFrames."""
import unittest
from unittest.mock import patch, MagicMock

from matrix_schema.datamodel.pandera import get_matrix_node_schema, get_matrix_edge_schema


class TestPanderaPySpark(unittest.TestCase):
    """Test Pandera schema with PySpark DataFrames."""

    def setUp(self):
        """Set up test data for PySpark."""
        # Mock PySpark DataFrame data
        self.valid_node_rows = [
            {
                "id": "example:Node001",
                "name": "Aspirin",
                "category": "biolink:Drug",
                "description": "A drug used to reduce pain",
                "equivalent_identifiers": ["CHEBI:15365"],
                "all_categories": ["biolink:Drug"],
                "publications": ["PMID:12345678"],
                "labels": ["Acetylsalicylic Acid"],
                "international_resource_identifier": "http://purl.obolibrary.org/obo/CHEBI_15365",
                "upstream_data_source": ["DrugBank"]
            }
        ]

        self.valid_edge_rows = [
            {
                "subject": "example:Node001",
                "predicate": "biolink:treats",
                "object": "example:Node002",
                "knowledge_level": "knowledge_assertion",
                "agent_type": "manual_agent",
                "primary_knowledge_source": "infores:drugbank",
                "aggregator_knowledge_source": ["infores:omim"],
                "publications": ["PMID:98765432"],
                "subject_aspect_qualifier": "mode of action",
                "subject_direction_qualifier": "inhibits",
                "object_aspect_qualifier": "treatment",
                "object_direction_qualifier": "reduces",
                "upstream_data_source": ["DrugBank"],
                "num_references": 5,
                "num_sentences": 3
            }
        ]

    @patch('matrix_schema.datamodel.pandera.T')
    def test_schema_types(self, mock_types):
        """Test that schema uses correct PySpark types."""
        # Mock PySpark types
        mock_types.StringType.return_value = "StringType"
        mock_types.IntegerType.return_value = "IntegerType"
        mock_types.ArrayType.return_value = "ArrayType"

        node_schema = get_matrix_node_schema()
        edge_schema = get_matrix_edge_schema()

        # Verify schemas were created
        self.assertIsNotNone(node_schema)
        self.assertIsNotNone(edge_schema)

    def test_enum_validation_setup(self):
        """Test that enum validation is properly configured."""
        node_schema = get_matrix_node_schema()
        edge_schema = get_matrix_edge_schema()

        # Check that category column has validation
        category_column = node_schema.columns.get("category")
        self.assertIsNotNone(category_column)
        self.assertTrue(hasattr(category_column, 'checks'))

        # Check that predicate column has validation
        predicate_column = edge_schema.columns.get("predicate")
        self.assertIsNotNone(predicate_column)
        self.assertTrue(hasattr(predicate_column, 'checks'))

    def test_schema_structure(self):
        """Test schema structure and required fields."""
        node_schema = get_matrix_node_schema()
        edge_schema = get_matrix_edge_schema()

        # Check node schema has all expected columns
        expected_node_columns = [
            "id", "name", "category", "description", "equivalent_identifiers",
            "all_categories", "publications", "labels", 
            "international_resource_identifier", "upstream_data_source"
        ]
        for col in expected_node_columns:
            self.assertIn(col, node_schema.columns)

        # Check edge schema has all expected columns
        expected_edge_columns = [
            "subject", "predicate", "object", "knowledge_level", "agent_type",
            "primary_knowledge_source", "aggregator_knowledge_source", "publications",
            "subject_aspect_qualifier", "subject_direction_qualifier",
            "object_aspect_qualifier", "object_direction_qualifier",
            "upstream_data_source", "num_references", "num_sentences"
        ]
        for col in expected_edge_columns:
            self.assertIn(col, edge_schema.columns)

    def test_unique_constraints(self):
        """Test unique constraints are configured."""
        node_schema = get_matrix_node_schema()
        edge_schema = get_matrix_edge_schema()

        # Check unique constraints
        self.assertEqual(node_schema.unique, ["id"])
        self.assertEqual(edge_schema.unique, ["subject", "predicate", "object"])

    def test_strict_mode(self):
        """Test that schemas are configured in strict mode."""
        node_schema = get_matrix_node_schema()
        edge_schema = get_matrix_edge_schema()

        self.assertTrue(node_schema.strict)
        self.assertTrue(edge_schema.strict)


if __name__ == "__main__":
    unittest.main()