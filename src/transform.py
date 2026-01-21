import pandas as pd
from src.utils import setup_logger
from config.settings import COLUMNAS_CAPITAL, COLUMNAS_PROVISION, COLUMNAS_VENCIDA, COLUMNAS_RIESGO, COLUMNAS_FLOAT

logger = setup_logger()

def transform(data_CAP_VEN, data_PROV):
    #-----------------------------------#
    # DATOS: CAPITAL / VENCIDO / RIESGO #
    #-----------------------------------#
    try:
        if data_CAP_VEN.empty or data_PROV.empty:
            raise ValueError("Uno de los DataFrames de entrada está vacío. No se puede transformar.")
    
        try:
            logger.debug("Convirtiendo columnas a tipo float...")
            data_CAP_VEN = data_CAP_VEN.astype({col: float for col in COLUMNAS_FLOAT})
            data_PROV = data_PROV.astype({'valor': 'float'})
        except KeyError as e:
            logger.error(f"Error de esquema: Falta una columna esperada en el DataFrame: {e}")
            raise

        logger.info("Calculando indicadores de Capital y Riesgo...")
        dt_capital = ( # dt: data transform
            data_CAP_VEN
            .groupby(['nombreentidad','codigo_entidad'])
            .agg(capital = pd.NamedAgg(column = COLUMNAS_CAPITAL[0], aggfunc = "sum"))
        )
        dt_vencido = (
            data_CAP_VEN
            .groupby(['nombreentidad','codigo_entidad'])
            .apply(lambda x: x[COLUMNAS_VENCIDA].sum(axis = 1).sum())
            .reset_index(name = 'vencido')
        )
        dt_riesgo = (
            data_CAP_VEN
            .groupby(['nombreentidad','codigo_entidad'])
            .apply(lambda x: x[COLUMNAS_RIESGO].sum(axis = 1).sum())
            .reset_index(name = 'riesgo')

        )
        dt = (
            dt_capital
            .merge(dt_vencido, on = 'codigo_entidad', how = 'left')
            .merge(dt_riesgo, on = 'codigo_entidad', how = 'left')
        )
        #------------------#
        # DATOS: PROVISION #
        #------------------#
        logger.info("Calculando indicadores de Provisiones...")
        data_PROV = (
            data_PROV
            .groupby(['nombre_entidad','codigo_entidad'])
            .agg(provision = pd.NamedAgg(column = COLUMNAS_PROVISION[0], aggfunc = "sum"))
        )
        data_PROV['provision'] = data_PROV['provision'].fillna(0)

        dt = (
            dt
            .merge(data_PROV, on = 'codigo_entidad', how = 'left')
        )

        dt['provision'] = dt['provision'].fillna(0)
        logger.info("Transformación finalizada correctamente.")
        return dt
    except Exception as e:
        logger.error(f"Error inesperado en la transformación: {str(e)}")
        raise