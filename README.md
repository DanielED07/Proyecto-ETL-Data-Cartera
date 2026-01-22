# Pipeline de Indicadores Financieros - SFC (Colombia)

Este proyecto es un pipeline de ingeniería de datos (ETL) que automatiza la extracción, transformación y carga de datos de cartera de las compañías de financiamiento y bancos en Colombia, utilizando la API de **Datos Abiertos (datos.gov.co)**.

## 1. Estructura del Proyecto
```bash
Proyecto-ETL-Data-Cartera
├── config/
│   └── settings.py              # Define las CONSTANTES
├── data/
│   └── processed/               # Volumen Procesado: Archivos xlsx y .db cargan aqui
├── logs/                        # Logs Procesados: logs cargan aqui
├── src/
│   ├── extract.py               # Llamado a la API 
│   ├── load.py                  # Lógica para guardar en SQLite o bases de datos
│   ├── transform.py             # Lógica de limpieza y definición de datos
│   └── utils.py                 # Funciones auxiliares
├── .gitignore                   # Archivos a ignorar en el repo
├── main.py                      # Orquestador
├── README.md                    # Documentación del proyecto
└── requirements.txt             # Paquetes necesarios
```

## 2. Requisitos Previos

* Python 3.8 o superior.
* Conexión a internet (para llamadas a la API).

## 3. Instalación y Ejecución

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/DanielED07/Proyecto-ETL-Data-Cartera.git](https://github.com/DanielED07/Proyecto-ETL-Data-Cartera.git)
   cd nombre-del-proyecto
   ```

2. Ejecutar ETL (main.py):
   ```bash
   python main.py --fecha 2024-05-31
   ```