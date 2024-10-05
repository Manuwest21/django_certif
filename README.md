Résumé du Projet de l'Application "Zéro Gaspi : délices personnalisés"

1. Introduction

L'association « Zéro Gaspi » s'engage à lutter contre le gaspillage alimentaire en aidant les utilisateurs à mieux exploiter les aliments proches de leur date de péremption. Ce projet vise à développer une application qui simplifie cette démarche en fournissant des recettes adaptées aux ingrédients disponibles chez les utilisateurs.

2. Présentation de l'Application

L'application proposera une interface sécurisée, accessible via authentification. Elle permettra aux utilisateurs de sélectionner les ingrédients disponibles, de spécifier leur quantité et de définir leurs préférences en matière de temps de préparation. En intégrant un outil d'intelligence artificielle, l'application générera des recettes personnalisées, facilitant ainsi la cuisine et encourageant une gestion proactive des aliments.

3. Outils Utilisés

L'architecture technique de l'application repose sur plusieurs outils et technologies clés :

    Langages de programmation : Python, HTML/CSS, et Django Template Language pour le développement des interfaces web.
    Framework : Django, utilisé pour le développement de l'application, permettant une gestion simplifiée des bases de données et des interactions avec les utilisateurs.
    Bases de données : SQLite, via Django ORM, pour la gestion des données des utilisateurs et de leurs préférences alimentaires.
    Bibliothèques : requests pour les requêtes API, facilitant l'intégration des fonctionnalités d'OpenAI.
    Services PaaS Azure :
        Azure OpenAI : Intégration des fonctionnalités d'intelligence artificielle pour analyser les ingrédients et générer des recettes.
        Azure Container Registry (ACR) : Stockage et gestion des images Docker.
        Azure Container Instances (ACI) : Déploiement des images Docker pour assurer l'accès à l'application via une adresse web sécurisée.
    Outils de conteneurisation : Docker, utilisé pour créer des images de l’application, garantissant une scalabilité et une maintenance faciles.
    Contrôle de version : GitHub, pour gérer le code source de l'application, avec CI/CD via GitHub Actions pour automatiser les tests et les déploiements.

4. Automatisation et Livraison Continue

La chaîne CI/CD commence par la validation des données pour garantir la qualité des jeux de données utilisés. Les workflows se déclenchent via un fichier YAML, exécutant des jobs successifs : récupération du code, installation de Python et des dépendances, et vérification de la couverture des tests avant le déploiement.

Le déploiement continu se met en place après un push, créant une nouvelle image Docker et la poussant vers le registre de conteneurs Azure en utilisant des informations d'identification sécurisées. Les workflows se déclenchent lors d'événements comme les pushes vers dev5 ou les pull requests vers dev11, assurant des vérifications automatisées pour maintenir la stabilité du code.

GitHub Actions est utilisé pour son intégration native avec GitHub, facilitant la configuration des workflows CI/CD. Les fichiers YAML permettent une personnalisation aisée et un accès gratuit pour les dépôts publics, idéal pour des projets à coût limité.
Intégration de l’API OpenAI

L'intégration de l'API Azure OpenAI avec GPT-4 offre puissance et sécurité, garantissant une gestion efficace des ressources avec un faible coût. L'hébergement dans le même environnement que l'application Django améliore les performances et réduit la latence.

La sécurité est renforcée par une gestion avancée des identités. L'API nécessite une clé API pour l'authentification, limitant l'accès aux utilisateurs autorisés. Azure respecte les normes de protection des données, garantissant la conformité internationale des données traitées.

Conclusion

Ce projet d'application est un pas important vers la lutte contre le gaspillage alimentaire, en offrant aux utilisateurs des outils pratiques et accessibles pour optimiser l'utilisation de leurs ressources alimentaires. En intégrant des fonctionnalités personnalisées et des normes d'accessibilité, l'application se présente comme un allié précieux dans la cuisine quotidienne.
