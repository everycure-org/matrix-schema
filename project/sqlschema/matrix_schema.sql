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

CREATE TABLE "MatrixEdgeCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MatrixNodeCollection" (
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