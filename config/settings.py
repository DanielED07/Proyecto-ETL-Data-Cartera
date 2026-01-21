#-------------------------------#
# PARAMETROS FASE DE EXTRACCIÓN #
#-------------------------------#
API_KEY1 = "https://www.datos.gov.co/resource/rvii-eis8.json"
API_KEY2 = "https://www.datos.gov.co/resource/mxk5-ce6w.json"
LISTA_CUENTAS = ['148700','148800','148900','149100','149300','149400','149500']
LISTA_TIPO_ENTIDAD = ['1', '4'] # 1: BANCOS | 4 : COMPAÑIAS DE FINANCIAMIENTO
QUERY_TIPO_ENTIDAD = "TIPO_ENTIDAD IN ({})".format(", ".join("'" + tipo + "'" for tipo in LISTA_TIPO_ENTIDAD))
QUERY_CUENTAS = "CUENTA IN ({})".format(", ".join("'" + cuenta + "'" for cuenta in LISTA_CUENTAS)) + " AND " + QUERY_TIPO_ENTIDAD + " AND MONEDA IN (0)"



COLUMNAS_CAPITAL = ['_1_saldo_de_la_cartera_a']
COLUMNAS_PROVISION = ['valor']
COLUMNAS_VENCIDA = [
    '_3_vencida_1_2_meses',
    '_4_vencida_2_3_meses',
    '_5_vencida_1_3_meses',
    '_6_vencida_3_4_meses',
    '_7_vencida_de_4_meses',
    '_8_vencida_3_6_meses',
    '_9_vencida_6_meses',
    '_10_vencida_1_4_meses',
    '_11_vencida_4_6_meses',
    '_12_vencida_6_12_meses',
    '_13_vencida_12_18_meses',
    '_14_vencida_12_meses',
    '_15_vencida_18_meses'
]
COLUMNAS_RIESGO = [
    '_20_calificaci_n_de_riesgo',
    '_22_calificaci_n_de_riesgo',
    '_24_calificaci_n_de_riesgo',
    '_26_calificaci_n_de_riesgo'
    ]
COLUMNAS_FLOAT = COLUMNAS_CAPITAL+COLUMNAS_VENCIDA+COLUMNAS_RIESGO