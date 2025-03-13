-- # Class: "MatrixNode" Description: "A node in the Biolink knowledge graph."
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: Human-readable name of the entity.
--     * Slot: category Description: Biolink category of the entity.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: international_resource_identifier Description: IRI of the entity.
--     * Slot: MatrixNodeCollection_id Description: Autocreated FK slot
-- # Class: "MatrixEdge" Description: "An edge representing a relationship between two nodes in the Biolink knowledge graph."
--     * Slot: id Description: 
--     * Slot: subject Description: The subject entity in the edge.
--     * Slot: predicate Description: The predicate defining the relationship.
--     * Slot: object Description: The object entity in the edge.
--     * Slot: knowledge_level Description: Knowledge level of the relationship.
--     * Slot: primary_knowledge_source Description: Primary source of the knowledge in the edge.
--     * Slot: subject_aspect_qualifier Description: Aspect qualifier for the subject.
--     * Slot: subject_direction_qualifier Description: Direction qualifier for the subject.
--     * Slot: object_aspect_qualifier Description: Aspect qualifier for the object.
--     * Slot: object_direction_qualifier Description: Direction qualifier for the object.
--     * Slot: MatrixEdgeCollection_id Description: Autocreated FK slot
-- # Class: "MatrixEdgeCollection" Description: "A holder for MatrixEdge objects."
--     * Slot: id Description: 
-- # Class: "MatrixNodeCollection" Description: "A holder for MatrixNode objects."
--     * Slot: id Description: 
-- # Class: "DiseaseListEntry" Description: "A disease entry in the disease list."
--     * Slot: id Description: 
--     * Slot: category_class Description: The disase identifier. Slot name should probably be renamed?
--     * Slot: label Description: The name of the disease.
--     * Slot: definition Description: The definition of the disease.
--     * Slot: is_matrix_manually_excluded Description: Flag to denote this disease was manually excluded from the disease list by a Matrix medical expert.
--     * Slot: is_matrix_manually_included Description: Flag to denote this disease was manually included from the disease list by a Matrix medical expert.
--     * Slot: is_clingen Description: Flag to denote that this disease term is used directly by https://clinicalgenome.org/ (a major authority on genetic diseases), which is a strong indication that it corresponds to a real disease entity.
--     * Slot: is_grouping_subset Description: Flag to denote this disease is manually curated to be a grouping term.
--     * Slot: is_grouping_subset_ancestor Description: Flag to denote this disease is a parent of a disease that was manually curated to be a grouping term.
--     * Slot: is_orphanet_subtype Description: Flag to denote this disease is manually curated to be a disease subtype according to Orphanet (https://www.orpha.net/), one of the most important rare disease authorities in the world.
--     * Slot: is_orphanet_subtype_descendant Description: Flag to denote this disease is a child/descendant of a disease that is manually curated  to be a disease subtype according to Orphanet (https://www.orpha.net/), one of the most  important rare disease authorities in the world. If it is a descendant of a subtype, it most likely is a subtype itself.
--     * Slot: is_omimps Description: Flag to denote this disease is manually curated to be a phenotypic series according to OMIM (https://www.omim.org/),  one of the most important genetic disease authorities in the world.  A Phenotypic Series is a grouping of genetic heterogeneity of similar phenotypes across the genome.
--     * Slot: is_omimps_descendant Description: Flag to denote this disease is a child/descendant of a disease that is manually curated  to be a phenotypic series according to OMIM (https://www.omim.org/), one of the most  important genetic disease authorities in the world. If it is a descendant of a phenotypic series, it most likely is a proper genetic disease entity (or subtype).
--     * Slot: is_leaf Description: Flag to denote this disease is a leaf node in the disease hierarchy.  A leaf node is a node that has no children in the hierarchy.
--     * Slot: is_leaf_direct_parent Description: Flag to denote this disease is a direct parent of a leaf node in the disease hierarchy.  A direct parent of a leaf rarely corresponds to a grouping, and often is a proper disease entity.
--     * Slot: is_orphanet_disorder Description: Flag to denote this disease is manually curated to be a disease according to Orphanet (https://www.orpha.net/),  one of the most important rare disease authorities in the world.  A disorder according to Orphanet usually corresponds to a proper disease entity, not a grouping or a subtype.
--     * Slot: is_omim Description: Flag to denote this disease is manually curated to be a disease according to OMIM (https://www.omim.org/),  one of the most important genetic disease authorities in the world.  A disease according to OMIM usually corresponds to a proper disease entity or a subtype, not a disease grouping.
--     * Slot: is_icd_category Description: Flag to denote this disease was corresponds to an ICD category. Category codes (or subcategory codes), for example A01.1 (Paratyphoid fever A),  can be recognised by containing a period (.) character and usually represent specific  diagnosable diseases.
--     * Slot: is_icd_chapter_code Description: Flag to denote this disease was corresponds to an ICD chapter code. Chapter codes (or block codes), for example A00-B99 (Certain infectious and parasitic diseases).  These codes can be recognised by containing a dash (-) character, and usually represent broad categories of diseases.
--     * Slot: is_icd_chapter_header Description: Flag to denote this disease was corresponds to an ICD chapter header. Chapter headers (or chapter titles), for example A00 (Cholera) can be identified by codes without dashes or periods and are usually the top-level categories within each chapter. Most of the time, these are not proper diseases, but groupings of diseases.
--     * Slot: is_icd_billable Description: Flag to denote this disease was corresponds to an ICD code that is billable. Billable codes are usually the most specific codes that can be used for billing purposes, and are most of the time diagnosable diseases.
--     * Slot: is_mondo_subtype Description: Flag to denote this disease was identified to be a subtype through lexical matching. This method is maintained by the Every Cure medical team and the Disease List team.
--     * Slot: is_pathway_defect Description: Flag to denote this disease corresponds to a pathway defect rather than a proper disease.
--     * Slot: is_susceptibility Description: Flag to denote this disease corresponds to a susceptibility rather than a proper disease.
--     * Slot: is_paraphilic Description: Flag to denote this disease corresponds to a paraphilic disorder rather than a proper disease.
--     * Slot: is_acquired Description: Flag to denote this disease corresponds to an acquired form of a disease.
--     * Slot: is_andor Description: Flag to denote this disease corresponds to a disease that is a combination of two or more diseases.
--     * Slot: is_withorwithout Description: Flag to denote this disease corresponds to a disease that can be present with or without some other pathological condition.
--     * Slot: is_obsoletion_candidate Description: Flag to denote that this disease is marked for obsoletion in the (near) future. This status does not guarantee that the disease will be obsoleted, but it is a strong indication.
--     * Slot: is_unclassified_hereditary Description: Flag to denote that this disease has no descendants (is a leaf) and  is classified broadly as an hereditary disease, but lacks any further classification.
--     * Slot: official_matrix_filter Description: Flag to denote this disease corresponds to a disease that can be treated with small molecules or biologics. This flag is maintained as a combination of default filters by the Matrix team. Changes to this filter should be discussed on the Matrix disease list issue tracker (https://github.com/everycure-org/matrix-disease-list/issues). **Warning**. This flag is in early alpha state, and its use in production systems is not recommended.
--     * Slot: tag_qaly_lost Description: Tag denoting the degree to which Quality-Adjusted Life Year (QALY) lost. Disease terms are automatically tagged using an LLM. Problems/issues should be reported on the Matrix disease list issue  tracker (https://github.com/everycure-org/matrix-disease-list/issues).
--     * Slot: subset_group_id Description: The identifier of a disease representing the subtype series this disease belongs to.
--     * Slot: subset_group_label Description: The name (label) of a disease representing the subtype series this disease belongs to.
--     * Slot: other_subsets_count Description: The number of other subtypes in the subset this disease belongs to.
--     * Slot: MatrixDiseaseList_id Description: Autocreated FK slot
-- # Class: "MatrixDiseaseList" Description: "A list of diseases."
--     * Slot: id Description: 
-- # Class: "MatrixNode_equivalent_identifiers" Description: ""
--     * Slot: MatrixNode_id Description: Autocreated FK slot
--     * Slot: equivalent_identifiers Description: List of equivalent identifiers for the entity.
-- # Class: "MatrixNode_all_categories" Description: ""
--     * Slot: MatrixNode_id Description: Autocreated FK slot
--     * Slot: all_categories Description: All categories associated with the entity.
-- # Class: "MatrixNode_publications" Description: ""
--     * Slot: MatrixNode_id Description: Autocreated FK slot
--     * Slot: publications Description: Publications associated with the entity.
-- # Class: "MatrixNode_labels" Description: ""
--     * Slot: MatrixNode_id Description: Autocreated FK slot
--     * Slot: labels Description: Alternative labels for the entity.
-- # Class: "MatrixNode_upstream_data_source" Description: ""
--     * Slot: MatrixNode_id Description: Autocreated FK slot
--     * Slot: upstream_data_source Description: Sources from which this entity's data originates.
-- # Class: "MatrixEdge_aggregator_knowledge_source" Description: ""
--     * Slot: MatrixEdge_id Description: Autocreated FK slot
--     * Slot: aggregator_knowledge_source Description: Aggregators of the knowledge.
-- # Class: "MatrixEdge_publications" Description: ""
--     * Slot: MatrixEdge_id Description: Autocreated FK slot
--     * Slot: publications Description: Publications associated with the entity.
-- # Class: "MatrixEdge_upstream_data_source" Description: ""
--     * Slot: MatrixEdge_id Description: Autocreated FK slot
--     * Slot: upstream_data_source Description: Sources from which this entity's data originates.
-- # Class: "DiseaseListEntry_synonyms" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: synonyms Description: Any exact synonyms of the disease.
-- # Class: "DiseaseListEntry_subsets" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: subsets Description: The subsets of the disease in which it is part.
-- # Class: "DiseaseListEntry_crossreferences" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: crossreferences Description: Cross-references to other databases and ontologies.
-- # Class: "DiseaseListEntry_harrisons_view" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: harrisons_view Description: Tag to denote this disease to be part of a grouping according to the Harrison's textbook. Top-level classes in Mondo are manually curated by the Mondo team to "belong" to a Harrison's textbook chapter. Disagreements should be reported on the Mondo issue tracker (https://github.com/monarch-initiative/mondo/issues).
-- # Class: "DiseaseListEntry_mondo_txgnn" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: mondo_txgnn Description: Tag to denote this disease to be part of a grouping as defined by the txgnn paper. Disease classes in Mondo are manually curated by the Mondo team to "belong" to a txgnn category. Disagreements should be reported on the Mondo issue  tracker (https://github.com/monarch-initiative/mondo/issues).
-- # Class: "DiseaseListEntry_mondo_top_grouping" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: mondo_top_grouping Description: Tag to denote this disease to be a . Disease classes in Mondo are manually curated by the Mondo team to "belong" to a txgnn category. Disagreements should be reported on the Mondo issue  tracker (https://github.com/monarch-initiative/mondo/issues).
-- # Class: "DiseaseListEntry_medical_specialization" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: medical_specialization Description: Tag this disease with a medical specialisation. Disease classes are automatically tagged by an LLM. Problems/issues should be reported on the Matrix disease list issue  tracker (https://github.com/everycure-org/matrix-disease-list/issues).
-- # Class: "DiseaseListEntry_txgnn" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: txgnn Description: Tag this disease to be part of a grouping as defined by the txgnn paper. Disease classes in Mondo are automatically assigned to a txgnn category using an LLM. Problems/issues should be reported on the Matrix disease list issue  tracker (https://github.com/everycure-org/matrix-disease-list/issues).
-- # Class: "DiseaseListEntry_anatomical" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: anatomical Description: Tag to denote this disease to be part of a grouping according to the anatomical location. Disease terms are automatically tagged using an LLM. Problems/issues should be reported on the Matrix disease list issue  tracker (https://github.com/everycure-org/matrix-disease-list/issues).
-- # Class: "DiseaseListEntry_is_pathogen_caused" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: is_pathogen_caused Description: Flag to denote if this disease is caused by a pathogen. Disease classes are automatically flagged using an LLM. Problems/issues should be reported on the Matrix disease list issue  tracker (https://github.com/everycure-org/matrix-disease-list/issues).
-- # Class: "DiseaseListEntry_is_cancer" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: is_cancer Description: Flag to denote if this disease corresponds to a cancer type. Disease classes are automatically flagged using an LLM. Problems/issues should be reported on the Matrix disease list issue  tracker (https://github.com/everycure-org/matrix-disease-list/issues).
-- # Class: "DiseaseListEntry_is_glucose_dysfunction" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: is_glucose_dysfunction Description: Flag to denote if this disease corresponds to a glucose dysfunction. Disease classes are automatically flagged using an LLM. tracker (https://github.com/everycure-org/matrix-disease-list/issues).
-- # Class: "DiseaseListEntry_tag_existing_treatment" Description: ""
--     * Slot: DiseaseListEntry_id Description: Autocreated FK slot
--     * Slot: tag_existing_treatment Description: Flag to denote if this disease has some existing treatment. Disease classes are automatically flagged using an LLM. Problems/issues should be reported on the Matrix disease list issue  tracker (https://github.com/everycure-org/matrix-disease-list/issues).

CREATE TABLE "MatrixEdgeCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MatrixNodeCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MatrixDiseaseList" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MatrixNode" (
	id TEXT NOT NULL, 
	name TEXT, 
	category TEXT NOT NULL, 
	description TEXT, 
	international_resource_identifier TEXT, 
	"MatrixNodeCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	FOREIGN KEY("MatrixNodeCollection_id") REFERENCES "MatrixNodeCollection" (id)
);
CREATE TABLE "MatrixEdge" (
	id INTEGER NOT NULL, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	knowledge_level TEXT, 
	primary_knowledge_source TEXT, 
	subject_aspect_qualifier TEXT, 
	subject_direction_qualifier TEXT, 
	object_aspect_qualifier TEXT, 
	object_direction_qualifier TEXT, 
	"MatrixEdgeCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (subject, predicate, object), 
	FOREIGN KEY("MatrixEdgeCollection_id") REFERENCES "MatrixEdgeCollection" (id)
);
CREATE TABLE "DiseaseListEntry" (
	id INTEGER NOT NULL, 
	category_class TEXT, 
	label TEXT, 
	definition TEXT, 
	is_matrix_manually_excluded BOOLEAN, 
	is_matrix_manually_included BOOLEAN, 
	is_clingen BOOLEAN, 
	is_grouping_subset BOOLEAN, 
	is_grouping_subset_ancestor BOOLEAN, 
	is_orphanet_subtype BOOLEAN, 
	is_orphanet_subtype_descendant BOOLEAN, 
	is_omimps BOOLEAN, 
	is_omimps_descendant BOOLEAN, 
	is_leaf BOOLEAN, 
	is_leaf_direct_parent BOOLEAN, 
	is_orphanet_disorder BOOLEAN, 
	is_omim BOOLEAN, 
	is_icd_category BOOLEAN, 
	is_icd_chapter_code BOOLEAN, 
	is_icd_chapter_header BOOLEAN, 
	is_icd_billable BOOLEAN, 
	is_mondo_subtype BOOLEAN, 
	is_pathway_defect BOOLEAN, 
	is_susceptibility BOOLEAN, 
	is_paraphilic BOOLEAN, 
	is_acquired BOOLEAN, 
	is_andor BOOLEAN, 
	is_withorwithout BOOLEAN, 
	is_obsoletion_candidate BOOLEAN, 
	is_unclassified_hereditary BOOLEAN, 
	official_matrix_filter BOOLEAN, 
	tag_qaly_lost TEXT NOT NULL, 
	subset_group_id TEXT, 
	subset_group_label TEXT, 
	other_subsets_count INTEGER, 
	"MatrixDiseaseList_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("MatrixDiseaseList_id") REFERENCES "MatrixDiseaseList" (id)
);
CREATE TABLE "MatrixNode_equivalent_identifiers" (
	"MatrixNode_id" TEXT, 
	equivalent_identifiers TEXT, 
	PRIMARY KEY ("MatrixNode_id", equivalent_identifiers), 
	FOREIGN KEY("MatrixNode_id") REFERENCES "MatrixNode" (id)
);
CREATE TABLE "MatrixNode_all_categories" (
	"MatrixNode_id" TEXT, 
	all_categories TEXT, 
	PRIMARY KEY ("MatrixNode_id", all_categories), 
	FOREIGN KEY("MatrixNode_id") REFERENCES "MatrixNode" (id)
);
CREATE TABLE "MatrixNode_publications" (
	"MatrixNode_id" TEXT, 
	publications TEXT, 
	PRIMARY KEY ("MatrixNode_id", publications), 
	FOREIGN KEY("MatrixNode_id") REFERENCES "MatrixNode" (id)
);
CREATE TABLE "MatrixNode_labels" (
	"MatrixNode_id" TEXT, 
	labels TEXT, 
	PRIMARY KEY ("MatrixNode_id", labels), 
	FOREIGN KEY("MatrixNode_id") REFERENCES "MatrixNode" (id)
);
CREATE TABLE "MatrixNode_upstream_data_source" (
	"MatrixNode_id" TEXT, 
	upstream_data_source TEXT, 
	PRIMARY KEY ("MatrixNode_id", upstream_data_source), 
	FOREIGN KEY("MatrixNode_id") REFERENCES "MatrixNode" (id)
);
CREATE TABLE "MatrixEdge_aggregator_knowledge_source" (
	"MatrixEdge_id" INTEGER, 
	aggregator_knowledge_source TEXT, 
	PRIMARY KEY ("MatrixEdge_id", aggregator_knowledge_source), 
	FOREIGN KEY("MatrixEdge_id") REFERENCES "MatrixEdge" (id)
);
CREATE TABLE "MatrixEdge_publications" (
	"MatrixEdge_id" INTEGER, 
	publications TEXT, 
	PRIMARY KEY ("MatrixEdge_id", publications), 
	FOREIGN KEY("MatrixEdge_id") REFERENCES "MatrixEdge" (id)
);
CREATE TABLE "MatrixEdge_upstream_data_source" (
	"MatrixEdge_id" INTEGER, 
	upstream_data_source TEXT, 
	PRIMARY KEY ("MatrixEdge_id", upstream_data_source), 
	FOREIGN KEY("MatrixEdge_id") REFERENCES "MatrixEdge" (id)
);
CREATE TABLE "DiseaseListEntry_synonyms" (
	"DiseaseListEntry_id" INTEGER, 
	synonyms TEXT, 
	PRIMARY KEY ("DiseaseListEntry_id", synonyms), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_subsets" (
	"DiseaseListEntry_id" INTEGER, 
	subsets TEXT, 
	PRIMARY KEY ("DiseaseListEntry_id", subsets), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_crossreferences" (
	"DiseaseListEntry_id" INTEGER, 
	crossreferences TEXT, 
	PRIMARY KEY ("DiseaseListEntry_id", crossreferences), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_harrisons_view" (
	"DiseaseListEntry_id" INTEGER, 
	harrisons_view TEXT, 
	PRIMARY KEY ("DiseaseListEntry_id", harrisons_view), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_mondo_txgnn" (
	"DiseaseListEntry_id" INTEGER, 
	mondo_txgnn TEXT, 
	PRIMARY KEY ("DiseaseListEntry_id", mondo_txgnn), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_mondo_top_grouping" (
	"DiseaseListEntry_id" INTEGER, 
	mondo_top_grouping TEXT, 
	PRIMARY KEY ("DiseaseListEntry_id", mondo_top_grouping), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_medical_specialization" (
	"DiseaseListEntry_id" INTEGER, 
	medical_specialization TEXT, 
	PRIMARY KEY ("DiseaseListEntry_id", medical_specialization), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_txgnn" (
	"DiseaseListEntry_id" INTEGER, 
	txgnn TEXT, 
	PRIMARY KEY ("DiseaseListEntry_id", txgnn), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_anatomical" (
	"DiseaseListEntry_id" INTEGER, 
	anatomical TEXT, 
	PRIMARY KEY ("DiseaseListEntry_id", anatomical), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_is_pathogen_caused" (
	"DiseaseListEntry_id" INTEGER, 
	is_pathogen_caused BOOLEAN, 
	PRIMARY KEY ("DiseaseListEntry_id", is_pathogen_caused), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_is_cancer" (
	"DiseaseListEntry_id" INTEGER, 
	is_cancer BOOLEAN, 
	PRIMARY KEY ("DiseaseListEntry_id", is_cancer), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_is_glucose_dysfunction" (
	"DiseaseListEntry_id" INTEGER, 
	is_glucose_dysfunction BOOLEAN, 
	PRIMARY KEY ("DiseaseListEntry_id", is_glucose_dysfunction), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);
CREATE TABLE "DiseaseListEntry_tag_existing_treatment" (
	"DiseaseListEntry_id" INTEGER, 
	tag_existing_treatment BOOLEAN, 
	PRIMARY KEY ("DiseaseListEntry_id", tag_existing_treatment), 
	FOREIGN KEY("DiseaseListEntry_id") REFERENCES "DiseaseListEntry" (id)
);