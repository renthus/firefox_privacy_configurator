# Firefox Privacy Configurator

Este projeto permite aplicar configurações de privacidade no Firefox de maneira simples e automatizada.

## Como usar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seuusuario/firefox_privacy_configurator.git
    cd firefox_privacy_configurator
    ```

2. **Configure o caminho do perfil do Firefox**:
    - Abra o Firefox.
    - Digite `about:support` na barra de endereços e pressione Enter.
    - Localize a seção **"Diretório de Perfil"**.
    - Copie o caminho completo exibido.
    - Abra o arquivo `config.json` e cole o caminho copiado no campo `"firefox_profile_path"`.

3. **Instale as dependências**:
    - Crie um ambiente virtual:
      ```bash
      python -m venv venv
      ```
    - Ative o ambiente virtual:
      - No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
      - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
    - Instale as dependências:
      ```bash
      pip install -r requirements.txt
      ```

4. **Execute o script**:
    ```bash
    python main.py
    ```

## Como funciona

O script procura o perfil do Firefox no caminho fornecido no arquivo `config.json`, e aplica configurações de privacidade, como:

- Desativação de cache e coleta de dados.
- Desativação de funcionalidades de rastreamento e geolocalização.
- Alteração de várias configurações de segurança e privacidade no arquivo `prefs.js`.

## Contribuições

Se você quiser contribuir, sinta-se à vontade para fazer um fork do repositório e enviar pull requests!

## Desenvolvedores
| [<img src="https://avatars.githubusercontent.com/u/49447595?v=4" width=115><br><sub>Renato Maldonado</sub>](https://github.com/renthus)
| :---: |

