import pandera as pa
from pandera import Column, DataFrameSchema, Check, Index


MATRIXNODE_SCHEMA = DataFrameSchema({
    
    "id": Column(
        str,
        nullable=False
    ),
    "name": Column(
        str,
        nullable=True
    ),
    "category": Column(
        str,
        nullable=False
    ),
    "description": Column(
        str,
        nullable=True
    ),
    "equivalent_identifiers": Column(
        str,
        nullable=True
    ),
    "all_categories": Column(
        str,
        nullable=True
    ),
    "publications": Column(
        str,
        nullable=True
    ),
    "labels": Column(
        str,
        nullable=True
    ),
    "international_resource_identifier": Column(
        str,
        nullable=True
    ),
    "upstream_data_source": Column(
        str,
        nullable=False
    ),
},

    unique=["id", ],

    strict=True,
    coerce=True,
)

MATRIXEDGE_SCHEMA = DataFrameSchema({
    
    "subject": Column(
        str,
        nullable=False
    ),
    "predicate": Column(
        str,
        nullable=False
    ),
    "object": Column(
        str,
        nullable=False
    ),
    "knowledge_level": Column(
        str,
        nullable=True
    ),
    "primary_knowledge_source": Column(
        str,
        nullable=True
    ),
    "aggregator_knowledge_source": Column(
        str,
        nullable=True
    ),
    "publications": Column(
        str,
        nullable=True
    ),
    "subject_aspect_qualifier": Column(
        str,
        nullable=True
    ),
    "subject_direction_qualifier": Column(
        str,
        nullable=True
    ),
    "object_aspect_qualifier": Column(
        str,
        nullable=True
    ),
    "object_direction_qualifier": Column(
        str,
        nullable=True
    ),
    "upstream_data_source": Column(
        str,
        nullable=False
    ),
},

    unique=["subject", "predicate", "object", ],

    strict=True,
    coerce=True,
)

MATRIXEDGECOLLECTION_SCHEMA = DataFrameSchema({
    
    "entries": Column(
        str,
        nullable=True
    ),
},

    strict=True,
    coerce=True,
)
