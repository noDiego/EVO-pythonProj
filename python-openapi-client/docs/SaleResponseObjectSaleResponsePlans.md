# SaleResponseObjectSaleResponsePlans

Plan utilizado en la transacción.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificador interno formado por el TEF por una combinación de datos del plan especifico. Si el plan no posee un código de emisor, el último campo no estará presente (ni el _). | [optional] 
**plan_code** | **str** | código de el plan. | [optional] 
**foreign_identifier** | **str** | ID externo para que el punto de venta pueda reconocer el plan. | [optional] 
**issuer** | **str** | ID del emisor que se encuentra disponible para este plan. | [optional] 
**description** | **str** | Descripción del plan. | [optional] 
**facility_payments** | **int** | Cantidad de cuotas que permite este plan | [optional] 
**facility_type** | **str** | Tipo de Plan de Financiación | [optional] 
**currency_code** | **str** | código de Moneda - ISO 4217 &lt;https://en.wikipedia.org/wiki/ISO_4217 Se puede utilizar la Codificación Alfabética o Numérica &lt;br /&gt;   * Num   - Alpha - Description &lt;br /&gt;   * &#39;032&#39; - &#39;ARS&#39; - Pesos Argentinos &lt;br /&gt;   * &#39;152&#39; - &#39;CLP&#39; - Pesos Chilenos &lt;br/&gt;   * &#39;484&#39; - &#39;MXN&#39; - Pesos Mexicanos &lt;br/&gt;   * &#39;840&#39; - &#39;USD&#39; - dólares Americanos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;858&#39; - &#39;UYU&#39; - Pesos Uruguayos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;986&#39; - &#39;BRL&#39; - Real Brasileño | [optional] 
**rate** | **float** | Porcentaje de recargo completo para el monto de la operación. | [optional] 
**amount** | **float** | Monto debido al porcentaje de recargo. | [optional] 
**offline_amount_limit** | **float** | Monto máximo para operar de forma OFFLINE. | [optional] 
**deferral** | [**SaleResponseObjectSaleResponsePlansDeferral**](SaleResponseObjectSaleResponsePlansDeferral.md) |  | [optional] 
**cashback** | [**SaleResponseObjectSaleResponsePlansCashback**](SaleResponseObjectSaleResponsePlansCashback.md) |  | [optional] 
**tna** | **float** | Se informará la tasa nominal anual, en casos en que el plan elegido para realizar la venta lo posea. Por ejemplo, el plan especial llamado Plan V de Prisma informará este valor, dado que se obtendrá dinámicamente, consultandolo instante a instante. | [optional] 
**tem** | **float** | Se informará la tasa efectiva mensual, en casos en que el plan elegido para realizar la venta lo posea.  | [optional] 
**tea** | **float** | Tasa Efectiva anual. Este campo estará presente solo si el tipo de plan es dinámico, o si fue ingresado un valor en la base de datos. | [optional] 
**cft** | **float** | Costo Financiero Total. Este campo estará presente solo si el tipo de plan es dinámico, o si fue ingresado un valor en la base de datos.         | [optional] 
**value_facility_payments** | **float** | Monto final a pagar en cada una de las cuotas en las que se divida la compra | [optional] 
**issuer_name** | **str** | Nombre del emisor de este plan. Estará presente solo si existe un solo emisor para todos los planes, o si el plan es dinámico | [optional] 
**is_dynamic** | **bool** | Flag que indica si el plan es del tipo dinamico o no | [optional] 
**category** | **str** | Campo que le permite al punto de venta elegir entre un plan u otro | [optional] 
**posor_device_actions** | **[str]** | Lista de Acciones que debe ejecutar el POS o el Dispositvo para el caso que este Plan sea seleccionado. Acciones para el Device &lt;b&gt;RequestPIN&lt;/b&gt; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


