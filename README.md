# Univers-des-mondes-
Solution permettant a rick et morty de savoir dans quel monde aller.
CAHIER DES CHARGES : LE TRIBUNAL DES DEUX MONDES
Workshop National RickLab™ — Bachelor 2
EPSI — Septembre 2026
1. PRÉSENTATION DU PROJET
1.1. Contexte
Dans le cadre du workshop national "RickLab™" de l'EPSI, les étudiants doivent concevoir un prototype technologique interactif mêlant électronique, programmation, IA et fabrication numérique. Le projet doit s'inspirer de l'univers de Rick et Morty et respecter la philosophie du laboratoire : ambition, absurdité, innovation et impact.
1.2. Présentation du Projet
"Le Tribunal des Deux Mondes" est un gadget interactif qui simule un portail interdimensionnel. L'utilisateur scanne une carte RFID pour choisir son monde (Visuel ou Invisible). Il répond à une question à voix haute. Une IA analyse sa réponse et rend un verdict (VÉRITÉ ou MENSONGE). Le verdict s'affiche sur un écran LED, le boîtier réagit physiquement (vibration, mouvement), et un monde virtuel à l'écran d'ordinateur réagit en temps réel.
1.3. Objectifs
Objectif principal : Créer un prototype interactif, ambitieux et fonctionnel qui combine électronique, IA et réalité virtuelle.
Objectifs secondaires :
Expérimenter avec de nouvelles technologies (IA, WebSockets, RFID).
Sortir de la zone de confort technique.
Proposer un projet fun, original et mémorable pour la soutenance.
2. SPÉCIFICATIONS FONCTIONNELLES
2.1. Les Deux Mondes
Caractéristique
Monde Visuel (Français)
Monde Invisible (Anglais)
 
Langue
Français
Anglais
Ambiance
Laboratoire aseptisé, couleurs vives
Chaos, glitchs, couleurs sombres
Personnalité IA
Logique, factuelle
Folle, sarcastique
Réaction VÉRITÉ
Portail s'ouvre en douceur
Portail s'illumine
Réaction MENSONGE
Portail se fissure
Portail explose

2.2. Scénario d'Utilisation
L'utilisateur scanne une carte RFID (Rick = Monde Visuel, Morty = Monde Invisible).
L'écran LED affiche la question : "As-tu ouvert le portail ?"
Le monde virtuel correspondant s'affiche à l'écran d'ordinateur.
L'utilisateur répond à voix haute.
Le PC convertit la voix en texte et l'affiche sur l'écran LED.
Le PC interroge l'IA (avec le contexte du monde).
L'IA rend un verdict (VÉRITÉ ou MENSONGE).
L'ESP32 affiche le verdict, fait vibrer le boîtier si mensonge.
Le monde virtuel réagit au verdict.
2.3. Contraintes Fonctionnelles
Le système doit être interactif : l'utilisateur doit voir une réaction immédiate.
Le système doit gérer l'attente (message de chargement pendant la réflexion de l'IA).
Le système doit être robuste : si le Wi-Fi coupe, un message d'erreur doit s'afficher.
3. SPÉCIFICATIONS TECHNIQUES
3.1. Matériel Embarqué (Obligatoire)
Composant
Rôle
Quantité
 
ESP32
Microcontrôleur principal
1
Lecteur RFID RC522
Identification de l'utilisateur
1
Écran OLED SSD1306 (I2C)
Affichage des messages
1
Cerveau Moteur
Contrôle du servomoteur
1
Servomoteur
Mouvement physique (aiguille, trappe)
1
LED RGB
Feedback visuel (vert/rouge)
1
Micro USB
Capture vocale (relié au PC)
1
Plaquettes, câbles, résistances
Connexions
—
Boîtier imprimé en 3D
Structure (myDIL)
1

3.2. Logiciels et Technologies
Domaine
Technologie
Rôle
 
Embarqué
Arduino IDE (C++)
Programmation de l'ESP32
PC
Python
Chef d'orchestre (voix, IA, communication)
Reconnaissance Vocale
SpeechRecognition + PyAudio
Voix → Texte
Communication
PySerial
PC → ESP32 (USB)
IA
OpenAI API / Groq / Ollama
Analyse et verdict
Monde Virtuel
HTML / CSS / JavaScript (Three.js)
Interface visuelle réactive
Serveur Local
Flask + WebSockets
Communication PC ↔ Monde Virtuel
CAO
Fusion 360 / Tinkercad
Modélisation du boîtier
Fabrication
Imprimante 3D (myDIL)
Impression du boîtier

