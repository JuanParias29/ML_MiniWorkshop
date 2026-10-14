## Diccionario de variables

### Datos y atribución

Fuente: [Brazilian E-Commerce Public Dataset by Olist en Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), publicado por Olist (ficha mantenida por `olistbr`). La ficha anuncia aproximadamente 100.000 pedidos de 2016–2018, nueve archivos CSV y un tamaño total cercano a 126 MB. Según la ficha, la información es histórica y está anonimizada; aun así, contiene campos de ubicación y texto que no se necesitan para estos ejercicios.

Las variables y ejemplos que aparecen a continuación corresponden al esquema esperado de la versión 2 del dataset, no a una inspección de archivos descargados en este repositorio. Los ejemplos son ilustrativos. El script `scripts/prepare_data.py` valida las columnas mínimas que usan los ejercicios cuando se proporcionan archivos CSV locales. Para consultar los valores nulos y los tipos inferidos de una descarga concreta, ejecute el script y revise `DataFrame.dtypes` y `DataFrame.isna()`.

Los identificadores se tratan como texto; los prefijos postales, como códigos de texto, aunque contengan dígitos. Las claves candidatas y relaciones se derivan del esquema y deben validarse en la versión descargada antes de usarse en producción.

### `olist_orders_dataset.csv` — Pedidos

| Variable | Tipo esperado | Descripción | Ejemplo |
|---|---|---|---|
| `order_id` | Texto | Identificador del pedido. | `e481f51cbdc54678b7cc49136f2d6af7` |
| `customer_id` | Texto | Identificador del cliente asociado al pedido. | `9ef432eb6251297304e76186b10a928d` |
| `order_status` | Texto categórico | Estado del pedido. | `delivered` |
| `order_purchase_timestamp` | Fecha y hora | Momento en que se realizó la compra. | `2017-10-02 10:56:33` |
| `order_approved_at` | Fecha y hora; puede tener nulos | Momento en que se aprobó el pago. | `2017-10-02 11:07:15` |
| `order_delivered_carrier_date` | Fecha y hora; puede tener nulos | Momento en que el pedido fue entregado al transportador. | `2017-10-04 19:55:00` |
| `order_delivered_customer_date` | Fecha y hora; puede tener nulos | Momento en que el pedido llegó al cliente. | `2017-10-10 21:25:13` |
| `order_estimated_delivery_date` | Fecha y hora | Fecha estimada de entrega. | `2017-10-18 00:00:00` |

**Relaciones y uso:** `order_id` identifica el pedido y se relaciona con `order_items.order_id`. `customer_id` se relaciona con `customers.customer_id`. Se utiliza en las tres rutas; en particular, para consultar la fecha de compra y el estado.

### `olist_customers_dataset.csv` — Clientes

| Variable | Tipo esperado | Descripción | Ejemplo |
|---|---|---|---|
| `customer_id` | Texto | Identificador del cliente asociado a un pedido. | `9ef432eb6251297304e76186b10a928d` |
| `customer_unique_id` | Texto | Identificador seudónimo que permite agrupar pedidos de una misma persona. | `7c396fd4830fd04220f754e42b4e5bff` |
| `customer_zip_code_prefix` | Código de texto | Prefijo postal del cliente. | `3149` |
| `customer_city` | Texto | Ciudad registrada para el cliente. | `sao paulo` |
| `customer_state` | Texto | Estado de Brasil registrado para el cliente. | `SP` |

**Relaciones y uso:** `customer_id` se relaciona con `orders.customer_id`. `customer_unique_id` permite agrupar pedidos de una misma persona seudónima y se usa para recompra y segmentación. Los campos geográficos no se usan en estos ejercicios.

### `olist_order_items_dataset.csv` — Artículos de pedido

| Variable | Tipo esperado | Descripción | Ejemplo |
|---|---|---|---|
| `order_id` | Texto | Identificador del pedido al que pertenece la línea. | `e481f51cbdc54678b7cc49136f2d6af7` |
| `order_item_id` | Entero | Número de línea dentro del pedido. | `1` |
| `product_id` | Texto | Identificador del producto de la línea. | `87285b34884572647811a353c7ac498a` |
| `seller_id` | Texto | Identificador del vendedor. | `3504c0cb71d7fa48d967e0e4c94d59d9` |
| `shipping_limit_date` | Fecha y hora | Fecha límite prevista para que el vendedor entregue el artículo al transportador. | `2017-10-06 11:07:15` |
| `price` | Numérico | Precio registrado para la línea del artículo. | `29.99` |
| `freight_value` | Numérico | Valor del flete asociado a la línea. | `8.72` |

**Relaciones y uso:** la clave candidata de una línea es (`order_id`, `order_item_id`). `order_id` se relaciona con `orders.order_id` y `product_id` con `products.product_id`. Se usa en las rutas de pronóstico, recompra y segmentación.

### `olist_products_dataset.csv` — Productos

