"""Integration tests for Pandera schema with real example data."""
import os
import unittest
import pandas as pd
import yaml
from typing import Dict, Any

from matrix_schema.datamodel.pandera import get_matrix_node_schema, get_matrix_edge_schema


class TestPanderaIntegration(unittest.TestCase):
    """Integration tests using real example data files."""

    def setUp(self):
        """Set up paths to example data."""
        self.root = os.path.join(os.path.dirname(__file__), '..')
        self.data_dir = os.path.join(self.root, "src", "data", "examples", "valid")
        
        self.node_file = os.path.join(self.data_dir, "MatrixNodeList-001.yaml")
        self.edge_file = os.path.join(self.data_dir, "MatrixEdgeList-001.yaml")

    def load_yaml_data(self, file_path: str) -> Dict[str, Any]:
        """Load YAML data from file."""
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    def test_real_node_data_validation(self):
        """Test Pandera validation against real node example data."""
        if not os.path.exists(self.node_file):
            self.skipTest(f"Node example file not found: {self.node_file}")

        # Load example data
        data = self.load_yaml_data(self.node_file)
        nodes = data.get('nodes', [])
        
        if not nodes:
            self.skipTest("No nodes found in example data")

        # Convert to DataFrame format expected by Pandera
        df_data = {
            'id': [],
            'name': [],
            'category': [],
            'description': [],
            'equivalent_identifiers': [],
            'all_categories': [],
            'publications': [],
            'labels': [],
            'international_resource_identifier': [],
            'upstream_data_source': []
        }

        for node in nodes:
            for key in df_data.keys():
                df_data[key].append(node.get(key))

        df = pd.DataFrame(df_data)
        
        # Validate with Pandera schema
        schema = get_matrix_node_schema()
        pandas_schema = schema.build_for_type(type(df))
        try:
            validated_df = pandas_schema.validate(df)
            self.assertIsInstance(validated_df, pd.DataFrame)
            self.assertEqual(len(validated_df), len(nodes))
        except Exception as e:
            self.fail(f"Real node data failed Pandera validation: {e}")

    def test_real_edge_data_validation(self):
        """Test Pandera validation against real edge example data."""
        if not os.path.exists(self.edge_file):
            self.skipTest(f"Edge example file not found: {self.edge_file}")

        # Load example data
        data = self.load_yaml_data(self.edge_file)
        edges = data.get('edges', [])
        
        if not edges:
            self.skipTest("No edges found in example data")

        # Convert to DataFrame format expected by Pandera
        df_data = {
            'subject': [],
            'predicate': [],
            'object': [],
            'knowledge_level': [],
            'agent_type': [],
            'primary_knowledge_source': [],
            'aggregator_knowledge_source': [],
            'publications': [],
            'subject_aspect_qualifier': [],
            'subject_direction_qualifier': [],
            'object_aspect_qualifier': [],
            'object_direction_qualifier': [],
            'upstream_data_source': [],
            'num_references': [],
            'num_sentences': []
        }

        for edge in edges:
            for key in df_data.keys():
                df_data[key].append(edge.get(key))

        df = pd.DataFrame(df_data)
        
        # Validate with Pandera schema
        schema = get_matrix_edge_schema()
        pandas_schema = schema.build_for_type(type(df))
        try:
            validated_df = pandas_schema.validate(df)
            self.assertIsInstance(validated_df, pd.DataFrame)
            self.assertEqual(len(validated_df), len(edges))
        except Exception as e:
            self.fail(f"Real edge data failed Pandera validation: {e}")

    def test_enum_values_in_real_data(self):
        """Test that enum values in real data are valid."""
        # Test node categories
        if os.path.exists(self.node_file):
            data = self.load_yaml_data(self.node_file)
            nodes = data.get('nodes', [])
            
            from matrix_schema.datamodel.matrix_schema_pydantic import NodeCategoryEnum
            valid_categories = [cat.value for cat in NodeCategoryEnum]
            
            for node in nodes:
                category = node.get('category')
                if category:
                    self.assertIn(category, valid_categories, 
                                f"Invalid category in real data: {category}")

        # Test edge predicates
        if os.path.exists(self.edge_file):
            data = self.load_yaml_data(self.edge_file)
            edges = data.get('edges', [])
            
            from matrix_schema.datamodel.matrix_schema_pydantic import PredicateEnum, KnowledgeLevelEnum, AgentTypeEnum
            valid_predicates = [pred.value for pred in PredicateEnum]
            valid_knowledge_levels = [kl.value for kl in KnowledgeLevelEnum]
            valid_agent_types = [at.value for at in AgentTypeEnum]
            
            for edge in edges:
                predicate = edge.get('predicate')
                if predicate:
                    self.assertIn(predicate, valid_predicates,
                                f"Invalid predicate in real data: {predicate}")
                
                knowledge_level = edge.get('knowledge_level')
                if knowledge_level:
                    self.assertIn(knowledge_level, valid_knowledge_levels,
                                f"Invalid knowledge_level in real data: {knowledge_level}")
                
                agent_type = edge.get('agent_type')
                if agent_type:
                    self.assertIn(agent_type, valid_agent_types,
                                f"Invalid agent_type in real data: {agent_type}")

if __name__ == "__main__":
    unittest.main()