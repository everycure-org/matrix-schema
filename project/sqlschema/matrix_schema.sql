-- # Class: "MatrixNode" Description: "A node in the Biolink knowledge graph."
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: category Description: 
--     * Slot: description Description: 
--     * Slot: equivalent_identifiers Description: 
--     * Slot: all_categories Description: 
--     * Slot: publications Description: 
--     * Slot: labels Description: 
--     * Slot: international_resource_identifier Description: 
--     * Slot: upstream_data_source Description: 
--     * Slot: MatrixNodeCollection_id Description: Autocreated FK slot
-- # Class: "MatrixEdge" Description: "An edge representing a relationship between two nodes in the Biolink knowledge graph."
--     * Slot: id Description: 
--     * Slot: subject Description: 
--     * Slot: predicate Description: 
--     * Slot: object Description: 
--     * Slot: knowledge_level Description: 
--     * Slot: primary_knowledge_source Description: 
--     * Slot: aggregator_knowledge_source Description: 
--     * Slot: publications Description: 
--     * Slot: subject_aspect_qualifier Description: 
--     * Slot: subject_direction_qualifier Description: 
--     * Slot: object_aspect_qualifier Description: 
--     * Slot: object_direction_qualifier Description: 
--     * Slot: upstream_data_source Description: 
--     * Slot: MatrixEdgeCollection_id Description: Autocreated FK slot
-- # Class: "MatrixEdgeCollection" Description: "A holder for MatrixEdge objects."
--     * Slot: id Description: 
-- # Class: "MatrixNodeCollection" Description: "A holder for MatrixNode objects."
--     * Slot: id Description: 
-- # Class: "DiseaseListEntry" Description: "A disease entry in the disease list."
--     * Slot: id Description: 
--     * Slot: category_class Description: 
--     * Slot: label Description: 
--     * Slot: definition Description: 
--     * Slot: synonyms Description: 
--     * Slot: subsets Description: 
--     * Slot: crossreferences Description: 
--     * Slot: is_matrix_manually_excluded Description: 
--     * Slot: is_matrix_manually_included Description: 
--     * Slot: is_clingen Description: 
--     * Slot: is_grouping_subset Description: 
--     * Slot: is_grouping_subset_ancestor Description: 
--     * Slot: is_orphanet_subtype Description: 
--     * Slot: is_orphanet_subtype_descendant Description: 
--     * Slot: is_omimps Description: 
--     * Slot: is_omimps_descendant Description: 
--     * Slot: is_leaf Description: 
--     * Slot: is_leaf_direct_parent Description: 
--     * Slot: is_orphanet_disorder Description: 
--     * Slot: is_omim Description: 
--     * Slot: is_icd_category Description: 
--     * Slot: is_icd_chapter_code Description: 
--     * Slot: is_icd_chapter_header Description: 
--     * Slot: is_icd_billable Description: 
--     * Slot: is_mondo_subtype Description: 
--     * Slot: is_pathway_defect Description: 
--     * Slot: is_susceptibility Description: 
--     * Slot: is_paraphilic Description: 
--     * Slot: is_acquired Description: 
--     * Slot: is_andor Description: 
--     * Slot: is_withorwithout Description: 
--     * Slot: is_obsoletion_candidate Description: 
--     * Slot: is_unclassified_hereditary Description: 
--     * Slot: official_matrix_filter Description: 
--     * Slot: harrisons_view Description: 
--     * Slot: mondo_txgnn Description: 
--     * Slot: mondo_top_grouping Description: 
--     * Slot: medical_specialization Description: 
--     * Slot: txgnn Description: 
--     * Slot: anatomical Description: 
--     * Slot: is_pathogen_caused Description: 
--     * Slot: is_cancer Description: 
--     * Slot: is_glucose_dysfunction Description: 
--     * Slot: tag_existing_treatment Description: 
--     * Slot: tag_qaly_lost Description: 
--     * Slot: subset_group_id Description: 
--     * Slot: subset_group_label Description: 
--     * Slot: other_subsets_count Description: 
--     * Slot: MatrixDiseaseList_id Description: Autocreated FK slot
-- # Class: "MatrixDiseaseList" Description: "A list of diseases."
--     * Slot: id Description: 

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
	equivalent_identifiers TEXT, 
	all_categories TEXT, 
	publications TEXT, 
	labels TEXT, 
	international_resource_identifier TEXT, 
	upstream_data_source TEXT, 
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
	aggregator_knowledge_source TEXT, 
	publications TEXT, 
	subject_aspect_qualifier TEXT, 
	subject_direction_qualifier TEXT, 
	object_aspect_qualifier TEXT, 
	object_direction_qualifier TEXT, 
	upstream_data_source TEXT, 
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
	synonyms TEXT, 
	subsets TEXT, 
	crossreferences TEXT, 
	is_matrix_manually_excluded TEXT, 
	is_matrix_manually_included TEXT, 
	is_clingen TEXT, 
	is_grouping_subset TEXT, 
	is_grouping_subset_ancestor TEXT, 
	is_orphanet_subtype TEXT, 
	is_orphanet_subtype_descendant TEXT, 
	is_omimps TEXT, 
	is_omimps_descendant TEXT, 
	is_leaf TEXT, 
	is_leaf_direct_parent TEXT, 
	is_orphanet_disorder TEXT, 
	is_omim TEXT, 
	is_icd_category TEXT, 
	is_icd_chapter_code TEXT, 
	is_icd_chapter_header TEXT, 
	is_icd_billable TEXT, 
	is_mondo_subtype TEXT, 
	is_pathway_defect TEXT, 
	is_susceptibility TEXT, 
	is_paraphilic TEXT, 
	is_acquired TEXT, 
	is_andor TEXT, 
	is_withorwithout TEXT, 
	is_obsoletion_candidate TEXT, 
	is_unclassified_hereditary TEXT, 
	official_matrix_filter TEXT, 
	harrisons_view TEXT, 
	mondo_txgnn TEXT, 
	mondo_top_grouping TEXT, 
	medical_specialization TEXT, 
	txgnn TEXT, 
	anatomical TEXT, 
	is_pathogen_caused TEXT, 
	is_cancer TEXT, 
	is_glucose_dysfunction TEXT, 
	tag_existing_treatment TEXT, 
	tag_qaly_lost TEXT, 
	subset_group_id TEXT, 
	subset_group_label TEXT, 
	other_subsets_count TEXT, 
	"MatrixDiseaseList_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("MatrixDiseaseList_id") REFERENCES "MatrixDiseaseList" (id)
);