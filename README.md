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

## Données

![Lien entre les tables](https://raw.githubusercontent.com/Diaure/Classification-Risque-Credit-Pipeline-MLOps-/master/Images/Schemas_tables.png)

![Tables](https://github.com/Diaure/Classification-Risque-Credit-Pipeline-MLOps-/master/Images/Schemas_tables.png)

![Data](https://github.com/Diaure/Classification-Risque-Credit-Pipeline-MLOps-/blob/master/Images/Approche_mlops.png)

Nous avons reçu des données provenant de sources multiples:
- Socio‑démographiques
- Historiques de crédit
- Comportements de paiement
- Interactions avec d’autres institutions

##