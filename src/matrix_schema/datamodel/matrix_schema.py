# Auto generated from matrix_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-02-09T09:47:57
# Schema: matrix-schema
#
# id: https://w3id.org/everycure-org/matrix-schema
# description: The collected MATRIX schemas
# license: BSD-3

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MATRIX_SCHEMA = CurieNamespace('matrix_schema', 'https://w3id.org/everycure-org/matrix-schema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MATRIX_SCHEMA


# Types

# Class references
class MatrixNodeId(extended_str):
    pass


@dataclass(repr=False)
class MatrixNode(YAMLRoot):
    """
    A node in the Biolink knowledge graph.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MATRIX_SCHEMA["MatrixNode"]
    class_class_curie: ClassVar[str] = "matrix_schema:MatrixNode"
    class_name: ClassVar[str] = "MatrixNode"
    class_model_uri: ClassVar[URIRef] = MATRIX_SCHEMA.MatrixNode

    id: Union[str, MatrixNodeId] = None
    category: str = None
    upstream_data_source: str = None
    name: Optional[str] = None
    description: Optional[str] = None
    equivalent_identifiers: Optional[str] = None
    all_categories: Optional[str] = None
    publications: Optional[str] = None
    labels: Optional[str] = None
    international_resource_identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MatrixNodeId):
            self.id = MatrixNodeId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, str):
            self.category = str(self.category)

        if self._is_empty(self.upstream_data_source):
            self.MissingRequiredField("upstream_data_source")
        if not isinstance(self.upstream_data_source, str):
            self.upstream_data_source = str(self.upstream_data_source)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.equivalent_identifiers is not None and not isinstance(self.equivalent_identifiers, str):
            self.equivalent_identifiers = str(self.equivalent_identifiers)

        if self.all_categories is not None and not isinstance(self.all_categories, str):
            self.all_categories = str(self.all_categories)

        if self.publications is not None and not isinstance(self.publications, str):
            self.publications = str(self.publications)

        if self.labels is not None and not isinstance(self.labels, str):
            self.labels = str(self.labels)

        if self.international_resource_identifier is not None and not isinstance(self.international_resource_identifier, str):
            self.international_resource_identifier = str(self.international_resource_identifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MatrixEdge(YAMLRoot):
    """
    An edge representing a relationship between two nodes in the Biolink knowledge graph.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MATRIX_SCHEMA["MatrixEdge"]
    class_class_curie: ClassVar[str] = "matrix_schema:MatrixEdge"
    class_name: ClassVar[str] = "MatrixEdge"
    class_model_uri: ClassVar[URIRef] = MATRIX_SCHEMA.MatrixEdge

    subject: str = None
    predicate: str = None
    object: str = None
    upstream_data_source: str = None
    knowledge_level: Optional[str] = None
    primary_knowledge_source: Optional[str] = None
    aggregator_knowledge_source: Optional[str] = None
    publications: Optional[str] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[str] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        if self._is_empty(self.upstream_data_source):
            self.MissingRequiredField("upstream_data_source")
        if not isinstance(self.upstream_data_source, str):
            self.upstream_data_source = str(self.upstream_data_source)

        if self.knowledge_level is not None and not isinstance(self.knowledge_level, str):
            self.knowledge_level = str(self.knowledge_level)

        if self.primary_knowledge_source is not None and not isinstance(self.primary_knowledge_source, str):
            self.primary_knowledge_source = str(self.primary_knowledge_source)

        if self.aggregator_knowledge_source is not None and not isinstance(self.aggregator_knowledge_source, str):
            self.aggregator_knowledge_source = str(self.aggregator_knowledge_source)

        if self.publications is not None and not isinstance(self.publications, str):
            self.publications = str(self.publications)

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, str):
            self.subject_direction_qualifier = str(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, str):
            self.object_direction_qualifier = str(self.object_direction_qualifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MatrixEdgeCollection(YAMLRoot):
    """
    A holder for MatrixEdge objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MATRIX_SCHEMA["MatrixEdgeCollection"]
    class_class_curie: ClassVar[str] = "matrix_schema:MatrixEdgeCollection"
    class_name: ClassVar[str] = "MatrixEdgeCollection"
    class_model_uri: ClassVar[URIRef] = MATRIX_SCHEMA.MatrixEdgeCollection

    entries: Optional[Union[Union[dict, MatrixEdge], List[Union[dict, MatrixEdge]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=MatrixEdge, key_name="subject", keyed=False)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MATRIX_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=MATRIX_SCHEMA.name, name="name", curie=MATRIX_SCHEMA.curie('name'),
                   model_uri=MATRIX_SCHEMA.name, domain=None, range=Optional[str])

slots.category = Slot(uri=MATRIX_SCHEMA.category, name="category", curie=MATRIX_SCHEMA.curie('category'),
                   model_uri=MATRIX_SCHEMA.category, domain=None, range=str)

slots.description = Slot(uri=MATRIX_SCHEMA.description, name="description", curie=MATRIX_SCHEMA.curie('description'),
                   model_uri=MATRIX_SCHEMA.description, domain=None, range=Optional[str])

slots.equivalent_identifiers = Slot(uri=MATRIX_SCHEMA.equivalent_identifiers, name="equivalent_identifiers", curie=MATRIX_SCHEMA.curie('equivalent_identifiers'),
                   model_uri=MATRIX_SCHEMA.equivalent_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.all_categories = Slot(uri=MATRIX_SCHEMA.all_categories, name="all_categories", curie=MATRIX_SCHEMA.curie('all_categories'),
                   model_uri=MATRIX_SCHEMA.all_categories, domain=None, range=Optional[Union[str, List[str]]])

slots.publications = Slot(uri=MATRIX_SCHEMA.publications, name="publications", curie=MATRIX_SCHEMA.curie('publications'),
                   model_uri=MATRIX_SCHEMA.publications, domain=None, range=Optional[Union[str, List[str]]])

slots.labels = Slot(uri=MATRIX_SCHEMA.labels, name="labels", curie=MATRIX_SCHEMA.curie('labels'),
                   model_uri=MATRIX_SCHEMA.labels, domain=None, range=Optional[Union[str, List[str]]])

slots.international_resource_identifier = Slot(uri=MATRIX_SCHEMA.international_resource_identifier, name="international_resource_identifier", curie=MATRIX_SCHEMA.curie('international_resource_identifier'),
                   model_uri=MATRIX_SCHEMA.international_resource_identifier, domain=None, range=Optional[str])

slots.upstream_data_source = Slot(uri=MATRIX_SCHEMA.upstream_data_source, name="upstream_data_source", curie=MATRIX_SCHEMA.curie('upstream_data_source'),
                   model_uri=MATRIX_SCHEMA.upstream_data_source, domain=None, range=Optional[Union[str, List[str]]])

slots.subject = Slot(uri=MATRIX_SCHEMA.subject, name="subject", curie=MATRIX_SCHEMA.curie('subject'),
                   model_uri=MATRIX_SCHEMA.subject, domain=None, range=str)

slots.predicate = Slot(uri=MATRIX_SCHEMA.predicate, name="predicate", curie=MATRIX_SCHEMA.curie('predicate'),
                   model_uri=MATRIX_SCHEMA.predicate, domain=None, range=str)

slots.object = Slot(uri=MATRIX_SCHEMA.object, name="object", curie=MATRIX_SCHEMA.curie('object'),
                   model_uri=MATRIX_SCHEMA.object, domain=None, range=str)

slots.knowledge_level = Slot(uri=MATRIX_SCHEMA.knowledge_level, name="knowledge_level", curie=MATRIX_SCHEMA.curie('knowledge_level'),
                   model_uri=MATRIX_SCHEMA.knowledge_level, domain=None, range=Optional[str])

slots.primary_knowledge_source = Slot(uri=MATRIX_SCHEMA.primary_knowledge_source, name="primary_knowledge_source", curie=MATRIX_SCHEMA.curie('primary_knowledge_source'),
                   model_uri=MATRIX_SCHEMA.primary_knowledge_source, domain=None, range=Optional[str])

slots.aggregator_knowledge_source = Slot(uri=MATRIX_SCHEMA.aggregator_knowledge_source, name="aggregator_knowledge_source", curie=MATRIX_SCHEMA.curie('aggregator_knowledge_source'),
                   model_uri=MATRIX_SCHEMA.aggregator_knowledge_source, domain=None, range=Optional[Union[str, List[str]]])

slots.subject_aspect_qualifier = Slot(uri=MATRIX_SCHEMA.subject_aspect_qualifier, name="subject_aspect_qualifier", curie=MATRIX_SCHEMA.curie('subject_aspect_qualifier'),
                   model_uri=MATRIX_SCHEMA.subject_aspect_qualifier, domain=None, range=Optional[str])

slots.subject_direction_qualifier = Slot(uri=MATRIX_SCHEMA.subject_direction_qualifier, name="subject_direction_qualifier", curie=MATRIX_SCHEMA.curie('subject_direction_qualifier'),
                   model_uri=MATRIX_SCHEMA.subject_direction_qualifier, domain=None, range=Optional[str])

slots.object_aspect_qualifier = Slot(uri=MATRIX_SCHEMA.object_aspect_qualifier, name="object_aspect_qualifier", curie=MATRIX_SCHEMA.curie('object_aspect_qualifier'),
                   model_uri=MATRIX_SCHEMA.object_aspect_qualifier, domain=None, range=Optional[str])

slots.object_direction_qualifier = Slot(uri=MATRIX_SCHEMA.object_direction_qualifier, name="object_direction_qualifier", curie=MATRIX_SCHEMA.curie('object_direction_qualifier'),
                   model_uri=MATRIX_SCHEMA.object_direction_qualifier, domain=None, range=Optional[str])

slots.matrixNode__id = Slot(uri=MATRIX_SCHEMA.id, name="matrixNode__id", curie=MATRIX_SCHEMA.curie('id'),
                   model_uri=MATRIX_SCHEMA.matrixNode__id, domain=None, range=URIRef)

slots.matrixNode__name = Slot(uri=MATRIX_SCHEMA.name, name="matrixNode__name", curie=MATRIX_SCHEMA.curie('name'),
                   model_uri=MATRIX_SCHEMA.matrixNode__name, domain=None, range=Optional[str])

slots.matrixNode__category = Slot(uri=MATRIX_SCHEMA.category, name="matrixNode__category", curie=MATRIX_SCHEMA.curie('category'),
                   model_uri=MATRIX_SCHEMA.matrixNode__category, domain=None, range=str)

slots.matrixNode__description = Slot(uri=MATRIX_SCHEMA.description, name="matrixNode__description", curie=MATRIX_SCHEMA.curie('description'),
                   model_uri=MATRIX_SCHEMA.matrixNode__description, domain=None, range=Optional[str])

slots.matrixNode__equivalent_identifiers = Slot(uri=MATRIX_SCHEMA.equivalent_identifiers, name="matrixNode__equivalent_identifiers", curie=MATRIX_SCHEMA.curie('equivalent_identifiers'),
                   model_uri=MATRIX_SCHEMA.matrixNode__equivalent_identifiers, domain=None, range=Optional[str])

slots.matrixNode__all_categories = Slot(uri=MATRIX_SCHEMA.all_categories, name="matrixNode__all_categories", curie=MATRIX_SCHEMA.curie('all_categories'),
                   model_uri=MATRIX_SCHEMA.matrixNode__all_categories, domain=None, range=Optional[str])

slots.matrixNode__publications = Slot(uri=MATRIX_SCHEMA.publications, name="matrixNode__publications", curie=MATRIX_SCHEMA.curie('publications'),
                   model_uri=MATRIX_SCHEMA.matrixNode__publications, domain=None, range=Optional[str])

slots.matrixNode__labels = Slot(uri=MATRIX_SCHEMA.labels, name="matrixNode__labels", curie=MATRIX_SCHEMA.curie('labels'),
                   model_uri=MATRIX_SCHEMA.matrixNode__labels, domain=None, range=Optional[str])

slots.matrixNode__international_resource_identifier = Slot(uri=MATRIX_SCHEMA.international_resource_identifier, name="matrixNode__international_resource_identifier", curie=MATRIX_SCHEMA.curie('international_resource_identifier'),
                   model_uri=MATRIX_SCHEMA.matrixNode__international_resource_identifier, domain=None, range=Optional[str])

slots.matrixNode__upstream_data_source = Slot(uri=MATRIX_SCHEMA.upstream_data_source, name="matrixNode__upstream_data_source", curie=MATRIX_SCHEMA.curie('upstream_data_source'),
                   model_uri=MATRIX_SCHEMA.matrixNode__upstream_data_source, domain=None, range=str)

slots.matrixEdge__subject = Slot(uri=MATRIX_SCHEMA.subject, name="matrixEdge__subject", curie=MATRIX_SCHEMA.curie('subject'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__subject, domain=None, range=str)

slots.matrixEdge__predicate = Slot(uri=MATRIX_SCHEMA.predicate, name="matrixEdge__predicate", curie=MATRIX_SCHEMA.curie('predicate'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__predicate, domain=None, range=str)

slots.matrixEdge__object = Slot(uri=MATRIX_SCHEMA.object, name="matrixEdge__object", curie=MATRIX_SCHEMA.curie('object'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__object, domain=None, range=str)

slots.matrixEdge__knowledge_level = Slot(uri=MATRIX_SCHEMA.knowledge_level, name="matrixEdge__knowledge_level", curie=MATRIX_SCHEMA.curie('knowledge_level'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__knowledge_level, domain=None, range=Optional[str])

slots.matrixEdge__primary_knowledge_source = Slot(uri=MATRIX_SCHEMA.primary_knowledge_source, name="matrixEdge__primary_knowledge_source", curie=MATRIX_SCHEMA.curie('primary_knowledge_source'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__primary_knowledge_source, domain=None, range=Optional[str])

slots.matrixEdge__aggregator_knowledge_source = Slot(uri=MATRIX_SCHEMA.aggregator_knowledge_source, name="matrixEdge__aggregator_knowledge_source", curie=MATRIX_SCHEMA.curie('aggregator_knowledge_source'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__aggregator_knowledge_source, domain=None, range=Optional[str])

slots.matrixEdge__publications = Slot(uri=MATRIX_SCHEMA.publications, name="matrixEdge__publications", curie=MATRIX_SCHEMA.curie('publications'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__publications, domain=None, range=Optional[str])

slots.matrixEdge__subject_aspect_qualifier = Slot(uri=MATRIX_SCHEMA.subject_aspect_qualifier, name="matrixEdge__subject_aspect_qualifier", curie=MATRIX_SCHEMA.curie('subject_aspect_qualifier'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__subject_aspect_qualifier, domain=None, range=Optional[str])

slots.matrixEdge__subject_direction_qualifier = Slot(uri=MATRIX_SCHEMA.subject_direction_qualifier, name="matrixEdge__subject_direction_qualifier", curie=MATRIX_SCHEMA.curie('subject_direction_qualifier'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__subject_direction_qualifier, domain=None, range=Optional[str])

slots.matrixEdge__object_aspect_qualifier = Slot(uri=MATRIX_SCHEMA.object_aspect_qualifier, name="matrixEdge__object_aspect_qualifier", curie=MATRIX_SCHEMA.curie('object_aspect_qualifier'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__object_aspect_qualifier, domain=None, range=Optional[str])

slots.matrixEdge__object_direction_qualifier = Slot(uri=MATRIX_SCHEMA.object_direction_qualifier, name="matrixEdge__object_direction_qualifier", curie=MATRIX_SCHEMA.curie('object_direction_qualifier'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__object_direction_qualifier, domain=None, range=Optional[str])

slots.matrixEdge__upstream_data_source = Slot(uri=MATRIX_SCHEMA.upstream_data_source, name="matrixEdge__upstream_data_source", curie=MATRIX_SCHEMA.curie('upstream_data_source'),
                   model_uri=MATRIX_SCHEMA.matrixEdge__upstream_data_source, domain=None, range=str)

slots.matrixEdgeCollection__entries = Slot(uri=MATRIX_SCHEMA.entries, name="matrixEdgeCollection__entries", curie=MATRIX_SCHEMA.curie('entries'),
                   model_uri=MATRIX_SCHEMA.matrixEdgeCollection__entries, domain=None, range=Optional[Union[Union[dict, MatrixEdge], List[Union[dict, MatrixEdge]]]])