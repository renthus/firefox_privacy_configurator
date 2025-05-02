import os

def find_firefox_profile():
    # Caminho padrão do perfil no Windows
    firefox_profile_path = os.path.expanduser(r"~\AppData\Roaming\Mozilla\Firefox\Profiles")
    if os.path.exists(firefox_profile_path):
        # Procura por todos os diretórios dentro de Profiles
        for profile_dir in os.listdir(firefox_profile_path):
            profile_path = os.path.join(firefox_profile_path, profile_dir)
            # Verifica se é um diretório e se contém o arquivo prefs.js
            prefs_js_path = os.path.join(profile_path, 'prefs.js')
            if os.path.isdir(profile_path) and os.path.isfile(prefs_js_path):
                return profile_path, prefs_js_path
    return None, None

def main():
    print("🔍 Buscando perfil padrão do Firefox...")
    
    # Buscar o perfil
    profile_path, prefs_js_path = find_firefox_profile()
    
    if profile_path and prefs_js_path:
        print(f"[✔] Perfil localizado: {profile_path}")
        print(f"[✔] Arquivo prefs.js encontrado: {prefs_js_path}")
        
        # Alterações no prefs.js (exemplo de lógica)
        try:
            with open(prefs_js_path, 'a') as prefs_file:
                # Exemplo de configuração de privacidade a ser adicionada no prefs.js
                prefs_file.write('\nuser_pref("privacy.donottrackheader.enabled", true);')
                prefs_file.write('\nuser_pref("browser.formfill.enable", false);')
                prefs_file.write('\nuser_pref("browser.cache.disk.enable", false);')
                prefs_file.write('\nuser_pref("browser.cache.disk_cache_ssl", false);')
                prefs_file.write('\nuser_pref("browser.cache.offline.enable", false);')
                prefs_file.write('\nuser_pref("dom.event.clipboardevents.enabled", false);')
                prefs_file.write('\nuser_pref("geo.enabled", false);')
                prefs_file.write('\nuser_pref("network.cookie.lifetimePolicy", 2);')
                prefs_file.write('\nuser_pref("plugin.scan.plid.all", false);')
                prefs_file.write('\nuser_pref("browser.safebrowsing.phishing.enabled", false);')
                prefs_file.write('\nuser_pref("browser.safebrowsing.malware.enabled", false);')
                prefs_file.write('\nuser_pref("media.navigator.enabled", false);')
                prefs_file.write('\nuser_pref("dom.battery.enabled", false);')
                prefs_file.write('\nuser_pref("extensions.pocket.enabled", false);')
                prefs_file.write('\nuser_pref("default.browser.agent.enabled", false);')
                prefs_file.write('\nuser_pref("media.peerconnection.enabled", false);')
                prefs_file.write('\nuser_pref("media.peerconnection.turn.disable", true);')
                prefs_file.write('\nuser_pref("media.peerconnection.use_document_iceservers", false);')
                prefs_file.write('\nuser_pref("media.peerconnection.video.enabled", false);')
            print("[✔] Configurações de privacidade aplicadas com sucesso!")
        except Exception as e:
            print(f"[✘] Erro ao configurar o Firefox: {e}")
    else:
        print(f"[✘] Erro: Arquivo prefs.js não encontrado.")
        print("ℹ️  Abra o Firefox uma vez com o perfil padrão para gerar o arquivo prefs.js.")

if __name__ == '__main__':
    main()
