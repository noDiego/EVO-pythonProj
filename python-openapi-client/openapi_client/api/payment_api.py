"""
    EVO Payment API

    <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 32px;\">API de Pagos</h1> <br /><br /> <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 24px;\">Descripción del Servicio</h1> <p style=\"color:#004785;\"><b><u>Documentación en formato OpenAPI 3.0</b></u></p> <br/> Contrato especificado según especificaciones https://www.openapis.org/ y https://swagger.io/.<br /><br />  En el site https://editor.swagger.io/ se dispone de un  Viewer, Editor y  Generar de Código ( SDK ) para varios lenguajes de programación; incluyendo JAVA, C#, C++, Perl, Node.js, GO, PHP, Ruby y otros.<br/><br/> Para <b>ver</b> la documentación o <b>generar</b> código de la librería cliente o SDK  se deberá selecciónar en el menú horizontal  la opción <b>File</b>, en el menú vertical que se depliega la opción <b>Import File</b> y luego se deberá selecciónar el archivo del contrato deseado, ya sea  extensión <b>.json</b> o <b>.yaml</b>. <br/><br/> Además se puede generar el código de la librería cliente desde la línea de comandos a través de la herramienta  <b>CLI</b>  de  <b>OpenAPI Generator</b>. Esta presenta generadores de SDK en mayor variedad de lenguajes de programación.  En el site https://openapi-generator.tech/docs/installation se documenta cómo  <b>instalar</b> la herramienta CLI.<br/><br/> Los clientes generados contienen, adicionalmente al código,  la documentación de uso del mismo en <b>README.md</b>, como también en el subdirectorio <b>docs</b> toda la documentación del API o servicio y sus operaciones, con el detalle de los  campos o elementos y su dominio.<br /><br /><br /><br /> <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 24px;\">Notas a tener en cuenta para realizar la Integración</h1><br/> <p style=\"color:#004785;\"><b><u>Conceptos y/ Mecanismos relevantes Soportados por el Protocolo de Integración</u></b></p> <br/><br/> <span>&#8226;</span> <b>Interpretración de las Respuesta</b>,<br /><br/> El único campo que indica si la transacción fue aprobada, rechazada, o tienen algun error, es el elemento de las respuestas llamado <b>ResponseActions</b>, el  cual es un <b>ARRAY</b> de valores. Cada uno de estos indica una acción a realizar. Los elementos <b>ResponseCode</b>  y <b>ResponseMessage</b> son solamente informativos y por lo tanto no deben usarse para tomar acciones y los mismos pueden cambiar en base a la configuración de la Plataforma.<br/><br/> <span>&#8226;</span> <b>Bloque de transacciones</b>, permite Confirmar o Cancelar/Revertir todas las transacciones que forman parte de un bloque. <br/><br/> El POS puede definir un bloque o conjunto de transacciones simplemente indicando en todas ellas el mismo valor en el atributo/elemento/campo opcional llamado <b>Block</b>.<br/>  La operación <b>BlockCancel</b>, permite que el POS pueda solicitar a la plataforma la reversión y/o cancelación de todo el bloque de transacciones .<br/> La operación <b>BlockClose</b>, confirma todas las transacciones que forman parte del bloque especificado.<br/> Si el POS no posee un identificador unívoco de la transacción de venta, al momento de interactuar contra la plataforma podrá obtener uno con la operación  <b>BlockCreate</b>. Si el elemento o campo <b>Block</b>  existe y su contenido es Vacío o Nulo la plataforma realiza un <b>BlockCreate</b> automáticamente.<br /><br/> <span>&#8226;</span> <b>Reversas por Ruptura de Secuencia</b>. Evita la necesidad de persistir datos de la reversa y ahorra una transacción en el flujo.<br/>   El método llamado de ruptura de secuencia es utilizado para detectar los casos en los cuales el POS o Caja no pudo recibir una respuesta del mismo o no pudo procesarla adecuadamente. De esta forma permite a la misma reversar la transacción que no pudo procesar el POS o recibir la respuesta si fuese necesario.     En todo requerimiento el POS debe enviar el campo/elemento Sequence, con el valor recibido en el anterior requerimiento o vacío en el primero.    La plataforma  genera una nueva secuencia solamente cuando el requerimiento realizado es reversible o cuando se produce una ruptura.  Por lo tanto los comandos en los cuales la plataforma  genera una nueva secuencia son <b>Sale</b>, <b>Void</b>, <b>Authorize*</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b>, <b>Confirm</b>, <b>Close</b> y <b>Cancel</b>.    En caso de que la plataforma reverse el requerimiento previo retornará en la respuesta los siguiente campos o elementos.   <blockquote><b>WasReversePrevious</b>, con valor <b>1</b><br/>   <b>ReversedAnswerKey</b> conteniendo el <b>AnswerKey</b> de la transacción reversada<br/>   <b>ReversedSequence</b> conteniendo el <b>Sequence </b>de la transacción reversada</blockquote>    En caso de que la plataforma no reverse el requerimiento previo retornará los siguientes campos o elementos <blockquote><b>WasReversePrevious</b>, con valor <b>0</b></blockquote> <br/> <span>&#8226;</span> <b>Reversas Tradicionales</b>. El POS debe repetir el mismo requerimiento adicionando el atributo/elemento <b>IsReverse</b> con valor <b>1</b>.  Se debe tener en cuenta que en esta modalidad la plataforma no retorna los siguientes atributos/elementos.    <blockquote>   <b>WasReversePrevious</b><br/>   <b>ReversedAnswerKey</b><br/>   <b>ReversedSequence</b>   </blockquote>    <span>&#8226;</span> <b>Transacción Opcional de Confirmación</b>, ya que el mecanismo anterior permite que cada transacción Reverse o Confirme la anterior.<br/><br/> <span>&#8226;</span> <b>La Plataforma indica siempre las acciones que se deben realizar</b><br/><br/> <span>&#8226;</span><span>&#8226;</span> <b>Solicitar datos adicionales</b> ( <b>RequiredInformation</b> ), indicando no sólo cuáles son, sino también de qué tipo, valor  inicial, patrón de validación, si son mandatorios o no, qué Label se presenta al usuario, qué ayuda se presenta al usuario, etc.<br/> <span>&#8226;</span><span>&#8226;</span> <b>Mostrar Mensajes en Pantalla</b>. <span>&#8226;</span><span>&#8226;</span> <b>Imprimir Tickets</b>, ya sea en papel o capturar digitalmente el mismo, como así también el Layout de los mismos.<br/><br/><br/> <span>&#8226;</span> <b>Compresión de la trama</b> en base a codificación de los campos numéricos, string siempre de longitud variable, uso de sinónimos en los  campos, para que el programador programe usando los nombres largos y en el transporte se usen sus sinónimos cortos. <br/> <br/> <span>&#8226;</span> <b>Seguridad de los Datos Sensibles y de la Transaccion</b>, El elemento <b>Security</b> debera estar presente solo si los datos sensibles <b>CardNumber</b>, <b>ExpDate</b>, <b>PIN</b>, <b>Track1</b>, <b>Track2</b>, <b>SecurityCode</b> y  <b>CardCryptogram</b> deban ser envidos encriptados y por lo tanto este le elemento nos permite indicar el metodo de encriptacion utilizado y los datos adicionales que sean requeridos por la encriptacion. Si por ejemplo fuese el elemento PIN usando DUKPT y el resto de los datos sencible Track1, Track2 y SecurityCode, se deberian enviar  de la siguiente forma: </br>        \"Security” :  [         {           \"Type\": \"PIN\",           \"Values\":  [               {                    \"Name\": \"Method\",                   \"Value\": \"DUKPT\"               },               {                    \"Name\": \"KSN\",                   \"Value\": \"1234567890ABCDEF\"               },               {                    \"Name\": \"CRC32\",                   \"Value\": \"12345\"               },               {                    \"Name\": \"PlainTextLength\",                   \"Value\": \"4\"               },               {                    \"Name\": \"CipherCounter\",                   \"Value\": \"123\"               },               {                    \"Name\": \"ConsecutiveFailedCiphersCounter\",                   \"Value\": \"123\"               },               {                    \"Name\": \"Data\",                   \"Value\": \"01234567890123456\"               }           ]          },         {           \"Type\": \"SensitiveData\",           \"Values\":  [               {                    \"Name\": \"Method\",                   \"Value\": \"DUKPT-eGlobal\"               },               {                    \"Name\": \"KSN\",                   \"Value\": \"1234567890ABCDEF\"               },               {                    \"Name\": \"Track1CRC32\",                   \"Value\": \"12345\"               },               {                    \"Name\": \"Track2CRC32\",                   \"Value\": \"12345\"               },               {                    \"Name\": \"Track1Length\",                   \"Value\": \"79\"               },               {                    \"Name\": \"Track2Length\",                   \"Value\": \"37\"               },               {                    \"Name\": \"SecurityCodeLength\",                   \"Value\": \"3\"               },               {                    \"Name\": \"CipherCounter\",                   \"Value\": \"123\"               },               {                    \"Name\": \"ConsecutiveFailedCiphersCounter\",                   \"Value\": \"123\"               },               {                    \"Name\": \"Data\",                   \"Value\": \"1ahbcd23412345123412b213b1324b1234b2134b2134132b4123b23\"               }           ]          },         {           \"Type\": \"3DSecure\",           \"Values\":  [               {                    \"Name\": \"Method\",                   \"Value\": \"3DS-SNAP\"               },               {                                           \"Name\":  \"TransactionStatus\",                   \"Value\": \"SuccessfullyAuthenticated\"               },               {                                           \"Name\":  \"AuthenticationECI\",                   \"Value\": \"05\"               },               {                                           \"Name\":  \"IsChallengeMandated\",                   \"Value\": \"false\"               },               ...               {                                           \"Name\":  \"AcsReferenceNumber\",                   \"Value\": \"3DS_LOA_ACS_PPFU_020100_00009\"               },               {                    \"Name\":  \"ProcessedAsDataOnly\",                   \"Value\": \"false\"               }           ]          }               ] </br> Para el caso de DUKPT-eGlobal, <b>Track2</b>, <b>SecurityCode</b> y <b>Track1</b> se cifraran formando parte del mismo Bloque, El mismo se debera formar con el Track2 ( reemplazando el signo = por el digito D ) completandolo hasta los 38 digitos con el digito F, luego el  SecurityCode completandolo hasta 10 digitos y por ultimo el Track1 padeado completando el bloque  de los 208 digitos.  </br> Este elemento <b>Security</b> sera utilizado para enviar cualquier dato de autenticacion del pagador por ejemplo 3DSecure, para el caso de que el proveedor de la Autenticacion sea SNAP se deberan contener como valores todos los elementos definidos en el objeto <b>ThreeDSInformation</b>.     </br> Este mecanismo podra utilizarse en el futuro para encriptar otros datos que sean sensibles pero no del medio de pago, si no de las personas. </br> <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 24px;\">Log de Cambios</h1></br> <span>&#8226;</span> <b>Versión 5.6.1</b> <span>&#8226;</span><span>&#8226;</span> Se añade el campo <b>MerchantCategory</b> en las respuestas de todas las transacciones. Sólo se enviará en caso de que la categoría de la compañia exista.</br> <span>&#8226;</span> <b>Versión 5.6.0</b> <span>&#8226;</span><span>&#8226;</span> Los campos <b>ResponseCode</b>, <b>ResponseMessage</b> y <b>ResponseActions</b> son <b>obligatorios</b> en las respuestas de todas las transacciones.</br> <span>&#8226;</span> <b>Versión 5.5.7</b> <span>&#8226;</span><span>&#8226;</span> Se añade el elemento <b>Notification</b>. El mismo se encuentra dentro de <b>SaleResponse</b> y <b>AuthorizeSaleResponse</b>. Notificación a generar alertas vía e-mail.</br> <span>&#8226;</span> <b>Versión 5.5.6</b> <span>&#8226;</span><span>&#8226;</span> Se añaden los elementos <b>CardAppLabel</b>, <b>CardAuthRequestCryptogram</b> y <b>CardAuthResponseCryptogram</b>, para facilitar el analisis de los POS y ReadingDevices, el contenido de dichos elementos se encontraba en Tag de los elementos CardCryptogram y CardCryptogramResponse.</br> <span>&#8226;</span>  <b>Versión 5.5.5</b> <span>&#8226;</span><span>&#8226;</span> Se modifican los elementos <b>AuthorizeSale</b> y <b>AuthorizeSaleResponse</b> para su correcta documentación. Además, se añade el campo <b>ReadingDeviceOperatingFrom</b> el cual indica desde cuando se encuentra operativo o encendido el dispositivo</br> <span>&#8226;</span> <b>Versión 5.5.4</b> <span>&#8226;</span><span>&#8226;</span> Se renombra el atributo <b>ReasonReverse</b> a <b>ReverseReason</b>. Dicho campo permite notificar en las Reversas la razón por la cual fue necesario generarla.</br> <span>&#8226;</span> <b>Versión 5.5.3</b> <span>&#8226;</span><span>&#8226;</span> Se agregan atributos al elemento <b>Configuration</b> para la operación <b>PaymentMethod</b>. Por otra parte, se añade el mismo en todas las operaciones donde no se encontraba documentado. </br><b>• Versión 5.5.2</b> <span>&#8226;</span><span>&#8226;</span> Se Agrega el elemento <b>Payer</b> con los datos del Pagador. Originalmente hasta esta version se envian los mismos en el elemento <b>Customer</b>, pero desde ahora se permite que se informen personas ( fisicas y juridicas ) como cliente comprador y como pagador. Si el elemento <b>Payer</b> no esta presente se tomaran los datos del elemento <b>Customer</b>. Se da soporte al Tipo de Ticket Payer.</br> <span>&#8226;</span> <b>Versión 5.5.1</b> </br> <span>&#8226;</span><span>&#8226;</span> Se completa la documentacion de los Elementos <b>Seller</b> y <b>Customer</b>, agregandose los atributos <b>City</b> y  <b>AbbreviatedName</b>.<br/>   <span>&#8226;</span><span>&#8226;</span> Se unifica la definicion del Elemento  <b>Customer</b> .<br/>   <span>&#8226;</span><span>&#8226;</span> Se agrega el Elemento <b>PaymentFacilitatorID</b> para indicar el Identificador de Facilitador de pagos o Payfac.</br> <span>&#8226;</span> <b>Versión 5.5.0</b> </br> <span>&#8226;</span><span>&#8226;</span> El elemento <b>ResponseActions</b> y <b>PosOrDeviceAction</b> de todas las operaciones deja de ser una lista.<br/>  de elementos en un string y se convierte en un array de string. Cada valor de la lista anterior está representada por un elemento del array.<br/>   <span>&#8226;</span><span>&#8226;</span> Se agregan los campos <b>ForeignIdentifier</b>, <b>SmallImage</b> y <b>LargeImage</b> en el campo <b>Wallets</b> de la operación <b>WalletsResponse</b>.<br/> <span>&#8226;</span><span>&#8226;</span> En el campo <b>PaymentMethods</b> de la operación <b>PaymentMethodsResponse</b> se agregan las properties <b>Imag</b>, <b>SmallImage</b> y <b>LargeImage</b>. Además se adiciona el campo <b>ID</b> en <b>Category</b> y el campo <b>ForeignIdentifier</b> en <b>Type</b>. <br/> <span>&#8226;</span><span>&#8226;</span> Se agrupan los campos relacionados con los datos del cliente y del vendedor en dos únicos campos de tipo objeto denominados <b>Customer</b> y <b>Seller</b>, respectivamente.<br/> <span>&#8226;</span><span>&#8226;</span> El elemento Layout del campo <b>Tickets</b> se convierte en un array de objetos que contiene elementos que permiten describir, dar formato y codificar los datos a imprimir. <br/> <span>&#8226;</span><span>&#8226;</span> Se documenta la operación <b>OrderStatus</b>.</br> <span>&#8226;</span><span>&#8226;</span> Los campos que refieren a tiempo y fecha se convierten en formato date-time. </br> <span>&#8226;</span><span>&#8226;</span> Se agrega el campo <b>ForeignResponseCode</b> en todas las respuestas de las operaciones, como un código de para el sistema externo, es decir, para la aplicación cliente que se comunica con el TEF.</br> <span>&#8226;</span><span>&#8226;</span> Se adiciona el campo <b>CardGetMode</b> que permite indicar por cada elemento que contiene los datos sensibles, si están encriptados y también el algoritmo usado. En caso de no estar especificado se asume PLAIN.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega el campo <b>OrigReference</b> en aquellas operaciones que pueden referenciar a una transacción previa, como <b>Void</b>, <b>Return</b> y <b>GetTransaction</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se cambia la estrutura de la respuesta de la Operacion <b>GetTransacion</b> por errores. </br> <span>&#8226;</span><span>&#8226;</span> Se agregan las acciones Ok, Error y Retry en los campos <b>ResponseActions</b>.</br> <span>&#8226;</span><span>&#8226;</span> En aquellas operaciones financieras en las que se especifica la tarjeta se agrega en el requerimiento el campo <b>Pin</b>y en la respuesta el campo <b>WorkingKeys</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega el campo <b>Security</b> con el objetivo de indicar los datos sensibles de seguridad de una transacción tanto en los requerimientos como en las respuestas de las operaciones disponibles.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega la operacion <b>KeysRenewal</b> Las claves podran ser retornadas en el elemento <b>Security</b> y en caso de obtener como accion de respuesta <b>KeysRenewal</b> se esta indicando que esta nueva operacion debe ser ejecutada.<br/>      <span>&#8226;</span><span>&#8226;</span> Se agrega la opcion <b>Signature</b>  .<br/>     <span>&#8226;</span><span>&#8226;</span> Se agrega el elemento  <b>CategoryCode</b> para especificar el MCC del Vendedor y/o del Cliente  .<br/>     <span>&#8226;</span><span>&#8226;</span> Se agregan los Elementos <b>MerchantID</b>, <b>TerminalID</b>, <b>TraceNumber</b> y <b>SettlementBatchNumber</b> En los requerimientos, en caso que los mismos contengan valor los mismos seran utilizados para enviar al Host Resolutor de la Transaccion.</br>  <span>&#8226;</span><span>&#8226;</span> Se agregan los valores para pagos recurrentes a  los Elementos  <b>CardReadMode</b> y  <b>CardReadModeDescription</b> <span>&#8226;</span> <b>Versión 5.4.0</b> </br> <span>&#8226;</span><span>&#8226;</span> Se cambia la dirección IP por el nombre.</br> <span>&#8226;</span><span>&#8226;</span> Se contemplan los Datos del <b>Vendedor/Seller</b> y del <b>Cliente/Customer</b> en las operaciones  <b>WalletRequest</b>, <b>Sale</b>, <b>AuthorizeSale</b>, <b>DebtPayment</b>,  <b>Deposit</b>,  <b>Settlement</b>,  <b>Capture</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se Agregan los elementos <b>POSGEO</b> y <b>ReadingDeviceGEO</b> para que el dispositivo de lectura y el Punto de venta Notifiquen su coordenadas georefenciales en el momento de que se realiza la transacción.</br> <span>&#8226;</span><span>&#8226;</span> Se unifica y amplía el elemento <b>RequiredInformation</b>  tanto en los requerimientos como en las respuestas</br>  <span>&#8226;</span><span>&#8226;</span> Se cambia el tipo el elemento <b>CurrencyCode</b> a string para permitir cualquieras de la notaciones posibles.</br> <span>&#8226;</span><span>&#8226;</span> Se cambia el  elemento <b>Currency</b> por <b>CurrencyCode</b>  en el elemento <b>Plans</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se contemplan del detalle ( elemento <b>Products</b> ) de la venta en las operaciones  <b>WalletRequest</b>, <b>Sale</b>, <b>Void</b>, <b>Return</b>, <b>AuthorizeSale</b>, <b>DebtPayment</b>,  <b>VoidDebtPayment</b>, <b>Deposit</b>,  <b>Settlement</b>,  <b>Capture</b>.</br> <span>&#8226;</span><span>&#8226;</span> Agregamos la operación <b>DebtInquiry</b> que actua como sinónimo de <b>BalanceInquery</b>, la cual podía ser usada para consulta de Saldo y también de deuda.</br> <span>&#8226;</span><span>&#8226;</span> Se corrigen los tipos de Datos de Varios campos <b>Amount</b> que en lugar de string debían ser number.</br> <span>&#8226;</span><span>&#8226;</span> Se agregan las operaciones <b>QueryCompanies</b> y <b>QueryLineOfBusiness</b> para la consulta de Rubros y Empresas que se pueden utilizar para pagar Servicios/Deuda/Facturas con la operación <b>DebtPayment</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se adiciona el elemento <b>Companies</b> en la Operacion <b>BalanceInquiry</b> para el caso de que existan mas de una Compania para el mismo codigo o identificador de la deuda o factura a pagar y adicionalmente se agrega para ese caso la posibilidad de especificar a que compania corrende el Pago en el elemento <b>DebtCompanyIdentification</b> en la operación <b>DebtPayment</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se adiciona el elemento <b>BaseAmonut</b> en los requerimientos de las operación <b>Return</b>, el elemento <b>Reference</b>  en las operaciones <b>Sale</b>, <b>AuthorizeSale</b>, <b>Void</b>, <b>Return</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b>, <b>GetTransaction</b> y <b>WalletRequest</b>.  Además, se agregan los elementos <b>TaxFinancialCostAmount</b>, <b>TaxFinancialCostPercentage</b>, <b>FinancialCostAmount</b>, <b>FinancialCostPercentage</b> y <b>RequestAmount</b>  en las respuestas de dichas operaciones.</br> <span>&#8226;</span><span>&#8226;</span> En cada plan que se devuelve a través del <b>PaymentMethodResponse</b> estarán presentes <b>TaxFinancialCostAmount</b>,  <b>TaxFinancialCostPercentage</b>, <b>FinancialCostAmount</b> y <b>FinancialCostPercentage</b>. </br> <span>&#8226;</span><span>&#8226;</span> Se agregan los elementos  <b>CardAppName</b> y <b>CardAppIdentifier</b> en las peticiones de las operaciones <b>Sale</b>, <b>AuthorizeSale</b>,  <b>Void</b>, <b>Return</b>, <b>PaymentMethods</b>, <b>GetCard</b>, <b>Validate</b>, <b>DebtInquiery</b>, <b>BalanceInquiry</b>, <b>DebtPayment</b> y <b>VoidDebtPayment</b>.  Además, se agregan en las respuestas de algunas de ellas.</br> <span>&#8226;</span><span>&#8226;</span> Se cambia la estructura del elemento <b>Tickets</b> de las respuestas donde el elemento <b>Action</b>  hace referencia a las acciones que debe ejecutar el punto de venta, el elemento <b>DeviceAction</b> a las acciones que debe ejecutar el dispositivo y <b>ExecutedAction</b> a las acciones  que ejecutó la plataforma para sus <b>Tickets</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se adicionan los elementos <b>POSOrDeviceAction</b>, <b>OperationMode</b> y <b>OperationModeDescription</b> a la operación <b>Configure</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega el elemento <b>RemainderAmount</b> a la operación <b>GetBlockResponse</b> que hace referencia a la diferencia entre el monto total de la transacción y las devoluciones parciales realizadas.</br> <span>&#8226;</span><span>&#8226;</span> Se corrijen errores en la definición de varios campos, como <b>ReadingDeviceType</b> y <b>CardReadMode</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se reemplaza el campo <b>ApplicationIdentification</b> por <b>SystemIdentification</b> en las operaciones <b>EnableService</b>, <b>Wallets</b>, <b>QueryCompanies</b>,  <b>QueryLineOfBusiness</b> y sus respectivas respuestas. </br> <span>&#8226;</span><span>&#8226;</span> Se agregan el identifidor Tributario en <b>Sale</b>, <b>AuthorizeSale</b>, <b>Void</b>,  <b>Return</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b> y <b>Debtinquery</b> que permite transacciones con <b>Token</b> ( <b>CredentialToken</b> y  <b>CredentialIssuerToken</b> ). En estas operaciones se elimina de mandatorias al campo <b>BranchIdentification</b> y <b>POSIdentification</b><br/> <span>&#8226;</span><span>&#8226;</span> Se agrega la operación <b>Enrollment</b>, la cual permite transacciones con <b>Token</b> ( <b>CredentialToken</b> y  <b>CredentialIssuerToken</b> ) y pagos recurrentes.</br> <span>&#8226;</span><span>&#8226;</span> El campo <b>ResponseAction</b> deja de ser un enum y se convierte en string. Se indica en la descripción los posibles actions.</br> <span>&#8226;</span><span>&#8226;</span> Se agregan los campos <b>SellerIdentification</b> y <b>SellerIdentificationType</b> en aquellas operaciones en las que se especifican con los datos del vendedor.</br> <span>&#8226;</span><span>&#8226;</span> El campo <b>FacilityPayments</b> deja de ser mandatario en las operaciones <b>Enrollment</b> y <b>Sale</b>. </br> <span>&#8226;</span><span>&#8226;</span> Se elimina la posibilidad de envío en el header HTTP.<br/> <span>&#8226;</span><span>&#8226;</span> Se agregan los campos <b>CashbackAmount</b> y <b>TipAmount</b> en la operación <b>WalletRequest</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se adiciona en el campo <b>CardReadMode</b> la opción K de Token.<br/> <span>&#8226;</span><span>&#8226;</span> Se corrige el campo <b>Answertype</b> y se modifica por <b>AnswerType</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se agregan los campos referidos al vendedor en las operaciones <b>Void</b> y <b>Return</b>. <br/> <span>&#8226;</span><span>&#8226;</span> Se crea un primer nivel para cada operación de tipo objeto. <br/>  <span>&#8226;</span><span>&#8226;</span> Se crea el campo <b>InputTokens</b> como un array de objetos que contienen Name y Value como properties en las operaciones <b>Sale</b>, <b>AuthorizeSale</b>, <b>Void</b>, <b>Return</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b> y <b>DebtInquiry</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Los elementos <b>Action</b>, <b>DeviceAction</b> y <b>ExecutedAction</b> del campo <b>Tickets</b> dejan de ser de tipo string y se convierten en arrays.<br/>     <span>&#8226;</span><span>&#8226;</span> Se agrega el elemento <b>AdditionalInformation</b> en las respuestas de todas las operaciones.<br/>     </br> <span>&#8226;</span> <b>Versión 5.3.0</b> Se amplía la definición de la Operación <b>Configure</b> permitiendo tanto en la respuesta como en el requerimiento los elementos <b>Operations</b>, <b>Tables</b> y <b>Files</b></br></br> Se agregan los elementos <b>VoidSupport</b>, <b>ReturnSupport</b>, <b>WalletUseInVoidTransaction</b> y <b>WalletUseInReturnTransaction</b> en las caracteristicas de un Wallet.<br/><br/> Se agrega el Valor <b>Display</b> en el elemento <b>ResponseActions</b> indicando que se debe mostrar en el Display del Dispositivo o Aplicativo el contenido del elemento <b>DisplayResponseMessage</b>.  En la respuesta de la operación  <b>BalanceInquery</b> se agregan los elementos <b>AmountAvailable</b> y <b>PointsAvailable</b> para indicar los saldos.</br> Se especifica en la documentación que el Cancel puede ser usado para Cancelar un Pago con Wallets en Curso.</br></br> Se agregan elementos en los Requerimientos y en las respuestas opcionales entre los POS* que permiten describir las características del punto de venta, los Device* que permiten especificar las características del Dispositivo de Lectura.<br/>   Se cambió el elemento <b>AnswerIdentification</b> por <b>AnswerKey</b>  para compatibilizar con el servicio de Pagos.<br/><br/>     Se agregaron <b>AccountNumber</b>, <b>AccountType</b> y <b>Balance</b> en las operaciones <b>BalanceInquiry</b> y <b>DebtPayment</b> .<br/><br/>     Se agregaron las Operaciones <b>Confirm</b> y  <b>Cancel</b>, donde la Operación <b>Confirm</b> es usada para confirmar un pago recibido por el POS o Aplicativo del comercio. Existen Wallets en los que la confirmación es automática y se indica en el Elemento  <b>AutoConfirm</b> de la respuesta del comando <b>Wallets</b>. La operación <b>Cancel</b> puede ser utilizada a partir de que la Plataforma retorne la acción <b>PaymentFlowIsCancelable</b> en la respuesta de una operación <b>WalletRequest</b>. El Wallet soporta Cancelación de Requerimiento lo cual está indicado con el Elemento <b>SupportRequestCancel</b> dentro de las propiedades de  los Wallets que son retornados por la Operación <b>Wallets</b>.<br/> Se agregó como carasterística de los Wallets también el elemento <b>SupportValidityOfTheRequest</b> que indica si en el primer requerimiento de la Operación <b>WalletRequest</b> se puede enviar el elemento <b>TransactionTimeout</b> que especifica el tiempo de vida de la intención de pago. Superado ese tiempo no se podrá pagar y el ciclo de reintento será detenido por la plataforma, indicado por las siguientes acciones: <b>Completed</b> y <b>Error</b>.<br/> Se agrega el Elemento <b>Tickets</b> en la respuesta de una Operación <b>WalletRequest</b>. El elemento estará presente si como acción está presente el Valor <b>Tickets</b>, indicando que los mismos deberán ser Impresos, capturados digitalmente, etc. según se indique. <br/><br/> Se permite en la Operación <b>PaymentMethod</b> la búsqueda por el Id o el ForeignIdentification<br/><br/> <span>&#8226;</span> <b>Versión 5.2.6</b> Se cambia el nombre del elemento <b>DateTime</b> por <b>TransactionDateTime</b> en la operación <b>WalletRequest</b>.<br/><br/> <span>&#8226;</span> <b>Versión 5.2.5</b> Se agregan en los Planes el atributo <b>POSOrDeviceActions</b> que permite indecarle al Dispositivo que debe solicitar  PIN para esa transacción y eso lo indica enviando la acción <b>RequestPIN</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se agrega el <b>ResponseActions</b> <b>Configure</b> que indica que se debe ejecutar una reconfiguración para obtener  parámetros nuevos ya que hay alguna actualización. <span>&#8226;</span><span>&#8226;</span> Se agregan las Operaciones <b>Wallets</b>, <b>WalletRequest</b> y <b>EnableService</b>, las mismas pueden formar parte  de un Block y forman parte de la ruptura de Secuencia.<br/><br/> <span>&#8226;</span> <b>Versión 5.2.4</b> Se agrega el identifidor Tributario en <b>OrderInitial</b>, que permite transacciones con <b>Token</b> ( <b>CredentialToken</b> y  <b>CredentialIssuerToken</b> ).<br/> <span>&#8226;</span><span>&#8226;</span> Se completa el <b>GetCardResponse</b> para que contenga los  elementos <b>PaymentMethod</b> y <b>Plans</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se completa el <b>PaymentMethodResponse</b> para que contenga los elementos <b>PaymentMethod</b> y <b>Plans</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se agrega en el <b>GetCard</b>: permite forzar un modo de lectura y permite solicitar los datos leídos al POS <b>CardGetMode</b>. <br/><br/> <span>&#8226;</span><span>&#8226;</span> Se permite el envío de datos del cliente <b>Customer*</b> en las operaciones Financieras.<br/><br/> <span>&#8226;</span> <b>Versión 5.2.3</b> Se cambian los valores posibles para <b>ResponseActionCancel</b> en las operaciones <b>GetBlock</b> y <b>GetTransaction</b>.<br/>   <br/> <span>&#8226;</span> <b>Versión 5.2.2</b> Se agrega el Atributo <b>ReasonReverse</b> que permite notificar en las Reversas la razón por la cual fue necesario  generarla, el atributo <b>ReasonSequenceBreak</b> que permite indicar la razón por la cual se produce la ruptura de secuencia que podrá generar una reversa si  fuese necesario, y el atributo </b>Reason</b> en la operación <b>Cancel</b>.<br/>   <br/> <span>&#8226;</span> <b>Versión 5.2.1</b> Se agrega el Atributo <b>IsReverse</b> en todos las operaciones reversables.<br/>   <br/><br/> <br/><br/> <br/><p style=\"color:Blue;\">&copy;2019-2021 EVO Payments Inc. All rights reserved.</p>The EVO Payments name, logo and related trademarks and service marks, owned<br /> by EVO Payments, are registered and/or used in the<br /> United States and many foreign countries. All other trademarks,<br /> service marks and trade names referenced in this site are the property<br /> of their respective owners.<br /> <br /> <br /> ANY USE, COPYING OR REPRODUCTION OF THE TRADEMARKS, LOGOS, INFORMATION,<br />  IMAGES OR DESIGNS CONTAINED IN THIS SITE IS STRICTLY<br />  PROHIBITED WITHOUT THE PRIOR WRITTEN PERMISSION OF EVO Payments Inc.<br /> <br />   # noqa: E501

    The version of the OpenAPI document: 5.6.1
    Contact: integrations@evopayments.mx
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.authorize_sale_object import AuthorizeSaleObject
from openapi_client.model.authorize_sale_response_object import AuthorizeSaleResponseObject
from openapi_client.model.balance_inquiry_object import BalanceInquiryObject
from openapi_client.model.balance_inquiry_response_object import BalanceInquiryResponseObject
from openapi_client.model.block_cancel_object import BlockCancelObject
from openapi_client.model.block_cancel_response_object import BlockCancelResponseObject
from openapi_client.model.block_close_object import BlockCloseObject
from openapi_client.model.block_close_response_object import BlockCloseResponseObject
from openapi_client.model.block_create_object import BlockCreateObject
from openapi_client.model.block_create_response_object import BlockCreateResponseObject
from openapi_client.model.cancel_object import CancelObject
from openapi_client.model.cancel_response_object import CancelResponseObject
from openapi_client.model.capture_object import CaptureObject
from openapi_client.model.capture_response_object import CaptureResponseObject
from openapi_client.model.close_object import CloseObject
from openapi_client.model.close_response_object import CloseResponseObject
from openapi_client.model.configure_object import ConfigureObject
from openapi_client.model.configure_response_object import ConfigureResponseObject
from openapi_client.model.confirm_object import ConfirmObject
from openapi_client.model.confirm_response_object import ConfirmResponseObject
from openapi_client.model.debt_inquiry_object import DebtInquiryObject
from openapi_client.model.debt_inquiry_response_object import DebtInquiryResponseObject
from openapi_client.model.debt_payment_object import DebtPaymentObject
from openapi_client.model.debt_payment_response_object import DebtPaymentResponseObject
from openapi_client.model.deposit_object import DepositObject
from openapi_client.model.deposit_response_object import DepositResponseObject
from openapi_client.model.enable_service_object import EnableServiceObject
from openapi_client.model.enable_service_response_object import EnableServiceResponseObject
from openapi_client.model.enrollment_object import EnrollmentObject
from openapi_client.model.enrollment_response_object import EnrollmentResponseObject
from openapi_client.model.get_block_object import GetBlockObject
from openapi_client.model.get_block_response_object import GetBlockResponseObject
from openapi_client.model.get_card_object import GetCardObject
from openapi_client.model.get_card_response_object import GetCardResponseObject
from openapi_client.model.get_transaction_object import GetTransactionObject
from openapi_client.model.get_transaction_response_object import GetTransactionResponseObject
from openapi_client.model.keep_alive_object import KeepAliveObject
from openapi_client.model.keep_alive_response_object import KeepAliveResponseObject
from openapi_client.model.keys_renewal_object import KeysRenewalObject
from openapi_client.model.order_final_object import OrderFinalObject
from openapi_client.model.order_final_response_object import OrderFinalResponseObject
from openapi_client.model.order_get_object import OrderGetObject
from openapi_client.model.order_get_response_object import OrderGetResponseObject
from openapi_client.model.order_initial_object import OrderInitialObject
from openapi_client.model.order_initial_response_object import OrderInitialResponseObject
from openapi_client.model.order_status_object import OrderStatusObject
from openapi_client.model.order_status_response_object import OrderStatusResponseObject
from openapi_client.model.payment_method_object import PaymentMethodObject
from openapi_client.model.payment_method_response_object import PaymentMethodResponseObject
from openapi_client.model.payment_methods_object import PaymentMethodsObject
from openapi_client.model.payment_methods_response_object import PaymentMethodsResponseObject
from openapi_client.model.query_companies_object import QueryCompaniesObject
from openapi_client.model.query_companies_response_object import QueryCompaniesResponseObject
from openapi_client.model.query_line_of_business_object import QueryLineOfBusinessObject
from openapi_client.model.query_line_of_business_response_object import QueryLineOfBusinessResponseObject
from openapi_client.model.return_object import ReturnObject
from openapi_client.model.return_response_object import ReturnResponseObject
from openapi_client.model.sale_object import SaleObject
from openapi_client.model.sale_response_object import SaleResponseObject
from openapi_client.model.settlement_object import SettlementObject
from openapi_client.model.settlement_response_object import SettlementResponseObject
from openapi_client.model.validate_object import ValidateObject
from openapi_client.model.validate_response_object import ValidateResponseObject
from openapi_client.model.void_debt_payment_object import VoidDebtPaymentObject
from openapi_client.model.void_debt_payment_response_object import VoidDebtPaymentResponseObject
from openapi_client.model.void_object import VoidObject
from openapi_client.model.void_response_object import VoidResponseObject
from openapi_client.model.wallet_request_object import WalletRequestObject
from openapi_client.model.wallet_request_response_object import WalletRequestResponseObject
from openapi_client.model.wallets_object import WalletsObject
from openapi_client.model.wallets_response_object import WalletsResponseObject


class PaymentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.authorize_sale_post_endpoint = _Endpoint(
            settings={
                'response_type': (AuthorizeSaleResponseObject,),
                'auth': [],
                'endpoint_path': '/AuthorizeSale',
                'operation_id': 'authorize_sale_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'authorize_sale_object',
                ],
                'required': [
                    'authorize_sale_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'authorize_sale_object':
                        (AuthorizeSaleObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'authorize_sale_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.balance_inquiry_post_endpoint = _Endpoint(
            settings={
                'response_type': (BalanceInquiryResponseObject,),
                'auth': [],
                'endpoint_path': '/BalanceInquiry',
                'operation_id': 'balance_inquiry_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'balance_inquiry_object',
                ],
                'required': [
                    'balance_inquiry_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'balance_inquiry_object':
                        (BalanceInquiryObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'balance_inquiry_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.block_cancel_post_endpoint = _Endpoint(
            settings={
                'response_type': (BlockCancelResponseObject,),
                'auth': [],
                'endpoint_path': '/BlockCancel',
                'operation_id': 'block_cancel_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'block_cancel_object',
                ],
                'required': [
                    'block_cancel_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'block_cancel_object':
                        (BlockCancelObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'block_cancel_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.block_close_post_endpoint = _Endpoint(
            settings={
                'response_type': (BlockCloseResponseObject,),
                'auth': [],
                'endpoint_path': '/BlockClose',
                'operation_id': 'block_close_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'block_close_object',
                ],
                'required': [
                    'block_close_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'block_close_object':
                        (BlockCloseObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'block_close_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.block_create_post_endpoint = _Endpoint(
            settings={
                'response_type': (BlockCreateResponseObject,),
                'auth': [],
                'endpoint_path': '/BlockCreate',
                'operation_id': 'block_create_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'block_create_object',
                ],
                'required': [
                    'block_create_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'block_create_object':
                        (BlockCreateObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'block_create_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.cancel_post_endpoint = _Endpoint(
            settings={
                'response_type': (CancelResponseObject,),
                'auth': [],
                'endpoint_path': '/Cancel',
                'operation_id': 'cancel_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'cancel_object',
                ],
                'required': [
                    'cancel_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'cancel_object':
                        (CancelObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'cancel_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.capture_post_endpoint = _Endpoint(
            settings={
                'response_type': (CaptureResponseObject,),
                'auth': [],
                'endpoint_path': '/Capture',
                'operation_id': 'capture_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'capture_object',
                ],
                'required': [
                    'capture_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'capture_object':
                        (CaptureObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'capture_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.close_post_endpoint = _Endpoint(
            settings={
                'response_type': (CloseResponseObject,),
                'auth': [],
                'endpoint_path': '/Close',
                'operation_id': 'close_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'close_object',
                ],
                'required': [
                    'close_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'close_object':
                        (CloseObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'close_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.configure_post_endpoint = _Endpoint(
            settings={
                'response_type': (ConfigureResponseObject,),
                'auth': [],
                'endpoint_path': '/Configure',
                'operation_id': 'configure_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'configure_object',
                ],
                'required': [
                    'configure_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'configure_object':
                        (ConfigureObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'configure_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.confirm_post_endpoint = _Endpoint(
            settings={
                'response_type': (ConfirmResponseObject,),
                'auth': [],
                'endpoint_path': '/Confirm',
                'operation_id': 'confirm_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'confirm_object',
                ],
                'required': [
                    'confirm_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'confirm_object':
                        (ConfirmObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'confirm_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.debt_inquiry_post_endpoint = _Endpoint(
            settings={
                'response_type': (DebtInquiryResponseObject,),
                'auth': [],
                'endpoint_path': '/DebtInquiry',
                'operation_id': 'debt_inquiry_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'debt_inquiry_object',
                ],
                'required': [
                    'debt_inquiry_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'debt_inquiry_object':
                        (DebtInquiryObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'debt_inquiry_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.debt_payment_post_endpoint = _Endpoint(
            settings={
                'response_type': (DebtPaymentResponseObject,),
                'auth': [],
                'endpoint_path': '/DebtPayment',
                'operation_id': 'debt_payment_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'debt_payment_object',
                ],
                'required': [
                    'debt_payment_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'debt_payment_object':
                        (DebtPaymentObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'debt_payment_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.deposit_post_endpoint = _Endpoint(
            settings={
                'response_type': (DepositResponseObject,),
                'auth': [],
                'endpoint_path': '/Deposit',
                'operation_id': 'deposit_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'deposit_object',
                ],
                'required': [
                    'deposit_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'deposit_object':
                        (DepositObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'deposit_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.enable_service_post_endpoint = _Endpoint(
            settings={
                'response_type': (EnableServiceResponseObject,),
                'auth': [],
                'endpoint_path': '/EnableService',
                'operation_id': 'enable_service_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'enable_service_object',
                ],
                'required': [
                    'enable_service_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'enable_service_object':
                        (EnableServiceObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'enable_service_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.enrollment_post_endpoint = _Endpoint(
            settings={
                'response_type': (EnrollmentResponseObject,),
                'auth': [],
                'endpoint_path': '/Enrollment',
                'operation_id': 'enrollment_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'enrollment_object',
                ],
                'required': [
                    'enrollment_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'enrollment_object':
                        (EnrollmentObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'enrollment_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.get_block_post_endpoint = _Endpoint(
            settings={
                'response_type': (GetBlockResponseObject,),
                'auth': [],
                'endpoint_path': '/GetBlock',
                'operation_id': 'get_block_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'get_block_object',
                ],
                'required': [
                    'get_block_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'get_block_object':
                        (GetBlockObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'get_block_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.get_card_post_endpoint = _Endpoint(
            settings={
                'response_type': (GetCardResponseObject,),
                'auth': [],
                'endpoint_path': '/GetCard',
                'operation_id': 'get_card_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'get_card_object',
                ],
                'required': [
                    'get_card_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'get_card_object':
                        (GetCardObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'get_card_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.get_transaction_post_endpoint = _Endpoint(
            settings={
                'response_type': (GetTransactionResponseObject,),
                'auth': [],
                'endpoint_path': '/GetTransaction',
                'operation_id': 'get_transaction_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'get_transaction_object',
                ],
                'required': [
                    'get_transaction_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'get_transaction_object':
                        (GetTransactionObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'get_transaction_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.keep_alive_post_endpoint = _Endpoint(
            settings={
                'response_type': (KeepAliveResponseObject,),
                'auth': [],
                'endpoint_path': '/KeepAlive',
                'operation_id': 'keep_alive_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'keep_alive_object',
                ],
                'required': [
                    'keep_alive_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'keep_alive_object':
                        (KeepAliveObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'keep_alive_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.keys_renewal_post_endpoint = _Endpoint(
            settings={
                'response_type': (KeysRenewalObject,),
                'auth': [],
                'endpoint_path': '/KeysRenewal',
                'operation_id': 'keys_renewal_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'keys_renewal_object',
                ],
                'required': [
                    'keys_renewal_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'keys_renewal_object':
                        (KeysRenewalObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'keys_renewal_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.order_final_post_endpoint = _Endpoint(
            settings={
                'response_type': (OrderFinalResponseObject,),
                'auth': [],
                'endpoint_path': '/OrderFinal',
                'operation_id': 'order_final_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'order_final_object',
                ],
                'required': [
                    'order_final_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'order_final_object':
                        (OrderFinalObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'order_final_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.order_get_post_endpoint = _Endpoint(
            settings={
                'response_type': (OrderGetResponseObject,),
                'auth': [],
                'endpoint_path': '/OrderGet',
                'operation_id': 'order_get_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'order_get_object',
                ],
                'required': [
                    'order_get_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'order_get_object':
                        (OrderGetObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'order_get_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.order_initial_post_endpoint = _Endpoint(
            settings={
                'response_type': (OrderInitialResponseObject,),
                'auth': [],
                'endpoint_path': '/OrderInitial',
                'operation_id': 'order_initial_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'order_initial_object',
                ],
                'required': [
                    'order_initial_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'order_initial_object':
                        (OrderInitialObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'order_initial_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.order_status_post_endpoint = _Endpoint(
            settings={
                'response_type': (OrderStatusResponseObject,),
                'auth': [],
                'endpoint_path': '/OrderStatus',
                'operation_id': 'order_status_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'order_status_object',
                ],
                'required': [
                    'order_status_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'order_status_object':
                        (OrderStatusObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'order_status_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.payment_method_post_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentMethodResponseObject,),
                'auth': [],
                'endpoint_path': '/PaymentMethod',
                'operation_id': 'payment_method_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_method_object',
                ],
                'required': [
                    'payment_method_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'payment_method_object':
                        (PaymentMethodObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'payment_method_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.payment_methods_post_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentMethodsResponseObject,),
                'auth': [],
                'endpoint_path': '/PaymentMethods',
                'operation_id': 'payment_methods_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_methods_object',
                ],
                'required': [
                    'payment_methods_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'payment_methods_object':
                        (PaymentMethodsObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'payment_methods_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.query_companies_post_endpoint = _Endpoint(
            settings={
                'response_type': (QueryCompaniesResponseObject,),
                'auth': [],
                'endpoint_path': '/QueryCompanies',
                'operation_id': 'query_companies_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_companies_object',
                ],
                'required': [
                    'query_companies_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'query_companies_object':
                        (QueryCompaniesObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'query_companies_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.query_line_of_business_post_endpoint = _Endpoint(
            settings={
                'response_type': (QueryLineOfBusinessResponseObject,),
                'auth': [],
                'endpoint_path': '/QueryLineOfBusiness',
                'operation_id': 'query_line_of_business_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_line_of_business_object',
                ],
                'required': [
                    'query_line_of_business_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'query_line_of_business_object':
                        (QueryLineOfBusinessObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'query_line_of_business_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.return_post_endpoint = _Endpoint(
            settings={
                'response_type': (ReturnResponseObject,),
                'auth': [],
                'endpoint_path': '/Return',
                'operation_id': 'return_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'return_object',
                ],
                'required': [
                    'return_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'return_object':
                        (ReturnObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'return_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.sale_post_endpoint = _Endpoint(
            settings={
                'response_type': (SaleResponseObject,),
                'auth': [],
                'endpoint_path': '/Sale',
                'operation_id': 'sale_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'sale_object',
                ],
                'required': [
                    'sale_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'sale_object':
                        (SaleObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'sale_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.settlement_post_endpoint = _Endpoint(
            settings={
                'response_type': (SettlementResponseObject,),
                'auth': [],
                'endpoint_path': '/Settlement',
                'operation_id': 'settlement_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'settlement_object',
                ],
                'required': [
                    'settlement_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'settlement_object':
                        (SettlementObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'settlement_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.validate_post_endpoint = _Endpoint(
            settings={
                'response_type': (ValidateResponseObject,),
                'auth': [],
                'endpoint_path': '/Validate',
                'operation_id': 'validate_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'validate_object',
                ],
                'required': [
                    'validate_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'validate_object':
                        (ValidateObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'validate_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.void_debt_payment_post_endpoint = _Endpoint(
            settings={
                'response_type': (VoidDebtPaymentResponseObject,),
                'auth': [],
                'endpoint_path': '/VoidDebtPayment',
                'operation_id': 'void_debt_payment_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'void_debt_payment_object',
                ],
                'required': [
                    'void_debt_payment_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'void_debt_payment_object':
                        (VoidDebtPaymentObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'void_debt_payment_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.void_post_endpoint = _Endpoint(
            settings={
                'response_type': (VoidResponseObject,),
                'auth': [],
                'endpoint_path': '/Void',
                'operation_id': 'void_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'void_object',
                ],
                'required': [
                    'void_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'void_object':
                        (VoidObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'void_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.wallet_request_post_endpoint = _Endpoint(
            settings={
                'response_type': (WalletRequestResponseObject,),
                'auth': [],
                'endpoint_path': '/WalletRequest',
                'operation_id': 'wallet_request_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'wallet_request_object',
                ],
                'required': [
                    'wallet_request_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'wallet_request_object':
                        (WalletRequestObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'wallet_request_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.wallets_post_endpoint = _Endpoint(
            settings={
                'response_type': (WalletsResponseObject,),
                'auth': [],
                'endpoint_path': '/Wallets',
                'operation_id': 'wallets_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'wallets_object',
                ],
                'required': [
                    'wallets_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'wallets_object':
                        (WalletsObject,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'wallets_object': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )

    def authorize_sale_post(
        self,
        authorize_sale_object,
        **kwargs
    ):
        """Autorización de Venta sin Captura o Pre Autorización  # noqa: E501

        Si se desea enviar una compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.authorize_sale_post(authorize_sale_object, async_req=True)
        >>> result = thread.get()

        Args:
            authorize_sale_object (AuthorizeSaleObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AuthorizeSaleResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['authorize_sale_object'] = \
            authorize_sale_object
        return self.authorize_sale_post_endpoint.call_with_http_info(**kwargs)

    def balance_inquiry_post(
        self,
        balance_inquiry_object,
        **kwargs
    ):
        """Consulta de Saldo/Deuda de cuenta/Credencial  # noqa: E501

        Consulta de saldo, deuda de la cuenta asociada a la credencial o método de identificación utilizado.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.balance_inquiry_post(balance_inquiry_object, async_req=True)
        >>> result = thread.get()

        Args:
            balance_inquiry_object (BalanceInquiryObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BalanceInquiryResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['balance_inquiry_object'] = \
            balance_inquiry_object
        return self.balance_inquiry_post_endpoint.call_with_http_info(**kwargs)

    def block_cancel_post(
        self,
        block_cancel_object,
        **kwargs
    ):
        """Cancelación del último bloque de transacciones realizadas.  # noqa: E501

        Luego de realizar una serie de operaciones de compra/autorización, anulación y/o devolución, y haber procesado correctamente cada una de las respuestas, estas operaciones se realizaron con esta funcionalidad activada (es decir, enviando un Número de bloque a la cual asociar estas operaciones), se debe enviar una confirmación, para asi eliminar las reversas que se encuentran pendientes de envio en caso de que el punto de venta decida deshacer la venta completa por el motivo que sea, o una cancelación, para asi enviar esas reversas pendientes y asi deshacerlas por completo. Si el punto de venta envia un nuevo Número de bloque confirmar o cancelar previamente el anterior, la Plataforma procederá a confirmar o cancelar automaticamente el bloque de transacciones pendientes, según como haya sido configurado para actuar en este escenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.block_cancel_post(block_cancel_object, async_req=True)
        >>> result = thread.get()

        Args:
            block_cancel_object (BlockCancelObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BlockCancelResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['block_cancel_object'] = \
            block_cancel_object
        return self.block_cancel_post_endpoint.call_with_http_info(**kwargs)

    def block_close_post(
        self,
        block_close_object,
        **kwargs
    ):
        """Confirmación del último bloque de transacciones realizadas.  # noqa: E501

        Luego de realizar una serie de operaciones de compra/autorización, anulación y/o devolución, y haber procesado correctamente cada una de las respuestas, estas operaciones se realizaron con esta funcionalidad activada (es decir, enviando un número de bloque a la cual asociar estas operaciones), se debe enviar una confirmación, para asi eliminar las reversas que se encuentran pendientes de envío en caso de que el punto de venta decida deshacer la venta completa por el motivo que sea, o una cancelación, para así enviar esas reversas pendientes y deshacerlas por completo. Si el punto de venta envía un nuevo número de bloque confirmar o cancelar previamente el anterior, la Plataforma procederá a confirmar o cancelar automáticamente el bloque de transacciones pendientes, segín como haya sido configurado para actuar en este escenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.block_close_post(block_close_object, async_req=True)
        >>> result = thread.get()

        Args:
            block_close_object (BlockCloseObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BlockCloseResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['block_close_object'] = \
            block_close_object
        return self.block_close_post_endpoint.call_with_http_info(**kwargs)

    def block_create_post(
        self,
        block_create_object,
        **kwargs
    ):
        """Crea un Identificador de Bloque-Block de transacciones.  # noqa: E501

        Operación utilizada para crear un Bloque de transacciones, esta operación se ejecuta en forma implícita en cualquier operación que Contenga el atributo <b>Block</b> sin valor en el requirimiento. Utilizado por sistemas que no poseen un identificador único de su operación.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.block_create_post(block_create_object, async_req=True)
        >>> result = thread.get()

        Args:
            block_create_object (BlockCreateObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BlockCreateResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['block_create_object'] = \
            block_create_object
        return self.block_create_post_endpoint.call_with_http_info(**kwargs)

    def cancel_post(
        self,
        cancel_object,
        **kwargs
    ):
        """Cancela una Transacción en Curso, Inciada con un GetCard/WalletRequest.  # noqa: E501

        Se utiliza para cancelar una Operación en la cual la Plataforma posee el control del dispositivo de lectura, y ya no desea continuar con la transacción. Utilizado despúes de ejecutar GetCard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_post(cancel_object, async_req=True)
        >>> result = thread.get()

        Args:
            cancel_object (CancelObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CancelResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['cancel_object'] = \
            cancel_object
        return self.cancel_post_endpoint.call_with_http_info(**kwargs)

    def capture_post(
        self,
        capture_object,
        **kwargs
    ):
        """Confirmación de un consumo previo.  # noqa: E501

        Operación de confirmación de una autorización sin Captura del tipo Authorize realizada previamente (normalmente en Operaciones de Checking-Checkout).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.capture_post(capture_object, async_req=True)
        >>> result = thread.get()

        Args:
            capture_object (CaptureObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CaptureResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['capture_object'] = \
            capture_object
        return self.capture_post_endpoint.call_with_http_info(**kwargs)

    def close_post(
        self,
        close_object,
        **kwargs
    ):
        """Utilizada por el POS para indicar que finalizo su sesion.  # noqa: E501

        Con esta operación el POS esta indicando a la plataforma que finaliza su session de Trabajo, la misma se reinicia con cuialquier nueva operación enviada por el POS.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.close_post(close_object, async_req=True)
        >>> result = thread.get()

        Args:
            close_object (CloseObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CloseResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['close_object'] = \
            close_object
        return self.close_post_endpoint.call_with_http_info(**kwargs)

    def configure_post(
        self,
        configure_object,
        **kwargs
    ):
        """Permite crear configuración en Plataforma  # noqa: E501

        Al ejecutar esta operación se permite que Plataforma cree el Dispositivo físico ( PINPAD ) en sus tablas de configuración y lo asocie al Aplicativo-Empresa-Sucursal-Caja.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.configure_post(configure_object, async_req=True)
        >>> result = thread.get()

        Args:
            configure_object (ConfigureObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ConfigureResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['configure_object'] = \
            configure_object
        return self.configure_post_endpoint.call_with_http_info(**kwargs)

    def confirm_post(
        self,
        confirm_object,
        **kwargs
    ):
        """Confirmación de la última operación realizada.  # noqa: E501

        Luego de realizar una operación de compra/autorización, anulación o devolución, y haber procesado correctamente la respuesta, se debe enviar una confirmación, de forma de eliminar la reversa que se encuentra pendiente de envío en caso de que esa respuesta no sea procesada por el punto de venta o no llegue a su destino.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.confirm_post(confirm_object, async_req=True)
        >>> result = thread.get()

        Args:
            confirm_object (ConfirmObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ConfirmResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['confirm_object'] = \
            confirm_object
        return self.confirm_post_endpoint.call_with_http_info(**kwargs)

    def debt_inquiry_post(
        self,
        debt_inquiry_object,
        **kwargs
    ):
        """Consulta de Deuda de cuenta/credencial  # noqa: E501

        Consulta de saldo, deuda de la cuenta asociada a la credencial o método de identificación utilizado.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.debt_inquiry_post(debt_inquiry_object, async_req=True)
        >>> result = thread.get()

        Args:
            debt_inquiry_object (DebtInquiryObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DebtInquiryResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['debt_inquiry_object'] = \
            debt_inquiry_object
        return self.debt_inquiry_post_endpoint.call_with_http_info(**kwargs)

    def debt_payment_post(
        self,
        debt_payment_object,
        **kwargs
    ):
        """Pago de Deuda, Resumen de Cuenta o Saldo.  # noqa: E501

        Pago de Deuda, Resumen de Cuenta o Saldo.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.debt_payment_post(debt_payment_object, async_req=True)
        >>> result = thread.get()

        Args:
            debt_payment_object (DebtPaymentObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DebtPaymentResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['debt_payment_object'] = \
            debt_payment_object
        return self.debt_payment_post_endpoint.call_with_http_info(**kwargs)

    def deposit_post(
        self,
        deposit_object,
        **kwargs
    ):
        """Confirmación de un consumo previo.  # noqa: E501

        Operación de confirmación de una autorización sin Captura del tipo Authorize realizada previamente (normalmente en Operaciones de Checking-Checkout ).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.deposit_post(deposit_object, async_req=True)
        >>> result = thread.get()

        Args:
            deposit_object (DepositObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DepositResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['deposit_object'] = \
            deposit_object
        return self.deposit_post_endpoint.call_with_http_info(**kwargs)

    def enable_service_post(
        self,
        enable_service_object,
        **kwargs
    ):
        """Permite Habilitar el uso de un Servicio  # noqa: E501

        Esta operación es solamente utilizada para habilitar un Servicio  para la cadena Comercial, la Sucursal o la Terminal.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.enable_service_post(enable_service_object, async_req=True)
        >>> result = thread.get()

        Args:
            enable_service_object (EnableServiceObject): Objeto que contendrá los datos del Requerimiento para Habilitar un Servicio.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            EnableServiceResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['enable_service_object'] = \
            enable_service_object
        return self.enable_service_post_endpoint.call_with_http_info(**kwargs)

    def enrollment_post(
        self,
        enrollment_object,
        **kwargs
    ):
        """Suscripción al servicio de pagos Tokenizados y pagos recurrentes.  # noqa: E501

        Si se desea enviar una compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.enrollment_post(enrollment_object, async_req=True)
        >>> result = thread.get()

        Args:
            enrollment_object (EnrollmentObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            EnrollmentResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['enrollment_object'] = \
            enrollment_object
        return self.enrollment_post_endpoint.call_with_http_info(**kwargs)

    def get_block_post(
        self,
        get_block_object,
        **kwargs
    ):
        """Recupera los identificadores de las transacciones que  lo componen.  # noqa: E501

        Luego de realizar una serie de operaciones de compra/autorización, anulación y/o devolución, y haber procesado correctamente cada una de las respuestas, estas operaciones se realizaron con esta funcionalidad activada (es decir, enviando un Número de bloque a la cual asociar estas operaciones), se debe enviar una confirmación, para asi eliminar las reversas que se encuentran pendientes de envio en caso de que el punto de venta decida deshacer la venta completa por el motivo que sea, o una cancelación, para asi enviar esas reversas pendientes y asi deshacerlas por completo. Si el punto de venta envía un nuevo Número de bloque confirmar o cancelar previamente el anterior, La Plataforma procederá a confirmar o cancelar automáticamente el bloque de transacciones pendientes, según como haya sido configurado para actuar en este escenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_block_post(get_block_object, async_req=True)
        >>> result = thread.get()

        Args:
            get_block_object (GetBlockObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GetBlockResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['get_block_object'] = \
            get_block_object
        return self.get_block_post_endpoint.call_with_http_info(**kwargs)

    def get_card_post(
        self,
        get_card_object,
        **kwargs
    ):
        """Solicitud de Lectura del Medio de Pago  # noqa: E501

        Utilizada solamente en el caso de que el Aplicativo Integrado no tenga el control  del Lector y el mismo esté en control de la Plataforma.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_card_post(get_card_object, async_req=True)
        >>> result = thread.get()

        Args:
            get_card_object (GetCardObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GetCardResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['get_card_object'] = \
            get_card_object
        return self.get_card_post_endpoint.call_with_http_info(**kwargs)

    def get_transaction_post(
        self,
        get_transaction_object,
        **kwargs
    ):
        """Recupera los datos de la transacción especificada.   # noqa: E501

        Recupera todos los datos de la transacción referenciada por el elemento OrigAnswerKey.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_post(get_transaction_object, async_req=True)
        >>> result = thread.get()

        Args:
            get_transaction_object (GetTransactionObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GetTransactionResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['get_transaction_object'] = \
            get_transaction_object
        return self.get_transaction_post_endpoint.call_with_http_info(**kwargs)

    def keep_alive_post(
        self,
        keep_alive_object,
        **kwargs
    ):
        """Mensaje que informa si está disponible el Servicio Authorize.  # noqa: E501

        Luego de realizar una serie de operaciones de compra/autorización, anulación y/o devolución, y haber procesado correctamente cada una de las respuestas, estas operaciones se realizaron con esta funcionalidad activada (es decir, enviando un Número de bloque a la cual asociar estas operaciones), se debe enviar una confirmación, para asi eliminar las reversas que se encuentran pendientes de envío en caso de que el punto de venta decida deshacer la venta completa por el motivo que sea, o una cancelación, para así enviar esas reversas pendientes y deshacerlas por completo. Si el punto de venta envía un nuevo Número de bloque confirmar o cancelar previamente el anterior, el Plataforma procederá a confirmar o cancelar automáticamente el bloque de transacciones pendientes, según como haya sido configurado para actuar en este escenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.keep_alive_post(keep_alive_object, async_req=True)
        >>> result = thread.get()

        Args:
            keep_alive_object (KeepAliveObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            KeepAliveResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['keep_alive_object'] = \
            keep_alive_object
        return self.keep_alive_post_endpoint.call_with_http_info(**kwargs)

    def keys_renewal_post(
        self,
        keys_renewal_object,
        **kwargs
    ):
        """Renovacion de Llaves  # noqa: E501

        Renovacion de llaves  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.keys_renewal_post(keys_renewal_object, async_req=True)
        >>> result = thread.get()

        Args:
            keys_renewal_object (KeysRenewalObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            KeysRenewalObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['keys_renewal_object'] = \
            keys_renewal_object
        return self.keys_renewal_post_endpoint.call_with_http_info(**kwargs)

    def order_final_post(
        self,
        order_final_object,
        **kwargs
    ):
        """Reclamar el estatus de la operación de compra.  # noqa: E501

        Con está operación se puede obtener el status de la operación de compra iniciada con PaymentInital. Si la compra ya ha sido liquidada por el cliente o no.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.order_final_post(order_final_object, async_req=True)
        >>> result = thread.get()

        Args:
            order_final_object (OrderFinalObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OrderFinalResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['order_final_object'] = \
            order_final_object
        return self.order_final_post_endpoint.call_with_http_info(**kwargs)

    def order_get_post(
        self,
        order_get_object,
        **kwargs
    ):
        """Recuperar la operación iniciada por el comercio, para su compra.  # noqa: E501

        Con este método el cliente podrá recuperar los datos para realizar la compra de un producto o servicio y posteriormente ejecutar la compra con la operación Sale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.order_get_post(order_get_object, async_req=True)
        >>> result = thread.get()

        Args:
            order_get_object (OrderGetObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OrderGetResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['order_get_object'] = \
            order_get_object
        return self.order_get_post_endpoint.call_with_http_info(**kwargs)

    def order_initial_post(
        self,
        order_initial_object,
        **kwargs
    ):
        """Indica el inicio de una operación de venta.  # noqa: E501

        Con esta operación el comercio deberá indicar un inicio de transación de venta, mandando toda la información al switch, donde posteriormente el cliente deberá recuperar para realizar la compra.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.order_initial_post(order_initial_object, async_req=True)
        >>> result = thread.get()

        Args:
            order_initial_object (OrderInitialObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OrderInitialResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['order_initial_object'] = \
            order_initial_object
        return self.order_initial_post_endpoint.call_with_http_info(**kwargs)

    def order_status_post(
        self,
        order_status_object,
        **kwargs
    ):
        """Recuperación del Estado de una Transacción Iniciada por el OrderInitial.  # noqa: E501

        Si se desea recuperar el estado de una transacción iniciada, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.order_status_post(order_status_object, async_req=True)
        >>> result = thread.get()

        Args:
            order_status_object (OrderStatusObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OrderStatusResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['order_status_object'] = \
            order_status_object
        return self.order_status_post_endpoint.call_with_http_info(**kwargs)

    def payment_method_post(
        self,
        payment_method_object,
        **kwargs
    ):
        """Consulta de  \"planes\" financieros para un Medio de Pago.  # noqa: E501

        Los Planes financieros indican cuotas, diferimiento, monedas, rangos de importe, modos de ingreso y otros atributos de configuración permitidos. Utilizado si se desea conocer los planes financieros relaciónados a un número de tarjeta/Token/Identificador Alternativo especificado. Si es un número de Tarjeta, el mismo podrá estar enmascarado.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.payment_method_post(payment_method_object, async_req=True)
        >>> result = thread.get()

        Args:
            payment_method_object (PaymentMethodObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PaymentMethodResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['payment_method_object'] = \
            payment_method_object
        return self.payment_method_post_endpoint.call_with_http_info(**kwargs)

    def payment_methods_post(
        self,
        payment_methods_object,
        **kwargs
    ):
        """Consulta de los Medios de Pago  disponibles.  # noqa: E501

        Utilizado para obtener la lista de los medios de pagos disponibles, para quien está realizando el requerimiento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.payment_methods_post(payment_methods_object, async_req=True)
        >>> result = thread.get()

        Args:
            payment_methods_object (PaymentMethodsObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PaymentMethodsResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['payment_methods_object'] = \
            payment_methods_object
        return self.payment_methods_post_endpoint.call_with_http_info(**kwargs)

    def query_companies_post(
        self,
        query_companies_object,
        **kwargs
    ):
        """Consulta de Empresas para el Pago de Servicios o Deuda  # noqa: E501

        Esta operación Entrega la Lista de Empresas o Servicios que pueden ser pagados por la plataforma.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query_companies_post(query_companies_object, async_req=True)
        >>> result = thread.get()

        Args:
            query_companies_object (QueryCompaniesObject): Objeto que contendrá los datos del Requerimiento para obtener la lista de Empresas.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            QueryCompaniesResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['query_companies_object'] = \
            query_companies_object
        return self.query_companies_post_endpoint.call_with_http_info(**kwargs)

    def query_line_of_business_post(
        self,
        query_line_of_business_object,
        **kwargs
    ):
        """Consulta de Rubros de Empresas para el Pago de Servicios o Deuda  # noqa: E501

        Esta operación entrega la Lista de Rubros que pueden ser pagados por la plataforma.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query_line_of_business_post(query_line_of_business_object, async_req=True)
        >>> result = thread.get()

        Args:
            query_line_of_business_object (QueryLineOfBusinessObject): Objeto que contendrá los datos del Requerimiento para obtener la lista de Rubros.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            QueryLineOfBusinessResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['query_line_of_business_object'] = \
            query_line_of_business_object
        return self.query_line_of_business_post_endpoint.call_with_http_info(**kwargs)

    def return_post(
        self,
        return_object,
        **kwargs
    ):
        """Realización de una devolución de operación de compra/autorización.  # noqa: E501

        Si se desea enviar una devolución de compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_post(return_object, async_req=True)
        >>> result = thread.get()

        Args:
            return_object (ReturnObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ReturnResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['return_object'] = \
            return_object
        return self.return_post_endpoint.call_with_http_info(**kwargs)

    def sale_post(
        self,
        sale_object,
        **kwargs
    ):
        """Realización de una compra/Autorización de compra  # noqa: E501

        Si se desea enviar una compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sale_post(sale_object, async_req=True)
        >>> result = thread.get()

        Args:
            sale_object (SaleObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SaleResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['sale_object'] = \
            sale_object
        return self.sale_post_endpoint.call_with_http_info(**kwargs)

    def settlement_post(
        self,
        settlement_object,
        **kwargs
    ):
        """Confirmación de un consumo previo.  # noqa: E501

        Operación de confirmación de una autorización sin Captura realizada previamente por la Operación Authorize/AuthorizeSale realizada. (Normalmente en Operaciones de Checking-Checkout). Las Operaciones Settlement, Deposit y Capure son sinómimos, pueden usarse cualquiera de ellas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.settlement_post(settlement_object, async_req=True)
        >>> result = thread.get()

        Args:
            settlement_object (SettlementObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SettlementResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['settlement_object'] = \
            settlement_object
        return self.settlement_post_endpoint.call_with_http_info(**kwargs)

    def validate_post(
        self,
        validate_object,
        **kwargs
    ):
        """Realización de una Validación  # noqa: E501

        Si se desea enviar una compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.validate_post(validate_object, async_req=True)
        >>> result = thread.get()

        Args:
            validate_object (ValidateObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ValidateResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['validate_object'] = \
            validate_object
        return self.validate_post_endpoint.call_with_http_info(**kwargs)

    def void_debt_payment_post(
        self,
        void_debt_payment_object,
        **kwargs
    ):
        """Cancelación de  Pago de Deuda, Saldo o Resumen.  # noqa: E501

        Operación utilizada para anular un Pago de Deuda realizado previamente.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.void_debt_payment_post(void_debt_payment_object, async_req=True)
        >>> result = thread.get()

        Args:
            void_debt_payment_object (VoidDebtPaymentObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            VoidDebtPaymentResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['void_debt_payment_object'] = \
            void_debt_payment_object
        return self.void_debt_payment_post_endpoint.call_with_http_info(**kwargs)

    def void_post(
        self,
        void_object,
        **kwargs
    ):
        """Operación de Cancelación/Anulación.  # noqa: E501

        Esta operación actúa como un comodín. Cuando el Plataforma procesa un requerimiento de este tipo, dependiendo del tipo de operación original a la que se refiera, del estado de ella, y algunos parámetros más, se enviará finalmente una devolución o una anulación. La forma en la que este tipo de requerimiento opera es la siguiente: si la operación se encuentra abierta (sin haber sido enviado el cierre de lote) y la operación proviene del mismo número de terminal con la cual se realizó la operación original, finalmente la transacción financiera que se enviará al host será una anulación. Por el contrario, si alguna de las condiciones anteriores no se cumple, se realizará una devolución total de la operación original. En ese caso, se debe cumplir que no haya sido devuelta de forma parcial anteriormente. Vale aclarar también que si se el resultado es una anulación, la transacción original podrá ser una compra/autorización, una devolución o un pago de resumen. Sin embargo, si es una devolución, la original solo podrá ser una compra/autorización. Para cualquier otro escenario donde algo de ello no se cumpla, la petición será rechazada.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.void_post(void_object, async_req=True)
        >>> result = thread.get()

        Args:
            void_object (VoidObject): Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            VoidResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['void_object'] = \
            void_object
        return self.void_post_endpoint.call_with_http_info(**kwargs)

    def wallet_request_post(
        self,
        wallet_request_object,
        **kwargs
    ):
        """Inicia un transacción contra el Wallet  # noqa: E501

        Esta operación sera utilizada para obtener el código o método de identificación del Wallet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.wallet_request_post(wallet_request_object, async_req=True)
        >>> result = thread.get()

        Args:
            wallet_request_object (WalletRequestObject): Objeto que contendrá los datos del Requerimiento para obtener el Requerimeinto del Wallet.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            WalletRequestResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['wallet_request_object'] = \
            wallet_request_object
        return self.wallet_request_post_endpoint.call_with_http_info(**kwargs)

    def wallets_post(
        self,
        wallets_object,
        **kwargs
    ):
        """Obtiene la Lista de Wallets Disponibles  # noqa: E501

        Esta operación es solamente utilizada para obtener la lista de Wallets con las cuales el sistema puede operar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.wallets_post(wallets_object, async_req=True)
        >>> result = thread.get()

        Args:
            wallets_object (WalletsObject): Objeto que contendrá los datos del Requerimiento para obtener los Wallets disponibles.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            WalletsResponseObject
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['wallets_object'] = \
            wallets_object
        return self.wallets_post_endpoint.call_with_http_info(**kwargs)

