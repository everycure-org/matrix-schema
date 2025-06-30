import pyspark.sql.types as T
import pandera as pa

from matrix.utils.pandera_utils import Column, DataFrameSchema

# Import the enums from the pydantic model
from .matrix_schema import (
    PredicateEnum,
    NodeCategoryEnum,
    KnowledgeLevelEnum,
    AgentTypeEnum
)


MATRIX_NODE_SCHEMA = DataFrameSchema(
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

MATRIX_EDGE_SCHEMA = DataFrameSchema(
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