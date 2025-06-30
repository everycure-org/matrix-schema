## Add your own custom Makefile targets here

gen-biolink-imports:  
	$(RUN) python src/matrix_schema/utils/generate_biolink_imports.py

gen-valid-edge-type-table:
	$(RUN) python src/matrix_schema/utils/generate_valid_edge_type_table.py

gen-pydantic:
	$(RUN) gen-pydantic --meta None src/matrix_schema/schema/matrix_schema.yaml > src/matrix_schema/datamodel/matrix_schema_pydantic.py

gen-pandera: gen-pydantic
	@echo "The pandera schema currently needs to be updated manually in src/matrix_schema/datamodel/pandera.py"

gen-project: gen-pydantic gen-pandera gen-biolink-imports gen-valid-edge-type-table
