# PyPitations

## Le projet 

Les signaux cardiaques décrits au sein des électrocardiogrammes (ECG) décrivent les battements de coeur.

Le but de ce projet est de classifier des signaux cardiaques de patients normaux et de patients atteints d’arythmie ou d’infarctus du myocarde à l'aide de la Data Science, des techniques et méthodes apprises lors de notre formation de Data Scientist :

Le projet s'est donc articulé comme suit :

- la compréhension du sujet, la découverte de la problématique
- l'exploration, la visualisation des données disponibles (données MIT-BIH et PTB)
- la définition d'une stratégie
- l'utilisation de différents modèles d'apprentissage (machine learning, deep learning, transfer learning)
- l'analyse des résultats des classifications
- la création d'une API pour requêter les modèles sur le dataset MIT BIH test (seuls les algos de regression logistique et SVM seront disponibles pour test)
- le déploiement de cette API dans un cluster Kubernetes

## Pour exécuter le rapport streamlit

```
streamlit run streamlit/app.py
```

## Pour déployer l'api dans un cluster k8s

Avec minikube:
```
minikube start
bash api/k8s/setup.sh
```

