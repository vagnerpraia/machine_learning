# -*- coding: iso-8859-1 -*-

'''
Created on 4 de dez de 2016

@author: vagnerpraia
'''

import pandas as pd



def load_rais(root_path):
    print 'Load Rais'
    
    file_path= root_path + 'RAIS.csv'
    df = pd.read_csv(file_path, delimiter=';')
    df = df.rename(columns = {'id_estab': 'cnpj'})
    
    return df



def load_oscip(root_path):
    print 'Load OSCIP'
    
    file_path = root_path + 'OSCIP.csv'
    df = pd.read_csv(file_path, delimiter=';')
    df = df.rename(columns = {'CNPJ': 'cnpj'})
    
    return df



def load_siconv(root_path):
    print 'Load Siconv'
    
    file_path_siconv_convenios = root_path + 'Siconv Convênios.csv'
    file_path_siconv_propostas = root_path + 'Siconv Propostas.csv'
    file_path_siconv_programas_propostas = root_path + 'Siconv Programas Propostas.csv'
    file_path_siconv_programas = root_path + 'Siconv Programas.csv'
    
    df_siconv_propostas = pd.read_csv(file_path_siconv_propostas, delimiter=';')
    df_siconv_propostas_convenios = pd.read_csv(file_path_siconv_programas_propostas, delimiter=';')
    df_siconv_programas = pd.read_csv(file_path_siconv_programas, delimiter=';')
    
    df_siconv_convenios = pd.read_csv(file_path_siconv_convenios, delimiter=';', dtype={'NR_PROCESSO': str})
    df_siconv_convenios['VL_GLOBAL_CONV'] = df_siconv_convenios['VL_GLOBAL_CONV'].str.replace(',','.').astype(float)
    
    
    
    df = pd.merge(df_siconv_propostas, df_siconv_convenios, on='ID_PROPOSTA', how='inner')
    df = pd.merge(df, df_siconv_propostas_convenios, on='ID_PROPOSTA', how='inner')
    df = pd.merge(df, df_siconv_programas, on='ID_PROGRAMA', how='inner')
    
    df = df.rename(columns = {'IDENTIF_PROPONENTE': 'cnpj'})
    
    return df



def load_finep(root_path):
    print 'Load Finep'
    
    file_path = root_path + 'Finep.csv'
    df = pd.read_csv(file_path, delimiter=';')
    df['CNPJ Proponente'] = df['CNPJ Proponente'].str.replace('.', '').str.replace('/', '').str.replace('-', '').astype(float)
    df = df.rename(columns = {'CNPJ Proponente': 'cnpj'})
    
    return df



def load_salic(root_path):
    print 'Load Salic'
    
    file_path = root_path + 'Salic.csv'
    df = pd.read_csv(file_path, delimiter=';')
    df = df.rename(columns = {'CgcCpf': 'cnpj'})
    
    return df



def load_cebas_assistencia_social(root_path):
    print 'Load CEBAS Assistência Social'
    
    file_path = root_path + 'CEBAS Assistência Social.csv'
    df = pd.read_csv(file_path, delimiter=';')
    df['CNPJ'] = df['CNPJ'].str.replace('.', '').str.replace('/', '').str.replace('-', '').astype(float)
    df = df.rename(columns = {'CNPJ': 'cnpj'})
    
    return df



def load_cebas_educacao(root_path):
    print 'Load CEBAS Educação'
    
    file_path = root_path + 'CEBAS Educação.csv'
    df = pd.read_csv(file_path, delimiter=';')
    df = df.rename(columns = {'CNPJ': 'cnpj'})
    
    return df



def load_cebas_saude(root_path):
    print 'Load CEBAS Saúde'
    
    file_path = root_path + 'CEBAS Saúde.csv'
    df = pd.read_csv(file_path, delimiter=';')
    df = df.rename(columns = {'NU CPF CNPJ': 'cnpj'})
    
    return df



def load_cnea(root_path):
    print 'Load CNEA'
    
    file_path = root_path + 'CNEA.csv'
    df = pd.read_csv(file_path, delimiter=';')
    df['CNPJ'] = df['CNPJ'].str.replace('.', '').str.replace('/', '').str.replace('-', '').astype(float)
    df = df.rename(columns = {'CNPJ': 'cnpj'})
    
    return df



def load_final(root_path):
    print 'Load Final'
    
    file_path = root_path + 'Final.csv'
    df = pd.read_csv(file_path, delimiter=';')
    
    return df
