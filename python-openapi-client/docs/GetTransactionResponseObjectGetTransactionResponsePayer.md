# GetTransactionResponseObjectGetTransactionResponsePayer

Datos del Pagador

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification** | **str** | Identificador del Pagador | [optional] 
**identification_type** | **str** | Tipo de documento del Pagador. CI, Cédula de identidad - PAS, Pasaporte, Documento nacional de identidad, Contrato - CONTRACT, Número de Cuenta - ACCOUNT_NUMBER | [optional] 
**email** | **str** | Email del Pagador | [optional] 
**document_type** | **str** | Tipo de documento del Pagador. CI, Cédula de identidad - PAS, Pasaporte, Documento nacional de identidad, Contrato - CONTRACT, Número de Cuenta - ACCOUNT_NUMBER | [optional] 
**document_number** | **str** | Número de Documento o identificación del Pagador | [optional] 
**first_name** | **str** | Primer Nombre del Pagador | [optional] 
**last_name** | **str** | Apellido del Pagador | [optional] 
**middle_name** | **str** | Nombre/s del Medio | [optional] 
**abbreviated_name** | **str** | Nombre Abreviado | [optional] 
**phone** | **str** | Número de Teléfono | [optional] 
**zip_code** | **str** | Código Postal | [optional] 
**address_street** | **str** | Dirección, calle | [optional] 
**address_number** | **str** | Número esterior | [optional] 
**address_internal** | **str** | Datos Adicionales de la dirección, apartamento, unidad , etc. | [optional] 
**address_suburb** | **str** | Colonia, Barrio | [optional] 
**address_delegation** | **str** | Delegación | [optional] 
**city** | **str** | Código Postal | [optional] 
**state** | **str** | Estado o Provincia | [optional] 
**country** | **str** | País | [optional] 
**category_code** | **int** | Tipo o de categoría  del Comercio Pagador (ISO 18245) | [optional] 
**tax_category_type** | **str** | Tipo de categoría tributaria del Pagador | [optional] 
**tax_identification_type** | **str** | Identificador  Tributario ( RFC-Mexico, RUT-Chile, CUIT/CUIL-Argentina, etc) | [optional] 
**tax_identification** | **str** | Identificador  Tributario | [optional] 
**notify_url** | **str** | URL para notificación del Pagador | [optional] 
**customer** | [**SaleObjectSaleCustomer**](SaleObjectSaleCustomer.md) |  | [optional] 
**amount_to_apply** | **float** | Importe o Monto de la Transacción a aplicar. | [optional] 
**amount_charged** | **float** | Importe o Monto de la Transacción que efectivamente se cobro , si se envía en Void o Return en lugar de Amount, se genera un Ajuste si el Host lo soporta. | [optional] 
**cashback_amount** | **float** | Monto del dinero en efectivo (cashback). | [optional] 
**tip_amount** | **float** | Importe o Monto de la Propina. | [optional] 
**plan** | **str** | Código/ID de Plan ( obtenido por la Operación PaymentMethod ) , en caso de ser enviado no se requiere en la Transacción el envío de CurrencyCode ni FacilityPayments | [optional] 
**currency_code** | **str** | código de Moneda - ISO 4217 &lt;https://en.wikipedia.org/wiki/ISO_4217 Se puede utilizar la Codificación Alfabética o Numérica &lt;br /&gt;   * Num   - Alpha - Description &lt;br /&gt;   * &#39;032&#39; - &#39;ARS&#39; - Pesos Argentinos &lt;br /&gt;   * &#39;152&#39; - &#39;CLP&#39; - Pesos Chilenos &lt;br/&gt;   * &#39;484&#39; - &#39;MXN&#39; - Pesos Mexicanos &lt;br/&gt;   * &#39;840&#39; - &#39;USD&#39; - dólares Americanos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;858&#39; - &#39;UYU&#39; - Pesos Uruguayos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;986&#39; - &#39;BRL&#39; - Real Brasileño | [optional] 
**facility_payments** | **float** | Cantidad de cuotas en las que sera realizada la transacción | [optional] 
**facility_type** | **str** | Tipo de Plan de Financiación | [optional] 
**tna** | **float** | Se informará la tasa nominal anual, en casos en que el plan elegido para realizar la venta lo posea. Por ejemplo, el plan especial llamado Plan V de Prisma informara este valor, dado que se obtendra dinamicamente, consultandolo instante a instante | [optional] 
**tem** | **float** | Se informará la tasa efectiva mensual, en casos en que el plan elegido para realizar la venta lo posea. Por ejemplo, el plan especial llamado Plan V de Prisma informara este valor, dado que se obtendra dinamicamente, consultandolo instante a instante | [optional] 
**tea** | **float** | Tasa Efectiva anual. Este campo estara presente solo si el tipo de plan es dinamico, o si fue ingresado un valor en la base de datos | [optional] 
**cft** | **float** | Costo Financiero Total. Este campo estara presente solo si el tipo de plan es dinamico, o si fue ingresado un valor en la base de datos         | [optional] 
**merchant_category** | [**SaleResponseObjectSaleResponseMerchantCategory**](SaleResponseObjectSaleResponseMerchantCategory.md) |  | [optional] 
**products** | [**[SaleResponseObjectSaleResponseProducts]**](SaleResponseObjectSaleResponseProducts.md) | Detalle de Productos de la Operación. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


