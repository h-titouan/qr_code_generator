# QR Code Generator 📷

Un script Python permettant de générer des QR Codes pour :  
✅ Un **lien URL**  
✅ Une **connexion Wi-Fi automatique**  

## 📌 Fonctionnalités  
- Générer un QR Code pointant vers une URL.  
- Générer un QR Code permettant une connexion Wi-Fi sans avoir à entrer le mot de passe.  
- Sauvegarde automatique des QR Codes en image `.png`.  

## 🛠️ Installation  
Assure-toi d’avoir **Python 3.x** installé sur ton système.  
Installe la bibliothèque nécessaire avec :  
```sh
pip install qrcode[pil]  
```

## 🚀 Utilisation

Exécute le script en Python : `python qrcode_generator.py`     

Ou importe les fonctions dans un autre projet :

### 1️⃣ Générer un QR Code pour une URL

```python
from qrcode_generator import generate_url_qr

generate_url_qr("https://example.com", "mon_qr.png")
```

### 2️⃣ Générer un QR Code pour un réseau Wi-Fi  

```python
from qrcode_generator import generate_wifi_qr  

generate_wifi_qr("NomDuReseau", "MotDePasse")  
```

## 📂 Arborescence du projet

Une fois les fonctions exécutées l'arborescence du projet sera la suivante :   

📁 QRCodeGenerator  
 ├── qrcode_generator.py  # Script principal  
 ├── README.md            # Documentation  
 ├── testurl.png          # QR Code pointant vers une URL  
 ├── wifi_qr.png          # QR Code Wi-Fi  