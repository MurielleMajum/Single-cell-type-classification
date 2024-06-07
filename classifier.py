import pandas as pd
import numpy as np
import scanpy as sc

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel


class Classifier(object):
    def __init__(self):
        base_models = [
            ('MLPClassifier', make_pipeline(
                StandardScaler(with_mean=True, with_std=True),
                #PCA(n_components=50),
                SelectFromModel(Lasso(alpha=0.06283860093330873)),
                MLPClassifier(hidden_layer_sizes=(128, 128), activation='relu', solver='adam', max_iter=1043),
            )),
        
           ('gradient_boosting', make_pipeline(StandardScaler(), SelectFromModel(Lasso(alpha=0.2169988938150142)), GradientBoostingClassifier(learning_rate=0.3225152497855646, n_estimators=81, max_depth=5) )) ,   #PCA(n_components=80),
        
            #('knn', make_pipeline(TruncatedSVD(n_components=20),KNeighborsClassifier(n_neighbors=5))),
        
            #('svc_classifier', make_pipeline(StandardScaler(with_mean=True, with_std=True), SelectFromModel(Lasso(alpha=0.06283860093330873)), SVC(kernel='linear', C=0.1))),  #PCA(n_components=100), 

           # ('rf', make_pipeline(StandardScaler(), SelectFromModel(Lasso(alpha=0.06283860093330873)), RandomForestClassifier(random_state=42, n_estimators= 96, max_features=15))),
        ]
                
        self.pipe = make_pipeline(
            StandardScaler(with_mean=True, with_std=True),
            StackingClassifier(estimators=base_models, final_estimator=MLPClassifier(hidden_layer_sizes=(64, 64), activation='relu', solver='adam', max_iter=1187))
        )
        self.highly_variable_genes = None

    def _preprocess_X(self, X_sparse):
        X_dense = X_sparse.toarray()

        adata = sc.AnnData(X_dense)

        sc.pp.normalize_total(adata, target_sum=1e4)
        sc.pp.log1p(adata)
        if self.highly_variable_genes is None:
            sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
            self.highly_variable_genes = adata.var.highly_variable
        adata = adata[:, self.highly_variable_genes]
        sc.pp.scale(adata, max_value=10)

        return adata.X

    def fit(self, X_sparse, y):
        X = self._preprocess_X(X_sparse)
        self.pipe.fit(X, y)
        self.classes_ = self.pipe.classes_

    def predict_proba(self, X_sparse):
        X = self._preprocess_X(X_sparse)
        return self.pipe.predict_proba(X)
