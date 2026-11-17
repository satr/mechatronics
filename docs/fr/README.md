# Mechatronics Training — Français

**Lire cette page en:** [en](../en/README.md) · [fr](README.md) · [de](../de/README.md) · [it](../it/README.md) · [es](../es/README.md) · [pt](../pt/README.md) · [zh](../zh/README.md) · [ja](../ja/README.md) · [nb](../nb/README.md) · [ru](../ru/README.md) · [ko](../ko/README.md) · [fi](../fi/README.md) · [pl](../pl/README.md)

> [!WARNING]
> **Avertissement :** Ces ressources pédagogiques assistées par IA peuvent contenir des erreurs, des traductions inexactes et des hypothèses incorrectes. Utilisation à vos risques et périls. Vérifiez les calculs indépendamment et n'utilisez aucun exemple pour piloter des machines réelles.

Introduction autonome au mouvement, au calcul différentiel et intégral, aux méthodes numériques, aux systèmes du premier ordre et à l'énergie de rotation.

## Sommaire

1. [Bases du calcul différentiel et intégral](notes/00-calculus-foundations.md)
2. [Mouvement, dérivées et intégrales](notes/01-motion-calculus.md)
3. [Dynamique du premier ordre et rotation](notes/02-first-order-dynamics.md)
4. [Table des intégrales](INTEGRAL_TABLE.md)
5. [Table des dérivées](DERIVATIVE_TABLE.md)
6. [Aide-mémoire des formules](CHEATSHEET.md)
7. [Exercices Python](exercises/README.md)
8. [Symboles et notation](SYMBOLS.md) · [Glossaire des unités](UNITS.md)
9. [Table trigonométrique et exemples mécaniques](TRIGONOMETRY.md)
10. [Commande en boucle fermée : PID et couple de maintien](notes/03-feedback-control.md)
11. [Repères du robot : position et rotation](notes/04-coordinate-frames.md)
12. [Rotation, vitesse et singularités](notes/05-velocity-jacobian.md)
13. [ROS 2 : architecture, nœuds et exercice Docker](notes/06-ros2-foundations.md)

[Dépôt / choix de la langue](../../README.md) · [Sécurité et exactitude](SAFETY.md) · [Licences](LICENSING.md)

## Points essentiels

Étudier une section, refaire le calcul, exécuter la simulation hors ligne et expliquer le résultat avec ses propres mots. Les modèles sont idéalisés, pas des descriptions certifiées d'équipements réels.

Les termes techniques en anglais sont indiqués entre parenthèses lors de leur première présentation.


Les chapitres contiennent des graphiques et des schémas. Les liens de fin de chapitre expliquent l’origine de 4t et de 63.2 %.


**Python / Installer Python et créer un environnement virtuel (Windows/macOS/Linux):** [exercises/README.md](exercises/README.md).

## ROS 2 Jazzy sans GUI : articulation virtuelle

[ROS 2 Jazzy sans GUI : articulation virtuelle](notes/07-ros2-control-lab.md) — URDF · TF2 · ros2_control · mock hardware · ARM64.

**Architecture robot ROS 2 :** [Cinq étapes, diagramme Mermaid et lexique](notes/08-ros2-robot-architecture.md).

**Sans Compose :** [Lancer directement l'image ROS officielle](../../ros2/PLAIN_DOCKER.md).
