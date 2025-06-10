## Add your own custom Makefile targets here

gen-biolink-imports:  
	$(RUN) python src/matrix_schema/utils/generate_biolink_imports.py

gen-valid-edge-type-table:
	$(RUN) python src/matrix_schema/utils/generate_valid_edge_type_table.py

gen-pandera: src/resources/pandera-schema.py.jinja2 $(SOURCE_SCHEMA_PATH)
	$(RUN) jinjanate $^ -o $(PYMODEL)/pandera-schema.py

gen-project: gen-pandera gen-biolink-imports gen-valid-edge-type-table
