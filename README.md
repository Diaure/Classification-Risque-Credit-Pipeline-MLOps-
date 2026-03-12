# Classification Risque Crédit - Pipeline MLOps

## Contexte
L’entreprise souhaite mettre en place un système automatisé de scoring crédit capable :
- d’estimer la probabilité de défaut d’un client,
- de classer automatiquement une demande en crédit accordé ou crédit refusé,
- tout en garantissant transparence et industrialisation du cycle de vie du modèle.

Ce projet s’inscrit dans une démarche MLOps complète, du tracking d’expérimentations jusqu’au serving du modèle.

## Objectifs du projet

Ce projet a pour objectif principal de **construire et optimiser un modèle de scoring prédictif du risque de défaut**.

Autrement dit, il faudra:
- Analyser les variables explicatives:
    - Feature importance globale
    - Explicabilité locale (niveau client)

- Implémenter une démarche MLOps complète:
    - Tracking des expérimentations
    - Model Registry
    - Serving

- Optimiser un score métier prenant en compte:
    - Le déséquilibre de classes
    - Le coût asymétrique des erreurs (FN = 10 × FP)

- Comparer plusieurs modèles via Cross-Validation et GridSearch.

## Sources de données

![Lien entre les tables](https://raw.githubusercontent.com/Diaure/Classification-Risque-Credit-Pipeline-MLOps-/master/Images/Schemas_tables.png)

Nous avons reçu des données provenant de sources multiples:
- Socio‑démographiques
- Historiques de crédit
- Comportements de paiement
- Interactions avec d’autres institutions

## Nettoyage structurel des données

Avant toute modélisation, un nettoyage approfondi a été réalisé pour garantir la qualité des données :

**1. Harmonisation des types**
- Conversion des dates en format datetime
- Uniformisation des variables catégorielles
- Correction des types numériques (float/int)

**2. Préparation des valeurs manquantes & outliers**

L’objectif ici n’est pas de *“nettoyer à la main”*, mais de préparer les données pour qu’elles soient
traitées de manière systématique dans le pipeline MLOps, sans logique ad hoc.

**3. Nettoyage structurel**
- Harmonisation des noms de varibales et modifications des formats
- Suppression des colonnes constantes ou quasi‑constantes
- Suppression des identifiants non pertinents
- Vérification des doublons
- Fusion des tables <> obtenir un seul historique complet des comportements des clients.

## Feature Engineering

Pour chaque client, des agrégations (*min, max, mean, count, sum*) ont été calculées sur les tables.

Concernant les colonnes crées, nous avons choisi d'intéger des varialbles majoritairement liées au comportement réel de remboursement du crédit:
- **PAYMENT_DELAY**: retard réel vs prévu
- **LATE_PAYMENT**: indicateur de retard
- **PARTIAL_PAYMENT**: paiement incomplet
- **EARLY_PAYMENT**: paiement anticipé
- **PAYMENT_RATIO**: montant payé / montant
- **UTILIZATION**: utilisation du crédit
PAYMENT_RATIO : ratio paiement / retraits


## Analyse exploratoire — Conclusions clés
L’analyse exploratoire a permis d’identifier plusieurs signaux forts sur le profil des *mauvais payeurs*:

**1. Variables socio‑démographiques**
- Revenus faibles présentent un taux de défaut plus élevé
- Les célibataires et divorcés sont plus à risque
- Les niveaux d’éducation inférieurs sont associés à un risque accru

**2. Historique de crédit**
- Les clients ayant déjà eu des retards plus risqués
- La capacité de remboursement du client est un des indicateurs forts
- Un ratio payé/dû traduisant des paiements irréguliers.

**3. Comportement de paiement**
- Les refus antérieurs sont très prédictifs
- Les nouveaux clients sont plus incertains
- Les retards successifs sont très discriminants

## Approche MLOps

![Lien entre les tables](https://raw.githubusercontent.com/Diaure/Classification-Risque-Credit-Pipeline-MLOps-/master/Images/Approche_mlops.png)