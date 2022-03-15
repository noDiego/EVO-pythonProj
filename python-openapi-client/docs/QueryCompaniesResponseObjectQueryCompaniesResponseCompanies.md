# QueryCompaniesResponseObjectQueryCompaniesResponseCompanies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificacion de la Compania | [optional] 
**name** | **str** | Nombre de la compania | [optional] 
**description** | **str** | Descripcion de la compania | [optional] 
**line_of_business_identification** | **str** | Rubro de Pertenencias de la Compania | [optional] 
**order** | **int** | Orden | [optional] 
**amount_type** | **int** | Tipo de Importe que se puede usar para pagar esta empresa | [optional] 
**enable_recurring_payment** | **bool** | Indicador de Habilitacion de Pagos Recurrentes | [optional] 
**provider** | **str** | Identificador del Proveedor del Servicio | [optional] 
**additional_information** | [**[QueryCompaniesResponseObjectQueryCompaniesResponseAdditionalInformation]**](QueryCompaniesResponseObjectQueryCompaniesResponseAdditionalInformation.md) | En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


