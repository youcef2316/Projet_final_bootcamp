# README

# Assistant Médical - Prédiction de Maladies

Ce projet est une application intelligente qui prédit la **maladie la plus probable** à partir de **symptômes** saisis par l'utilisateur.  
Il utilise un **modèle d'arbre de décision** entraîné sur un jeu de données médical.  

---

## Objectifs

- Permettre à l'utilisateur de saisir plusieurs symptômes
- Prédire la maladie la plus probable via un modèle ML
- Afficher les précautions recommandées
- Interface simple via **Streamlit** ou **chatbot**

---

## Contenu du dépôt

| Fichier                         | Description                                         |
|--------------------------------|-----------------------------------------------------|
| `Chatbot_med_app.py`           | Script principal avec interface utilisateur         |
| `decision_tree.pkl`            | Modèle d’arbre de décision entraîné                 |
| `label_encoder.pkl`            | Encodeur pour les labels (maladies)                 |
| `columns.pkl`                  | Liste des symptômes utilisés pour l’entraînement    |
| `requirements.txt`             | Liste des dépendances à installer                   |
| `Presentation PROJET_FINAL.pdf`| Présentation du projet au format PDF                |

---

## Modèle de Machine Learning

- **Algorithme** : `DecisionTreeClassifier`
- **Données d’entraînement** : Dataset structuré (symptômes en colonnes, maladie cible)
- **Validation** : Validation croisée
- **Prétraitement** : Label encoding des maladies, vectorisation des symptômes

---

## Installation et exécution

      1. Cloner le dépôt :
         ```bash
         git clone https://github.com/youcef2316/Projet_final_bootcamp.git
         cd Projet_final_bootcamp
      2. Installer les dépendances :
         ```bash
         pip install -r requirements.txt
   ### **Lancer l'application Streamlit**
      3. Lancer l'application Streamlit :
         ```bash
         streamlit run Chatbot_med_app.py

---

## Exemple d’utilisation
- **Symptômes entrés** : `fever`, `cough`, `fatigue`  
- **Maladie prédite** : `Flu`  
- **Précautions** : Boire beaucoup d’eau, se reposer, consulter un médecin si les symptômes persistent
---
##  Auteur
**Youcef Bengrid**  
Projet réalisé dans le cadre du **bootcamp Data Science 2025** (Alger).



   
