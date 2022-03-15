# GetTransactionResponseObjectGetTransactionResponseTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_actions** | **[str]** | Acciones a realizar por parte del POS y/o PINPAD en base al resultado de la operación que ha sido procesada. Cada uno de estos actions o acciones están concatenadas por comas. Los posibles actions son OK, OK, NotExist, ConfigurationError, SystemError, ResourceError, ProcessError, Configure. | [optional] 
**response_message** | **str** | Descripción del resultado del proceso del requerimiento recibido. Esta descripción es generada por la plataforma, no por el Host que termine resolviendo la transacción. | [optional] 
**foreign_response_code** | **str** | Código de respuesta para el sistema externo, es decir, para la aplicación cliente que se comunica con el TEF. | [optional] 
**response_code** | **int** | Código de Respuesta Interno de la plataforma, el POS debe actuar por lo que indican las acciones especificadas en ResponseActions y no por el código de respuesta informado en este campo o elemento, pero es una buena práctica que sea persistido por el mismo. | [optional] 
**tax_financial_cost_amount** | **float** | Monto del recargo impositivo aplicado al costo financiero que la transacción tiene | [optional] 
**tax_financial_cost_percentage** | **float** | Porcentaje de recargo impositivo a aplicar sobre el monto del costo financiero | [optional] 
**financial_cost_amount** | **float** | Monto del Costo financiero total generado en base al plan elegido | [optional] 
**financial_cost_percentage** | **float** | Porcentaje del costo financiero a aplicar al monto de la transacción | [optional] 
**request_amount** | **float** | Monto libre de costos financerios e impuestos por el que la venta se realizó. El monto cobrado realmente no es este, dado que no incluye las tasas e impuestos | [optional] 
**amount** | **float** | Importe o Monto de la Transacción. | [optional] 
**alternative_amount** | **float** | Monto con la que se realizó transacción. Si este valor es recibido, la búsqueda de los planes será limitada con este criterio. | [optional] 
**host_result_code** | **int** | Código de Resultado retornado por el Host Adquirente. | [optional] 
**host_message** | **str** | Mensaje Retornado por el Host Adquirente, normalmente asociado al valor de HostResultCode | [optional] 
**host_code** | **str** | código de autorización retornado por el Host que resuelve la transacción. | [optional] 
**host_date_time** | **datetime** | Fecha y Hora de la transacción retornada por el Host que resuelve la Transacción - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**transmition_date_time** | **datetime** | Fecha y hora de transmision de la operación hacia el host - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**auth_ticket** | **int** | Número Ticket  o Voucher Generado para la Plataforma. | [optional] 
**auth_rrn** | **str** | Número de identificación de la transacción, utilizado por la mayoría de los hosts para realizar anulaciones y devoluciones | [optional] 
**identifier_for_the_adquirer** | **str** | Identificador que genera el Host Adquirente para la Transacción en algunos podrá ser igual al AuthRRN | [optional] 
**payment_facilitator_id** | **str** | Identificador de facilitador de pagos o Payfac. | [optional] 
**merchant_id** | **str** | Número de comercio utilizado para realizar la transacción. Este Número es asignado por el host, y parametrizado en la BD, relaciónado a cada uno de los planes disponibles. | [optional] 
**terminal_id** | **int** | Identificador de Terminal por el cual se envía la Transacción al Host. | [optional] 
**terminal_trace** | **int** | Número de Trace/Secuencia que genera la plataforma para la transacción asociado al TerminalID. | [optional] 
**settlement_batch_number** | **int** | Para aquellos host que exista el concepto de Lote, es el número de lote al cual pertenece la transacción. | [optional] 
**host_id** | **int** | Número de identificación del host al cual fue enviada la petición, y por el cual fue finalmente procesada | [optional] 
**issuer_name** | **str** | Nombre del Emisor de la Credencial o Tarjeta que se usó en la transacción. | [optional] 
**card_description** | **str** | Nombre de la Tarjeta que se usó en la transacción, usado para la impresión del voucher. | [optional] 
**payment_method_description** | **str** | Descripción o nombre de la marca con la cual la tarjeta fue identificada | [optional] 
**plan_description** | **str** | Descripción del plan utilizado para para realizar la operación | [optional] 
**card_read_mode** | **str** | Modo de ingreso de los datos de la tarjeta. Los posibles valores significan: C - EMV Chip / B - Banda magnética / L - Contactless Chip / S - Contactless Banda / M - Manual (Tarjeta Presente) / T - Digitada (Tarjeta no Presente) / E - ECOMMERCE (Ventas por Internet)  / F - FALLBACK (Banda por falla en Chip) / K - TOKEN / R - Recurring ( Pagos Recurrentes ) | [optional] 
**card_number** | **str** | Número de Tarjeta, en el caso de las respuestas el mismo estará enmascarado. | [optional] 
**card_number_masked** | **str** | Número de tarjeta enmascarado, según indica la parametrización en la base de datos. Se utilizará para imprimir en el cupón | [optional] 
**card_hashing** | **str** | Hash de la tarjeta generado por la plataforma. | [optional] 
**currency_description** | **str** | Descripción del tipo de cambio utilizado en la transacción | [optional] 
**currency_symbol** | **str** | Simbolo monetario del tipo de cambio utilizado en la transacción | [optional] 
**card_cryptogram_response** | **str** | Tags EMV en format TLV recibidos desde el Host. | [optional] 
**card_app_name** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_app_identifier** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**card_app_label** | **str** | Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