3.3. Contraintes Techniques
Utilisation obligatoire du myDIL : Le boîtier doit être imprimé en 3D ou découpé au laser.
Utilisation obligatoire de l'IA : L'IA doit être utilisée de manière justifiée (analyse de la réponse, verdict).
Utilisation obligatoire de capteurs/actionneurs : RFID, écran, moteur, LED.
Programmation obligatoire : Le projet doit intégrer une véritable partie logicielle (embarqué + PC + web).
4. SPÉCIFICATIONS FONCTIONNELLES DÉTAILLÉES
4.1. Module RFID
Lecture de l'ID de la carte.
Association ID → Monde (Rick = Visuel, Morty = Invisible).
Affichage du monde sélectionné sur l'écran LED.
4.2. Module Audio
Capture de la voix via micro USB.
Conversion voix → texte (SpeechRecognition).
Affichage du texte reconnu sur l'écran LED.
4.3. Module IA
Envoi du texte + contexte du monde à l'IA.
Prompt structuré : "Tu es un juge interdimensionnel. Monde : [Visuel/Invisible]. Réponse : [texte]. Réponds en 3 mots max."
Réception du verdict (VÉRITÉ / MENSONGE).
4.4. Module ESP32
Réception des ordres du PC via USB.
Affichage du verdict sur l'écran LED.
Activation du moteur si MENSONGE.
Activation de la LED RGB (vert/rouge).
4.5. Module Monde Virtuel
Affichage du monde correspondant (Visuel ou Invisible).
Animation du portail (rotation, ouverture, explosion).
Réaction au verdict : ouverture (VÉRITÉ) ou explosion (MENSONGE).
5. PHILOSOPHIE DU PROJET (RickLab™)
Conformément au cahier des charges du workshop, le projet respecte les règles suivantes :
Un prototype moche mais génial > un prototype propre mais banal.
Un projet ambitieux qui échoue intelligemment > un projet sans risque.
L'humour, le storytelling et la mise en scène sont encouragés.
Les projets absurdes sont acceptés… tant qu'il y a une vraie réflexion technique derrière.
La sécurité reste obligatoire, même dans les multivers.
6. LIVRABLES
Livrable
Format
Échéance
 
Prototype fonctionnel
Boîtier + ESP32 + PC
Semaine 5
Documentation technique
PDF (schémas, code commenté)
Semaine 6
README GitHub
Markdown
Semaine 6
Démo de soutenance
Présentation orale + démo live
Semaine 6
Monde virtuel
Page HTML/JS fonctionnelle
Semaine 5

7. PLANNING PRÉVISIONNEL
Semaine
Tâches
Livrable
 
Semaine 1
Câblage ESP32, test RFID, écran, moteur
ESP32 fonctionnel
Semaine 2
Communication PC ↔ ESP32, reconnaissance vocale
Python ↔ ESP32
Semaine 3
Intégration IA, tests de verdict
IA fonctionnelle
Semaine 4
Création du monde virtuel (HTML/JS)
Interface web
Semaine 5
Assemblage final, impression 3D
Prototype complet
Semaine 6
Documentation, soutenance
Dossier + Démo

8. RISQUES ET MITIGATION
Risque
Probabilité
Impact
Mitigation
 
Wi-Fi instable
Moyenne
Élevé
Utiliser Ollama en local (IA locale)
Latence IA
Élevée
Moyen
Écran de chargement, prompt court
Problème d'alimentation
Moyenne
Élevé
Batterie externe pour l'ESP32
Reconnaissance vocale imprécise
Moyenne
Moyen
Tester avec un micro de qualité, environnement calme
Manque de temps
Élevée
Élevé
Prioriser les étapes 1 à 4, simplifier le monde virtuel

9. CONCLUSION
Le projet "Le Tribunal des Deux Mondes" est un projet ambitieux qui combine électronique, IA, reconnaissance vocale et réalité virtuelle. Il respecte parfaitement la philosophie du RickLab™ : innovation, créativité et impact. En suivant ce cahier des charges, l'équipe s'engage à livrer un prototype fonctionnel, documenté et mémorable pour la soutenance.
