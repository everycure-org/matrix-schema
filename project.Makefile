## Add your own custom Makefile targets here

.PHONY: generate_biolink_imports
gen-biolink-imports:  
	$(RUN) python src/matrix_schema/utils/generate_biolink_imports.py

.PHONY: generate_valid_edge_type_table
gen-valid-edge-type-table:
	$(RUN) python src/matrix_schema/utils/generate_valid_edge_type_table.py

.PHONY: gen-pydantic
gen-pydantic:
	$(RUN) gen-pydantic --meta None src/matrix_schema/schema/matrix_schema.yaml > src/matrix_schema/datamodel/matrix_schema_pydantic.py

# generate pandera schemas
.PHONY: gen-pandera
gen-pandera:
	python -m matrix_schema.generators.panderagen $(SOURCE_SCHEMA_PATH) -c MatrixNode -c MatrixEdge -c UnionedNode -c UnionedEdge --output $(PYMODEL)/pandera.py


gen-project: gen-pydantic gen-pandera gen-biolink-imports gen-valid-edge-type-table
