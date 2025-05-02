@"
#!/bin/bash

# Criação do ambiente virtual
python3 -m venv venv

# Ativação do ambiente virtual
source venv/bin/activate

# Instalação das dependências
pip install -r requirements.txt

echo "Ambiente virtual configurado com sucesso!"
"@ | Out-File -Encoding UTF8 setup_env.sh