# Single-cell-type-classification
Ce projet est réalisé en groupe de 3 dans le cadre de l'UE Data Camp de notre programme de master de data science. Il consiste à classe les cellules en quatre types en fonction des différents gènes présents dans celles-ci.

# suivi-datacamp
Les points hebdomadaires se feront sur ce README.md

| Membres de l'équipe |
| ------------------- |
| Aline GABRIEL       |
| Alimatou TRAORE     |
| Murielle MAJUM      |

# Récapitulatif des scores

| team |	submission|	bal_acc|	train time [s]|	validation time [s]	|	submitted at (UTC)|
| ----------- | ------------- |------------ |----------- |------- |---------- |
|	MurielleMajum|	GAB_TRA_2	|0.87|	124.554377	|2.807956	|2023-12-12 13:21:49|
|Aline_G	|GAB_TRA_SE_15|	0.86	|767.834606	|2.906096	|	2023-12-12 21:06:31|
|	MurielleMajum	|GAB_TRA_SE_10|	0.86	|66.537567|	2.032510|	2023-12-07 19:14:12|
|Alimatou_Traore	|SKD_MAA_3|	0.84|	338.033050|	2.525157 |	2023-12-10 15:07:12|
|Aline_G	|GTM_V1|	0.82	|147.770997|	4.238968|	2023-11-28 09:35:52|
| Aline_G| 	MLP_AG_AT_MM_V2b	| 0.78	| 10.112936| 	2.041714	| 2023-11-21 12:34:45| 
| Aline_G | MLP_AG_AT_MM_V2 |	0.77 | 10.138159	| 2.079607	| 2023-11-21 12:16:21|
| Aline_G | MLP_AG_AT_MM	| 0.73	|41.767641	| 1.422422	|2023-11-21 08:17:53 |


# Points
##  26 octobre

### Objectifs 

  * Bonne installation des outils
  * Compréhension des données et des objectifs du projet
  * Première analyse descriptive

### Avancement
  * Discussion : données génétiques
  * Problème de réduction de dimension : étude de différentes méthodes ( ACP , Lasso, ... )
    
##  2 novembre 

### Objectifs 
  * Etude bibliographique : méthodes adaptées
  * Premiers résultats
    
### Avancement
  * Premiers résultats: Utilisation des méthodes de SVM, KNN qui donnent une accuracy meilleure que la méthode de Random Forest
  * Discussion sur les hyperparamètres des modèles
  * Discussion sur le prétraitement de données
       * Normalisation des données: méthode min-max?
       * ACP : nous avons remarqué que 12 composantes principales permettent d'expliquer plus de 80% de la variance. Est-ce vraiment suffisant ?
       * Nous cherchons de nouvelles methodes de réduction de dimension 

##  14 Novembre

### Objectifs
  * Ajuster les hyperparamètres
  * Essayer d'autres modèles
  * Travailler sur le prétraitement des données (échelle logarithmique ?)

