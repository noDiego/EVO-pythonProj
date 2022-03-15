# BalanceInquiryObjectBalanceInquiry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_identification** | **str** | ID que identifica la companía desde donde proviene la petición. | 
**system_identification** | **str** | ID que identifica el sistema desde donde proviene la petición. | 
**branch_identification** | **str** | ID que identifica la sucursal desde donde proviene la petición. Esta sucursal pertenece a una determinada companía. | [optional] 
**pos_identification** | **str** | ID que identifica la caja o punto de venta desde donde proviene la petición. Este punto de venta pertenece a una determinada sucursal y companía. | [optional] 
**service_version** | **str** | Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible. | [optional] 
**sequence** | **str** | Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma. | [optional] 
**security** | [**[SaleObjectSaleSecurity]**](SaleObjectSaleSecurity.md) | Datos asociados a la seguridad de la transacción o de elementos sensibles. | [optional] 
**block** | **str** | ID que identifica a un grupo de transacciones que serán confirmadas o canceladas | [optional] 
**reason_sequence_break** | **str** | Motivo por el cual se requiere romper la secuencia. | [optional] 
**reading_device_type** | **str** | Tipo de dispositivo utilizado para ingresar los datos de la tarjeta. En función al dispositivo usado, serán realizadas ciertas verificaciones, por lo que ciertos datos serán requeridos. CustomerKeyboard, utilizado para ingreso manual de tarjeta a través de un portal web, por ejemplo - Keyboard, utilizado para ingreso manual de la tarjeta por parte del vendedor - MagneticStripReader, lector de banda de tarjetas por emulación de teclado, u otro valor configurado  que indentifique el dispositivo que se esta utilizando. | [optional] 
**card_app_name** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_app_identifier** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_app_label** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_auth_request_cryptogram** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_auth_response_cryptogram** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_read_mode** | **str** | Modo de ingreso de los datos de la tarjeta. Los posibles valores significan: C - EMV Chip / B - Banda magnética / L - Contactless Chip / S - Contactless Banda / M - Manual (Tarjeta Presente) / T - Digitada (Tarjeta no Presente) / E - ECOMMERCE (Ventas por Internet)  / F - FALLBACK (Banda por falla en Chip) / K - TOKEN / R - Recurring ( Pagos Recurrentes ) | [optional] 
**card_get_mode** | **str** | Indican por cada elemento que contiene los datos sensibles, si están encriptados  y también el algoritmo usado. En caso de no estar especificado se asume PLAIN. | [optional] 
**card_number** | **str** | Número de Tarjeta, en el caso de las respuestas el mismo estará enmascarado. | [optional] 
**card_number_masked** | **str** | Número de tarjeta enmascarado, según indica la parametrización en la base de datos. Se utilizará para imprimir en el cupón.             | [optional] 
**card_exp** | **str** | Fecha de vencimiento de la tarjeta. Este dato sera necesario si el modo de ingreso fue manual/digitada. | [optional] 
**track1** | **str** | Banda Número 1 de la tarjeta. Este dato sera necesario si el modo de ingreso fue por banda (deslizando la banda por el lector). | [optional] 
**track2** | **str** | Banda Número 2 de la tarjeta. Este dato sera necesario si el modo de ingreso fue por banda (deslizando la banda por el lector). | [optional] 
**input_tokens** | [**[SaleObjectSaleInputTokens]**](SaleObjectSaleInputTokens.md) | Tokens. | [optional] 
**security_code** | **str** | Código de seguridad de la tarjeta. | [optional] 
**pin** | **str** | PIN block | [optional] 
**card_last_four_digits** | **str** | últimos 4 digitos de la tarjeta, ingresado a partir de lo que el vendedor verifica en la superficie de la tarjeta. Este dato solo sera requerido para ciertos tipos de dispositivos de capturas, como por ejemplo lectores de tarjetas por emulación de teclado, y siempre y cuando la parametrización de la marca de la tarjeta asi lo indique. | [optional] 
**payer** | [**SaleObjectSalePayer**](SaleObjectSalePayer.md) |  | [optional] 
**customer** | [**SaleObjectSaleCustomer**](SaleObjectSaleCustomer.md) |  | [optional] 
**payment_facilitator_id** | **str** | Identificador de facilitador de pagos o Payfac. | [optional] 
**merchant_id** | **str** | Número de comercio utilizado para realizar la transacción. Este Número es asignado por el host, y parametrizado en la BD, relacionado a cada uno de los planes disponibles. | [optional] 
**terminal_id** | **str** | Identificador de Terminal por el cual se envía la Transacción al Host. | [optional] 
**terminal_trace** | **int** | Número de Trace/Secuencia que genera la plataforma para la transacción asociado al TerminalID. | [optional] 
**settlement_batch_number** | **int** | Para aquellos host que exista el concepto de lote, es el número de lote al cual pertenece la transacción. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


