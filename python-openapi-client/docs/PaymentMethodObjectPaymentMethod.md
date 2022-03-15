# PaymentMethodObjectPaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_identification** | **str** | ID que identifica la companía desde donde proviene la petición. | 
**system_identification** | **str** | ID que identifica el sistema desde donde proviene la petición. | 
**branch_identification** | **str** | ID que identifica la sucursal desde donde proviene la petición. Esta sucursal pertenece a una determinada companía. | [optional] 
**pos_identification** | **str** | ID que identifica la caja o punto de venta desde donde proviene la petición. Este punto de venta pertenece a una determinada sucursal y companía. | [optional] 
**request_type** | **str** | Tipo de Operación que se está requiriendo, solo necesario sobre formatos que no soportan elementos complejos o compuestos. | [optional] 
**service_version** | **str** | Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible. | [optional] 
**sequence** | **str** | Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma. | [optional] 
**security** | [**[SaleObjectSaleSecurity]**](SaleObjectSaleSecurity.md) | Datos asociados a la seguridad de la transacción o de elementos sensibles. | [optional] 
**block** | **str** | ID que identifica a un grupo de transacciones que serán confirmadas o canceladas. | [optional] 
**ticket** | **str** | Ticket Digitalizado ( Total o parte del mismo por ejemplo la Firma Digitalizada )    codificado en Base64. | [optional] 
**ticket_answer_key** | **str** | Identificador Unívoco de la Transacción que se quiere Referenciar a la cual pertenece el Ticket Digitalizado. El valor fue obtenido en el campo o elemento AnswerKey de la Respuesta de la transacción referenciada. Si la firma fue capturada previamente y se envía en el requerimiento de la misma Operación Sale, Authorize*, Void, Return, Adjustment, DebtPayment, VoidDebtPayment o Enrollment no es necesario que se envíe este elemento o campo. | [optional] 
**timeout** | **float** | Tiempo de espera que el POS espera al PINPAD para obtener la respuesta al requerimiento.  | [optional] 
**request_key** | **str** | ID generado para la identificación por parte del Plataforma de la información generada en la ejecución de un GetCard o un Payment Method. Será necesario para que un mensaje de Sale, Void, PaymentMethod o Enrollment  identifique el contexto generado y lo utilice para esa operación. | [optional] 
**reason_sequence_break** | **str** | Motivo por el cual se requiere romper la secuencia. | [optional] 
**transaction_type** | **str** | Tipo de Transacción (Sale, Void, Return, Authorize,...) por la cual se está realizado el requerimiento | [optional] 
**pos_type** | **str** | Tipo de punto de venta. | [optional] 
**pos_version** | **str** | Versión del Aplicativo del punto de Venta. | [optional] 
**pos_address** | **str** | Dirección IP de la Caja o POS. | [optional] 
**pos_serial** | **str** | Número de serie o identificador unívoco del punto de venta. | [optional] 
**posgeo** | **str** | Coordenadas Geográficas del aplicativo de punto de venta | [optional] 
**reading_device_type** | **str** | Tipo de dispositivo utilizado para ingresar los datos de la tarjeta. En función al dispositivo usado, serán realizadas ciertas verificaciones, por lo que ciertos datos serán requeridos. CustomerKeyboard, utilizado para ingreso manual de tarjeta a través de un portal web, por ejemplo - Keyboard, utilizado para ingreso manual de la tarjeta por parte del vendedor - MagneticStripReader, lector de banda de tarjetas por emulación de teclado, u otro valor configurado  que indentifique el dispositivo que se esta utilizando. | [optional] 
**reading_device_operating_from** | **datetime** | Indica desde cuando se encuentra operativo o encendido el dispositivo | [optional] 
**reading_device_version** | **str** | Versión del dispositivo. | [optional] 
**reading_device_address** | **str** | Dirección IP o MAC Address del dispositivo. | [optional] 
**reading_device_serial** | **str** | Número de serie o identificador unívoco del dispositivo. | [optional] 
**reading_device_geo** | **str** | Coordenadas Geográficas del dispositivo de lectura | [optional] 
**user_id** | **str** | Identificador del usuario que está realizando la Transacción. | [optional] 
**user_name** | **str** | Nombre del usuario que está realizando la Transacción. | [optional] 
**amount** | **float** | Importe o Monto de la Transacción. | [optional] 
**alternative_amount** | **float** | Monto con la que se realizó transacción. Si este valor es recibido, la búsqueda de los planes será limitada con este criterio. | [optional] 
**currency_code** | **str** | Código de Moneda - ISO 4217 &lt;https://en.wikipedia.org/wiki/ISO_4217 Se puede utilizar la Codificación Alfabética o Numérica &lt;br /&gt;   * Num   - Alpha - Description &lt;br /&gt;   * &#39;032&#39; - &#39;ARS&#39; - Pesos Argentinos &lt;br /&gt;   * &#39;152&#39; - &#39;CLP&#39; - Pesos Chilenos &lt;br/&gt;   * &#39;484&#39; - &#39;MXN&#39; - Pesos Mexicanos &lt;br/&gt;   * &#39;840&#39; - &#39;USD&#39; - dólares Americanos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;858&#39; - &#39;UYU&#39; - Pesos Uruguayos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;986&#39; - &#39;BRL&#39; - Real Brasileño | [optional] 
**facility_payments** | **float** | Cantidad de cuotas en las que será realizada la transacción | [optional] 
**facility_type** | **str** | Tipo de Plan de Financiación | [optional] 
**card_app_name** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_app_identifier** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_app_label** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_auth_request_cryptogram** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_auth_response_cryptogram** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_read_mode** | **str** | Modo de ingreso de los datos de la tarjeta. Los posibles valores significan: C - EMV Chip / B - Banda magnética / L - Contactless Chip / S - Contactless Banda / M - Manual (Tarjeta Presente) / T - Digitada (Tarjeta no Presente) / E - ECOMMERCE (Ventas por Internet)  / F - FALLBACK (Banda por falla en Chip) / K - TOKEN / R - Recurring ( Pagos Recurrentes ) | [optional] 
**card_number** | **str** | Número de Tarjeta, en el caso de las respuestas el mismo estará enmascarado. | [optional] 
**card_number_masked** | **str** | Número de tarjeta enmascarado, según indica la parametrización en la base de datos. Se utilizará para imprimir en el cupón.             | [optional] 
**payment_method_id** | **int** | ID del  metodo de pago que se requerie la información | [optional] 
**payment_method_foreign_identifier** | **int** | ID externo de este metodo de pago, utilizado por el punto de venta para reconocer al medio de pago en su base de datos | [optional] 
**orig_transaction_type** | **str** | Tipo de operación financiera a la cual se pretende anular o devolver, para la cual se pretende utilizar esta lectura de tarjeta. Este campo sera de uso obligatorio solo para determinados tipos de dispositivos de captura. | [optional] 
**issuer** | **str** | ID del emisor que se encuentra disponible para este plan | [optional] 
**get_dinamic_plans** | **float** | Flag utilizado para indicar si se quiere conocer los planes dinamicos tambien, como Plan V de Prisma. | [optional] 
**payment_facilitator_id** | **str** | Identificador de facilitador de pagos o Payfac. | [optional] 
**merchant_id** | **str** | Número de comercio utilizado para realizar la transacción. Este Número es asignado por el host, y parametrizado en la BD, relacionado a cada uno de los planes disponibles. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


