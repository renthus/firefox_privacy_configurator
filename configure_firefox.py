import os
import json

def load_config():
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("Erro: O arquivo de configuração 'config.json' não foi encontrado.")
        return None

def apply_firefox_privacy_settings(profile_path):
    prefs_file = os.path.join(profile_path, 'prefs.js')

    if not os.path.exists(prefs_file):
        print(f"[✘] Erro ao configurar o Firefox: Arquivo {prefs_file} não encontrado.")
        print("ℹ️  Abra o Firefox uma vez com o perfil selecionado para gerar o arquivo prefs.js.")
        return False

    try:
        with open(prefs_file, 'a') as file:
            # Adicionando as configurações desejadas no prefs.js
            file.write('\n// Configurações de privacidade aplicadas automaticamente\n')
            file.write('user_pref("privacy.history.custom", true);\n') # Nunca memorizar o histórico
            file.write('user_pref("signon.rememberSignons", false);\n')  # Nunca salvar senhas
            file.write('user_pref("places.history.enabled", false);\n') # Desativar histórico
            file.write('user_pref("browser.urlbar.placeholderName", "DuckDuckGo");\n')  # Define DuckDuckGo como mecanismo de busca padrão
            file.write('user_pref("dom.security.https_only_mode", true);\n')  # Ativar modo somente HTTPS em todas as janelas
            file.write('user_pref("browser.formfill.enable", false);\n') # Desabilitar preenchimento automático de formulários
            file.write('user_pref("browser.cache.disk.enable", false);\n') # Desabilitar cache em disco
            file.write('user_pref("browser.cache.disk_cache_ssl", false);\n') # Desabilitar cache de SSL
            file.write('user_pref("browser.cache.offline.enable", false);\n') # Desabilitar cache offline
            file.write('user_pref("dom.event.clipboardevents.enabled", false);\n') # Desabilitar eventos de clipboard
            file.write('user_pref("geo.enabled", false);\n') # Desabilitar geolocalização
            file.write('user_pref("network.cookie.lifetimePolicy", 2);\n') # Política de cookies para não manter cookies após o fim da sessão
            file.write('user_pref("plugin.scan.plid.all", false);\n') # Desabilitar plugins
            file.write('user_pref("browser.safebrowsing.phishing.enabled", false);\n') # Desabilitar proteção contra phishing
            file.write('user_pref("browser.safebrowsing.malware.enabled", false);\n') # Desabilitar proteção contra malware
            file.write('user_pref("media.navigator.enabled", false);\n') # Desabilitar WebRTC
            file.write('user_pref("dom.battery.enabled", false);\n') # Desabilitar eventos de bateria
            file.write('user_pref("extensions.pocket.enabled", false);\n') # Desabilitar Pocket
            file.write('user_pref("default.browser.agent.enabled", false);\n') # Desabilitar agentes de navegador
            file.write('user_pref("media.peerconnection.enabled", false);\n') # Desabilitar WebRTC
            file.write('user_pref("media.peerconnection.turn.disable", true);\n') # Desabilitar TURN no WebRTC
            file.write('user_pref("media.peerconnection.use_document_iceservers", false);\n') # Desabilitar ICE servers
            file.write('user_pref("media.peerconnection.video.enabled", false);\n') # Desabilitar vídeo WebRTC

        print("[✔] Configurações aplicadas com sucesso!")
        return True
    except Exception as e:
        print(f"[✘] Erro ao configurar o Firefox: {str(e)}")
        return False

def main():
    config = load_config()

    if config is None:
        print("Erro ao carregar as configurações. Verifique se o arquivo 'config.json' está presente.")
        return

    profile_path = config.get('firefox_profile_path')
    if not profile_path or not os.path.exists(profile_path):
        print(f"[✘] O perfil do Firefox não foi encontrado no caminho: {profile_path}")
        print("ℹ️  Verifique o arquivo 'config.json' e forneça o caminho correto para o perfil.")
        return

    print(f"🔍 Buscando perfil padrão do Firefox...\n[✔] Perfil localizado: {profile_path}")
    print("🔧 Aplicando configurações de privacidade...")
    
    if apply_firefox_privacy_settings(profile_path):
        print("Configurações aplicadas com sucesso!")
    else:
        print("Falha ao aplicar as configurações.")

if __name__ == "__main__":
    main()
