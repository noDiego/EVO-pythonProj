# SaleResponseObjectSaleResponseNotificationControlUseRule

Si la razón es ControlUse, se va a incluir el ID, el Name y el Template de la regla.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id del control de la regla | [optional] 
**name** | **str** | Nombre del control de la regla | [optional] 
**template** | **str** | Mensaje a enviar en la cadena de e-mails. En caso de no haber una notificación en ControlUse, se va a generar un objeto con los mensajes provenientes de Branch, Company, Channels y Platform en caso de que estos no se encuentren vacíos. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


