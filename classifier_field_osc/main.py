# -*- coding: iso-8859-1 -*-

'''
Created on 4 de dez de 2016

@author: vagnerpraia
'''

import timeit
import numpy as np
import pandas as pd
from features_osc import load_features
from selection_feature import variance_threshold, select_k_best_chi2, select_k_best_f_classif, select_k_best_mutual_info_classif, select_rfe, select_rfecv, select_select_from_model
from execute_predict import execute_logistic_regression, execute_gaussian_nb, execute_k_neighbors_classifier, \
                            execute_decision_tree_classifier, execute_svc, execute_ada_boost_classifier, \
                            execute_random_forest_classifier



start_time = timeit.default_timer()



def load_data(load_file_data = False):
    if load_file_data:
        df = pd.read_csv('D:/Users/vagnerpraia/Desktop/Classificação de OSCs/Base de Dados/Final.csv', delimiter=';')
    else:
        df = load_features()
        df.to_csv('D:/Users/vagnerpraia/Desktop/Classificação de OSCs/Base de Dados/Final.csv', sep=';')
    return df



def load_select_features(load_file_select_features = False, load_file_data = True):
    if load_file_select_features:
        data = pd.read_csv('D:/Users/vagnerpraia/Desktop/Classificação de OSCs/Base de Dados/Features.csv', delimiter=';')
    else:
        df = load_data(load_file_data)
        
        index_outro = df.loc[(df['cebas_saude'] == False) & (df['cebas_educacao'] == False) & (df['cnea'] == False)].index
        df_outro = df.loc[np.random.choice(index_outro, 1000, replace=False)]
        df_assistencia_social = df.loc[(df['cebas_saude'] == False) & (df['cebas_assistencia_social'] == True)]
        df_educacao = df.loc[(df['cebas_saude'] == False) & (df['cebas_educacao'] == True)]
        df_ambiental = df.loc[(df['cebas_saude'] == False) & (df['cnea'] == True)]
        df_saude = df.loc[df['cebas_saude'] == True]
        
        data = df_saude.append(df_educacao).append(df_ambiental).append(df_assistencia_social)#.append(df_outro)

        data.to_csv('D:/Users/vagnerpraia/Desktop/Classificação de OSCs/Base de Dados/Features.csv', sep=';')
    
    return data



data = load_select_features(True, True)

features_names = ['codemun', 'sbcl_cnae20', 'nat_jur2009', 'tamestab', 'qtd_vinc_ativos', 'oscip', \
                          'cebas_assistencia_social', 'cebas_educacao', 'cnea', 'quant_propostas_siconv', \
                          'quant_convenios_siconv', 'eficacia_propostas_siconv', 'valor_total_convenios_siconv', \
                          'media_valor_convenios_siconv', 'ano_fundacao', 'ano_fechamento', 'fechada', 'tempo_atuacao', 
                          'quant_incentivos_salic', 'quant_incentivos_finep']

target_name = ['cebas_saude']

print data.head(5)
data_features = data[features_names]
data_target = data[target_name]


print data_features.head(5)
data_features = select_k_best_mutual_info_classif(data_features, data_target)
print data_features[0:5]

'''
execute_logistic_regression(data_features, data_target)
execute_gaussian_nb(data_features, data_target)
execute_k_neighbors_classifier(data_features, data_target)
execute_decision_tree_classifier(data_features, data_target)
execute_svc(data_features, data_target)
execute_random_forest_classifier(data_features, data_target)
'''
execute_ada_boost_classifier(data_features, data_target)


'''
elapsed = timeit.default_timer() - start_time
#print 'Time execution:' + str(elapsed)
'''