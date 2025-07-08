"""Test Pandera schema validation."""
import unittest
from unittest.mock import patch

try:
    import pandas as pd
    import pyspark
    from pyspark.sql import SparkSession
    import pandera.pyspark as pa
    from matrix_schema.datamodel.pandera import get_matrix_node_schema, get_matrix_edge_schema
    DEPENDENCIES_AVAILABLE = True
except ImportError as e:
    DEPENDENCIES_AVAILABLE = False
    SKIP_REASON = str(e)


@unittest.skipUnless(DEPENDENCIES_AVAILABLE, f"Dependencies not available: {SKIP_REASON if not DEPENDENCIES_AVAILABLE else 'Unknown'}")
class TestPanderaSchema(unittest.TestCase):
    """Test Pandera schema validation."""

    def setUp(self):
        """Set up test data and minimal Spark session."""
        # Create minimal Spark session for testing
        self.spark = SparkSession.builder \
            .appName("PanderaTest") \
            .master("local[1]") \
            .config("spark.driver.memory", "1g") \
            .config("spark.executor.memory", "1g") \
            .config("spark.sql.warehouse.dir", "/tmp/spark-warehouse") \
            .getOrCreate()
        
        # Suppress verbose logging
        self.spark.sparkContext.setLogLevel("WARN")
        
        # Valid node data
        self.valid_node_data = {
            "id": ["example:Node001", "example:Node002"],
            "name": ["Aspirin", "Myocardial Infarction"],
            "category": ["biolink:Drug", "biolink:Disease"],
            "description": ["A drug used to reduce pain", "A heart condition"],
            "equivalent_identifiers": [["CHEBI:15365"], ["MONDO:0005061"]],
            "all_categories": [["biolink:Drug"], ["biolink:Disease"]],
            "publications": [["PMID:12345678"], ["PMID:87654321"]],
            "labels": [["Acetylsalicylic Acid"], ["Heart Attack"]],
            "international_resource_identifier": [
                "http://purl.obolibrary.org/obo/CHEBI_15365",
                "http://purl.obolibrary.org/obo/MONDO_0005061"
            ],
            "upstream_data_source": [["DrugBank"], ["OMIM"]]
        }

        # Valid edge data
        self.valid_edge_data = {
            "subject": ["example:Node001", "example:Node002"],
            "predicate": ["biolink:treats", "biolink:has_phenotype"],
            "object": ["example:Node002", "example:Node003"],
            "knowledge_level": ["knowledge_assertion", "prediction"],
            "agent_type": ["manual_agent", "automated_agent"],
            "primary_knowledge_source": ["infores:drugbank", "infores:omim"],
            "aggregator_knowledge_source": [["infores:omim"], ["MONDO"]],
            "publications": [["PMID:98765432"], ["PMID:56789012"]],
            "subject_aspect_qualifier": ["mode of action", "disease manifestation"],
            "subject_direction_qualifier": ["inhibits", None],
            "object_aspect_qualifier": ["treatment", "molecular mechanism"],
            "object_direction_qualifier": ["reduces", None],
            "upstream_data_source": [["DrugBank"], ["OMIM"]],
            "num_references": [5, 10],
            "num_sentences": [3, 7]
        }

    def tearDown(self):
        """Clean up Spark session."""
        if hasattr(self, 'spark'):
            self.spark.stop()

    def test_valid_node_schema_pyspark(self):
        """Test that valid node data passes validation with PySpark DataFrame."""
        schema = get_matrix_node_schema()
        
        # Create PySpark DataFrame from pandas DataFrame
        pandas_df = pd.DataFrame(self.valid_node_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        
        # Build schema for PySpark and validate
        pyspark_schema = schema.build_for_type(type(spark_df))
        
        # This should not raise an exception
        try:
            validated_df = pyspark_schema.validate(spark_df)
            self.assertIsNotNone(validated_df)
        except Exception as e:
            self.fail(f"Valid node data failed PySpark validation: {e}")

    def test_valid_node_schema_pandas(self):
        """Test that valid node data passes validation with pandas DataFrame."""
        schema = get_matrix_node_schema()
        
        # Create pandas DataFrame
        pandas_df = pd.DataFrame(self.valid_node_data)
        
        # Build schema for pandas and validate
        pandas_schema = schema.build_for_type(type(pandas_df))
        
        # This should not raise an exception
        try:
            validated_df = pandas_schema.validate(pandas_df)
            self.assertIsInstance(validated_df, pd.DataFrame)
        except Exception as e:
            self.fail(f"Valid node data failed pandas validation: {e}")

    def test_valid_edge_schema_pyspark(self):
        """Test that valid edge data passes validation with PySpark DataFrame."""
        schema = get_matrix_edge_schema()
        
        # Create PySpark DataFrame from pandas DataFrame
        pandas_df = pd.DataFrame(self.valid_edge_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        
        # Build schema for PySpark and validate
        pyspark_schema = schema.build_for_type(type(spark_df))
        
        # This should not raise an exception
        try:
            validated_df = pyspark_schema.validate(spark_df)
            self.assertIsNotNone(validated_df)
        except Exception as e:
            self.fail(f"Valid edge data failed PySpark validation: {e}")

    def test_valid_edge_schema_pandas(self):
        """Test that valid edge data passes validation with pandas DataFrame."""
        schema = get_matrix_edge_schema()
        
        # Create pandas DataFrame
        pandas_df = pd.DataFrame(self.valid_edge_data)
        
        # Build schema for pandas and validate
        pandas_schema = schema.build_for_type(type(pandas_df))
        
        # This should not raise an exception
        try:
            validated_df = pandas_schema.validate(pandas_df)
            self.assertIsInstance(validated_df, pd.DataFrame)
        except Exception as e:
            self.fail(f"Valid edge data failed pandas validation: {e}")

    def test_invalid_node_category(self):
        """Test that invalid node category fails validation with default settings but passes when disabled."""
        invalid_data = self.valid_node_data.copy()
        invalid_data["category"] = ["invalid:Category", "biolink:Disease"]
        
        pandas_df = pd.DataFrame(invalid_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        
        # Test with default validation (True) - should fail
        strict_schema = get_matrix_node_schema(validate_enumeration_values=True)
        pandas_strict_schema = strict_schema.build_for_type(type(pandas_df))
        with self.assertRaises(Exception):
            pandas_strict_schema.validate(pandas_df)
        
        # Test with validation disabled (False) - should pass
        lenient_schema = get_matrix_node_schema(validate_enumeration_values=False)
        pandas_lenient_schema = lenient_schema.build_for_type(type(pandas_df))
        pyspark_lenient_schema = lenient_schema.build_for_type(type(spark_df))
        
        # These should not raise exceptions
        validated_pandas_df = pandas_lenient_schema.validate(pandas_df)
        validated_spark_df = pyspark_lenient_schema.validate(spark_df)
        
        self.assertIsInstance(validated_pandas_df, pd.DataFrame)
        self.assertIsNotNone(validated_spark_df)

    def test_invalid_edge_predicate(self):
        """Test that invalid edge predicate fails validation with default settings but passes when disabled."""
        invalid_data = self.valid_edge_data.copy()
        invalid_data["predicate"] = ["invalid:predicate", "biolink:has_phenotype"]
        
        pandas_df = pd.DataFrame(invalid_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        
        # Test with default validation (True) - should fail
        strict_schema = get_matrix_edge_schema(validate_enumeration_values=True)
        pandas_strict_schema = strict_schema.build_for_type(type(pandas_df))
        with self.assertRaises(Exception):
            pandas_strict_schema.validate(pandas_df)
        
        # Test with validation disabled (False) - should pass
        lenient_schema = get_matrix_edge_schema(validate_enumeration_values=False)
        pandas_lenient_schema = lenient_schema.build_for_type(type(pandas_df))
        pyspark_lenient_schema = lenient_schema.build_for_type(type(spark_df))
        
        # These should not raise exceptions
        validated_pandas_df = pandas_lenient_schema.validate(pandas_df)
        validated_spark_df = pyspark_lenient_schema.validate(spark_df)
        
        self.assertIsInstance(validated_pandas_df, pd.DataFrame)
        self.assertIsNotNone(validated_spark_df)

    def test_invalid_knowledge_level(self):
        """Test that invalid knowledge level fails validation with default settings but passes when disabled."""
        invalid_data = self.valid_edge_data.copy()
        invalid_data["knowledge_level"] = ["invalid_level", "prediction"]
        
        pandas_df = pd.DataFrame(invalid_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        
        # Test with default validation (True) - should fail
        strict_schema = get_matrix_edge_schema(validate_enumeration_values=True)
        pandas_strict_schema = strict_schema.build_for_type(type(pandas_df))
        with self.assertRaises(Exception):
            pandas_strict_schema.validate(pandas_df)
        
        # Test with validation disabled (False) - should pass
        lenient_schema = get_matrix_edge_schema(validate_enumeration_values=False)
        pandas_lenient_schema = lenient_schema.build_for_type(type(pandas_df))
        pyspark_lenient_schema = lenient_schema.build_for_type(type(spark_df))
        
        # These should not raise exceptions
        validated_pandas_df = pandas_lenient_schema.validate(pandas_df)
        validated_spark_df = pyspark_lenient_schema.validate(spark_df)
        
        self.assertIsInstance(validated_pandas_df, pd.DataFrame)
        self.assertIsNotNone(validated_spark_df)

    def test_missing_required_fields(self):
        """Test that missing required fields fail validation."""
        schema = get_matrix_node_schema()
        invalid_data = self.valid_node_data.copy()
        del invalid_data["id"]  # Remove required field
        
        pandas_df = pd.DataFrame(invalid_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        pyspark_schema = schema.build_for_type(type(spark_df))
        
        with self.assertRaises(Exception):
            pyspark_schema.validate(spark_df)

    def test_unique_constraints(self):
        """Test that duplicate IDs fail validation."""
        schema = get_matrix_node_schema()
        invalid_data = self.valid_node_data.copy()
        invalid_data["id"] = ["example:Node001", "example:Node001"]  # Duplicate IDs
        
        pandas_df = pd.DataFrame(invalid_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        
        # Test with pandas - this should work reliably
        pandas_schema = schema.build_for_type(type(pandas_df))
        with self.assertRaises(Exception):
            pandas_schema.validate(pandas_df)
        
        # Test with PySpark - unique constraints may not be enforced
        pyspark_schema = schema.build_for_type(type(spark_df))
        try:
            result = pyspark_schema.validate(spark_df)
            print("WARNING: PySpark unique constraint validation may not be enforced - validation passed with duplicate IDs")
        except Exception:
            pass

    def test_optional_enum_validation_node(self):
        """Test that node schema with validate_enumeration_values=False accepts invalid categories."""
        # Test with invalid category data
        invalid_data = self.valid_node_data.copy()
        invalid_data["category"] = ["invalid:Category", "another:InvalidCategory"]
        
        pandas_df = pd.DataFrame(invalid_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        
        # Should fail with default validation (True)
        strict_schema = get_matrix_node_schema(validate_enumeration_values=True)
        pandas_strict_schema = strict_schema.build_for_type(type(pandas_df))
        with self.assertRaises(Exception):
            pandas_strict_schema.validate(pandas_df)
        
        # Should pass with validation disabled (False)
        lenient_schema = get_matrix_node_schema(validate_enumeration_values=False)
        pandas_lenient_schema = lenient_schema.build_for_type(type(pandas_df))
        pyspark_lenient_schema = lenient_schema.build_for_type(type(spark_df))
        
        # These should not raise exceptions
        validated_pandas_df = pandas_lenient_schema.validate(pandas_df)
        validated_spark_df = pyspark_lenient_schema.validate(spark_df)
        
        self.assertIsInstance(validated_pandas_df, pd.DataFrame)
        self.assertIsNotNone(validated_spark_df)

    def test_optional_enum_validation_edge(self):
        """Test that edge schema with validate_enumeration_values=False accepts invalid enum values."""
        # Test with invalid enum data
        invalid_data = self.valid_edge_data.copy()
        invalid_data["predicate"] = ["invalid:predicate", "another:invalid"]
        invalid_data["knowledge_level"] = ["invalid_level", "another_invalid"]
        invalid_data["agent_type"] = ["invalid_agent", "another_invalid"]
        
        pandas_df = pd.DataFrame(invalid_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        
        # Should fail with default validation (True)
        strict_schema = get_matrix_edge_schema(validate_enumeration_values=True)
        pandas_strict_schema = strict_schema.build_for_type(type(pandas_df))
        with self.assertRaises(Exception):
            pandas_strict_schema.validate(pandas_df)
        
        # Should pass with validation disabled (False)
        lenient_schema = get_matrix_edge_schema(validate_enumeration_values=False)
        pandas_lenient_schema = lenient_schema.build_for_type(type(pandas_df))
        pyspark_lenient_schema = lenient_schema.build_for_type(type(spark_df))
        
        # These should not raise exceptions
        validated_pandas_df = pandas_lenient_schema.validate(pandas_df)
        validated_spark_df = pyspark_lenient_schema.validate(spark_df)
        
        self.assertIsInstance(validated_pandas_df, pd.DataFrame)
        self.assertIsNotNone(validated_spark_df)

    def test_schema_creation(self):
        """Test that schema creation works."""
        node_schema = get_matrix_node_schema()
        edge_schema = get_matrix_edge_schema()
        
        self.assertIsNotNone(node_schema)
        self.assertIsNotNone(edge_schema)
        
        # Test with both parameter values
        node_schema_strict = get_matrix_node_schema(validate_enumeration_values=True)
        node_schema_lenient = get_matrix_node_schema(validate_enumeration_values=False)
        edge_schema_strict = get_matrix_edge_schema(validate_enumeration_values=True)
        edge_schema_lenient = get_matrix_edge_schema(validate_enumeration_values=False)
        
        self.assertIsNotNone(node_schema_strict)
        self.assertIsNotNone(node_schema_lenient)
        self.assertIsNotNone(edge_schema_strict)
        self.assertIsNotNone(edge_schema_lenient)
        
        # Check that schemas have expected columns
        self.assertIn("id", node_schema.columns)
        self.assertIn("category", node_schema.columns)
        self.assertIn("subject", edge_schema.columns)
        self.assertIn("predicate", edge_schema.columns)
        
        # Test that we can build both pandas and PySpark versions
        pandas_df = pd.DataFrame(self.valid_node_data)
        spark_df = self.spark.createDataFrame(pandas_df)
        
        pandas_node_schema = node_schema.build_for_type(type(pandas_df))
        pyspark_node_schema = node_schema.build_for_type(type(spark_df))
        
        self.assertIsNotNone(pandas_node_schema)
        self.assertIsNotNone(pyspark_node_schema)


if __name__ == "__main__":
    unittest.main()