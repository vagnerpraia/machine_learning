'''
Created on 6 de dez de 2016

@author: vagnerpraia
'''

from sklearn.datasets import load_iris

iris = load_iris()

print type(iris.data)
print '\n\n'
print type(iris.target)