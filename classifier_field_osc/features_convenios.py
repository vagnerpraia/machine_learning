'''
Created on 6 de dez de 2016

@author: vagnerpraia
'''

import pandas as pd
import load_file as lf

root_path = 'D:/Users/vagnerpraia/Desktop/Classificação de OSCs/Base de Dados/'



# Carregamento dos dados
df_rais = lf.load_rais(root_path)

df_siconv = lf.load_siconv(root_path)

df = df_rais



# Features de programas de convênios
df_siconv = pd.merge(df_siconv, df, on='cnpj', how='left')

# Propostas
df_temp = df_siconv.loc[df_siconv['ID_PROGRAMA'].notnull()]

df_temp['quant_osc_propostas'] = 0
df_propostas_temp = df_temp[['ID_PROGRAMA', 'quant_osc_propostas']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_propostas = pd.merge(df_siconv, df_propostas_temp, on='ID_PROGRAMA')

df_temp['quant_propostas_osc_assistencia_social'] = 0
df_propostas_temp = df_temp.loc[df_temp['cebas_assistencia_social'] == True][['ID_PROGRAMA', 'quant_propostas_osc_assistencia_social']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_propostas = pd.merge(df_propostas, df_propostas_temp, on='ID_PROGRAMA')

df_temp['quant_propostas_osc_saude'] = 0
df_propostas_temp = df_temp.loc[df_temp['cebas_saude'] == True][['ID_PROGRAMA', 'quant_propostas_osc_saude']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_propostas = pd.merge(df_propostas, df_propostas_temp, on='ID_PROGRAMA')

df_temp['quant_propostas_osc_educacao'] = 0
df_propostas_temp = df_temp.loc[df_temp['cebas_educacao'] == True][['ID_PROGRAMA', 'quant_propostas_osc_educacao']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_propostas = pd.merge(df_propostas, df_propostas_temp, on='ID_PROGRAMA')

df_temp['quant_propostas_osc_ambiental'] = 0
df_propostas_temp = df_temp.loc[df_temp['cnea'] == True][['ID_PROGRAMA', 'quant_propostas_osc_ambiental']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_propostas = pd.merge(df_propostas, df_propostas_temp, on='ID_PROGRAMA')

# Convênios
df_temp = df_siconv.loc[df_siconv['NR_CONVENIO'].notnull()]

df_temp['quant_osc_convenios'] = 0
df_convenios_temp = df_temp[['ID_PROGRAMA', 'quant_osc_convenios']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_convenios = pd.merge(df_siconv, df_convenios_temp, on='ID_PROGRAMA')

df_temp['quant_convenios_osc_assistencia_social'] = 0
df_convenios_temp = df_temp.loc[df_temp['cebas_assistencia_social'] == True][['ID_PROGRAMA', 'quant_convenios_osc_assistencia_social']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_convenios = pd.merge(df_convenios, df_convenios_temp, on='ID_PROGRAMA')

df_temp['quant_convenios_osc_saude'] = 0
df_convenios_temp = df_temp.loc[df_temp['cebas_saude'] == True][['ID_PROGRAMA', 'quant_convenios_osc_saude']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_convenios = pd.merge(df_convenios, df_convenios_temp, on='ID_PROGRAMA')

df_temp['quant_convenios_osc_educacao'] = 0
df_convenios_temp = df_temp.loc[df_temp['cebas_educacao'] == True][['ID_PROGRAMA', 'quant_convenios_osc_educacao']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_convenios = pd.merge(df_convenios, df_convenios_temp, on='ID_PROGRAMA')

df_temp['quant_convenios_osc_ambiental'] = 0
df_convenios_temp = df_temp.loc[df_temp['cnea'] == True][['ID_PROGRAMA', 'quant_convenios_osc_ambiental']].groupby(['ID_PROGRAMA'], as_index=False).count()
df_convenios = pd.merge(df_convenios, df_convenios_temp, on='ID_PROGRAMA')

df_propostas_convenios = pd.merge(df_propostas, df_convenios, on='ID_PROGRAMA', how='left')



# Resultado
pd.options.display.float_format = '{:,.2f}'.format
#df = df.sort_values(['quant_convenios'], ascending=[False])
print df_propostas_convenios