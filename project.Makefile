## Add your own custom Makefile targets here

gen-biolink-imports:  
	$(RUN) python src/utils/generate_biolink_imports.py

gen-pandera: src/resources/pandera-schema.py.jinja2 $(SOURCE_SCHEMA_PATH)
	$(RUN) jinjanate $^ -o $(PYMODEL)/pandera-schema.py

gen-project: gen-pandera gen-biolink-imports