### Avancement 
   
   * Résultats des différents modèles testés :
   * Alimatou
     *   SVM :  C= 10  , Kernel= "rbf"  et Train balanced accuracy : 0.772 Test balanced accuracy : 0.69
     *   KNN :  n_neighbors: 7  et Train balanced accuracy : 0.746  Test balanced accuracy : 0.630
     *   Random Forest :  max_depth: 10, n_estimators: 200 et Train balanced accuracy : 0.949 Test balanced accuracy : 0.595
   * Murielle
     *   Gradient Boosting Classifier : learning_rate=0.1, max_depth : 3, n_estimators=50, Test balanced accuracy : 0.683
     *   Réseaux de neurones convolutifs : MLP (hidden_layer_sizes=(100, 50), activation='relu', solver='adam', max_iter=1000), Test balanced accuracy : 0.76
     *   DecisionTreeClassifier : n_components=60, min_samples_split=2, min_samples_leaf=1, Test balanced accuracy : 0.668
     *   SVC : PCA(n_components=70), SVC(kernel='linear', C=1.0), Test balanced accuracy : 0.72
     *   Stacking (Bagging, DecisionTreeClassifier) : n_components=60, min_samples_split=2, min_samples_leaf=1, Test balanced accuracy : 0.697
     *   Stacking : MLP(hidden_layer_sizes=(100, 50), activation='relu', solver='adam', max_iter=1000) comme meta_model, et les modèles de base sont :
         * TroncatedSVD comme méthode de réduction de dimension avec n_components=100 pour SVC et n_components=65 pour RF
         * Random Forest: n_estimators=100, max_features=3, 
         * SVC: kernel='linear', C=1.0
         * Test balanced accuracy : 0.778 en local
         * Stacking : MLP(hidden_layer_sizes=(100, 50), activation='relu', solver='adam', max_iter=1000) comme meta_model, et les modèles de base sont :
         * TroncatedSVD comme méthode de réduction de dimension avec n_components=100 pour SVC et n_components=65 pour RF
         * Random Forest: n_estimators=100, max_features=3, 
         * SVC: kernel='linear', C=1.0
         * KNN: n_neighbors=5
         * Gradient boosting: n_estimators=100, learning_rate=0.1, max_depth=3
         * Test balanced accuracy : 0.778 en local
 
   * Aline

     | Modèles | Train balanced accuracy | Test balanced accuracy |
     | ----------- | ------------- |------------ |
     | SVM | 0.79 | 0.69 |
     |  LogisticRegression| 0.76 | 0.66 |
     |   KNeighbors| 0.78 | 0.62 |
     |  LDA|  0.66 |  0.61 |
     |   QDA| 0.72 | 0.53 |
     |  Réseaux de neurones MLP| 1.0 | 0.70 |

       

##  Mardi 21 Novembre

### Objectifs : Travailler sur le pretraitement des données
*  Élimination des cellules non étiquetées, débris et doublets
*  Suppression des gènes avec expression nulle
*  Transformation logarithmique de l'expression génique
*  Differents types de normalisation ?
*  Visualisation

### Avancement 
   * Alimatou
     * Documentation de Scanpy
     * Contrôle qualité
     * Filtration => problème de dimension ? => à revoir
     * Se restreindre à la mise à l'échelle log + Normalisation pour l'instant
     * Application sur les modèles suivants :
       
     | Modèles | Train balanced accuracy | Test balanced accuracy |
     | ----------- | ------------- |------------ |
     |  Naives Bayes | 0.992  | 0.338 |
     |  KNeighbors| 0.865 | 0.650|
     |  Random Forest| 1.000| 0.66 |
     |  SVM | 0.877 | 0.713 |
     |  GB | 1.000| 0.710 |  
     |  MLP| 1.00 |0.778 |
       
     
   * Murielle
      * Ce site nous a aidé à comprendre pourquoi on doit normaliser les données génomiques: https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-021-04278-2
      * Cette page github nous a donné une idée sur la classification des cellules: https://github.com/bradenkatzman/CellClassificationMachineLearning
      * Soumission sur RAMP

     | team |	submission|	bal_acc|	train time [s]|	validation time [s]	|max RAM [MB]|	submitted at (UTC)|
     | ----------- | ------------- |------------ |----------- |------- |--------- |---------- |
     |MurielleMajum |	GAB_TRA_PCA_MLP_0 |	0.78 | 12.372173 |	1.877850 |	0.0 | 2023-11-21 23:07:20|
     |MurielleMajum | GAB_TRA_STACK_2 | 0.73 |	124.941084 | 0.904338 	| 0.0 | 2023-11-25 22:13:40|
     |MurielleMajum |	GAB_TRA_STACK_3 |	0.72 | 134.558703 |	1.091253 |	0.0 |	2023-11-25 22:32:03|

     * Utilisation de ouvelles méthodes de d'optimisation d'hyperparamètres, notamment RandomizedSearchCV et BayesSearchCV
        * Des difficultés ont été rencontrées car le temps de compilation était très long (environ 20 minutes)
        * Mais les résultats étaient préférables avec cette méthode 
     * Test de nouveaux modèles:
        * AdaBoostClassifier : learning_rate=0.2, n_estimators=150, Test balanced accuracy : 0.569
        * ExtraTreesClassifier: splitter="best", max_depth=None, min_samples_split=2, min_samples_leaf=1, Test balanced accuracy : 0.553
        * Stacking :
           * Utilisation de PCA: n_components=50, 85, 50 pour réduction de dimension
           * SVC: kernel='linear', C=1.0
           * RandomForestClassifier(n_estimators=50,max_features=3)
           * MLPClassifier(hidden_layer_sizes=(100, 50), activation='relu', solver='adam', max_iter=1000)
           * Test balanced accuracy : 0.78
     
   * Aline
     * Modification de la fonction de preprocessing : 'Logarithmiser' les données + Normalisation
     * Je me suis concentrée sur le modèle MLP qui après un début de recherche des hyperparamètres optimaux m'a donné une Test balanced accuracy d'environ 73% 
     * Soumission RAMP avec un score de 73% deplus on remarque que le temps de calcul est assez élevé ( 41 secondes )
     * Je pense qu'il reste une petite marge d'amélioration dû aux hyperparamètres qui sont assez long à optimiser  : j'ai pour le moment atteint 77%-80%
     * Nouvelles soumissions RAMP avec un score de 77% et 78%
       


