# BlockCreateResponseObjectBlockCreateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_actions** | **[str]** | Acciones a realizar por parte del POS y/o PINPAD en base al resultado de la operación que ha sido procesada. Cada uno de estos actions o acciones están concatenadas por comas. Los posibles actions son OK, Approve, Refuse, IssuerCall, Tickets, WithHold, GetCard, UseTerminalToAuthorize, ConfigurationError, SystemError, ResourceError, ProcessError, Completed. | 
**response_message** | **str** | Descripción del resultado del proceso del requerimiento recibido. Esta descripción es generada por la plataforma, no por el Host que termine resolviendo la transacción. | 
**response_code** | **int** | Código de Respuesta Interno de la plataforma, el POS debe actuar por lo que indican las acciones especificadas en ResponseActions y no por el código de respuesta informado en este campo o elemento, pero es una buena práctica que sea persistido por el mismo. | 
**request_type** | **str** | Tipo de Operación que se requirió, contendrá el mismo valor que se recibió en el requerimiento, sobre formatos que no soportan elementos complejos o compuestos. | [optional] 
**company_identification** | **str** | ID que identifica la companía desde donde proviene la petición. | [optional] 
**system_identification** | **str** | ID que identifica el sistema desde donde proviene la petición. | [optional] 
**branch_identification** | **str** | ID que identifica la sucursal desde donde proviene la petición. Esta sucursal pertenece a una determinada companía. | [optional] 
**pos_identification** | **str** | ID que identifica la caja o punto de venta desde donde proviene la petición. Este punto de venta pertenece a una determinada sucursal y companía. | [optional] 
**foreign_response_code** | **str** | Código de respuesta para el sistema externo, es decir, para la aplicación cliente que se comunica con el TEF. | [optional] 
**answer_type** | **str** | Tipo de Operación que se está requiriendo, solo necesario sobre formatos que no soportan elementos complejos o compuestos. | [optional] 
**answer_key** | **str** | Código de identificación, generado por Plataforma, de la operación realizada | [optional] 
**request_key** | **str** | ID generado para la identificación por parte del Plataforma de la información generada en la ejecución de un GetCard o un Payment Method. Sera necesario para que un mensaje de Sale, Void o Payment Method identifique el contexto generado y lo utilice para esa operación. | [optional] 
**server_version** | **str** | Versión del Servicio de la Plataforma que resolvió el requerimiento. | [optional] 
**server_address** | **str** | Dirección IP del Server que atiende el requerimiento. | [optional] 
**server_instance** | **str** | Instancia de Server que atiende el requerimiento. | [optional] 
**server_node_name** | **str** | Nombre del Nodo que atendió el requerimiento. | [optional] 
**message_id** | **str** | Identificador Unívoco del Mensaje ( UUID v5 ). | [optional] 
**adapter_input_version** | **str** | Versión del  Adaptador de Protocolo Entrante que atiende el Requerimiento. | [optional] 
**adapter_input_address** | **str** | Dirección IP del Adaptador de Protocolo Entrante que atiende el requerimiento. | [optional] 
**adapter_input_node_name** | **str** | Nombre del Nodo del Adaptador de Protocolo Entrante que atiende el requerimiento. | [optional] 
**adapter_output_version** | **str** | Versión del  Adaptador de Protocolo Saliente que atiende el Requerimiento. | [optional] 
**adapter_output_address** | **str** | Dirección IP  del  Adaptador de Protocolo Saliente que atiende el Requerimiento. | [optional] 
**adapter_output_node_name** | **str** | Nombre del Nodo  del  Adaptador de Protocolo Saliente que atiende el Requerimiento. | [optional] 
**service_version** | **str** | Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible. | [optional] 
**sequence** | **str** | Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma. | [optional] 
**security** | [**[SaleObjectSaleSecurity]**](SaleObjectSaleSecurity.md) | Datos asociados a la seguridad de la transacción o de elementos sensibles. | [optional] 
**was_reverse_previous** | **int** | Flag indicador de generación de reversa para la última operación reversable | [optional] 
**reversed_answer_key** | **str** | ID que identifica a la operación que acaba de ser reversada. | [optional] 
**reversed_sequence** | **str** | Secuencia de la transacción que fue reversada | [optional] 
**committed_block** | **str** | ID del bloque de transacciones que ha sido confirmado de forma automática (es decir, sin recibir un requerimiento de BlockClose). Este escenario se presentará si el Plataforma así se ha configurado para actuar bajo esa circunstancia. | [optional] 
**reversed_block** | **str** | ID del bloque de transacciones que ha sido cancelado de forma automática (es decir, sin recibir un requerimiento de BlockClose). Este escenario se presentará si el Plataforma así se ha configurado para actuar bajo esa circunstancia. | [optional] 
**required_information** | [**[DebtPaymentObjectDebtPaymentRequiredInformation]**](DebtPaymentObjectDebtPaymentRequiredInformation.md) | En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente. | [optional] 
**additional_information** | [**[SaleResponseObjectSaleResponseAdditionalInformation]**](SaleResponseObjectSaleResponseAdditionalInformation.md) | En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente. | [optional] 
**display_response_message** | **[str]** | Información adicional/Mensaje promocional/Leyenda de respuesta a mostrar en pantalla en el ticket de la operación. Cada línea de este mensaje será un elemento dentro del array. | [optional] 
**block** | **str** | ID que identifica a un grupo de transacciones que serán confirmadas o canceladas | [optional] 
**configuration** | [**SaleResponseObjectSaleResponseConfiguration**](SaleResponseObjectSaleResponseConfiguration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