| Variable | Tipo esperado | Descripción | Ejemplo |
|---|---|---|---|
| `product_id` | Texto | Identificador del producto. | `87285b34884572647811a353c7ac498a` |
| `product_category_name` | Texto; puede tener nulos | Categoría original del producto, en portugués. | `utilidades_domesticas` |
| `product_name_lenght` | Numérico; puede tener nulos | Longitud registrada del nombre del producto. | `40` |
| `product_description_lenght` | Numérico; puede tener nulos | Longitud registrada de la descripción del producto. | `268` |
| `product_photos_qty` | Numérico; puede tener nulos | Cantidad de fotografías asociadas al producto. | `4` |
| `product_weight_g` | Numérico; puede tener nulos | Peso del producto en gramos. | `500` |
| `product_length_cm` | Numérico; puede tener nulos | Longitud del producto en centímetros. | `20` |
| `product_height_cm` | Numérico; puede tener nulos | Altura del producto en centímetros. | `10` |
| `product_width_cm` | Numérico; puede tener nulos | Ancho del producto en centímetros. | `15` |

**Relaciones y uso:** `product_id` se relaciona con `order_items.product_id`. La categoría se utiliza en las tres rutas.

### `product_category_name_translation.csv` — Traducción de categorías

| Variable | Tipo esperado | Descripción | Ejemplo |
|---|---|---|---|
| `product_category_name` | Texto | Nombre original de la categoría, en portugués. | `utilidades_domesticas` |
| `product_category_name_english` | Texto | Traducción al inglés de la categoría. | `housewares` |

**Relaciones y uso:** `product_category_name` se relaciona con `products.product_category_name`. La traducción es opcional y sirve para mostrar etiquetas legibles. Si una categoría no aparece en esta tabla, se conserva el nombre original o se etiqueta como `sin_categoria`.

### `olist_order_payments_dataset.csv` — Pagos

| Variable | Tipo esperado | Descripción | Ejemplo |
|---|---|---|---|
| `order_id` | Texto | Identificador del pedido al que corresponde el pago. | `e481f51cbdc54678b7cc49136f2d6af7` |
| `payment_sequential` | Entero | Secuencia del pago dentro del pedido. | `1` |
| `payment_type` | Texto categórico | Medio de pago utilizado. | `credit_card` |
| `payment_installments` | Entero | Número de cuotas del pago. | `1` |
| `payment_value` | Numérico | Valor registrado para el pago. | `18.12` |

**Relaciones y uso:** clave candidata compuesta (`order_id`, `payment_sequential`); `order_id` se relaciona con `orders.order_id`. No se requiere para estos ejercicios.

### `olist_order_reviews_dataset.csv` — Reseñas

| Variable | Tipo esperado | Descripción | Ejemplo |
|---|---|---|---|
| `review_id` | Texto | Identificador de la reseña. | `a54f0611adc9ed256b57ede6b6eb5114` |
| `order_id` | Texto | Identificador del pedido reseñado. | `e481f51cbdc54678b7cc49136f2d6af7` |
| `review_score` | Entero | Puntuación asignada a la compra. | `5` |
| `review_comment_title` | Texto; puede tener nulos | Título escrito para la reseña. | `Recomendo` |
| `review_comment_message` | Texto; puede tener nulos | Comentario escrito sobre la compra. | `Produto chegou no prazo.` |
| `review_creation_date` | Fecha y hora | Fecha de creación de la reseña. | `2018-01-18 00:00:00` |
| `review_answer_timestamp` | Fecha y hora; puede tener nulos | Momento en que se respondió la reseña. | `2018-01-18 21:46:59` |

**Relaciones y uso:** `order_id` se relaciona con `orders.order_id`. Puede haber más de una reseña por pedido. No se requiere para estos ejercicios y no se procesa el texto de las reseñas.

### `olist_sellers_dataset.csv` — Vendedores

| Variable | Tipo esperado | Descripción | Ejemplo |
|---|---|---|---|
| `seller_id` | Texto | Identificador del vendedor. | `3504c0cb71d7fa48d967e0e4c94d59d9` |
| `seller_zip_code_prefix` | Código de texto | Prefijo postal del vendedor. | `13023` |
| `seller_city` | Texto | Ciudad registrada para el vendedor. | `campinas` |
| `seller_state` | Texto | Estado de Brasil registrado para el vendedor. | `SP` |

**Relaciones y uso:** `seller_id` se relaciona con `order_items.seller_id`. No se requiere para estos ejercicios.

### `olist_geolocation_dataset.csv` — Geolocalización

| Variable | Tipo esperado | Descripción | Ejemplo |
|---|---|---|---|
| `geolocation_zip_code_prefix` | Código de texto | Prefijo postal asociado a la ubicación. | `01046` |
| `geolocation_lat` | Numérico | Latitud registrada. | `-23.546081` |
| `geolocation_lng` | Numérico | Longitud registrada. | `-46.644820` |
| `geolocation_city` | Texto | Ciudad asociada al prefijo postal. | `sao paulo` |
| `geolocation_state` | Texto | Estado de Brasil asociado a la ubicación. | `SP` |

**Relaciones y uso:** un prefijo postal puede aparecer en varias filas con coordenadas distintas; no se debe asumir que es único. Esta tabla no se requiere para los ejercicios.

## Relaciones usadas en los ejercicios

```text
customers.customer_id 1 ── * orders.customer_id
orders.order_id       1 ── * order_items.order_id
products.product_id   1 ── * order_items.product_id
products.product_category_name * ── 1 product_category_name_translation.product_category_name
customers.customer_unique_id agrupa pedidos asociados a customer_id
```