##  Mardi 28 Novembre

### Avancement 

* Alimatou
  * Lien Scanpy pour le Prétraitement : [Scanpy PBMC3k Tutorial](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html)

  * **Prétraitement :**
    * Identification des gènes avec des valeurs d'expression nulles :Nous avons filtré les gènes qui ont des valeurs d'expression nulles dans toutes les cellules pour garantir 
      une représentation significative.
    * Transformation des valeurs d'expression génique en échelle logarithmique 
    * Normalisation : Les données ont été normalisées pour équilibrer les effets des différences de couverture génique entre les cellules.
    * Sélection des variables hautement variables avec `var.highly_variable` de Scanpy : Nous avons identifié les gènes hautement variables qui contribuent le plus à la 
      variabilité biologique.
    * **Visualisation** avec T-SNE 

    * **Test sur nos meilleurs modèles :** Suite à ces étapes de prétraitement, tous mes modèles de base ont enregistré une augmentation significative de la balance accuracy, 
      démontrant ainsi l'efficacité du prétraitement dans l'amélioration des performances de nos modèles.

      
    | Modèles | Train balanced accuracy | Test balanced accuracy |
     | ----------- | ------------- |------------ |
     |  Random Forest | 1.000 | 0.700
     |  SVM | 0.897 | 0.792
     |  MLP| 1.00 |0.80|
     | Stacking avec (MLP , SVM , Random Forest | 0.993 | 0.809

    Mes Objectifs :
     * Comprendre ces modeles => optimiser
     * Analyser les resultats de la prediction => matrice de confusion 
     
    

  * Murielle
     * Sélection de variables: afin d'optimiser les résultats, des méthodes de sélection de variables on été testées, à savoir
        * Par Randon Forest en sélectionnant les variables qui contribuent le plus dans le modèle
        * Par Lasso en utilisant le même procédé
     * Utilisation du dernier stacking après sélection des variables par la méthode Lasso, on voit bien qu'il y'a eu une optimisation du score: Test balanced accuracy : 0.801
     * Soumission sur RAMP
       
       | team |	submission|	bal_acc|	train time [s]|	validation time [s]	|max RAM [MB]|	submitted at (UTC)|
       | ----------- | ------------- |------------ |----------- |------- |--------- |---------- |
       |MurielleMajum |	GAB_TRA_STACK_4 |	0.81 | 142.331705 |	3.245756 | 0.0 |	2023-11-28 11:25:29|
       |MurielleMajum | GAB_TRA_STAck_5 | 0.80 |	140.834686 | 3.428074 |	0.0 |	2023-11-28 22:39:47|

     * Objectifs:
       * Analyser les matrices de confusion
       * Choisir les meilleurs modèles en terme de temps d'exécution et d'accuracy simultanément
       * Continuer l'optimisation des paramètres de nos meilleurs modèles (notamment le dernier stacking)
  * Aline
     * Suite à la recherche des hyperparamètres optimaux d'un modèle MLP, j'ai atteint 78%-81% de test balanced accuracy, mais je stagne à ce niveau.
     * J'ai donc essayer de nouvelles méthodes et je me suis particulierement intéressée aux mélanges de modèles :
        * VotingClassifier
        * StackingClassifier
        * BaggingClassifier
        * AdaBoostClassifier
     * Nouvelle soumission : balanced accuracy 0.82% avec un StackingClassifier ( Random Forest + SVM + MLP )
     * Mon objectif actuel est de comprendre en détail ces modèles et d'ainsi trouver les modèles les plus adaptés en étudiant par ailleurs les matrices de confusion.
     
    | team |	submission|	bal_acc|	train time [s]|	validation time [s]	|	submitted at (UTC)|
    |------|-----|------|------|------|--------|
    |Aline_G	|GTM_V1|	0.82	|147.770997|	4.238968	|2023-11-28 09:35:52|

##  Mardi 5 Décembre

* Objectifs
  * Etude du préprocessing de nos données : log ? filtration sur certains gènes ? ...
  * Nouvelles méthodes de sélection de variables
  * Définition du plan de rédaction du rapport
    
* Alimatou
  
  * Submission apres preprocessing => selection des variables
  * Optimisation de nos meilleurs modèles
  * Analyser les resultats 
  * Preparation du rapport
    
   | team |	submission|	bal_acc|	train time [s]|	validation time [s]	|	submitted at (UTC)|
    |------|-----|------|------|------|--------|
    |Alimatou_Traore	|SKD_MAA_3|	0.84|	338.033050|	2.525157 |2023-12-10 15:07:12|
    |Alimatou_Traore	|SKD_MAA_4	|0.83|	331.835121	|2.453657	|2023-12-10 15:43:25 |
    |Alimatou_Traore	|SKD_MAA_2	|0.80	|387.140855|	3.927364 |2023-12-10 14:46:29 |
    
* Aline

| Modèles | Train balanced accuracy | Test balanced accuracy |
| ----------- | ------------- |------------ |
|  VotingClassifier | 0.989  | 0.80 |
|  StackingClassifier|  1.0 |  0.83 |
|  BaggingClassifier| 0.997 | 0.77 |
|  AdaBoostClassifier | 0.52 | 0.46 |

 Mon objectif : optimisation des hyperparamètres + preprocessing : filtrage 
 
* Murielle
  
  * D'après les matrices de confusion, le modèle MLP est celui qui prédit le mieux les cellules NK_cells, mais le moins bien les cellules T-cells_CD8+.
  * Comme nouvelle méthode de sélection de variables, j'ai utilisé la sélection par Random Forest, car c'est une méthode basée sur les arbres de décision; l’arbre est construit sur un sous-ensemble aléatoire des variables, et cela entraine donc la variabilité dans la sélection de variables, et évite un overfiting.
  * Une autre méthode de recherche d'hyperparamètres a été utilisée, à savoir la RandomizedSearch, car celle-ci est basée sur une recherche aléatoire, et donc peut se permettre de rechercher le meilleur paramètre dans un esspace continue, contrairement à la GridSearch qui fait ses combinaisons de paramètres dans des espaces discrets.
  * Loptimisation des hyperparamètres a donc été faite avec ces méthodes, la sélection des variables aussi, et des soumissions RAMP ont été réalisées entre temps. Nous les avons dans le tableau suivant:
 
| team |	submission|	bal_acc|	train time [s]|	validation time [s]	|	submitted at (UTC)|
|------|-----|------|------|------|--------|
|MurielleMajum |GAB_TRA_SE_1|	0.80|	152.838153 |	3.287925 |	2023-12-04 10:23:08|
|MurielleMajum	|GAB_TRA_2|	0.87|	124.554377|	2.807956 |2023-12-12 13:21:49|
|MurielleMajum	|GAB_TRA_6	|0.86|	190.099874	|3.051363 |2023-12-12 14:56:48 |
|MurielleMajum|GAB_2|0.85	|67.783815|	2.063865 |2023-12-12 12:47:13 |    
  

##  Lundi 11 Décembre

Rédaction du rapport sur Google Meet.

##  Mardi 12 Décembre
