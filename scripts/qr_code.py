import os
import qrcode

os.makedirs("outputs/codes", exist_ok=True)

nom = input("Nom du fichier : ")
texte = input("Texte ou URL : ")

img =  qrcode.make(texte)
img.save(f"outputs/codes/{nom}.png")

print("QR code généré avec succés")