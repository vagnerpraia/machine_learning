'''
Created on 8 de dez de 2016

@author: vagnerpraia
'''

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import cross_val_score

'''
classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0), warm_start=True),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]
'''

def prepare_data(data, target):
    return train_test_split(data, target, test_size=0.3, random_state=0)



def execute(model, data, target):
    data_train, data_test, target_train, target_test = prepare_data(data, target)

    model.fit(data_train, target_train.values.ravel())
    
    predicted = model.predict(data_test)
    print predicted[0:5]
    expected = target_test
    
    print(model)
    print('')
    
    scores = model.score(data_test, target_test)
    print(scores)
    print('')
    
    print(metrics.classification_report(expected, predicted))
    print('')
    
    scores = cross_val_score(model, data, target.values.ravel(), cv=10)
    print(scores)
    print('')



def execute_logistic_regression(data, target):
    model = LogisticRegression()
    execute(model, data, target)

def execute_gaussian_nb(data, target):
    model = GaussianNB()
    execute(model, data, target)

def execute_k_neighbors_classifier(data, target):
    model = KNeighborsClassifier()
    execute(model, data, target)

def execute_decision_tree_classifier(data, target):
    model = DecisionTreeClassifier()
    execute(model, data, target)

def execute_svc(data, target):
    model = SVC()
    execute(model, data, target)

def execute_ada_boost_classifier(data, target):
    model =  AdaBoostClassifier()
    execute(model, data, target)

def execute_random_forest_classifier(data, target):
    model =  RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
    execute(model, data, target)