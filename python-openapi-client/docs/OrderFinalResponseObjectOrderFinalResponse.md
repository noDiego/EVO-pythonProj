# OrderFinalResponseObjectOrderFinalResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_actions** | **[str]** | Acciones a realizar por parte del POS y/o PINPAD en base al resultado de la operación que ha sido procesada. Cada uno de estos actions o acciones están concatenadas por comas. Los posibles actions son OK, Approve, Refuse, IssuerCall, Tickets, WithHold, GetCard, UseTerminalToAuthorize, ConfigurationError, SystemError, ResourceError, ProcessError, Completed. | 
**response_message** | **str** | Descripción del resultado del proceso del requerimiento recibido. Esta descripción es generada por la plataforma, no por el Host que termine resolviendo la transacción. | 
**response_code** | **int** | Código de Respuesta Interno de la plataforma, el POS debe actuar por lo que indican las acciones especificadas en ResponseActions y no por el código de respuesta informado en este campo o elemento, pero es una buena práctica que sea persistido por el mismo. | 
**request_type** | **str** | Tipo de Operación que se requirió, contendrá el mismo valor que se recibió en el requerimiento, sobre formatos que no soportan elementos complejos o compuestos. | [optional] 
**system_identification** | **str** | ID que identifica el sistema desde donde proviene la petición. | [optional] 
**company_identification** | **str** | ID que identifica la companía desde donde proviene la petición. | [optional] 
**branch_identification** | **str** | ID que identifica la sucursal desde donde proviene la petición. Esta sucursal pertenece a una determinada companía. | [optional] 
**pos_identification** | **str** | ID que identifica la caja o punto de venta desde donde proviene la petición. Este punto de venta pertenece a una determinada sucursal y companía. | [optional] 
**foreign_response_code** | **str** | Código de respuesta para el sistema externo, es decir, para la aplicación cliente que se comunica con el TEF. | [optional] 
**service_version** | **str** | Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible. | [optional] 
**sequence** | **str** | Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma. | [optional] 
**security** | [**[SaleObjectSaleSecurity]**](SaleObjectSaleSecurity.md) | Datos asociados a la seguridad de la transacción o de elementos sensibles. | [optional] 
**additional_information** | [**[SaleResponseObjectSaleResponseAdditionalInformation]**](SaleResponseObjectSaleResponseAdditionalInformation.md) | En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente. | [optional] 
**required_information** | [**[DebtPaymentObjectDebtPaymentRequiredInformation]**](DebtPaymentObjectDebtPaymentRequiredInformation.md) | En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente. | [optional] 
**transaction_identification** | **str** | ID de la operación a realizar, generado por el sistema externo | [optional] 
**transaction_description** | **str** | Descripción del tipo de operación que se realizará | [optional] 
**payment_transaction_identification** | **str** | . | [optional] 
**host_response_code** | **str** | . | [optional] 
**host_response_message** | **str** | . | [optional] 
**host_response_action** | **str** | . | [optional] 
**host_merchant_identification** | **str** | . | [optional] 
**host_terminal_identification** | **str** | . | [optional] 
**host_batch_number** | **str** | . | [optional] 
**host_ticket_number** | **str** | . | [optional] 
**host_trace_number** | **str** | . | [optional] 
**host_retrieval_reference_number** | **str** | . | [optional] 
**host_transaction_identification** | **str** | . | [optional] 
**host_authorization_code** | **str** | . | [optional] 
**credential_token** | **str** | Token asociado a la Credencial Enrolada | [optional] 
**credential_issuer_token** | **str** | Emisor del Token asociado a la credencial enrolada | [optional] 
**plan_id** | **str** | . | [optional] 
**payment_method_id** | **str** | . | [optional] 
**host_id** | **str** | . | [optional] 
**acquirer_reference_data** | **str** | Identificador de la transacción, utilizado solo por algunos hosts para realizar anulaciones y devoluciones | [optional] 
**identifier_for_the_acquirer** | **str** | Identificador de la transacción generado por Plataforma para ser enviado al Adquirente | [optional] 
**configuration** | [**SaleResponseObjectSaleResponseConfiguration**](SaleResponseObjectSaleResponseConfiguration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


