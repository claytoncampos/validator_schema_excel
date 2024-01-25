### Instalação e Configuração
1. Clone o repositório:
```bash
git clone https://github.com/claytoncampos/validator_schema_excel.git
cd validator_schema_excel
```
2. Configure a versão correta do Python com `pyenv`:
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```
3. Instale as dependências do projeto:
```bash
python -m venv .venv
# O padrao é utilizar .venv
source .venv/bin/activate
# Usuários Linux e mac
.venv\Scripts\Activate
# Usuários Windows
pip install -r requirements.txt  
```

3. Execução do projeto local:
```bash
# Para rodar local
task run
# Rodar os testes
task test
```

4. Teste o deploy da aplicação:
```bash
https://validatorschemaexcel.streamlit.app/

#Para testar baixe o arquivo do diretorio /data/arquivo_excel.xlsx
Faça o upload na aplicação e veja a validação do schema
Veja na documentação o Schema válido https://claytoncampos.github.io/validator_schema_excel/
Edite o conteudo do arquivo e teste novamente a validação do schema
```

