# Firefox Privacy Configurator

Este projeto permite aplicar configurações de privacidade no Firefox de maneira simples e automatizada.

## 🔐 Configurações de Privacidade e Segurança Aplicadas

Este projeto aplica configurações avançadas ao Firefox com foco em **privacidade, segurança e anonimato**. Essas modificações automáticas garantem uma navegação mais segura e discreta, especialmente útil para profissionais de segurança, jornalistas, pesquisadores e qualquer pessoa preocupada com o rastreamento digital.

As configurações ajustadas impedem o armazenamento de histórico, bloqueiam vazamentos de IP via WebRTC, desativam o cache, geolocalização, preenchimento automático de formulários e comunicação com servidores externos. Sem essas alterações, o navegador pode vazar informações sensíveis como senhas, localização, histórico, IP real e hábitos de navegação, além de estar vulnerável a mecanismos de rastreamento por fingerprinting.

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

## Configurações Detalhadas

| Configuração | Descrição | Benefício | Risco se não aplicada |
|--------------|-----------|-----------|------------------------|
| `privacy.history.custom = true` | Ativa configurações personalizadas de histórico | Controle total sobre o que é armazenado | Histórico pode ser salvo sem consentimento |
| `signon.rememberSignons = false` | Não salvar senhas localmente | Protege credenciais contra malwares ou acessos indevidos | Armazenamento de senhas pode ser explorado |
| `places.history.enabled = false` | Desativa o histórico de navegação | Evita rastreamento de comportamento | Histórico pode revelar hábitos e comprometer privacidade |
| `browser.urlbar.placeholderName = "DuckDuckGo"` | Define DuckDuckGo como motor de busca | Busca anônima e sem rastreio | Mecanismos comuns rastreiam termos de busca |
| `dom.security.https_only_mode = true` | Ativa o modo apenas HTTPS | Garante comunicação segura | HTTP permite interceptação de dados |
| `browser.formfill.enable = false` | Desativa preenchimento automático | Evita inserção acidental de dados sensíveis | Campos podem ser preenchidos automaticamente em sites maliciosos |
| `browser.cache.disk.enable = false` | Desativa cache em disco | Impede armazenamento de dados acessados | Dados podem ser recuperados por terceiros |
| `browser.cache.disk_cache_ssl = false` | Evita cache de páginas HTTPS | Garante sigilo mesmo offline | Informações criptografadas podem ser expostas |
| `browser.cache.offline.enable = false` | Desativa cache offline | Reduz persistência de dados localmente | Sites podem guardar rastros mesmo offline |
| `dom.event.clipboardevents.enabled = false` | Impede sites de capturar eventos de copiar/colar | Bloqueia tentativas de monitoramento de ações | Sites podem rastrear interações com textos |
| `geo.enabled = false` | Desativa geolocalização | Protege identidade e localização | Localização pode ser usada para rastreamento |
| `network.cookie.lifetimePolicy = 2` | Cookies expiram ao fechar o navegador | Elimina rastros de sessão | Cookies persistentes mantêm rastreamento |
| `plugin.scan.plid.all = false` | Não carrega plugins do sistema automaticamente | Reduz exposição a falhas de segurança | Plugins antigos podem conter vulnerabilidades |
| `browser.safebrowsing.phishing.enabled = false`<br>`browser.safebrowsing.malware.enabled = false` | Desativa Safe Browsing | Reduz comunicação com Google | Perde proteção automática contra sites perigosos |
| `media.navigator.enabled = false` | Bloqueia acesso à câmera/mic | Impede ativação remota via WebRTC | Sites podem acessar mídia sem consentimento |
| `dom.battery.enabled = false` | Oculta nível de bateria | Impede rastreamento via fingerprint | Pode ser usada como identificador único |
| `extensions.pocket.enabled = false` | Desativa Pocket | Evita coleta de dados via leitura/sincronização | Pocket envia dados para servidores externos |
| `default.browser.agent.enabled = false` | Impede envio de dados à Mozilla | Reduz vazamento de metadados | Informações podem ser utilizadas para fingerprinting |
| `media.peerconnection.*` | Desativa completamente o WebRTC | Bloqueia vazamento de IP real, mesmo com VPN | IP real pode vazar por conexões P2P não criptografadas |

## Contribuições

Se você quiser contribuir, sinta-se à vontade para fazer um fork do repositório e enviar pull requests!

## Desenvolvedores
| [<img src="https://avatars.githubusercontent.com/u/49447595?v=4" width=115><br><sub>Renato Maldonado</sub>](https://github.com/renthus)
| :---: |

