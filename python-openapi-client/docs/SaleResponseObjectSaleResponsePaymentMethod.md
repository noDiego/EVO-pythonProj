# SaleResponseObjectSaleResponsePaymentMethod

Objeto representativo del método de pago reconocido.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID interno en la base de datos para este método de pago. | [optional] 
**foreign_identifier** | **str** | ID externo de este método de pago, utilizado por el punto de venta para reconocer el medio de pago en su base de datos. | [optional] 
**description** | **str** | Describe al metodo de pago. | [optional] 
**type** | [**SaleResponseObjectSaleResponsePaymentMethodType**](SaleResponseObjectSaleResponsePaymentMethodType.md) |  | [optional] 
**debit_account** | [**SaleResponseObjectSaleResponsePaymentMethodDebitAccount**](SaleResponseObjectSaleResponsePaymentMethodDebitAccount.md) |  | [optional] 
**category** | [**SaleResponseObjectSaleResponsePaymentMethodCategory**](SaleResponseObjectSaleResponsePaymentMethodCategory.md) |  | [optional] 
**issuers** | [**[SaleResponseObjectSaleResponsePaymentMethodIssuers]**](SaleResponseObjectSaleResponsePaymentMethodIssuers.md) | Cada elemento de este array representa a un emisor disponible para alguno de los planes informados bank. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


