#!/usr/bin/env bash

# Garante que o Python está no PATH
export PATH="/usr/local/bin:$PATH"

# Instala as dependências Python
pip install -r requirements.txt

# Opcional: Se você tiver um ambiente virtual, ative-o aqui
# source venv/bin/activate

echo "Build Python concluído com sucesso!"
