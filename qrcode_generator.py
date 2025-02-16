import qrcode

def generate_url_qr(url, file_path="qrcode.png"):
    """
    Génère un QR Code pour un lien et l'enregistre en image.
    
    :param url: Lien vers lequel le QR Code doit pointer.
    :param file_path: Chemin du fichier où sauvegarder l'image QR Code.
    """
    # Création de l'objet QR Code avec des paramètres de correction d'erreur
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)  # Ajout de l'URL dans le QR Code
    qr.make(fit=True)  # Génération du QR Code
    
    # Création et sauvegarde de l'image QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
    
    print(f"QR Code généré avec succès et enregistré sous : {file_path}")

def generate_wifi_qr(ssid, password, encryption="WPA", file_path="wifi_qr.png"):
    """
    Génère un QR Code pour une connexion Wi-Fi et l'affiche.
    
    :param ssid: Nom du réseau Wi-Fi.
    :param password: Mot de passe du réseau Wi-Fi.
    :param encryption: Type de chiffrement (WPA, WEP, nopass pour réseau ouvert).
    :param file_path: Chemin du fichier où sauvegarder l'image QR Code.
    """
    # Format spécifique pour un QR Code Wi-Fi
    wifi_text = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
    
    # Génération et sauvegarde du QR Code
    qr = qrcode.make(wifi_text)
    qr.save(file_path)

    print(f"QR Code Wi-Fi généré et enregistré sous : {file_path}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Générer un QR Code pour une URL
    generate_url_qr("https://github.com/h-titouan/", "testurl.png")

    # Générer un QR Code pour un réseau Wi-Fi
    generate_wifi_qr("NomDeTonReseau", "MotDePasseWiFi")
