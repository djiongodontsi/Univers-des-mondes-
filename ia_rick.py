import os
import numpy as np
import sounddevice as sd
import wave
from groq import Groq

# ============================================
# CONFIGURATION
# ============================================
GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxx"  # ⚠️ Remplace par ta vraie clé Groq
client = Groq(api_key=GROQ_API_KEY)

# ============================================
# FONCTION 1 : ENREGISTRER LA VOIX
# ============================================
def enregistrer_audio(duree=5, frequence=16000):
    print(f"🎤 Parle maintenant (tu as {duree} secondes)...")
    audio = sd.rec(int(duree * frequence), samplerate=frequence, channels=1, dtype='int16')
    sd.wait()
    fichier = "temp_audio.wav"
    with wave.open(fichier, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(frequence)
        wf.writeframes(audio.tobytes())
    print("✅ Enregistrement terminé.")
    return fichier

# ============================================
# FONCTION 2 : TRANSCRIRE AVEC GROQ WHISPER
# ============================================
def transcrire_audio(fichier):
    try:
        with open(fichier, "rb") as f:
            transcription = client.audio.transcriptions.create(
                file=(fichier, f.read()),
                model="whisper-large-v3-turbo",
                language="fr",
                response_format="text"
            )
        texte = transcription.strip()
        print(f"📝 Tu as dit : {texte}")
        return texte
    except Exception as e:
        print(f"❌ Erreur de transcription : {e}")
        return None

# ============================================
# FONCTION 3 : DEMANDER LE VERDICT À L'IA
# ============================================
def demander_verdict(reponse_utilisateur, monde="VISUEL"):
    prompt = f"""
Tu es un juge interdimensionnel dans l'univers de Rick et Morty.
L'utilisateur se trouve dans le MONDE {monde}.
Il a répondu à la question : "As-tu ouvert le portail ?"
Sa réponse est : "{reponse_utilisateur}"

Ta mission : Dis si c'est VRAI ou FAUX.
Réponds en 3 mots maximum. Sois sarcastique.
"""
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Tu es un juge. Tu réponds TOUJOURS en 3 mots maximum. Jamais plus."},
            {"role": "user", "content": prompt}
        ],

        model="openai/gpt-oss-20b",

        temperature=0.7,
        max_tokens=20
    )
    verdict = chat_completion.choices[0].message.content.strip()
    mots = verdict.split()
    if len(mots) > 3:
        verdict = " ".join(mots[:3])
    print(f"⚖️ Verdict : {verdict}")
    return verdict

# ============================================
# PROGRAMME PRINCIPAL
# ============================================
if __name__ == "__main__":
    print("=" * 50)
    print("🎭 TRIBUNAL DES DEUX MONDES - IA")
    print("=" * 50)
    
    monde = "VISUEL"
    
    # Étape 1 : Enregistrer la voix
    fichier = enregistrer_audio(duree=5)
    
    # Étape 2 : Transcrire avec Groq Whisper
    reponse = transcrire_audio(fichier)
    
    # Étape 3 : Demander le verdict à l'IA
    if reponse:
        verdict = demander_verdict(reponse, monde)
        print("\n" + "=" * 50)
        print(f"📺 À AFFICHER SUR L'ÉCRAN LED : {verdict}")
        print("=" * 50)
    else:
        print("❌ Aucune réponse détectée.")
    

  # Nettoyage (désactivé pour garder le fichier)
    #if os.path.exists(fichier):
        #os.remove(fichier)

