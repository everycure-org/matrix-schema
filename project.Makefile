## Add your own custom Makefile targets here

gen-biolink-imports:  
	$(RUN) python src/matrix_schema/utils/generate_biolink_imports.py

gen-valid-edge-type-table:
	$(RUN) python src/matrix_schema/utils/generate_valid_edge_type_table.py

gen-pandera:
	@echo "The pandera schema currently needs to be updated manually in src/matrix_schema/datamodel/pandera.py"

gen-project: gen-pandera gen-biolink-imports gen-valid-edge-type-table
