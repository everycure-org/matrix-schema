# Auto generated from matrix_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-13T14:43:54
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

from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
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
    name: Optional[str] = None
    description: Optional[str] = None
    equivalent_identifiers: Optional[str] = None
    all_categories: Optional[str] = None
    publications: Optional[str] = None
    labels: Optional[str] = None
    international_resource_identifier: Optional[str] = None
    upstream_data_source: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MatrixNodeId):
            self.id = MatrixNodeId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, str):
            self.category = str(self.category)

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

        if self.upstream_data_source is not None and not isinstance(self.upstream_data_source, str):
            self.upstream_data_source = str(self.upstream_data_source)

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
    knowledge_level: Optional[str] = None
    primary_knowledge_source: Optional[str] = None
    aggregator_knowledge_source: Optional[str] = None
    publications: Optional[str] = None
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[str] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[str] = None
    upstream_data_source: Optional[str] = None

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

        if self.upstream_data_source is not None and not isinstance(self.upstream_data_source, str):
            self.upstream_data_source = str(self.upstream_data_source)

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


@dataclass(repr=False)
class MatrixNodeCollection(YAMLRoot):
    """
    A holder for MatrixNode objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MATRIX_SCHEMA["MatrixNodeCollection"]
    class_class_curie: ClassVar[str] = "matrix_schema:MatrixNodeCollection"
    class_name: ClassVar[str] = "MatrixNodeCollection"
    class_model_uri: ClassVar[URIRef] = MATRIX_SCHEMA.MatrixNodeCollection

    entries: Optional[Union[Dict[Union[str, MatrixNodeId], Union[dict, MatrixNode]], List[Union[dict, MatrixNode]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=MatrixNode, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseListEntry(YAMLRoot):
    """
    A disease entry in the disease list.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MATRIX_SCHEMA["DiseaseListEntry"]
    class_class_curie: ClassVar[str] = "matrix_schema:DiseaseListEntry"
    class_name: ClassVar[str] = "DiseaseListEntry"
    class_model_uri: ClassVar[URIRef] = MATRIX_SCHEMA.DiseaseListEntry

    category_class: Optional[str] = None
    label: Optional[str] = None
    definition: Optional[str] = None
    synonyms: Optional[str] = None
    subsets: Optional[str] = None
    crossreferences: Optional[str] = None
    is_matrix_manually_excluded: Optional[str] = None
    is_matrix_manually_included: Optional[str] = None
    is_clingen: Optional[str] = None
    is_grouping_subset: Optional[str] = None
    is_grouping_subset_ancestor: Optional[str] = None
    is_orphanet_subtype: Optional[str] = None
    is_orphanet_subtype_descendant: Optional[str] = None
    is_omimps: Optional[str] = None
    is_omimps_descendant: Optional[str] = None
    is_leaf: Optional[str] = None
    is_leaf_direct_parent: Optional[str] = None
    is_orphanet_disorder: Optional[str] = None
    is_omim: Optional[str] = None
    is_icd_category: Optional[str] = None
    is_icd_chapter_code: Optional[str] = None
    is_icd_chapter_header: Optional[str] = None
    is_icd_billable: Optional[str] = None
    is_mondo_subtype: Optional[str] = None
    is_pathway_defect: Optional[str] = None
    is_susceptibility: Optional[str] = None
    is_paraphilic: Optional[str] = None
    is_acquired: Optional[str] = None
    is_andor: Optional[str] = None
    is_withorwithout: Optional[str] = None
    is_obsoletion_candidate: Optional[str] = None
    is_unclassified_hereditary: Optional[str] = None
    official_matrix_filter: Optional[str] = None
    harrisons_view: Optional[str] = None
    mondo_txgnn: Optional[str] = None
    mondo_top_grouping: Optional[str] = None
    medical_specialization: Optional[str] = None
    txgnn: Optional[str] = None
    anatomical: Optional[str] = None
    is_pathogen_caused: Optional[str] = None
    is_cancer: Optional[str] = None
    is_glucose_dysfunction: Optional[str] = None
    tag_existing_treatment: Optional[str] = None
    tag_qaly_lost: Optional[str] = None
    subset_group_id: Optional[str] = None
    subset_group_label: Optional[str] = None
    other_subsets_count: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.category_class is not None and not isinstance(self.category_class, str):
            self.category_class = str(self.category_class)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.synonyms is not None and not isinstance(self.synonyms, str):
            self.synonyms = str(self.synonyms)

        if self.subsets is not None and not isinstance(self.subsets, str):
            self.subsets = str(self.subsets)

        if self.crossreferences is not None and not isinstance(self.crossreferences, str):
            self.crossreferences = str(self.crossreferences)

        if self.is_matrix_manually_excluded is not None and not isinstance(self.is_matrix_manually_excluded, str):
            self.is_matrix_manually_excluded = str(self.is_matrix_manually_excluded)

        if self.is_matrix_manually_included is not None and not isinstance(self.is_matrix_manually_included, str):
            self.is_matrix_manually_included = str(self.is_matrix_manually_included)

        if self.is_clingen is not None and not isinstance(self.is_clingen, str):
            self.is_clingen = str(self.is_clingen)

        if self.is_grouping_subset is not None and not isinstance(self.is_grouping_subset, str):
            self.is_grouping_subset = str(self.is_grouping_subset)

        if self.is_grouping_subset_ancestor is not None and not isinstance(self.is_grouping_subset_ancestor, str):
            self.is_grouping_subset_ancestor = str(self.is_grouping_subset_ancestor)

        if self.is_orphanet_subtype is not None and not isinstance(self.is_orphanet_subtype, str):
            self.is_orphanet_subtype = str(self.is_orphanet_subtype)

        if self.is_orphanet_subtype_descendant is not None and not isinstance(self.is_orphanet_subtype_descendant, str):
            self.is_orphanet_subtype_descendant = str(self.is_orphanet_subtype_descendant)

        if self.is_omimps is not None and not isinstance(self.is_omimps, str):
            self.is_omimps = str(self.is_omimps)

        if self.is_omimps_descendant is not None and not isinstance(self.is_omimps_descendant, str):
            self.is_omimps_descendant = str(self.is_omimps_descendant)

        if self.is_leaf is not None and not isinstance(self.is_leaf, str):
            self.is_leaf = str(self.is_leaf)

        if self.is_leaf_direct_parent is not None and not isinstance(self.is_leaf_direct_parent, str):
            self.is_leaf_direct_parent = str(self.is_leaf_direct_parent)

        if self.is_orphanet_disorder is not None and not isinstance(self.is_orphanet_disorder, str):
            self.is_orphanet_disorder = str(self.is_orphanet_disorder)

        if self.is_omim is not None and not isinstance(self.is_omim, str):
            self.is_omim = str(self.is_omim)

        if self.is_icd_category is not None and not isinstance(self.is_icd_category, str):
            self.is_icd_category = str(self.is_icd_category)

        if self.is_icd_chapter_code is not None and not isinstance(self.is_icd_chapter_code, str):
            self.is_icd_chapter_code = str(self.is_icd_chapter_code)

        if self.is_icd_chapter_header is not None and not isinstance(self.is_icd_chapter_header, str):
            self.is_icd_chapter_header = str(self.is_icd_chapter_header)

        if self.is_icd_billable is not None and not isinstance(self.is_icd_billable, str):
            self.is_icd_billable = str(self.is_icd_billable)

        if self.is_mondo_subtype is not None and not isinstance(self.is_mondo_subtype, str):
            self.is_mondo_subtype = str(self.is_mondo_subtype)

        if self.is_pathway_defect is not None and not isinstance(self.is_pathway_defect, str):
            self.is_pathway_defect = str(self.is_pathway_defect)

        if self.is_susceptibility is not None and not isinstance(self.is_susceptibility, str):
            self.is_susceptibility = str(self.is_susceptibility)

        if self.is_paraphilic is not None and not isinstance(self.is_paraphilic, str):
            self.is_paraphilic = str(self.is_paraphilic)

        if self.is_acquired is not None and not isinstance(self.is_acquired, str):
            self.is_acquired = str(self.is_acquired)

        if self.is_andor is not None and not isinstance(self.is_andor, str):
            self.is_andor = str(self.is_andor)

        if self.is_withorwithout is not None and not isinstance(self.is_withorwithout, str):
            self.is_withorwithout = str(self.is_withorwithout)

        if self.is_obsoletion_candidate is not None and not isinstance(self.is_obsoletion_candidate, str):
            self.is_obsoletion_candidate = str(self.is_obsoletion_candidate)

        if self.is_unclassified_hereditary is not None and not isinstance(self.is_unclassified_hereditary, str):
            self.is_unclassified_hereditary = str(self.is_unclassified_hereditary)

        if self.official_matrix_filter is not None and not isinstance(self.official_matrix_filter, str):
            self.official_matrix_filter = str(self.official_matrix_filter)

        if self.harrisons_view is not None and not isinstance(self.harrisons_view, str):
            self.harrisons_view = str(self.harrisons_view)

        if self.mondo_txgnn is not None and not isinstance(self.mondo_txgnn, str):
            self.mondo_txgnn = str(self.mondo_txgnn)

        if self.mondo_top_grouping is not None and not isinstance(self.mondo_top_grouping, str):
            self.mondo_top_grouping = str(self.mondo_top_grouping)

        if self.medical_specialization is not None and not isinstance(self.medical_specialization, str):
            self.medical_specialization = str(self.medical_specialization)

        if self.txgnn is not None and not isinstance(self.txgnn, str):
            self.txgnn = str(self.txgnn)

        if self.anatomical is not None and not isinstance(self.anatomical, str):
            self.anatomical = str(self.anatomical)

        if self.is_pathogen_caused is not None and not isinstance(self.is_pathogen_caused, str):
            self.is_pathogen_caused = str(self.is_pathogen_caused)

        if self.is_cancer is not None and not isinstance(self.is_cancer, str):
            self.is_cancer = str(self.is_cancer)

        if self.is_glucose_dysfunction is not None and not isinstance(self.is_glucose_dysfunction, str):
            self.is_glucose_dysfunction = str(self.is_glucose_dysfunction)

        if self.tag_existing_treatment is not None and not isinstance(self.tag_existing_treatment, str):
            self.tag_existing_treatment = str(self.tag_existing_treatment)

        if self.tag_qaly_lost is not None and not isinstance(self.tag_qaly_lost, str):
            self.tag_qaly_lost = str(self.tag_qaly_lost)

        if self.subset_group_id is not None and not isinstance(self.subset_group_id, str):
            self.subset_group_id = str(self.subset_group_id)

        if self.subset_group_label is not None and not isinstance(self.subset_group_label, str):
            self.subset_group_label = str(self.subset_group_label)

        if self.other_subsets_count is not None and not isinstance(self.other_subsets_count, str):
            self.other_subsets_count = str(self.other_subsets_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MatrixDiseaseList(YAMLRoot):
    """
    A list of diseases.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MATRIX_SCHEMA["MatrixDiseaseList"]
    class_class_curie: ClassVar[str] = "matrix_schema:MatrixDiseaseList"
    class_name: ClassVar[str] = "MatrixDiseaseList"
    class_model_uri: ClassVar[URIRef] = MATRIX_SCHEMA.MatrixDiseaseList

    entries: Optional[Union[Union[dict, DiseaseListEntry], List[Union[dict, DiseaseListEntry]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.entries, list):
            self.entries = [self.entries] if self.entries is not None else []
        self.entries = [v if isinstance(v, DiseaseListEntry) else DiseaseListEntry(**as_dict(v)) for v in self.entries]

        super().__post_init__(**kwargs)


# Enumerations
class AttributeTypeEnum(EnumDefinitionImpl):
    """
    Code used to describe the nature of a slot, for documentative purposes.
    """
    filter = PermissibleValue(
        text="filter",
        description="Attribute used as a boolean filter for the disease list.")
    grouping = PermissibleValue(
        text="grouping",
        description="Attribute used as a grouping/tagging attribute for the disease list.")

    _defn = EnumDefinition(
        name="AttributeTypeEnum",
        description="Code used to describe the nature of a slot, for documentative purposes.",
    )

class CurationTypeEnum(EnumDefinitionImpl):
    """
    Code used to describe how a slot / attribute was curated.
    """
    manual_everycure = PermissibleValue(
        text="manual_everycure",
        description="Manually curated by a Matrix medical expert.")
    manual_mondo = PermissibleValue(
        text="manual_mondo",
        description="Manually curated by the Mondo team.")
    llm = PermissibleValue(
        text="llm",
        description="Automatically curated by a script or algorithm.")
    ontology_hierarchy = PermissibleValue(
        text="ontology_hierarchy",
        description="Automatically extracted from the ontology hierarchy.")
    external_source = PermissibleValue(
        text="external_source",
        description="Automatically extracted from an external source.")
    lexical_matching = PermissibleValue(
        text="lexical_matching",
        description="Automatically curated from a lexical matching algorithm.")

    _defn = EnumDefinition(
        name="CurationTypeEnum",
        description="Code used to describe how a slot / attribute was curated.",
    )

# Slots
class slots:
    pass

slots.category_class = Slot(uri=MATRIX_SCHEMA.category_class, name="category_class", curie=MATRIX_SCHEMA.curie('category_class'),
                   model_uri=MATRIX_SCHEMA.category_class, domain=None, range=Optional[str])

slots.label = Slot(uri=MATRIX_SCHEMA.label, name="label", curie=MATRIX_SCHEMA.curie('label'),
                   model_uri=MATRIX_SCHEMA.label, domain=None, range=Optional[str])

slots.definition = Slot(uri=MATRIX_SCHEMA.definition, name="definition", curie=MATRIX_SCHEMA.curie('definition'),
                   model_uri=MATRIX_SCHEMA.definition, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=MATRIX_SCHEMA.synonyms, name="synonyms", curie=MATRIX_SCHEMA.curie('synonyms'),
                   model_uri=MATRIX_SCHEMA.synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.subsets = Slot(uri=MATRIX_SCHEMA.subsets, name="subsets", curie=MATRIX_SCHEMA.curie('subsets'),
                   model_uri=MATRIX_SCHEMA.subsets, domain=None, range=Optional[Union[str, List[str]]])

slots.crossreferences = Slot(uri=MATRIX_SCHEMA.crossreferences, name="crossreferences", curie=MATRIX_SCHEMA.curie('crossreferences'),
                   model_uri=MATRIX_SCHEMA.crossreferences, domain=None, range=Optional[Union[str, List[str]]])

slots.subset_group_id = Slot(uri=MATRIX_SCHEMA.subset_group_id, name="subset_group_id", curie=MATRIX_SCHEMA.curie('subset_group_id'),
                   model_uri=MATRIX_SCHEMA.subset_group_id, domain=None, range=Optional[str])

slots.subset_group_label = Slot(uri=MATRIX_SCHEMA.subset_group_label, name="subset_group_label", curie=MATRIX_SCHEMA.curie('subset_group_label'),
                   model_uri=MATRIX_SCHEMA.subset_group_label, domain=None, range=Optional[str])

slots.other_subsets_count = Slot(uri=MATRIX_SCHEMA.other_subsets_count, name="other_subsets_count", curie=MATRIX_SCHEMA.curie('other_subsets_count'),
                   model_uri=MATRIX_SCHEMA.other_subsets_count, domain=None, range=Optional[int])

slots.entries = Slot(uri=MATRIX_SCHEMA.entries, name="entries", curie=MATRIX_SCHEMA.curie('entries'),
                   model_uri=MATRIX_SCHEMA.entries, domain=None, range=Optional[Union[str, List[str]]])

slots.attribute_type = Slot(uri=MATRIX_SCHEMA.attribute_type, name="attribute_type", curie=MATRIX_SCHEMA.curie('attribute_type'),
                   model_uri=MATRIX_SCHEMA.attribute_type, domain=None, range=Optional[Union[str, "AttributeTypeEnum"]])

slots.curation_type = Slot(uri=MATRIX_SCHEMA.curation_type, name="curation_type", curie=MATRIX_SCHEMA.curie('curation_type'),
                   model_uri=MATRIX_SCHEMA.curation_type, domain=None, range=Optional[Union[str, "CurationTypeEnum"]])

slots.is_matrix_manually_excluded = Slot(uri=MATRIX_SCHEMA.is_matrix_manually_excluded, name="is_matrix_manually_excluded", curie=MATRIX_SCHEMA.curie('is_matrix_manually_excluded'),
                   model_uri=MATRIX_SCHEMA.is_matrix_manually_excluded, domain=None, range=Optional[Union[bool, Bool]])

slots.is_matrix_manually_included = Slot(uri=MATRIX_SCHEMA.is_matrix_manually_included, name="is_matrix_manually_included", curie=MATRIX_SCHEMA.curie('is_matrix_manually_included'),
                   model_uri=MATRIX_SCHEMA.is_matrix_manually_included, domain=None, range=Optional[Union[bool, Bool]])

slots.is_clingen = Slot(uri=MATRIX_SCHEMA.is_clingen, name="is_clingen", curie=MATRIX_SCHEMA.curie('is_clingen'),
                   model_uri=MATRIX_SCHEMA.is_clingen, domain=None, range=Optional[Union[bool, Bool]])

slots.is_grouping_subset = Slot(uri=MATRIX_SCHEMA.is_grouping_subset, name="is_grouping_subset", curie=MATRIX_SCHEMA.curie('is_grouping_subset'),
                   model_uri=MATRIX_SCHEMA.is_grouping_subset, domain=None, range=Optional[Union[bool, Bool]])

slots.is_grouping_subset_ancestor = Slot(uri=MATRIX_SCHEMA.is_grouping_subset_ancestor, name="is_grouping_subset_ancestor", curie=MATRIX_SCHEMA.curie('is_grouping_subset_ancestor'),
                   model_uri=MATRIX_SCHEMA.is_grouping_subset_ancestor, domain=None, range=Optional[Union[bool, Bool]])

slots.is_orphanet_subtype = Slot(uri=MATRIX_SCHEMA.is_orphanet_subtype, name="is_orphanet_subtype", curie=MATRIX_SCHEMA.curie('is_orphanet_subtype'),
                   model_uri=MATRIX_SCHEMA.is_orphanet_subtype, domain=None, range=Optional[Union[bool, Bool]])

slots.is_orphanet_subtype_descendant = Slot(uri=MATRIX_SCHEMA.is_orphanet_subtype_descendant, name="is_orphanet_subtype_descendant", curie=MATRIX_SCHEMA.curie('is_orphanet_subtype_descendant'),
                   model_uri=MATRIX_SCHEMA.is_orphanet_subtype_descendant, domain=None, range=Optional[Union[bool, Bool]])

slots.is_omimps = Slot(uri=MATRIX_SCHEMA.is_omimps, name="is_omimps", curie=MATRIX_SCHEMA.curie('is_omimps'),
                   model_uri=MATRIX_SCHEMA.is_omimps, domain=None, range=Optional[Union[bool, Bool]])

slots.is_omimps_descendant = Slot(uri=MATRIX_SCHEMA.is_omimps_descendant, name="is_omimps_descendant", curie=MATRIX_SCHEMA.curie('is_omimps_descendant'),
                   model_uri=MATRIX_SCHEMA.is_omimps_descendant, domain=None, range=Optional[Union[bool, Bool]])

slots.is_leaf = Slot(uri=MATRIX_SCHEMA.is_leaf, name="is_leaf", curie=MATRIX_SCHEMA.curie('is_leaf'),
                   model_uri=MATRIX_SCHEMA.is_leaf, domain=None, range=Optional[Union[bool, Bool]])

slots.is_leaf_direct_parent = Slot(uri=MATRIX_SCHEMA.is_leaf_direct_parent, name="is_leaf_direct_parent", curie=MATRIX_SCHEMA.curie('is_leaf_direct_parent'),
                   model_uri=MATRIX_SCHEMA.is_leaf_direct_parent, domain=None, range=Optional[Union[bool, Bool]])

slots.is_orphanet_disorder = Slot(uri=MATRIX_SCHEMA.is_orphanet_disorder, name="is_orphanet_disorder", curie=MATRIX_SCHEMA.curie('is_orphanet_disorder'),
                   model_uri=MATRIX_SCHEMA.is_orphanet_disorder, domain=None, range=Optional[Union[bool, Bool]])

slots.is_omim = Slot(uri=MATRIX_SCHEMA.is_omim, name="is_omim", curie=MATRIX_SCHEMA.curie('is_omim'),
                   model_uri=MATRIX_SCHEMA.is_omim, domain=None, range=Optional[Union[bool, Bool]])

slots.is_icd_category = Slot(uri=MATRIX_SCHEMA.is_icd_category, name="is_icd_category", curie=MATRIX_SCHEMA.curie('is_icd_category'),
                   model_uri=MATRIX_SCHEMA.is_icd_category, domain=None, range=Optional[Union[bool, Bool]])

slots.is_icd_chapter_code = Slot(uri=MATRIX_SCHEMA.is_icd_chapter_code, name="is_icd_chapter_code", curie=MATRIX_SCHEMA.curie('is_icd_chapter_code'),
                   model_uri=MATRIX_SCHEMA.is_icd_chapter_code, domain=None, range=Optional[Union[bool, Bool]])

slots.is_icd_chapter_header = Slot(uri=MATRIX_SCHEMA.is_icd_chapter_header, name="is_icd_chapter_header", curie=MATRIX_SCHEMA.curie('is_icd_chapter_header'),
                   model_uri=MATRIX_SCHEMA.is_icd_chapter_header, domain=None, range=Optional[Union[bool, Bool]])

slots.is_icd_billable = Slot(uri=MATRIX_SCHEMA.is_icd_billable, name="is_icd_billable", curie=MATRIX_SCHEMA.curie('is_icd_billable'),
                   model_uri=MATRIX_SCHEMA.is_icd_billable, domain=None, range=Optional[Union[bool, Bool]])

slots.is_mondo_subtype = Slot(uri=MATRIX_SCHEMA.is_mondo_subtype, name="is_mondo_subtype", curie=MATRIX_SCHEMA.curie('is_mondo_subtype'),
                   model_uri=MATRIX_SCHEMA.is_mondo_subtype, domain=None, range=Optional[Union[bool, Bool]])

slots.is_pathway_defect = Slot(uri=MATRIX_SCHEMA.is_pathway_defect, name="is_pathway_defect", curie=MATRIX_SCHEMA.curie('is_pathway_defect'),
                   model_uri=MATRIX_SCHEMA.is_pathway_defect, domain=None, range=Optional[Union[bool, Bool]])

slots.is_susceptibility = Slot(uri=MATRIX_SCHEMA.is_susceptibility, name="is_susceptibility", curie=MATRIX_SCHEMA.curie('is_susceptibility'),
                   model_uri=MATRIX_SCHEMA.is_susceptibility, domain=None, range=Optional[Union[bool, Bool]])

slots.is_paraphilic = Slot(uri=MATRIX_SCHEMA.is_paraphilic, name="is_paraphilic", curie=MATRIX_SCHEMA.curie('is_paraphilic'),
                   model_uri=MATRIX_SCHEMA.is_paraphilic, domain=None, range=Optional[Union[bool, Bool]])

slots.is_acquired = Slot(uri=MATRIX_SCHEMA.is_acquired, name="is_acquired", curie=MATRIX_SCHEMA.curie('is_acquired'),
                   model_uri=MATRIX_SCHEMA.is_acquired, domain=None, range=Optional[Union[bool, Bool]])

slots.is_andor = Slot(uri=MATRIX_SCHEMA.is_andor, name="is_andor", curie=MATRIX_SCHEMA.curie('is_andor'),
                   model_uri=MATRIX_SCHEMA.is_andor, domain=None, range=Optional[Union[bool, Bool]])

slots.is_withorwithout = Slot(uri=MATRIX_SCHEMA.is_withorwithout, name="is_withorwithout", curie=MATRIX_SCHEMA.curie('is_withorwithout'),
                   model_uri=MATRIX_SCHEMA.is_withorwithout, domain=None, range=Optional[Union[bool, Bool]])

slots.is_obsoletion_candidate = Slot(uri=MATRIX_SCHEMA.is_obsoletion_candidate, name="is_obsoletion_candidate", curie=MATRIX_SCHEMA.curie('is_obsoletion_candidate'),
                   model_uri=MATRIX_SCHEMA.is_obsoletion_candidate, domain=None, range=Optional[Union[bool, Bool]])

slots.is_unclassified_hereditary = Slot(uri=MATRIX_SCHEMA.is_unclassified_hereditary, name="is_unclassified_hereditary", curie=MATRIX_SCHEMA.curie('is_unclassified_hereditary'),
                   model_uri=MATRIX_SCHEMA.is_unclassified_hereditary, domain=None, range=Optional[Union[bool, Bool]])

slots.official_matrix_filter = Slot(uri=MATRIX_SCHEMA.official_matrix_filter, name="official_matrix_filter", curie=MATRIX_SCHEMA.curie('official_matrix_filter'),
                   model_uri=MATRIX_SCHEMA.official_matrix_filter, domain=None, range=Optional[Union[bool, Bool]])

slots.is_pathogen_caused = Slot(uri=MATRIX_SCHEMA.is_pathogen_caused, name="is_pathogen_caused", curie=MATRIX_SCHEMA.curie('is_pathogen_caused'),
                   model_uri=MATRIX_SCHEMA.is_pathogen_caused, domain=None, range=Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]])

slots.is_cancer = Slot(uri=MATRIX_SCHEMA.is_cancer, name="is_cancer", curie=MATRIX_SCHEMA.curie('is_cancer'),
                   model_uri=MATRIX_SCHEMA.is_cancer, domain=None, range=Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]])

slots.is_glucose_dysfunction = Slot(uri=MATRIX_SCHEMA.is_glucose_dysfunction, name="is_glucose_dysfunction", curie=MATRIX_SCHEMA.curie('is_glucose_dysfunction'),
                   model_uri=MATRIX_SCHEMA.is_glucose_dysfunction, domain=None, range=Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]])

slots.tag_existing_treatment = Slot(uri=MATRIX_SCHEMA.tag_existing_treatment, name="tag_existing_treatment", curie=MATRIX_SCHEMA.curie('tag_existing_treatment'),
                   model_uri=MATRIX_SCHEMA.tag_existing_treatment, domain=None, range=Optional[Union[Union[bool, Bool], List[Union[bool, Bool]]]])

slots.harrisons_view = Slot(uri=MATRIX_SCHEMA.harrisons_view, name="harrisons_view", curie=MATRIX_SCHEMA.curie('harrisons_view'),
                   model_uri=MATRIX_SCHEMA.harrisons_view, domain=None, range=Optional[Union[str, List[str]]])

slots.mondo_txgnn = Slot(uri=MATRIX_SCHEMA.mondo_txgnn, name="mondo_txgnn", curie=MATRIX_SCHEMA.curie('mondo_txgnn'),
                   model_uri=MATRIX_SCHEMA.mondo_txgnn, domain=None, range=Optional[Union[str, List[str]]])

slots.mondo_top_grouping = Slot(uri=MATRIX_SCHEMA.mondo_top_grouping, name="mondo_top_grouping", curie=MATRIX_SCHEMA.curie('mondo_top_grouping'),
                   model_uri=MATRIX_SCHEMA.mondo_top_grouping, domain=None, range=Optional[Union[str, List[str]]])

slots.medical_specialization = Slot(uri=MATRIX_SCHEMA.medical_specialization, name="medical_specialization", curie=MATRIX_SCHEMA.curie('medical_specialization'),
                   model_uri=MATRIX_SCHEMA.medical_specialization, domain=None, range=Optional[Union[str, List[str]]])

slots.txgnn = Slot(uri=MATRIX_SCHEMA.txgnn, name="txgnn", curie=MATRIX_SCHEMA.curie('txgnn'),
                   model_uri=MATRIX_SCHEMA.txgnn, domain=None, range=Optional[Union[str, List[str]]])

slots.anatomical = Slot(uri=MATRIX_SCHEMA.anatomical, name="anatomical", curie=MATRIX_SCHEMA.curie('anatomical'),
                   model_uri=MATRIX_SCHEMA.anatomical, domain=None, range=Optional[Union[str, List[str]]])

slots.tag_qaly_lost = Slot(uri=MATRIX_SCHEMA.tag_qaly_lost, name="tag_qaly_lost", curie=MATRIX_SCHEMA.curie('tag_qaly_lost'),
                   model_uri=MATRIX_SCHEMA.tag_qaly_lost, domain=None, range=str,
                   pattern=re.compile(r'^(low|medium|high|very_high|none)$'))

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MATRIX_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=MATRIX_SCHEMA.name, name="name", curie=MATRIX_SCHEMA.curie('name'),
                   model_uri=MATRIX_SCHEMA.name, domain=None, range=Optional[str])

slots.category = Slot(uri=MATRIX_SCHEMA.category, name="category", curie=MATRIX_SCHEMA.curie('category'),
                   model_uri=MATRIX_SCHEMA.category, domain=None, range=Optional[str])

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
                   model_uri=MATRIX_SCHEMA.subject, domain=None, range=Optional[str])

slots.predicate = Slot(uri=MATRIX_SCHEMA.predicate, name="predicate", curie=MATRIX_SCHEMA.curie('predicate'),
                   model_uri=MATRIX_SCHEMA.predicate, domain=None, range=Optional[str])

slots.object = Slot(uri=MATRIX_SCHEMA.object, name="object", curie=MATRIX_SCHEMA.curie('object'),
                   model_uri=MATRIX_SCHEMA.object, domain=None, range=Optional[str])

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
                   model_uri=MATRIX_SCHEMA.matrixNode__upstream_data_source, domain=None, range=Optional[str])

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
                   model_uri=MATRIX_SCHEMA.matrixEdge__upstream_data_source, domain=None, range=Optional[str])

slots.matrixEdgeCollection__entries = Slot(uri=MATRIX_SCHEMA.entries, name="matrixEdgeCollection__entries", curie=MATRIX_SCHEMA.curie('entries'),
                   model_uri=MATRIX_SCHEMA.matrixEdgeCollection__entries, domain=None, range=Optional[Union[Union[dict, MatrixEdge], List[Union[dict, MatrixEdge]]]])

slots.matrixNodeCollection__entries = Slot(uri=MATRIX_SCHEMA.entries, name="matrixNodeCollection__entries", curie=MATRIX_SCHEMA.curie('entries'),
                   model_uri=MATRIX_SCHEMA.matrixNodeCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, MatrixNodeId], Union[dict, MatrixNode]], List[Union[dict, MatrixNode]]]])

slots.diseaseListEntry__category_class = Slot(uri=MATRIX_SCHEMA.category_class, name="diseaseListEntry__category_class", curie=MATRIX_SCHEMA.curie('category_class'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__category_class, domain=None, range=Optional[str])

slots.diseaseListEntry__label = Slot(uri=MATRIX_SCHEMA.label, name="diseaseListEntry__label", curie=MATRIX_SCHEMA.curie('label'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__label, domain=None, range=Optional[str])

slots.diseaseListEntry__definition = Slot(uri=MATRIX_SCHEMA.definition, name="diseaseListEntry__definition", curie=MATRIX_SCHEMA.curie('definition'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__definition, domain=None, range=Optional[str])

slots.diseaseListEntry__synonyms = Slot(uri=MATRIX_SCHEMA.synonyms, name="diseaseListEntry__synonyms", curie=MATRIX_SCHEMA.curie('synonyms'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__synonyms, domain=None, range=Optional[str])

slots.diseaseListEntry__subsets = Slot(uri=MATRIX_SCHEMA.subsets, name="diseaseListEntry__subsets", curie=MATRIX_SCHEMA.curie('subsets'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__subsets, domain=None, range=Optional[str])

slots.diseaseListEntry__crossreferences = Slot(uri=MATRIX_SCHEMA.crossreferences, name="diseaseListEntry__crossreferences", curie=MATRIX_SCHEMA.curie('crossreferences'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__crossreferences, domain=None, range=Optional[str])

slots.diseaseListEntry__is_matrix_manually_excluded = Slot(uri=MATRIX_SCHEMA.is_matrix_manually_excluded, name="diseaseListEntry__is_matrix_manually_excluded", curie=MATRIX_SCHEMA.curie('is_matrix_manually_excluded'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_matrix_manually_excluded, domain=None, range=Optional[str])

slots.diseaseListEntry__is_matrix_manually_included = Slot(uri=MATRIX_SCHEMA.is_matrix_manually_included, name="diseaseListEntry__is_matrix_manually_included", curie=MATRIX_SCHEMA.curie('is_matrix_manually_included'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_matrix_manually_included, domain=None, range=Optional[str])

slots.diseaseListEntry__is_clingen = Slot(uri=MATRIX_SCHEMA.is_clingen, name="diseaseListEntry__is_clingen", curie=MATRIX_SCHEMA.curie('is_clingen'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_clingen, domain=None, range=Optional[str])

slots.diseaseListEntry__is_grouping_subset = Slot(uri=MATRIX_SCHEMA.is_grouping_subset, name="diseaseListEntry__is_grouping_subset", curie=MATRIX_SCHEMA.curie('is_grouping_subset'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_grouping_subset, domain=None, range=Optional[str])

slots.diseaseListEntry__is_grouping_subset_ancestor = Slot(uri=MATRIX_SCHEMA.is_grouping_subset_ancestor, name="diseaseListEntry__is_grouping_subset_ancestor", curie=MATRIX_SCHEMA.curie('is_grouping_subset_ancestor'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_grouping_subset_ancestor, domain=None, range=Optional[str])

slots.diseaseListEntry__is_orphanet_subtype = Slot(uri=MATRIX_SCHEMA.is_orphanet_subtype, name="diseaseListEntry__is_orphanet_subtype", curie=MATRIX_SCHEMA.curie('is_orphanet_subtype'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_orphanet_subtype, domain=None, range=Optional[str])

slots.diseaseListEntry__is_orphanet_subtype_descendant = Slot(uri=MATRIX_SCHEMA.is_orphanet_subtype_descendant, name="diseaseListEntry__is_orphanet_subtype_descendant", curie=MATRIX_SCHEMA.curie('is_orphanet_subtype_descendant'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_orphanet_subtype_descendant, domain=None, range=Optional[str])

slots.diseaseListEntry__is_omimps = Slot(uri=MATRIX_SCHEMA.is_omimps, name="diseaseListEntry__is_omimps", curie=MATRIX_SCHEMA.curie('is_omimps'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_omimps, domain=None, range=Optional[str])

slots.diseaseListEntry__is_omimps_descendant = Slot(uri=MATRIX_SCHEMA.is_omimps_descendant, name="diseaseListEntry__is_omimps_descendant", curie=MATRIX_SCHEMA.curie('is_omimps_descendant'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_omimps_descendant, domain=None, range=Optional[str])

slots.diseaseListEntry__is_leaf = Slot(uri=MATRIX_SCHEMA.is_leaf, name="diseaseListEntry__is_leaf", curie=MATRIX_SCHEMA.curie('is_leaf'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_leaf, domain=None, range=Optional[str])

slots.diseaseListEntry__is_leaf_direct_parent = Slot(uri=MATRIX_SCHEMA.is_leaf_direct_parent, name="diseaseListEntry__is_leaf_direct_parent", curie=MATRIX_SCHEMA.curie('is_leaf_direct_parent'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_leaf_direct_parent, domain=None, range=Optional[str])

slots.diseaseListEntry__is_orphanet_disorder = Slot(uri=MATRIX_SCHEMA.is_orphanet_disorder, name="diseaseListEntry__is_orphanet_disorder", curie=MATRIX_SCHEMA.curie('is_orphanet_disorder'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_orphanet_disorder, domain=None, range=Optional[str])

slots.diseaseListEntry__is_omim = Slot(uri=MATRIX_SCHEMA.is_omim, name="diseaseListEntry__is_omim", curie=MATRIX_SCHEMA.curie('is_omim'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_omim, domain=None, range=Optional[str])

slots.diseaseListEntry__is_icd_category = Slot(uri=MATRIX_SCHEMA.is_icd_category, name="diseaseListEntry__is_icd_category", curie=MATRIX_SCHEMA.curie('is_icd_category'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_icd_category, domain=None, range=Optional[str])

slots.diseaseListEntry__is_icd_chapter_code = Slot(uri=MATRIX_SCHEMA.is_icd_chapter_code, name="diseaseListEntry__is_icd_chapter_code", curie=MATRIX_SCHEMA.curie('is_icd_chapter_code'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_icd_chapter_code, domain=None, range=Optional[str])

slots.diseaseListEntry__is_icd_chapter_header = Slot(uri=MATRIX_SCHEMA.is_icd_chapter_header, name="diseaseListEntry__is_icd_chapter_header", curie=MATRIX_SCHEMA.curie('is_icd_chapter_header'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_icd_chapter_header, domain=None, range=Optional[str])

slots.diseaseListEntry__is_icd_billable = Slot(uri=MATRIX_SCHEMA.is_icd_billable, name="diseaseListEntry__is_icd_billable", curie=MATRIX_SCHEMA.curie('is_icd_billable'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_icd_billable, domain=None, range=Optional[str])

slots.diseaseListEntry__is_mondo_subtype = Slot(uri=MATRIX_SCHEMA.is_mondo_subtype, name="diseaseListEntry__is_mondo_subtype", curie=MATRIX_SCHEMA.curie('is_mondo_subtype'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_mondo_subtype, domain=None, range=Optional[str])

slots.diseaseListEntry__is_pathway_defect = Slot(uri=MATRIX_SCHEMA.is_pathway_defect, name="diseaseListEntry__is_pathway_defect", curie=MATRIX_SCHEMA.curie('is_pathway_defect'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_pathway_defect, domain=None, range=Optional[str])

slots.diseaseListEntry__is_susceptibility = Slot(uri=MATRIX_SCHEMA.is_susceptibility, name="diseaseListEntry__is_susceptibility", curie=MATRIX_SCHEMA.curie('is_susceptibility'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_susceptibility, domain=None, range=Optional[str])

slots.diseaseListEntry__is_paraphilic = Slot(uri=MATRIX_SCHEMA.is_paraphilic, name="diseaseListEntry__is_paraphilic", curie=MATRIX_SCHEMA.curie('is_paraphilic'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_paraphilic, domain=None, range=Optional[str])

slots.diseaseListEntry__is_acquired = Slot(uri=MATRIX_SCHEMA.is_acquired, name="diseaseListEntry__is_acquired", curie=MATRIX_SCHEMA.curie('is_acquired'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_acquired, domain=None, range=Optional[str])

slots.diseaseListEntry__is_andor = Slot(uri=MATRIX_SCHEMA.is_andor, name="diseaseListEntry__is_andor", curie=MATRIX_SCHEMA.curie('is_andor'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_andor, domain=None, range=Optional[str])

slots.diseaseListEntry__is_withorwithout = Slot(uri=MATRIX_SCHEMA.is_withorwithout, name="diseaseListEntry__is_withorwithout", curie=MATRIX_SCHEMA.curie('is_withorwithout'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_withorwithout, domain=None, range=Optional[str])

slots.diseaseListEntry__is_obsoletion_candidate = Slot(uri=MATRIX_SCHEMA.is_obsoletion_candidate, name="diseaseListEntry__is_obsoletion_candidate", curie=MATRIX_SCHEMA.curie('is_obsoletion_candidate'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_obsoletion_candidate, domain=None, range=Optional[str])

slots.diseaseListEntry__is_unclassified_hereditary = Slot(uri=MATRIX_SCHEMA.is_unclassified_hereditary, name="diseaseListEntry__is_unclassified_hereditary", curie=MATRIX_SCHEMA.curie('is_unclassified_hereditary'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_unclassified_hereditary, domain=None, range=Optional[str])

slots.diseaseListEntry__official_matrix_filter = Slot(uri=MATRIX_SCHEMA.official_matrix_filter, name="diseaseListEntry__official_matrix_filter", curie=MATRIX_SCHEMA.curie('official_matrix_filter'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__official_matrix_filter, domain=None, range=Optional[str])

slots.diseaseListEntry__harrisons_view = Slot(uri=MATRIX_SCHEMA.harrisons_view, name="diseaseListEntry__harrisons_view", curie=MATRIX_SCHEMA.curie('harrisons_view'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__harrisons_view, domain=None, range=Optional[str])

slots.diseaseListEntry__mondo_txgnn = Slot(uri=MATRIX_SCHEMA.mondo_txgnn, name="diseaseListEntry__mondo_txgnn", curie=MATRIX_SCHEMA.curie('mondo_txgnn'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__mondo_txgnn, domain=None, range=Optional[str])

slots.diseaseListEntry__mondo_top_grouping = Slot(uri=MATRIX_SCHEMA.mondo_top_grouping, name="diseaseListEntry__mondo_top_grouping", curie=MATRIX_SCHEMA.curie('mondo_top_grouping'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__mondo_top_grouping, domain=None, range=Optional[str])

slots.diseaseListEntry__medical_specialization = Slot(uri=MATRIX_SCHEMA.medical_specialization, name="diseaseListEntry__medical_specialization", curie=MATRIX_SCHEMA.curie('medical_specialization'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__medical_specialization, domain=None, range=Optional[str])

slots.diseaseListEntry__txgnn = Slot(uri=MATRIX_SCHEMA.txgnn, name="diseaseListEntry__txgnn", curie=MATRIX_SCHEMA.curie('txgnn'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__txgnn, domain=None, range=Optional[str])

slots.diseaseListEntry__anatomical = Slot(uri=MATRIX_SCHEMA.anatomical, name="diseaseListEntry__anatomical", curie=MATRIX_SCHEMA.curie('anatomical'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__anatomical, domain=None, range=Optional[str])

slots.diseaseListEntry__is_pathogen_caused = Slot(uri=MATRIX_SCHEMA.is_pathogen_caused, name="diseaseListEntry__is_pathogen_caused", curie=MATRIX_SCHEMA.curie('is_pathogen_caused'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_pathogen_caused, domain=None, range=Optional[str])

slots.diseaseListEntry__is_cancer = Slot(uri=MATRIX_SCHEMA.is_cancer, name="diseaseListEntry__is_cancer", curie=MATRIX_SCHEMA.curie('is_cancer'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_cancer, domain=None, range=Optional[str])

slots.diseaseListEntry__is_glucose_dysfunction = Slot(uri=MATRIX_SCHEMA.is_glucose_dysfunction, name="diseaseListEntry__is_glucose_dysfunction", curie=MATRIX_SCHEMA.curie('is_glucose_dysfunction'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__is_glucose_dysfunction, domain=None, range=Optional[str])

slots.diseaseListEntry__tag_existing_treatment = Slot(uri=MATRIX_SCHEMA.tag_existing_treatment, name="diseaseListEntry__tag_existing_treatment", curie=MATRIX_SCHEMA.curie('tag_existing_treatment'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__tag_existing_treatment, domain=None, range=Optional[str])

slots.diseaseListEntry__tag_qaly_lost = Slot(uri=MATRIX_SCHEMA.tag_qaly_lost, name="diseaseListEntry__tag_qaly_lost", curie=MATRIX_SCHEMA.curie('tag_qaly_lost'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__tag_qaly_lost, domain=None, range=Optional[str])

slots.diseaseListEntry__subset_group_id = Slot(uri=MATRIX_SCHEMA.subset_group_id, name="diseaseListEntry__subset_group_id", curie=MATRIX_SCHEMA.curie('subset_group_id'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__subset_group_id, domain=None, range=Optional[str])

slots.diseaseListEntry__subset_group_label = Slot(uri=MATRIX_SCHEMA.subset_group_label, name="diseaseListEntry__subset_group_label", curie=MATRIX_SCHEMA.curie('subset_group_label'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__subset_group_label, domain=None, range=Optional[str])

slots.diseaseListEntry__other_subsets_count = Slot(uri=MATRIX_SCHEMA.other_subsets_count, name="diseaseListEntry__other_subsets_count", curie=MATRIX_SCHEMA.curie('other_subsets_count'),
                   model_uri=MATRIX_SCHEMA.diseaseListEntry__other_subsets_count, domain=None, range=Optional[str])

slots.matrixDiseaseList__entries = Slot(uri=MATRIX_SCHEMA.entries, name="matrixDiseaseList__entries", curie=MATRIX_SCHEMA.curie('entries'),
                   model_uri=MATRIX_SCHEMA.matrixDiseaseList__entries, domain=None, range=Optional[Union[Union[dict, DiseaseListEntry], List[Union[dict, DiseaseListEntry]]]])