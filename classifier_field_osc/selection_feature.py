'''
Created on 8 de dez de 2016

@author: vagnerpraia
'''

from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif
from sklearn.feature_selection import RFE
from sklearn.feature_selection import RFECV
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import SelectFromModel

nr_features = 8

def variance_threshold(data):
    select_features = VarianceThreshold(threshold=(.8 * (1 - .8)))
    return select_features.fit_transform(data)

def select_k_best_chi2(data, target):
    return SelectKBest(chi2, k=nr_features).fit_transform(data, target.values.ravel())

def select_k_best_f_classif(data, target):
    return SelectKBest(f_classif, k=nr_features).fit_transform(data, target.values.ravel())

def select_k_best_mutual_info_classif(data, target):
    b = SelectKBest(mutual_info_classif, k=nr_features).fit_transform(data, target.values.ravel())
    return b

def select_rfe(data, target):
    model =  AdaBoostClassifier()
    rfe = RFE(model, nr_features, step=4)
    rfe = rfe.fit(data, target.values.ravel())
    
    #print(rfe.support_)
    #print(rfe.ranking_)
    
    return rfe.ranking_

def select_rfecv(data, target):
    model =  AdaBoostClassifier()
    rfecv = RFECV(estimator=model, step=1, cv=StratifiedKFold(2), scoring='accuracy')
    rfecv = rfecv.fit(data, target.values.ravel())
    
    print(rfecv.support_)
    print(rfecv.ranking_)
    
    return rfecv

def select_select_from_model(data, target):
    ada = AdaBoostClassifier().fit(data, target.values.ravel())
    model = SelectFromModel(ada, prefit=True)
    data = model.transform(data)
    print data.shape
    
    return data