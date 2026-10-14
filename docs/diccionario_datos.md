# Diccionario de datos de Olist

La ficha pública de Kaggle anuncia nueve CSV. Sus metadatos no detallan las
columnas; las listas siguientes corresponden al esquema publicado esperado del
dataset versión 2, no a una inspección de archivos descargados en este
repositorio. El script `scripts/prepare_data.py` valida las columnas mínimas
que usan los ejercicios al recibir CSV locales. Para obtener columnas, valores
nulos y tipos inferidos exactos de una descarga concreta, ejecute ese script y
consulte `DataFrame.dtypes`/`DataFrame.isna()` localmente.

Los tipos son los esperados al leer el CSV (identificadores como texto,
marcas de tiempo como fecha/hora, puntuaciones y medidas como numéricos);
algunos prefijos postales son códigos y deben tratarse como texto aunque
contengan dígitos. Claves candidatas marcadas aquí derivan del esquema; valide
unicidad/referencias en la versión descargada antes de usos productivos.

| Archivo / tabla | Columnas del esquema esperado | Claves y relaciones principales | Uso en las rutas |
| --- | --- | --- | --- |
| `olist_orders_dataset.csv` | `order_id` (texto), `customer_id` (texto), `order_status` (texto), `order_purchase_timestamp`, `order_approved_at`, `order_delivered_carrier_date`, `order_delivered_customer_date`, `order_estimated_delivery_date` (fechas/horas) | `order_id` identifica pedido; `customer_id` referencia `customers.customer_id`. | Las tres rutas; fecha de compra y estado. |
| `olist_customers_dataset.csv` | `customer_id`, `customer_unique_id` (texto), `customer_zip_code_prefix` (código), `customer_city`, `customer_state` (texto) | `customer_id` se enlaza con pedidos; `customer_unique_id` permite agrupar pedidos de la misma persona seudónima. | Recompra y segmentación para agrupar; los campos geográficos no se usan. |
| `olist_order_items_dataset.csv` | `order_id`, `order_item_id`, `product_id`, `seller_id` (texto/código), `shipping_limit_date` (fecha/hora), `price`, `freight_value` (numérico) | Clave candidata compuesta (`order_id`, `order_item_id`); `order_id` enlaza pedidos y `product_id` productos. | Pronóstico, recompra y segmentación. |
| `olist_products_dataset.csv` | `product_id`, `product_category_name` (texto), `product_name_lenght`, `product_description_lenght`, `product_photos_qty`, `product_weight_g`, `product_length_cm`, `product_height_cm`, `product_width_cm` (numérico, algunos nulos) | `product_id` enlaza líneas de pedido. | Categoría para las tres rutas. |
| `product_category_name_translation.csv` | `product_category_name`, `product_category_name_english` (texto) | `product_category_name` enlaza el nombre de categoría del producto. | Traducción opcional usada como etiqueta legible. |
| `olist_order_payments_dataset.csv` | `order_id` (texto), `payment_sequential` (entero), `payment_type` (texto), `payment_installments` (entero), `payment_value` (numérico) | Clave candidata compuesta (`order_id`, `payment_sequential`); se relaciona con pedidos. | No se requiere. |
| `olist_order_reviews_dataset.csv` | `review_id`, `order_id` (texto), `review_score` (entero), `review_comment_title`, `review_comment_message` (texto), `review_creation_date`, `review_answer_timestamp` (fechas/horas) | `order_id` se relaciona con pedidos; puede haber más de una fila/reseña por pedido. | No se requiere. No se procesa texto de reseñas. |
| `olist_sellers_dataset.csv` | `seller_id` (texto), `seller_zip_code_prefix` (código), `seller_city`, `seller_state` (texto) | `seller_id` enlaza las líneas de pedido. | No se requiere. |
| `olist_geolocation_dataset.csv` | `geolocation_zip_code_prefix` (código), `geolocation_lat`, `geolocation_lng` (numérico), `geolocation_city`, `geolocation_state` (texto) | Un prefijo puede aparecer en varias filas/coordenadas; no asumir clave única. | No se requiere. |

## Relaciones usadas

```text
customers.customer_id 1 ── * orders.customer_id
orders.order_id       1 ── * order_items.order_id
products.product_id   1 ── * order_items.product_id
products.product_category_name  * ── 1 product_category_name_translation.product_category_name
customers.customer_unique_id    agrupa pedidos asociados a customer_id
```

Las relaciones describen enlaces esperados, no una garantía de integridad para
cualquier descarga. La tabla de traducción puede no cubrir todas las categorías;
en ese caso se conserva el nombre original o se etiqueta como `sin_categoria`.

## Límites de interpretación y privacidad

- No hay columnas publicadas de inventario, disponibilidad, quiebre de stock,
  unidades pedidas no satisfechas ni intención de compra.
- No aparece una columna explícita `quantity`. El número de filas de
  `order_items` mide líneas de artículos observadas, no necesariamente unidades.
- `customer_unique_id` es un identificador seudónimo y se usa solo para
  agrupar. No se muestra en tablas, gráficos o interfaz; no se usan nombres,
  ubicaciones ni coordenadas.
- El texto de reseñas y los campos geográficos no se necesitan para estas
  prácticas; el conversor no los transforma.
- La ficha de Kaggle muestra CC BY-NC-SA 4.0. Datos originales y derivados
  quedan fuera del repositorio; la atribución y condiciones de licencia siguen
  aplicando a toda copia/transformación que se comparta.
