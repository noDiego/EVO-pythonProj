# SaleResponseObjectSaleResponseNotification

Notificación a generar alertas vía e-mail. El separador de la lista sera la coma (,).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Razón por la cuál se envía la notificación, puede ser BlackList, ExceptionList o ControlUse. | [optional] 
**message** | **str** | Mensaje a enviar el cuál puede ser proveniente de la sucursal, de la compañía, del canal o del sistema. Sólo se envía si la razón no es por Regla de control. | [optional] 
**control_use_rule** | [**SaleResponseObjectSaleResponseNotificationControlUseRule**](SaleResponseObjectSaleResponseNotificationControlUseRule.md) |  | [optional] 
**distribution_list** | [**SaleResponseObjectSaleResponseNotificationDistributionList**](SaleResponseObjectSaleResponseNotificationDistributionList.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


