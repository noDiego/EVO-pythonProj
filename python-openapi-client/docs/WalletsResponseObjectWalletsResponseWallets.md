# WalletsResponseObjectWalletsResponseWallets


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification** | **str** | Identificador o código de la Billetera o Wallet | [optional] 
**name** | **str** | Nombre del Wallet | [optional] 
**label** | **str** | Etiqueta a Mostrar para el Wallet | [optional] 
**image** | **str** | Nombre de la Imagen o Logo o la imagen codificado en base64 | [optional] 
**large_image** | **str** | Nombre de la Imagen o Logo o la imagen codificado en base64 | [optional] 
**small_image** | **str** | Nombre de la Imagen o Logo o la imagen codificado en base64 | [optional] 
**foreign_identifier** | **str** | ID externo de este metodo de pago, utilizado por el punto de venta para reconocer al medio de pago en su base de datos | [optional] 
**auto_confirm** | **bool** | Indica de las Operaciones Financieras son AutoConfirmadas para este Wallet | [optional] 
**support_request_cancel** | **bool** | Indica si dicho Wallet Soporta la cancelación del Requerimiento | [optional] 
**support_validity_of_the_request** | **bool** | Indica si dicho Wallet Soporta la en el envio de Requerimiento de Pago el tiempo de Vida del Requerimiento de Pagos usando el Elemento TransactionTimeout | [optional] 
**void_support** | **str** | Especifica el tipo las Canlelaciones/Anulaciones son soportadas | [optional] 
**wallet_use_in_void_transaction** | **bool** | Indica si para Cancelar/Anular una transacción es requerida nuevamente la interacción contra el Wallet | [optional] 
**return_support** | **str** | Especifica el tipo las Devoluciones son soportadas y de que tipo | [optional] 
**wallet_use_in_return_transaction** | **bool** | Indica si para Devolver una transacción es requerida nuevamente la interacción contra el Wallet | [optional] 
**amount_required** | **bool** | Indica Si el importe a cobrar debe enviarse en la Operación WalletRequest | [optional] 
**token_type** | **str** | Indica el Tipo de Token | [optional] 
**default_retry_time** | **int** | Tiempo por omision en caso de que no sea retornaro en la respuesta de la operación WalletRequest expresado en milisegúndos | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


