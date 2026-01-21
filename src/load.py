import sqlite3
import pandas as pd
from src.utils import setup_logger

logger = setup_logger()

def load_to_sqlite(df, db_path="data/processed/indicadores_sfc.db", table_name="indicadores_financieros"):
    """
    Carga el DataFrame transformado en una base de datos SQLite.
    """
    logger.info(f"Iniciando carga de datos en la tabla '{table_name}'...")
    
    conn = None
    try:
        # 1. Asegurar que el directorio de destino existe
        import os
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # 2. Establecer conexión
        conn = sqlite3.connect(db_path)
        
        # 3. Carga de datos
        # if_exists='replace' sobrescribe la tabla cada vez. 
        # Usa 'append' si quieres mantener un histórico (requiere manejar duplicados).
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        df.to_excel("data/processed/indicadores_sfc.xlsx", index=False)
        
        # Confirmar cambios
        conn.commit()
        
        logger.info(f"Carga exitosa. Se insertaron {len(df)} registros en {db_path}.")
        
    except Exception as e:
        logger.error(f"Error crítico durante la carga en SQLite: {e}")
        if conn:
            conn.rollback() # Revierte cambios si hubo error
        raise
        
    finally:
        if conn:
            conn.close()
            logger.debug("Conexión a SQLite cerrada.")