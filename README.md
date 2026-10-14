# Taller de Machine Learning aplicado a comercio electrónico

Repositorio educativo en español para introducir Machine Learning con datos de
comercio electrónico. Las tres rutas siguen las seis fases de CRISP-DM y usan
el conjunto público de Olist como caso de estudio.

## Rutas del taller

| Notebook | Pregunta | Alcance |
| --- | --- | --- |
| [01_pronostico_demanda.ipynb](./01_pronostico_demanda.ipynb) | ¿Cuántas líneas de artículos compradas podrían observarse en próximos periodos? | Ruta presencial principal (~1 hora); permite escoger categoría, agregación y horizonte. |
| [02_prediccion_recompra.ipynb](./02_prediccion_recompra.ipynb) | ¿Volverá a comprar un cliente en una ventana futura de 90 días? | Continuación: clasificación binaria con separación temporal para definir la etiqueta. |
| [03_segmentacion_clientes.ipynb](./03_segmentacion_clientes.ipynb) | ¿Qué patrones de compra similares aparecen entre clientes? | Continuación: RFM, escalado, K-Means e interpretación exploratoria. |

Cada notebook concluye con una interfaz pequeña de Gradio para probar el
modelo. En Google Colab la interfaz es temporal: no es un servicio persistente,
un despliegue de producción ni una recomendación para decisiones reales.

## Datos y atribución

Fuente: [Brazilian E-Commerce Public Dataset by Olist en Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce),
publicado por Olist (ficha mantenida por `olistbr`). La ficha de Kaggle anuncia
aproximadamente 100.000 pedidos de 2016–2018, nueve archivos CSV y un tamaño
total cercano a 126 MB. Es información histórica, anonimizada según la ficha,
pero contiene campos de ubicación y texto que no se necesitan para estos
ejercicios.

La licencia que muestra Kaggle es
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/):
atribuir la fuente, limitar el uso a fines no comerciales y compartir las
adaptaciones bajo la misma licencia, además de sus otros términos. Compruebe
la ficha y el texto legal antes de redistribuir o usar comercialmente datos o
derivados. El código de este repositorio está bajo MIT; eso no cambia la
licencia de los datos.

No se incluyen CSV ni Parquet. La API pública de Kaggle enumera nueve archivos
pero no expone sus columnas; la descarga anónima no estuvo disponible durante
la preparación de este repositorio. Por eso el [diccionario de datos](./docs/diccionario_datos.md)
documenta el esquema publicado esperado y el conversor verifica las columnas
necesarias frente a los CSV locales. No se afirma haber inspeccionado las filas
de la descarga original. Las fechas, tamaños y resultados que aparezcan al
ejecutar los notebooks dependerán de la versión descargada.

### Descargar y preparar los datos

1. Descargue el dataset desde la página oficial de Kaggle (inicie sesión y
   acepte las condiciones que Kaggle solicite). También puede usar la CLI
   oficial de Kaggle. No guarde `kaggle.json`, tokens ni credenciales dentro
   del repositorio: en local use la ubicación segura que documenta Kaggle; en
   Colab, use Secrets o cargue manualmente el archivo ZIP desde su equipo.
2. Descomprima los CSV originales, sin modificarlos, dentro de `data/raw/`.
   Esta carpeta está excluida de Git.
3. Instale dependencias y convierta las tablas usadas:

   ```bash
   python -m pip install -r requirements.txt
   python scripts/prepare_data.py
   ```

   El script valida encabezados, conserva las tablas originales y escribe
   Parquet en `data/processed/`, también excluida de Git. Solo convierte las
   tablas requeridas por los ejercicios: pedidos, clientes, líneas de pedido,
   productos y traducción de categorías.

4. Abra los notebooks desde la raíz del repositorio. Si el archivo Parquet
   esperado no existe, el notebook se detiene con instrucciones; vuelva a
   los pasos anteriores. No se generan resultados de ejemplo que puedan
   confundirse con resultados del dataset.

### Google Colab

Abra cada notebook en GitHub y seleccione **Open in Colab**, o clone este
repositorio en una sesión de Colab. Instale `requirements.txt`, descargue y
descomprima el dataset en `data/raw/`, ejecute `scripts/prepare_data.py` y
después ejecute las celdas del notebook en orden. La sesión y la interfaz
Gradio desaparecen al cerrar o reiniciar el entorno de Colab.

### Ejecución local

Requisitos: Python 3.10–3.13 y JupyterLab/Notebook. Cree un entorno virtual,
instale `requirements.txt`, descargue y prepare los datos con los pasos
anteriores y ejecute Jupyter desde la raíz del repositorio:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/prepare_data.py
jupyter lab
```

Las celdas de visualización y la interfaz Gradio requieren un navegador.

## Qué mide el ejercicio y qué no

El dataset registra pedidos y artículos comprados, no inventario, disponibilidad
ni quiebres de stock; por tanto, ningún notebook afirma medir demanda real o
ventas perdidas. Tampoco hay una columna de cantidad por línea en el esquema
publicado usado aquí. El notebook 01 pronostica el número de **filas/líneas de
artículo observadas en pedidos entregados**, una medida transaccional derivada,
no unidades ni demanda no satisfecha. Otras alternativas válidas son contar
órdenes por categoría y periodo; ambas siguen siendo compras observadas.

`customer_unique_id` permite agrupar las compras históricas por cliente para
los ejercicios de recompra y segmentación. Es un identificador seudónimo,
no una característica predictiva ni una identidad personal; no se muestra ni
se exporta en las demostraciones. Variables como inventario, stockout,
promociones, sesiones web o intención de compra no están disponibles en estas
tablas. Véase el diccionario para tablas, tipos esperados, claves y relaciones.

## Dependencias

Las versiones principales están fijadas en [requirements.txt](./requirements.txt).
El repositorio conserva la licencia MIT para el código educativo.
