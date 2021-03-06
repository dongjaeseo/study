import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.utils.testing import all_estimators
import warnings

warnings.filterwarnings('ignore')

dataset = load_iris()
x = dataset.data
y = dataset.target

x_train, x_test, y_train, y_test = train_test_split(x,y,train_size = 0.8, random_state = 33)

kfold = KFold(n_splits=5, shuffle = True)
allAlgorithms = all_estimators(type_filter = 'classifier')

for (name, algorithm) in allAlgorithms:
    try:
        model = algorithm()

        score = cross_val_score(model,x_train,y_train, cv = kfold)
        print(name, '의 정답률 : \n', score)
    except: 
        # continue
        print(name, '은 없는 놈!!!')

import sklearn
print(sklearn.__version__) # 0.23.2

# AdaBoostClassifier 의 정답률 :
#  [0.875      1.         1.         0.95833333 0.79166667]
# BaggingClassifier 의 정답률 :
#  [0.95833333 0.875      0.95833333 0.95833333 0.91666667]
# BernoulliNB 의 정답률 :
#  [0.29166667 0.33333333 0.29166667 0.33333333 0.25      ]
# CalibratedClassifierCV 의 정답률 :
#  [0.95833333 0.95833333 0.91666667 0.91666667 0.70833333]
# CategoricalNB 의 정답률 :
#  [0.91666667 0.875      0.95833333 0.95833333 0.91666667]
# CheckingClassifier 의 정답률 :
#  [0. 0. 0. 0. 0.]
# ClassifierChain 은 없는 놈!!!
# ComplementNB 의 정답률 :
#  [0.70833333 0.58333333 0.75       0.66666667 0.54166667]
# DecisionTreeClassifier 의 정답률 :
#  [0.95833333 0.91666667 0.91666667 1.         0.91666667]
# DummyClassifier 의 정답률 :
#  [0.33333333 0.08333333 0.33333333 0.20833333 0.125     ]
# ExtraTreeClassifier 의 정답률 :
#  [0.91666667 0.95833333 0.875      0.95833333 0.95833333]
# ExtraTreesClassifier 의 정답률 : 
#  [0.91666667 0.91666667 0.91666667 1.         1.        ]
# GaussianNB 의 정답률 :
#  [0.91666667 1.         0.95833333 1.         0.95833333]
# GaussianProcessClassifier 의 정답률 : 
#  [0.95833333 1.         1.         1.         0.875     ]
# GradientBoostingClassifier 의 정답률 : 
#  [0.95833333 0.91666667 0.95833333 0.95833333 0.95833333]
# HistGradientBoostingClassifier 의 정답률 : 
#  [0.875      0.95833333 0.95833333 0.95833333 1.        ]
# KNeighborsClassifier 의 정답률 :
#  [0.95833333 0.95833333 1.         0.95833333 0.95833333]
# LabelPropagation 의 정답률 : 
#  [0.95833333 1.         0.91666667 0.95833333 1.        ]
# LabelSpreading 의 정답률 :
#  [0.95833333 0.95833333 0.91666667 0.95833333 0.95833333]
# LinearDiscriminantAnalysis 의 정답률 : 
#  [1.         0.95833333 1.         0.95833333 0.95833333]
# LinearSVC 의 정답률 : 
#  [1.         0.91666667 0.95833333 0.95833333 0.95833333]
# LogisticRegression 의 정답률 : 
#  [0.91666667 1.         0.95833333 1.         0.91666667]
# LogisticRegressionCV 의 정답률 : 
#  [0.91666667 1.         1.         0.95833333 0.95833333]
# MLPClassifier 의 정답률 : 
#  [0.91666667 0.95833333 1.         1.         0.95833333]
# MultiOutputClassifier 은 없는 놈!!!
# MultinomialNB 의 정답률 :
#  [0.70833333 0.625      0.95833333 0.75       0.91666667]
# NearestCentroid 의 정답률 :
#  [0.91666667 1.         0.95833333 0.875      0.83333333]
# NuSVC 의 정답률 : 
#  [0.95833333 1.         0.83333333 1.         0.91666667]
# OneVsOneClassifier 은 없는 놈!!!
# OneVsRestClassifier 은 없는 놈!!!
# OutputCodeClassifier 은 없는 놈!!!
# PassiveAggressiveClassifier 의 정답률 : 
#  [0.91666667 0.875      0.83333333 0.875      0.66666667]
# Perceptron 의 정답률 : 
#  [1.         0.58333333 1.         0.54166667 0.66666667]
# QuadraticDiscriminantAnalysis 의 정답률 : 
#  [0.95833333 1.         0.95833333 1.         1.        ]
# RadiusNeighborsClassifier 의 정답률 :
#  [0.95833333 0.91666667 0.95833333 1.         0.91666667]
# RandomForestClassifier 의 정답률 : 
#  [0.95833333 0.875      1.         0.95833333 0.95833333]
# RidgeClassifier 의 정답률 :
#  [0.875      0.79166667 0.875      0.91666667 0.83333333]
# RidgeClassifierCV 의 정답률 : 
#  [0.83333333 0.875      0.75       0.91666667 0.875     ]
# SGDClassifier 의 정답률 :
#  [0.79166667 0.95833333 0.875      0.70833333 0.70833333]
# SVC 의 정답률 : 
#  [0.91666667 0.91666667 0.95833333 0.95833333 1.        ]
# StackingClassifier 은 없는 놈!!!
# VotingClassifier 은 없는 놈!!!