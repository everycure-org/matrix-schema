try:
    import pyspark.sql.types as T
    PYSPARK_AVAILABLE = True
except ImportError:
    T = None
    PYSPARK_AVAILABLE = False

try:
    import pandera.pyspark as pa
    from pandera.pyspark import Column, DataFrameSchema
    PANDERA_AVAILABLE = True
except ImportError:
    pa = None
    Column = None
    DataFrameSchema = None
    PANDERA_AVAILABLE = False

# Import the enums from the pydantic model
from .matrix_schema_pydantic import (
    PredicateEnum,
    NodeCategoryEnum,
    KnowledgeLevelEnum,
    AgentTypeEnum
)


def get_matrix_node_schema():
    """Get the Pandera schema for MatrixNode validation."""
    if not PYSPARK_AVAILABLE:
        raise ImportError("PySpark is required for Pandera schema. Install with: pip install pyspark")
    if not PANDERA_AVAILABLE:
        raise ImportError("Pandera PySpark is required for schema validation. Install with: pip install 'pandera[pyspark]'")
    
    return DataFrameSchema(
        columns={
            "id": Column(T.StringType(), nullable=False),
            "name": Column(T.StringType(), nullable=True),
            "category": Column(T.StringType(), nullable=False, 
                             checks=pa.Check.isin([category.value for category in NodeCategoryEnum])),
            "description": Column(T.StringType(), nullable=True),
            "equivalent_identifiers": Column(T.ArrayType(T.StringType()), nullable=True),
            "all_categories": Column(T.ArrayType(T.StringType()), nullable=True),
            "publications": Column(T.ArrayType(T.StringType()), nullable=True),
            "labels": Column(T.ArrayType(T.StringType()), nullable=True),
            "international_resource_identifier": Column(T.StringType(), nullable=True),
            "upstream_data_source": Column(T.ArrayType(T.StringType()), nullable=True),
        },
        unique=["id"],
        strict=True,
    )


def get_matrix_edge_schema():
    """Get the Pandera schema for MatrixEdge validation."""
    if not PYSPARK_AVAILABLE:
        raise ImportError("PySpark is required for Pandera schema. Install with: pip install pyspark")
    if not PANDERA_AVAILABLE:
        raise ImportError("Pandera PySpark is required for schema validation. Install with: pip install 'pandera[pyspark]'")
    
    return DataFrameSchema(
        columns={
            "subject": Column(T.StringType(), nullable=False),
            "predicate": Column(T.StringType(), nullable=False,
                              checks=pa.Check.isin([predicate.value for predicate in PredicateEnum])),
            "object": Column(T.StringType(), nullable=False),
            "knowledge_level": Column(T.StringType(), nullable=True,
                                    checks=pa.Check.isin([level.value for level in KnowledgeLevelEnum])),
            "agent_type": Column(T.StringType(), nullable=True,
                               checks=pa.Check.isin([agent.value for agent in AgentTypeEnum])),
            "primary_knowledge_source": Column(T.StringType(), nullable=True),
            "aggregator_knowledge_source": Column(T.ArrayType(T.StringType()), nullable=True),
            "publications": Column(T.ArrayType(T.StringType()), nullable=True),
            "subject_aspect_qualifier": Column(T.StringType(), nullable=True),
            "subject_direction_qualifier": Column(T.StringType(), nullable=True),
            "object_aspect_qualifier": Column(T.StringType(), nullable=True),
            "object_direction_qualifier": Column(T.StringType(), nullable=True),
            "upstream_data_source": Column(T.ArrayType(T.StringType()), nullable=True),
            # Additional fields from original pandera schema
            "num_references": Column(T.IntegerType(), nullable=True),
            "num_sentences": Column(T.IntegerType(), nullable=True),
        },
        unique=["subject", "predicate", "object"],
        strict=True,
    )