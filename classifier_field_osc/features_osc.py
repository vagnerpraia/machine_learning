# -*- coding: iso-8859-1 -*-

'''
Created on 5 de dez de 2016

@author: vagnerpraia
'''

import pandas as pd
import load_file as lf

def load_features():
    root_path = 'D:/Users/vagnerpraia/Desktop/Classificação de OSCs/Base de Dados/'
    
    
    
    # Carregamento dos dados
    df_rais = lf.load_rais(root_path)
    
    df_oscip = lf.load_oscip(root_path)
    df_cebas_assistencia_social = lf.load_cebas_assistencia_social(root_path)
    df_cebas_educacao = lf.load_cebas_educacao(root_path)
    df_cebas_saude = lf.load_cebas_saude(root_path)
    df_cnea = lf.load_cnea(root_path)
    
    df_siconv = lf.load_siconv(root_path)
    df_finep = lf.load_finep(root_path)
    df_salic = lf.load_salic(root_path)
    
    df = df_rais
    
    
    
    # Features de certificados, cadastros, títulos e afins
    df['oscip'] = False
    df['cebas_assistencia_social'] = False
    df['cebas_educacao'] = False
    df['cebas_saude'] = False
    df['cnea'] = False
    df['quant_certificado'] = 0
    
    index = df_rais.loc[df_rais['cnpj'].isin(df_oscip['cnpj'])].index
    df = df.set_value(index, 'oscip', True).set_value(index, 'quant_certificado', df['quant_certificado'] + 1)
    
    index = df_rais.loc[df_rais['cnpj'].isin(df_cebas_assistencia_social['cnpj'])].index
    df = df.set_value(index, 'cebas_assistencia_social', True).set_value(index, 'quant_certificado', df['quant_certificado'] + 1)
    
    index = df_rais.loc[df_rais['cnpj'].isin(df_cebas_educacao['cnpj'])].index
    df = df.set_value(index, 'cebas_educacao', True).set_value(index, 'quant_certificado', df['quant_certificado'] + 1)
    
    index = df_rais.loc[df_rais['cnpj'].isin(df_cebas_saude['cnpj'])].index
    df = df.set_value(index, 'cebas_saude', True).set_value(index, 'quant_certificado', df['quant_certificado'] + 1)
    
    index = df_rais.loc[df_rais['cnpj'].isin(df_cnea['cnpj'])].index
    df = df.set_value(index, 'cnea', True).set_value(index, 'quant_certificado', df['quant_certificado'] + 1)
    
    
    
    # Features do Siconv
    df_temp = df_siconv
    
    index = df_rais.loc[df['cnpj'].isin(df_temp['cnpj']) == False].index
    
    df_temp['quant_propostas_siconv'] = 0
    df_temp_propostas = df_temp[['cnpj', 'quant_propostas_siconv']].groupby(['cnpj'], as_index=False).count()
    df = pd.merge(df, df_temp_propostas, on='cnpj', how='left')
    df = df.set_value(index, 'quant_propostas_siconv', 0)
    
    df_temp['quant_convenios_siconv'] = 0
    df_temp_convenios = df_temp.loc[df_temp['NR_CONVENIO'].notnull()][['cnpj', 'quant_convenios_siconv']].groupby(['cnpj'], as_index=False).count()
    df = pd.merge(df, df_temp_convenios, on='cnpj', how='left')
    df = df.set_value(index, 'quant_convenios_siconv', 0)
    
    df['eficacia_propostas_siconv'] = df['quant_propostas_siconv'] / df['quant_convenios_siconv']
    df = df.set_value(index, 'eficacia_propostas_siconv', 0)
    
    df_temp = df_temp[['cnpj', 'VL_GLOBAL_CONV']].groupby(['cnpj'], as_index=False).sum()
    df_temp = df_temp.rename(columns={'VL_GLOBAL_CONV': 'valor_total_convenios_siconv'})
    df = pd.merge(df, df_temp, on='cnpj', how='left')
    df = df.set_value(index, 'valor_total_convenios_siconv', 0)
    
    df['media_valor_convenios_siconv'] = df['valor_total_convenios_siconv'] / df['quant_convenios_siconv']
    df = df.set_value(index, 'media_valor_convenios_siconv', 0)
    
    
    
    # Features da Rais
    index_fundacao = df.loc[df['data_abertura'].notnull()].index
    
    index_encerrado = df.loc[df['data_encerramento'].notnull()].index
    index_aberto = df.loc[df['data_encerramento'].isnull()].index
    
    df['ano_fundacao'] = 2016
    df['ano_fechamento'] = 2016
    df = df.set_value(index_fundacao, 'ano_fundacao', df['data_abertura'].str.split('/').str[2])
    df = df.set_value(index_encerrado, 'ano_fechamento', df['data_encerramento'].str.split('/').str[2])
    
    df['fechada'] = False
    df = df.set_value(index_encerrado, 'fechada', True)
    
    df['tempo_atuacao'] =  df['ano_fechamento'].astype(int) - df['ano_fundacao'].astype(int)
    df = df.set_value(index_aberto, 'ano_fechamento', 0)
    
    
    
    # Features da Salic
    df_temp = df_salic
    
    index = df_rais.loc[df['cnpj'].isin(df_temp['cnpj']) == False].index
    
    df_temp['quant_incentivos_salic'] = 0
    df_temp_propostas = df_temp[['cnpj', 'quant_incentivos_salic']].groupby(['cnpj'], as_index=False).count()
    df = pd.merge(df, df_temp_propostas, on='cnpj', how='left')
    df = df.set_value(index, 'quant_incentivos_salic', 0)
    
    
    
    # Features da Finep
    df_temp = df_finep
    
    index = df_rais.loc[df['cnpj'].isin(df_temp['cnpj']) == False].index
    
    df_temp['quant_incentivos_finep'] = 0
    df_temp_propostas = df_temp[['cnpj', 'quant_incentivos_finep']].groupby(['cnpj'], as_index=False).count()
    df = pd.merge(df, df_temp_propostas, on='cnpj', how='left')
    df = df.set_value(index, 'quant_incentivos_finep', 0)
    
    
    
    return df
