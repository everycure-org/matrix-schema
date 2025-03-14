## MatrixNodeList-001
### Input
```yaml
nodes:
- all_categories:
  - biolink:ChemicalEntity
  - biolink:Drug
  category: biolink:Drug
  description: A drug used to reduce pain, fever, and inflammation.
  equivalent_identifiers:
  - CHEBI:15365
  - DRUGBANK:DB00945
  id: example:Node001
  international_resource_identifier: http://purl.obolibrary.org/obo/CHEBI_15365
  labels:
  - Acetylsalicylic Acid
  name: Aspirin
  publications:
  - PMID:12345678
  upstream_data_source:
  - DrugBank
- all_categories:
  - biolink:Disease
  - biolink:PhenotypicFeature
  category: biolink:Disease
  description: A condition caused by reduced blood flow to the heart.
  equivalent_identifiers:
  - MONDO:0005061
  id: example:Node002
  international_resource_identifier: http://purl.obolibrary.org/obo/MONDO_0005061
  labels:
  - Heart Attack
  name: Myocardial Infarction
  publications:
  - PMID:87654321
  upstream_data_source:
  - OMIM
- all_categories:
  - biolink:ChemicalEntity
  category: biolink:ChemicalEntity
  description: A substance that inhibits the cyclooxygenase enzyme.
  equivalent_identifiers:
  - CHEBI:35544
  id: example:Node003
  international_resource_identifier: http://purl.obolibrary.org/obo/CHEBI_35544
  labels:
  - Cyclooxygenase Inhibitor
  name: COX Inhibitor
  publications:
  - PMID:23456789
  upstream_data_source:
  - ChEBI

```
## MatrixDiseaseList-001
### Input
```yaml
disease_list_entries:
- anatomical:
  - bone_disorder
  - joint_disorder
  category_class: MONDO:12345
  crossreferences:
  - MEDGEN:1843119
  - UMLS:C5679981
  - GARD:21216
  - Orphanet:295193
  - icd11.foundation:1391914407
  definition: ''
  harrisons_view:
  - hereditary_disease
  - chromosomal_disorder
  - musculoskeletal_system_disorder
  - disorder_of_development_or_morphogenesis
  is_acquired: false
  is_andor: false
  is_cancer: false
  is_clingen: false
  is_glucose_dysfunction: false
  is_grouping_subset: false
  is_grouping_subset_ancestor: false
  is_icd_billable: false
  is_icd_category: false
  is_icd_chapter_code: false
  is_icd_chapter_header: false
  is_leaf: true
  is_leaf_direct_parent: false
  is_matrix_manually_excluded: false
  is_matrix_manually_included: false
  is_mondo_subtype: false
  is_obsoletion_candidate: false
  is_omim: false
  is_omimps: false
  is_omimps_descendant: false
  is_orphanet_disorder: false
  is_orphanet_subtype: true
  is_orphanet_subtype_descendant: false
  is_paraphilic: false
  is_pathogen_caused: false
  is_pathway_defect: false
  is_susceptibility: false
  is_unclassified_hereditary: false
  is_withorwithout: false
  label: zygodactyly type 4
  medical_specialization:
  - orthopaedic
  - genetics_and_genomics
  mondo_top_grouping:
  - disorder_of_development_or_morphogenesis
  - musculoskeletal_system_disorder
  - chromosomal_disorder
  - hereditary_disease
  mondo_txgnn:
  - other
  official_matrix_filter: true
  other_subsets_count: 9
  subset_group_id: MONDO:12345
  subset_group_label: ''
  subsets:
  - mondo:harrisons_view_hereditary_disease
  - mondo:mondo_top_grouping_disorder_of_development_or_morphogenesis
  - mondo:tag_qualy_lost_other
  - mondo:tag_qaly_lost_member
  - mondo:harrisons_view_chromosomal_disorder
  - mondo:harrisons_view_musculoskeletal_system_disorder
  - mondo:medical_specialization_orthopaedic
  - mondo:ordo_subtype_of_a_disorder
  - mondo:is_glucose_dysfunction_member
  - mondo:txgnn_metabolic_disorder
  - mondo:medical_specialization_member
  - mondo:gard_rare
  - mondo:harrisons_view_disorder_of_development_or_morphogenesis
  - mondo:mondo_top_grouping_member
  - mondo:is_cancer_member
  - mondo:mondo_top_grouping_musculoskeletal_system_disorder
  - mondo:txgnn_member
  - mondo:is_pathogen_caused_false
  - mondo:is_glucose_dysfunction_false
  - mondo:tag_existing_treatment_false
  - mondo:anatomical_member
  - mondo:tag_existing_treatment_member
  - mondo:mondo_top_grouping_chromosomal_disorder
  - mondo:nord_rare
  - mondo:is_cancer_false
  - mondo:tag_qaly_lost_medium
  - mondo:anatomical_bone_disorder
  - mondo:mondo_txgnn_other
  - mondo:harrisons_view_member
  - mondo:anatomical_other
  - mondo:is_pathogen_caused_member
  - mondo:txgnn_autoimmune_diseases
  - mondo:mondo_top_grouping_hereditary_disease
  - mondo:anatomical_joint_disorder
  - mondo:medical_specialization_genetics_and_genomics
  - mondo:rare
  synonyms:
  - syndactyly type 1, Castilla type
  - SD1d
  - syndactyly type 1d
  - Zygodactyly, Castilla type
  - SD1, Castilla type
  tag_existing_treatment: false
  tag_qaly_lost: medium
  txgnn:
  - metabolic_disorder
  - autoimmune_diseases

```
## MatrixEdgeList-001
### Input
```yaml
edges:
- aggregator_knowledge_source:
  - OMIM
  knowledge_level: high
  object: example:Node002
  object_aspect_qualifier: treatment
  object_direction_qualifier: reduces
  predicate: biolink:treats
  primary_knowledge_source: DrugBank
  publications:
  - PMID:98765432
  subject: example:Node001
  subject_aspect_qualifier: mode of action
  subject_direction_qualifier: inhibits
  upstream_data_source:
  - DrugBank
- aggregator_knowledge_source:
  - MONDO
  knowledge_level: moderate
  object: example:Node003
  object_aspect_qualifier: molecular mechanism
  predicate: biolink:has_phenotype
  primary_knowledge_source: OMIM
  publications:
  - PMID:56789012
  subject: example:Node002
  subject_aspect_qualifier: disease manifestation
  upstream_data_source:
  - OMIM
- aggregator_knowledge_source:
  - DrugBank
  knowledge_level: low
  object: example:Node001
  object_aspect_qualifier: drug effect
  predicate: biolink:interacts_with
  primary_knowledge_source: ChEBI
  publications:
  - PMID:45678901
  subject: example:Node003
  subject_aspect_qualifier: biochemical interaction
  upstream_data_source:
  - ChEBI

```
