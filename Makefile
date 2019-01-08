.SILENT:

#------------------------------------------------------------------
# Desafio Zoox Smarth Data
#------------------------------------------------------------------

run: 
	@python questoes/q5.py

install:
	python setup.py install

remove_csv:
	rm -f noticias.csv

open_csv:
	vi noticias.csv

reload_db_force:
	rm -f noticias.db
	python core/db/database.py

crawler:
	python core/modules/crawler.py

processor:
	python core/modules/processor.py

indexer:
	python core/modules/indexer.py

pytest:
	py.test

run: remove_csv reload_db_force crawler processor indexer open_csv