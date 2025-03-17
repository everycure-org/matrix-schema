# Auto generated from matrix_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-14T12:01:22
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
class MatrixNodeId(URIorCURIE):
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
    equivalent_identifiers: Optional[Union[str, List[str]]] = empty_list()
    all_categories: Optional[Union[str, List[str]]] = empty_list()
    publications: Optional[Union[str, List[str]]] = empty_list()
    labels: Optional[Union[str, List[str]]] = empty_list()
    international_resource_identifier: Optional[str] = None
    upstream_data_source: Optional[Union[str, List[str]]] = empty_list()

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

        if not isinstance(self.equivalent_identifiers, list):
            self.equivalent_identifiers = [self.equivalent_identifiers] if self.equivalent_identifiers is not None else []
        self.equivalent_identifiers = [v if isinstance(v, str) else str(v) for v in self.equivalent_identifiers]

        if not isinstance(self.all_categories, list):
            self.all_categories = [self.all_categories] if self.all_categories is not None else []
        self.all_categories = [v if isinstance(v, str) else str(v) for v in self.all_categories]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, str) else str(v) for v in self.publications]

        if not isinstance(self.labels, list):
            self.labels = [self.labels] if self.labels is not None else []
        self.labels = [v if isinstance(v, str) else str(v) for v in self.labels]

        if self.international_resource_identifier is not None and not isinstance(self.international_resource_identifier, str):
            self.international_resource_identifier = str(self.international_resource_identifier)

        if not isinstance(self.upstream_data_source, list):
            self.upstream_data_source = [self.upstream_data_source] if self.upstream_data_source is not None else []
        self.upstream_data_source = [v if isinstance(v, str) else str(v) for v in self.upstream_data_source]

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
    aggregator_knowledge_source: Optional[Union[str, List[str]]] = empty_list()
    publications: Optional[Union[str, List[str]]] = empty_list()
    subject_aspect_qualifier: Optional[str] = None
    subject_direction_qualifier: Optional[str] = None
    object_aspect_qualifier: Optional[str] = None
    object_direction_qualifier: Optional[str] = None
    upstream_data_source: Optional[Union[str, List[str]]] = empty_list()

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

        if not isinstance(self.aggregator_knowledge_source, list):
            self.aggregator_knowledge_source = [self.aggregator_knowledge_source] if self.aggregator_knowledge_source is not None else []
        self.aggregator_knowledge_source = [v if isinstance(v, str) else str(v) for v in self.aggregator_knowledge_source]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, str) else str(v) for v in self.publications]

        if self.subject_aspect_qualifier is not None and not isinstance(self.subject_aspect_qualifier, str):
            self.subject_aspect_qualifier = str(self.subject_aspect_qualifier)

        if self.subject_direction_qualifier is not None and not isinstance(self.subject_direction_qualifier, str):
            self.subject_direction_qualifier = str(self.subject_direction_qualifier)

        if self.object_aspect_qualifier is not None and not isinstance(self.object_aspect_qualifier, str):
            self.object_aspect_qualifier = str(self.object_aspect_qualifier)

        if self.object_direction_qualifier is not None and not isinstance(self.object_direction_qualifier, str):
            self.object_direction_qualifier = str(self.object_direction_qualifier)

        if not isinstance(self.upstream_data_source, list):
            self.upstream_data_source = [self.upstream_data_source] if self.upstream_data_source is not None else []
        self.upstream_data_source = [v if isinstance(v, str) else str(v) for v in self.upstream_data_source]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MatrixEdgeList(YAMLRoot):
    """
    A container for MatrixEdge objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MATRIX_SCHEMA["MatrixEdgeList"]
    class_class_curie: ClassVar[str] = "matrix_schema:MatrixEdgeList"
    class_name: ClassVar[str] = "MatrixEdgeList"
    class_model_uri: ClassVar[URIRef] = MATRIX_SCHEMA.MatrixEdgeList

    edges: Optional[Union[Union[dict, MatrixEdge], List[Union[dict, MatrixEdge]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="edges", slot_type=MatrixEdge, key_name="subject", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MatrixNodeList(YAMLRoot):
    """
    A container for MatrixNode objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MATRIX_SCHEMA["MatrixNodeList"]
    class_class_curie: ClassVar[str] = "matrix_schema:MatrixNodeList"
    class_name: ClassVar[str] = "MatrixNodeList"
    class_model_uri: ClassVar[URIRef] = MATRIX_SCHEMA.MatrixNodeList

    nodes: Optional[Union[Dict[Union[str, MatrixNodeId], Union[dict, MatrixNode]], List[Union[dict, MatrixNode]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="nodes", slot_type=MatrixNode, key_name="id", keyed=True)

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

    category_class: str = None
    label: str = None
    synonyms: Union[str, List[str]] = None
    subsets: Union[str, List[str]] = None
    crossreferences: Union[str, List[str]] = None
    is_matrix_manually_excluded: Union[bool, Bool] = None
    is_matrix_manually_included: Union[bool, Bool] = None
    is_clingen: Union[bool, Bool] = None
    is_grouping_subset: Union[bool, Bool] = None
    is_grouping_subset_ancestor: Union[bool, Bool] = None
    is_orphanet_subtype: Union[bool, Bool] = None
    is_orphanet_subtype_descendant: Union[bool, Bool] = None
    is_omimps: Union[bool, Bool] = None
    is_omimps_descendant: Union[bool, Bool] = None
    is_leaf: Union[bool, Bool] = None
    is_leaf_direct_parent: Union[bool, Bool] = None
    is_orphanet_disorder: Union[bool, Bool] = None
    is_omim: Union[bool, Bool] = None
    is_icd_category: Union[bool, Bool] = None
    is_icd_chapter_code: Union[bool, Bool] = None
    is_icd_chapter_header: Union[bool, Bool] = None
    is_icd_billable: Union[bool, Bool] = None
    is_mondo_subtype: Union[bool, Bool] = None
    is_pathway_defect: Union[bool, Bool] = None
    is_susceptibility: Union[bool, Bool] = None
    is_paraphilic: Union[bool, Bool] = None
    is_acquired: Union[bool, Bool] = None
    is_andor: Union[bool, Bool] = None
    is_withorwithout: Union[bool, Bool] = None
    is_obsoletion_candidate: Union[bool, Bool] = None
    is_unclassified_hereditary: Union[bool, Bool] = None
    official_matrix_filter: Union[bool, Bool] = None
    harrisons_view: Union[str, List[str]] = None
    mondo_txgnn: Union[str, List[str]] = None
    mondo_top_grouping: Union[str, List[str]] = None
    medical_specialization: Union[str, List[str]] = None
    txgnn: Union[str, List[str]] = None
    anatomical: Union[str, List[str]] = None
    is_pathogen_caused: Union[bool, Bool] = None
    is_cancer: Union[bool, Bool] = None
    is_glucose_dysfunction: Union[bool, Bool] = None
    tag_existing_treatment: Union[bool, Bool] = None
    tag_qaly_lost: str = None
    definition: Optional[str] = None
    subset_group_id: Optional[str] = None
    subset_group_label: Optional[str] = None
    other_subsets_count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.category_class):
            self.MissingRequiredField("category_class")
        if not isinstance(self.category_class, str):
            self.category_class = str(self.category_class)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self._is_empty(self.synonyms):
            self.MissingRequiredField("synonyms")
        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self._is_empty(self.subsets):
            self.MissingRequiredField("subsets")
        if not isinstance(self.subsets, list):
            self.subsets = [self.subsets] if self.subsets is not None else []
        self.subsets = [v if isinstance(v, str) else str(v) for v in self.subsets]

        if self._is_empty(self.crossreferences):
            self.MissingRequiredField("crossreferences")
        if not isinstance(self.crossreferences, list):
            self.crossreferences = [self.crossreferences] if self.crossreferences is not None else []
        self.crossreferences = [v if isinstance(v, str) else str(v) for v in self.crossreferences]

        if self._is_empty(self.is_matrix_manually_excluded):
            self.MissingRequiredField("is_matrix_manually_excluded")
        if not isinstance(self.is_matrix_manually_excluded, Bool):
            self.is_matrix_manually_excluded = Bool(self.is_matrix_manually_excluded)

        if self._is_empty(self.is_matrix_manually_included):
            self.MissingRequiredField("is_matrix_manually_included")
        if not isinstance(self.is_matrix_manually_included, Bool):
            self.is_matrix_manually_included = Bool(self.is_matrix_manually_included)

        if self._is_empty(self.is_clingen):
            self.MissingRequiredField("is_clingen")
        if not isinstance(self.is_clingen, Bool):
            self.is_clingen = Bool(self.is_clingen)

        if self._is_empty(self.is_grouping_subset):
            self.MissingRequiredField("is_grouping_subset")
        if not isinstance(self.is_grouping_subset, Bool):
            self.is_grouping_subset = Bool(self.is_grouping_subset)

        if self._is_empty(self.is_grouping_subset_ancestor):
            self.MissingRequiredField("is_grouping_subset_ancestor")
        if not isinstance(self.is_grouping_subset_ancestor, Bool):
            self.is_grouping_subset_ancestor = Bool(self.is_grouping_subset_ancestor)

        if self._is_empty(self.is_orphanet_subtype):
            self.MissingRequiredField("is_orphanet_subtype")
        if not isinstance(self.is_orphanet_subtype, Bool):
            self.is_orphanet_subtype = Bool(self.is_orphanet_subtype)

        if self._is_empty(self.is_orphanet_subtype_descendant):
            self.MissingRequiredField("is_orphanet_subtype_descendant")
        if not isinstance(self.is_orphanet_subtype_descendant, Bool):
            self.is_orphanet_subtype_descendant = Bool(self.is_orphanet_subtype_descendant)

        if self._is_empty(self.is_omimps):
            self.MissingRequiredField("is_omimps")
        if not isinstance(self.is_omimps, Bool):
            self.is_omimps = Bool(self.is_omimps)

        if self._is_empty(self.is_omimps_descendant):
            self.MissingRequiredField("is_omimps_descendant")
        if not isinstance(self.is_omimps_descendant, Bool):
            self.is_omimps_descendant = Bool(self.is_omimps_descendant)

        if self._is_empty(self.is_leaf):
            self.MissingRequiredField("is_leaf")
        if not isinstance(self.is_leaf, Bool):
            self.is_leaf = Bool(self.is_leaf)

        if self._is_empty(self.is_leaf_direct_parent):
            self.MissingRequiredField("is_leaf_direct_parent")
        if not isinstance(self.is_leaf_direct_parent, Bool):
            self.is_leaf_direct_parent = Bool(self.is_leaf_direct_parent)

        if self._is_empty(self.is_orphanet_disorder):
            self.MissingRequiredField("is_orphanet_disorder")
        if not isinstance(self.is_orphanet_disorder, Bool):
            self.is_orphanet_disorder = Bool(self.is_orphanet_disorder)

        if self._is_empty(self.is_omim):
            self.MissingRequiredField("is_omim")
        if not isinstance(self.is_omim, Bool):
            self.is_omim = Bool(self.is_omim)

        if self._is_empty(self.is_icd_category):
            self.MissingRequiredField("is_icd_category")
        if not isinstance(self.is_icd_category, Bool):
            self.is_icd_category = Bool(self.is_icd_category)

        if self._is_empty(self.is_icd_chapter_code):
            self.MissingRequiredField("is_icd_chapter_code")
        if not isinstance(self.is_icd_chapter_code, Bool):
            self.is_icd_chapter_code = Bool(self.is_icd_chapter_code)

        if self._is_empty(self.is_icd_chapter_header):
            self.MissingRequiredField("is_icd_chapter_header")
        if not isinstance(self.is_icd_chapter_header, Bool):
            self.is_icd_chapter_header = Bool(self.is_icd_chapter_header)

        if self._is_empty(self.is_icd_billable):
            self.MissingRequiredField("is_icd_billable")
        if not isinstance(self.is_icd_billable, Bool):
            self.is_icd_billable = Bool(self.is_icd_billable)

        if self._is_empty(self.is_mondo_subtype):
            self.MissingRequiredField("is_mondo_subtype")
        if not isinstance(self.is_mondo_subtype, Bool):
            self.is_mondo_subtype = Bool(self.is_mondo_subtype)

        if self._is_empty(self.is_pathway_defect):
            self.MissingRequiredField("is_pathway_defect")
        if not isinstance(self.is_pathway_defect, Bool):
            self.is_pathway_defect = Bool(self.is_pathway_defect)

        if self._is_empty(self.is_susceptibility):
            self.MissingRequiredField("is_susceptibility")
        if not isinstance(self.is_susceptibility, Bool):
            self.is_susceptibility = Bool(self.is_susceptibility)

        if self._is_empty(self.is_paraphilic):
            self.MissingRequiredField("is_paraphilic")
        if not isinstance(self.is_paraphilic, Bool):
            self.is_paraphilic = Bool(self.is_paraphilic)

        if self._is_empty(self.is_acquired):
            self.MissingRequiredField("is_acquired")
        if not isinstance(self.is_acquired, Bool):
            self.is_acquired = Bool(self.is_acquired)

        if self._is_empty(self.is_andor):
            self.MissingRequiredField("is_andor")
        if not isinstance(self.is_andor, Bool):
            self.is_andor = Bool(self.is_andor)

        if self._is_empty(self.is_withorwithout):
            self.MissingRequiredField("is_withorwithout")
        if not isinstance(self.is_withorwithout, Bool):
            self.is_withorwithout = Bool(self.is_withorwithout)

        if self._is_empty(self.is_obsoletion_candidate):
            self.MissingRequiredField("is_obsoletion_candidate")
        if not isinstance(self.is_obsoletion_candidate, Bool):
            self.is_obsoletion_candidate = Bool(self.is_obsoletion_candidate)

        if self._is_empty(self.is_unclassified_hereditary):
            self.MissingRequiredField("is_unclassified_hereditary")
        if not isinstance(self.is_unclassified_hereditary, Bool):
            self.is_unclassified_hereditary = Bool(self.is_unclassified_hereditary)

        if self._is_empty(self.official_matrix_filter):
            self.MissingRequiredField("official_matrix_filter")
        if not isinstance(self.official_matrix_filter, Bool):
            self.official_matrix_filter = Bool(self.official_matrix_filter)

        if self._is_empty(self.harrisons_view):
            self.MissingRequiredField("harrisons_view")
        if not isinstance(self.harrisons_view, list):
            self.harrisons_view = [self.harrisons_view] if self.harrisons_view is not None else []
        self.harrisons_view = [v if isinstance(v, str) else str(v) for v in self.harrisons_view]

        if self._is_empty(self.mondo_txgnn):
            self.MissingRequiredField("mondo_txgnn")
        if not isinstance(self.mondo_txgnn, list):
            self.mondo_txgnn = [self.mondo_txgnn] if self.mondo_txgnn is not None else []
        self.mondo_txgnn = [v if isinstance(v, str) else str(v) for v in self.mondo_txgnn]

        if self._is_empty(self.mondo_top_grouping):
            self.MissingRequiredField("mondo_top_grouping")
        if not isinstance(self.mondo_top_grouping, list):
            self.mondo_top_grouping = [self.mondo_top_grouping] if self.mondo_top_grouping is not None else []
        self.mondo_top_grouping = [v if isinstance(v, str) else str(v) for v in self.mondo_top_grouping]

        if self._is_empty(self.medical_specialization):
            self.MissingRequiredField("medical_specialization")
        if not isinstance(self.medical_specialization, list):
            self.medical_specialization = [self.medical_specialization] if self.medical_specialization is not None else []
        self.medical_specialization = [v if isinstance(v, str) else str(v) for v in self.medical_specialization]

        if self._is_empty(self.txgnn):
            self.MissingRequiredField("txgnn")
        if not isinstance(self.txgnn, list):
            self.txgnn = [self.txgnn] if self.txgnn is not None else []
        self.txgnn = [v if isinstance(v, str) else str(v) for v in self.txgnn]

        if self._is_empty(self.anatomical):
            self.MissingRequiredField("anatomical")
        if not isinstance(self.anatomical, list):
            self.anatomical = [self.anatomical] if self.anatomical is not None else []
        self.anatomical = [v if isinstance(v, str) else str(v) for v in self.anatomical]

        if self._is_empty(self.is_pathogen_caused):
            self.MissingRequiredField("is_pathogen_caused")
        if not isinstance(self.is_pathogen_caused, Bool):
            self.is_pathogen_caused = Bool(self.is_pathogen_caused)

        if self._is_empty(self.is_cancer):
            self.MissingRequiredField("is_cancer")
        if not isinstance(self.is_cancer, Bool):
            self.is_cancer = Bool(self.is_cancer)

        if self._is_empty(self.is_glucose_dysfunction):
            self.MissingRequiredField("is_glucose_dysfunction")
        if not isinstance(self.is_glucose_dysfunction, Bool):
            self.is_glucose_dysfunction = Bool(self.is_glucose_dysfunction)

        if self._is_empty(self.tag_existing_treatment):
            self.MissingRequiredField("tag_existing_treatment")
        if not isinstance(self.tag_existing_treatment, Bool):
            self.tag_existing_treatment = Bool(self.tag_existing_treatment)

        if self._is_empty(self.tag_qaly_lost):
            self.MissingRequiredField("tag_qaly_lost")
        if not isinstance(self.tag_qaly_lost, str):
            self.tag_qaly_lost = str(self.tag_qaly_lost)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.subset_group_id is not None and not isinstance(self.subset_group_id, str):
            self.subset_group_id = str(self.subset_group_id)

        if self.subset_group_label is not None and not isinstance(self.subset_group_label, str):
            self.subset_group_label = str(self.subset_group_label)

        if self.other_subsets_count is not None and not isinstance(self.other_subsets_count, int):
            self.other_subsets_count = int(self.other_subsets_count)

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

    disease_list_entries: Optional[Union[Union[dict, DiseaseListEntry], List[Union[dict, DiseaseListEntry]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="disease_list_entries", slot_type=DiseaseListEntry, key_name="category_class", keyed=False)

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

slots.edges = Slot(uri=MATRIX_SCHEMA.edges, name="edges", curie=MATRIX_SCHEMA.curie('edges'),
                   model_uri=MATRIX_SCHEMA.edges, domain=None, range=Optional[Union[str, List[str]]])

slots.nodes = Slot(uri=MATRIX_SCHEMA.nodes, name="nodes", curie=MATRIX_SCHEMA.curie('nodes'),
                   model_uri=MATRIX_SCHEMA.nodes, domain=None, range=Optional[Union[str, List[str]]])

slots.disease_list_entries = Slot(uri=MATRIX_SCHEMA.disease_list_entries, name="disease_list_entries", curie=MATRIX_SCHEMA.curie('disease_list_entries'),
                   model_uri=MATRIX_SCHEMA.disease_list_entries, domain=None, range=Optional[Union[Union[dict, DiseaseListEntry], List[Union[dict, DiseaseListEntry]]]])

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
                   model_uri=MATRIX_SCHEMA.is_pathogen_caused, domain=None, range=Optional[Union[bool, Bool]])

slots.is_cancer = Slot(uri=MATRIX_SCHEMA.is_cancer, name="is_cancer", curie=MATRIX_SCHEMA.curie('is_cancer'),
                   model_uri=MATRIX_SCHEMA.is_cancer, domain=None, range=Optional[Union[bool, Bool]])

slots.is_glucose_dysfunction = Slot(uri=MATRIX_SCHEMA.is_glucose_dysfunction, name="is_glucose_dysfunction", curie=MATRIX_SCHEMA.curie('is_glucose_dysfunction'),
                   model_uri=MATRIX_SCHEMA.is_glucose_dysfunction, domain=None, range=Optional[Union[bool, Bool]])

slots.tag_existing_treatment = Slot(uri=MATRIX_SCHEMA.tag_existing_treatment, name="tag_existing_treatment", curie=MATRIX_SCHEMA.curie('tag_existing_treatment'),
                   model_uri=MATRIX_SCHEMA.tag_existing_treatment, domain=None, range=Optional[Union[bool, Bool]])

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

slots.MatrixNode_category = Slot(uri=MATRIX_SCHEMA.category, name="MatrixNode_category", curie=MATRIX_SCHEMA.curie('category'),
                   model_uri=MATRIX_SCHEMA.MatrixNode_category, domain=MatrixNode, range=str)

slots.MatrixNode_id = Slot(uri=SCHEMA.identifier, name="MatrixNode_id", curie=SCHEMA.curie('identifier'),
                   model_uri=MATRIX_SCHEMA.MatrixNode_id, domain=MatrixNode, range=Union[str, MatrixNodeId])

slots.MatrixEdge_subject = Slot(uri=MATRIX_SCHEMA.subject, name="MatrixEdge_subject", curie=MATRIX_SCHEMA.curie('subject'),
                   model_uri=MATRIX_SCHEMA.MatrixEdge_subject, domain=MatrixEdge, range=str)

slots.MatrixEdge_predicate = Slot(uri=MATRIX_SCHEMA.predicate, name="MatrixEdge_predicate", curie=MATRIX_SCHEMA.curie('predicate'),
                   model_uri=MATRIX_SCHEMA.MatrixEdge_predicate, domain=MatrixEdge, range=str)

slots.MatrixEdge_object = Slot(uri=MATRIX_SCHEMA.object, name="MatrixEdge_object", curie=MATRIX_SCHEMA.curie('object'),
                   model_uri=MATRIX_SCHEMA.MatrixEdge_object, domain=MatrixEdge, range=str)

slots.MatrixEdgeList_edges = Slot(uri=MATRIX_SCHEMA.edges, name="MatrixEdgeList_edges", curie=MATRIX_SCHEMA.curie('edges'),
                   model_uri=MATRIX_SCHEMA.MatrixEdgeList_edges, domain=MatrixEdgeList, range=Optional[Union[Union[dict, MatrixEdge], List[Union[dict, MatrixEdge]]]])

slots.MatrixNodeList_nodes = Slot(uri=MATRIX_SCHEMA.nodes, name="MatrixNodeList_nodes", curie=MATRIX_SCHEMA.curie('nodes'),
                   model_uri=MATRIX_SCHEMA.MatrixNodeList_nodes, domain=MatrixNodeList, range=Optional[Union[Dict[Union[str, MatrixNodeId], Union[dict, MatrixNode]], List[Union[dict, MatrixNode]]]])

slots.DiseaseListEntry_category_class = Slot(uri=MATRIX_SCHEMA.category_class, name="DiseaseListEntry_category_class", curie=MATRIX_SCHEMA.curie('category_class'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_category_class, domain=DiseaseListEntry, range=str)

slots.DiseaseListEntry_label = Slot(uri=MATRIX_SCHEMA.label, name="DiseaseListEntry_label", curie=MATRIX_SCHEMA.curie('label'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_label, domain=DiseaseListEntry, range=str)

slots.DiseaseListEntry_definition = Slot(uri=MATRIX_SCHEMA.definition, name="DiseaseListEntry_definition", curie=MATRIX_SCHEMA.curie('definition'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_definition, domain=DiseaseListEntry, range=Optional[str])

slots.DiseaseListEntry_synonyms = Slot(uri=MATRIX_SCHEMA.synonyms, name="DiseaseListEntry_synonyms", curie=MATRIX_SCHEMA.curie('synonyms'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_synonyms, domain=DiseaseListEntry, range=Union[str, List[str]])

slots.DiseaseListEntry_subsets = Slot(uri=MATRIX_SCHEMA.subsets, name="DiseaseListEntry_subsets", curie=MATRIX_SCHEMA.curie('subsets'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_subsets, domain=DiseaseListEntry, range=Union[str, List[str]])

slots.DiseaseListEntry_crossreferences = Slot(uri=MATRIX_SCHEMA.crossreferences, name="DiseaseListEntry_crossreferences", curie=MATRIX_SCHEMA.curie('crossreferences'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_crossreferences, domain=DiseaseListEntry, range=Union[str, List[str]])

slots.DiseaseListEntry_is_matrix_manually_excluded = Slot(uri=MATRIX_SCHEMA.is_matrix_manually_excluded, name="DiseaseListEntry_is_matrix_manually_excluded", curie=MATRIX_SCHEMA.curie('is_matrix_manually_excluded'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_matrix_manually_excluded, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_matrix_manually_included = Slot(uri=MATRIX_SCHEMA.is_matrix_manually_included, name="DiseaseListEntry_is_matrix_manually_included", curie=MATRIX_SCHEMA.curie('is_matrix_manually_included'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_matrix_manually_included, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_clingen = Slot(uri=MATRIX_SCHEMA.is_clingen, name="DiseaseListEntry_is_clingen", curie=MATRIX_SCHEMA.curie('is_clingen'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_clingen, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_grouping_subset = Slot(uri=MATRIX_SCHEMA.is_grouping_subset, name="DiseaseListEntry_is_grouping_subset", curie=MATRIX_SCHEMA.curie('is_grouping_subset'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_grouping_subset, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_grouping_subset_ancestor = Slot(uri=MATRIX_SCHEMA.is_grouping_subset_ancestor, name="DiseaseListEntry_is_grouping_subset_ancestor", curie=MATRIX_SCHEMA.curie('is_grouping_subset_ancestor'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_grouping_subset_ancestor, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_orphanet_subtype = Slot(uri=MATRIX_SCHEMA.is_orphanet_subtype, name="DiseaseListEntry_is_orphanet_subtype", curie=MATRIX_SCHEMA.curie('is_orphanet_subtype'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_orphanet_subtype, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_orphanet_subtype_descendant = Slot(uri=MATRIX_SCHEMA.is_orphanet_subtype_descendant, name="DiseaseListEntry_is_orphanet_subtype_descendant", curie=MATRIX_SCHEMA.curie('is_orphanet_subtype_descendant'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_orphanet_subtype_descendant, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_omimps = Slot(uri=MATRIX_SCHEMA.is_omimps, name="DiseaseListEntry_is_omimps", curie=MATRIX_SCHEMA.curie('is_omimps'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_omimps, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_omimps_descendant = Slot(uri=MATRIX_SCHEMA.is_omimps_descendant, name="DiseaseListEntry_is_omimps_descendant", curie=MATRIX_SCHEMA.curie('is_omimps_descendant'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_omimps_descendant, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_leaf = Slot(uri=MATRIX_SCHEMA.is_leaf, name="DiseaseListEntry_is_leaf", curie=MATRIX_SCHEMA.curie('is_leaf'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_leaf, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_leaf_direct_parent = Slot(uri=MATRIX_SCHEMA.is_leaf_direct_parent, name="DiseaseListEntry_is_leaf_direct_parent", curie=MATRIX_SCHEMA.curie('is_leaf_direct_parent'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_leaf_direct_parent, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_orphanet_disorder = Slot(uri=MATRIX_SCHEMA.is_orphanet_disorder, name="DiseaseListEntry_is_orphanet_disorder", curie=MATRIX_SCHEMA.curie('is_orphanet_disorder'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_orphanet_disorder, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_omim = Slot(uri=MATRIX_SCHEMA.is_omim, name="DiseaseListEntry_is_omim", curie=MATRIX_SCHEMA.curie('is_omim'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_omim, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_icd_category = Slot(uri=MATRIX_SCHEMA.is_icd_category, name="DiseaseListEntry_is_icd_category", curie=MATRIX_SCHEMA.curie('is_icd_category'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_icd_category, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_icd_chapter_code = Slot(uri=MATRIX_SCHEMA.is_icd_chapter_code, name="DiseaseListEntry_is_icd_chapter_code", curie=MATRIX_SCHEMA.curie('is_icd_chapter_code'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_icd_chapter_code, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_icd_chapter_header = Slot(uri=MATRIX_SCHEMA.is_icd_chapter_header, name="DiseaseListEntry_is_icd_chapter_header", curie=MATRIX_SCHEMA.curie('is_icd_chapter_header'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_icd_chapter_header, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_icd_billable = Slot(uri=MATRIX_SCHEMA.is_icd_billable, name="DiseaseListEntry_is_icd_billable", curie=MATRIX_SCHEMA.curie('is_icd_billable'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_icd_billable, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_mondo_subtype = Slot(uri=MATRIX_SCHEMA.is_mondo_subtype, name="DiseaseListEntry_is_mondo_subtype", curie=MATRIX_SCHEMA.curie('is_mondo_subtype'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_mondo_subtype, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_pathway_defect = Slot(uri=MATRIX_SCHEMA.is_pathway_defect, name="DiseaseListEntry_is_pathway_defect", curie=MATRIX_SCHEMA.curie('is_pathway_defect'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_pathway_defect, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_susceptibility = Slot(uri=MATRIX_SCHEMA.is_susceptibility, name="DiseaseListEntry_is_susceptibility", curie=MATRIX_SCHEMA.curie('is_susceptibility'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_susceptibility, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_paraphilic = Slot(uri=MATRIX_SCHEMA.is_paraphilic, name="DiseaseListEntry_is_paraphilic", curie=MATRIX_SCHEMA.curie('is_paraphilic'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_paraphilic, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_acquired = Slot(uri=MATRIX_SCHEMA.is_acquired, name="DiseaseListEntry_is_acquired", curie=MATRIX_SCHEMA.curie('is_acquired'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_acquired, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_andor = Slot(uri=MATRIX_SCHEMA.is_andor, name="DiseaseListEntry_is_andor", curie=MATRIX_SCHEMA.curie('is_andor'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_andor, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_withorwithout = Slot(uri=MATRIX_SCHEMA.is_withorwithout, name="DiseaseListEntry_is_withorwithout", curie=MATRIX_SCHEMA.curie('is_withorwithout'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_withorwithout, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_obsoletion_candidate = Slot(uri=MATRIX_SCHEMA.is_obsoletion_candidate, name="DiseaseListEntry_is_obsoletion_candidate", curie=MATRIX_SCHEMA.curie('is_obsoletion_candidate'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_obsoletion_candidate, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_unclassified_hereditary = Slot(uri=MATRIX_SCHEMA.is_unclassified_hereditary, name="DiseaseListEntry_is_unclassified_hereditary", curie=MATRIX_SCHEMA.curie('is_unclassified_hereditary'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_unclassified_hereditary, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_official_matrix_filter = Slot(uri=MATRIX_SCHEMA.official_matrix_filter, name="DiseaseListEntry_official_matrix_filter", curie=MATRIX_SCHEMA.curie('official_matrix_filter'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_official_matrix_filter, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_harrisons_view = Slot(uri=MATRIX_SCHEMA.harrisons_view, name="DiseaseListEntry_harrisons_view", curie=MATRIX_SCHEMA.curie('harrisons_view'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_harrisons_view, domain=DiseaseListEntry, range=Union[str, List[str]])

slots.DiseaseListEntry_mondo_txgnn = Slot(uri=MATRIX_SCHEMA.mondo_txgnn, name="DiseaseListEntry_mondo_txgnn", curie=MATRIX_SCHEMA.curie('mondo_txgnn'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_mondo_txgnn, domain=DiseaseListEntry, range=Union[str, List[str]])

slots.DiseaseListEntry_mondo_top_grouping = Slot(uri=MATRIX_SCHEMA.mondo_top_grouping, name="DiseaseListEntry_mondo_top_grouping", curie=MATRIX_SCHEMA.curie('mondo_top_grouping'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_mondo_top_grouping, domain=DiseaseListEntry, range=Union[str, List[str]])

slots.DiseaseListEntry_medical_specialization = Slot(uri=MATRIX_SCHEMA.medical_specialization, name="DiseaseListEntry_medical_specialization", curie=MATRIX_SCHEMA.curie('medical_specialization'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_medical_specialization, domain=DiseaseListEntry, range=Union[str, List[str]])

slots.DiseaseListEntry_txgnn = Slot(uri=MATRIX_SCHEMA.txgnn, name="DiseaseListEntry_txgnn", curie=MATRIX_SCHEMA.curie('txgnn'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_txgnn, domain=DiseaseListEntry, range=Union[str, List[str]])

slots.DiseaseListEntry_anatomical = Slot(uri=MATRIX_SCHEMA.anatomical, name="DiseaseListEntry_anatomical", curie=MATRIX_SCHEMA.curie('anatomical'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_anatomical, domain=DiseaseListEntry, range=Union[str, List[str]])

slots.DiseaseListEntry_is_pathogen_caused = Slot(uri=MATRIX_SCHEMA.is_pathogen_caused, name="DiseaseListEntry_is_pathogen_caused", curie=MATRIX_SCHEMA.curie('is_pathogen_caused'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_pathogen_caused, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_cancer = Slot(uri=MATRIX_SCHEMA.is_cancer, name="DiseaseListEntry_is_cancer", curie=MATRIX_SCHEMA.curie('is_cancer'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_cancer, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_is_glucose_dysfunction = Slot(uri=MATRIX_SCHEMA.is_glucose_dysfunction, name="DiseaseListEntry_is_glucose_dysfunction", curie=MATRIX_SCHEMA.curie('is_glucose_dysfunction'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_is_glucose_dysfunction, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_tag_existing_treatment = Slot(uri=MATRIX_SCHEMA.tag_existing_treatment, name="DiseaseListEntry_tag_existing_treatment", curie=MATRIX_SCHEMA.curie('tag_existing_treatment'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_tag_existing_treatment, domain=DiseaseListEntry, range=Union[bool, Bool])

slots.DiseaseListEntry_tag_qaly_lost = Slot(uri=MATRIX_SCHEMA.tag_qaly_lost, name="DiseaseListEntry_tag_qaly_lost", curie=MATRIX_SCHEMA.curie('tag_qaly_lost'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_tag_qaly_lost, domain=DiseaseListEntry, range=str,
                   pattern=re.compile(r'^(low|medium|high|very_high|none)$'))

slots.DiseaseListEntry_subset_group_id = Slot(uri=MATRIX_SCHEMA.subset_group_id, name="DiseaseListEntry_subset_group_id", curie=MATRIX_SCHEMA.curie('subset_group_id'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_subset_group_id, domain=DiseaseListEntry, range=Optional[str])

slots.DiseaseListEntry_subset_group_label = Slot(uri=MATRIX_SCHEMA.subset_group_label, name="DiseaseListEntry_subset_group_label", curie=MATRIX_SCHEMA.curie('subset_group_label'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_subset_group_label, domain=DiseaseListEntry, range=Optional[str])

slots.DiseaseListEntry_other_subsets_count = Slot(uri=MATRIX_SCHEMA.other_subsets_count, name="DiseaseListEntry_other_subsets_count", curie=MATRIX_SCHEMA.curie('other_subsets_count'),
                   model_uri=MATRIX_SCHEMA.DiseaseListEntry_other_subsets_count, domain=DiseaseListEntry, range=Optional[int])