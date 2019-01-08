.SILENT:

#------------------------------------------------------------------
# Desafio Zoox Smarth Data
#------------------------------------------------------------------
install:
	python setup.py install

q5: 
	@python questoes/q5.py

q6: 
	@python questoes/q6.py

q7: 
	@python questoes/q7.py

q8: 
	@python questoes/q8.py

q9: 
	@python questoes/q9.py

q11: 
	@python questoes/q11.py

q12: 
	@python questoes/q12.py


remove_csv:
	rm -f noticias.csv

open_csv:
	vi noticias.csv

reload_db_force:
	rm -f noticias.db
	python crawler/core/db/database.py

crawler:
	python crawler/core/modules/crawler.py

processor:
	python crawler/core/modules/processor.py

indexer:
	python crawler/core/modules/indexer.py

pytest:
	py.test

run_crawler: remove_csv reload_db_force crawler processor indexer open_csv