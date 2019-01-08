# Questões Práticas

Para execurtar cada uma das questões pode-se utilizar o comando make seguido abaixo:

```console

make q5
make q6
make q7
make q8
make q9
make q11
make q12

```

# Questão 10 - Crawler

O objetivo deste código é criar um rastreador que visite o site oantagonista.com e salvar um arquivo .csv as notícias mais recentes encontrada.
 
# Dependência
 - Python 3
 
# How to install

 1. clone o repositório.
 2. crie um virtualenv com o Python 3. (https://virtualenv.pypa.io/en/stable/)
 3. ative virtualenv.
 4. instalar as dependências. (pip install -r requirements.txt)
 5. executar o projeto.
 
 ```console
 git clone https://github.com/asafepy/desafio-zoox.git
 cd desafio-zoox
 virtualenv -p python3 .virtualenv
 source .virtualenv/bin/activate
 pip install -r requirements.txt
 cd crawler
 make install
 make run
```

# Como executar:

1. Instalar requisitos e o aplicativo;  
	- pip install -r requirements.txt
 
2. Criar banco de dados de aplicativos;
	- python core/db/database.py
 
3. Executar o Crawler;  
	- python core/modules/crawler.py
        
4. Executando o Processor;
	- python core/modules/processor.py

5. Executando Indexer:
	- python core/modules/indexer.py

7. Usando o Makefile
	
```console
make run
```

## Modules (core/modules) 
 
### crawler.py (MultiThread)
- Responsável pela captura de links do URL informado.

### processor.py (Multiprocess)
- Responsável por ler as informações brutas no banco de dados (WAIT) e atualizá-lo.
- Este é um aplicativo multiprocessado, você pode continuar executando em segundo plano e pode carregar quantos aplicativos desejar, você pode adicionar mais máquinas e / ou mais processos para aumentar a velocidade de processamento.

### indexer.py (SingleProcess)
- Responsável pela geração do arquivo csv, consulta o banco de dados para todos os registros processados e índices em uma planilha csv.