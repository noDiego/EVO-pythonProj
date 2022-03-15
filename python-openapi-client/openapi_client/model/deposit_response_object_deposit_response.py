"""
    EVO Payment API

    <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 32px;\">API de Pagos</h1> <br /><br /> <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 24px;\">Descripción del Servicio</h1> <p style=\"color:#004785;\"><b><u>Documentación en formato OpenAPI 3.0</b></u></p> <br/> Contrato especificado según especificaciones https://www.openapis.org/ y https://swagger.io/.<br /><br />  En el site https://editor.swagger.io/ se dispone de un  Viewer, Editor y  Generar de Código ( SDK ) para varios lenguajes de programación; incluyendo JAVA, C#, C++, Perl, Node.js, GO, PHP, Ruby y otros.<br/><br/> Para <b>ver</b> la documentación o <b>generar</b> código de la librería cliente o SDK  se deberá selecciónar en el menú horizontal  la opción <b>File</b>, en el menú vertical que se depliega la opción <b>Import File</b> y luego se deberá selecciónar el archivo del contrato deseado, ya sea  extensión <b>.json</b> o <b>.yaml</b>. <br/><br/> Además se puede generar el código de la librería cliente desde la línea de comandos a través de la herramienta  <b>CLI</b>  de  <b>OpenAPI Generator</b>. Esta presenta generadores de SDK en mayor variedad de lenguajes de programación.  En el site https://openapi-generator.tech/docs/installation se documenta cómo  <b>instalar</b> la herramienta CLI.<br/><br/> Los clientes generados contienen, adicionalmente al código,  la documentación de uso del mismo en <b>README.md</b>, como también en el subdirectorio <b>docs</b> toda la documentación del API o servicio y sus operaciones, con el detalle de los  campos o elementos y su dominio.<br /><br /><br /><br /> <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 24px;\">Notas a tener en cuenta para realizar la Integración</h1><br/> <p style=\"color:#004785;\"><b><u>Conceptos y/ Mecanismos relevantes Soportados por el Protocolo de Integración</u></b></p> <br/><br/> <span>&#8226;</span> <b>Interpretración de las Respuesta</b>,<br /><br/> El único campo que indica si la transacción fue aprobada, rechazada, o tienen algun error, es el elemento de las respuestas llamado <b>ResponseActions</b>, el  cual es un <b>ARRAY</b> de valores. Cada uno de estos indica una acción a realizar. Los elementos <b>ResponseCode</b>  y <b>ResponseMessage</b> son solamente informativos y por lo tanto no deben usarse para tomar acciones y los mismos pueden cambiar en base a la configuración de la Plataforma.<br/><br/> <span>&#8226;</span> <b>Bloque de transacciones</b>, permite Confirmar o Cancelar/Revertir todas las transacciones que forman parte de un bloque. <br/><br/> El POS puede definir un bloque o conjunto de transacciones simplemente indicando en todas ellas el mismo valor en el atributo/elemento/campo opcional llamado <b>Block</b>.<br/>  La operación <b>BlockCancel</b>, permite que el POS pueda solicitar a la plataforma la reversión y/o cancelación de todo el bloque de transacciones .<br/> La operación <b>BlockClose</b>, confirma todas las transacciones que forman parte del bloque especificado.<br/> Si el POS no posee un identificador unívoco de la transacción de venta, al momento de interactuar contra la plataforma podrá obtener uno con la operación  <b>BlockCreate</b>. Si el elemento o campo <b>Block</b>  existe y su contenido es Vacío o Nulo la plataforma realiza un <b>BlockCreate</b> automáticamente.<br /><br/> <span>&#8226;</span> <b>Reversas por Ruptura de Secuencia</b>. Evita la necesidad de persistir datos de la reversa y ahorra una transacción en el flujo.<br/>   El método llamado de ruptura de secuencia es utilizado para detectar los casos en los cuales el POS o Caja no pudo recibir una respuesta del mismo o no pudo procesarla adecuadamente. De esta forma permite a la misma reversar la transacción que no pudo procesar el POS o recibir la respuesta si fuese necesario.     En todo requerimiento el POS debe enviar el campo/elemento Sequence, con el valor recibido en el anterior requerimiento o vacío en el primero.    La plataforma  genera una nueva secuencia solamente cuando el requerimiento realizado es reversible o cuando se produce una ruptura.  Por lo tanto los comandos en los cuales la plataforma  genera una nueva secuencia son <b>Sale</b>, <b>Void</b>, <b>Authorize*</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b>, <b>Confirm</b>, <b>Close</b> y <b>Cancel</b>.    En caso de que la plataforma reverse el requerimiento previo retornará en la respuesta los siguiente campos o elementos.   <blockquote><b>WasReversePrevious</b>, con valor <b>1</b><br/>   <b>ReversedAnswerKey</b> conteniendo el <b>AnswerKey</b> de la transacción reversada<br/>   <b>ReversedSequence</b> conteniendo el <b>Sequence </b>de la transacción reversada</blockquote>    En caso de que la plataforma no reverse el requerimiento previo retornará los siguientes campos o elementos <blockquote><b>WasReversePrevious</b>, con valor <b>0</b></blockquote> <br/> <span>&#8226;</span> <b>Reversas Tradicionales</b>. El POS debe repetir el mismo requerimiento adicionando el atributo/elemento <b>IsReverse</b> con valor <b>1</b>.  Se debe tener en cuenta que en esta modalidad la plataforma no retorna los siguientes atributos/elementos.    <blockquote>   <b>WasReversePrevious</b><br/>   <b>ReversedAnswerKey</b><br/>   <b>ReversedSequence</b>   </blockquote>    <span>&#8226;</span> <b>Transacción Opcional de Confirmación</b>, ya que el mecanismo anterior permite que cada transacción Reverse o Confirme la anterior.<br/><br/> <span>&#8226;</span> <b>La Plataforma indica siempre las acciones que se deben realizar</b><br/><br/> <span>&#8226;</span><span>&#8226;</span> <b>Solicitar datos adicionales</b> ( <b>RequiredInformation</b> ), indicando no sólo cuáles son, sino también de qué tipo, valor  inicial, patrón de validación, si son mandatorios o no, qué Label se presenta al usuario, qué ayuda se presenta al usuario, etc.<br/> <span>&#8226;</span><span>&#8226;</span> <b>Mostrar Mensajes en Pantalla</b>. <span>&#8226;</span><span>&#8226;</span> <b>Imprimir Tickets</b>, ya sea en papel o capturar digitalmente el mismo, como así también el Layout de los mismos.<br/><br/><br/> <span>&#8226;</span> <b>Compresión de la trama</b> en base a codificación de los campos numéricos, string siempre de longitud variable, uso de sinónimos en los  campos, para que el programador programe usando los nombres largos y en el transporte se usen sus sinónimos cortos. <br/> <br/> <span>&#8226;</span> <b>Seguridad de los Datos Sensibles y de la Transaccion</b>, El elemento <b>Security</b> debera estar presente solo si los datos sensibles <b>CardNumber</b>, <b>ExpDate</b>, <b>PIN</b>, <b>Track1</b>, <b>Track2</b>, <b>SecurityCode</b> y  <b>CardCryptogram</b> deban ser envidos encriptados y por lo tanto este le elemento nos permite indicar el metodo de encriptacion utilizado y los datos adicionales que sean requeridos por la encriptacion. Si por ejemplo fuese el elemento PIN usando DUKPT y el resto de los datos sencible Track1, Track2 y SecurityCode, se deberian enviar  de la siguiente forma: </br>        \"Security” :  [         {           \"Type\": \"PIN\",           \"Values\":  [               {                    \"Name\": \"Method\",                   \"Value\": \"DUKPT\"               },               {                    \"Name\": \"KSN\",                   \"Value\": \"1234567890ABCDEF\"               },               {                    \"Name\": \"CRC32\",                   \"Value\": \"12345\"               },               {                    \"Name\": \"PlainTextLength\",                   \"Value\": \"4\"               },               {                    \"Name\": \"CipherCounter\",                   \"Value\": \"123\"               },               {                    \"Name\": \"ConsecutiveFailedCiphersCounter\",                   \"Value\": \"123\"               },               {                    \"Name\": \"Data\",                   \"Value\": \"01234567890123456\"               }           ]          },         {           \"Type\": \"SensitiveData\",           \"Values\":  [               {                    \"Name\": \"Method\",                   \"Value\": \"DUKPT-eGlobal\"               },               {                    \"Name\": \"KSN\",                   \"Value\": \"1234567890ABCDEF\"               },               {                    \"Name\": \"Track1CRC32\",                   \"Value\": \"12345\"               },               {                    \"Name\": \"Track2CRC32\",                   \"Value\": \"12345\"               },               {                    \"Name\": \"Track1Length\",                   \"Value\": \"79\"               },               {                    \"Name\": \"Track2Length\",                   \"Value\": \"37\"               },               {                    \"Name\": \"SecurityCodeLength\",                   \"Value\": \"3\"               },               {                    \"Name\": \"CipherCounter\",                   \"Value\": \"123\"               },               {                    \"Name\": \"ConsecutiveFailedCiphersCounter\",                   \"Value\": \"123\"               },               {                    \"Name\": \"Data\",                   \"Value\": \"1ahbcd23412345123412b213b1324b1234b2134b2134132b4123b23\"               }           ]          },         {           \"Type\": \"3DSecure\",           \"Values\":  [               {                    \"Name\": \"Method\",                   \"Value\": \"3DS-SNAP\"               },               {                                           \"Name\":  \"TransactionStatus\",                   \"Value\": \"SuccessfullyAuthenticated\"               },               {                                           \"Name\":  \"AuthenticationECI\",                   \"Value\": \"05\"               },               {                                           \"Name\":  \"IsChallengeMandated\",                   \"Value\": \"false\"               },               ...               {                                           \"Name\":  \"AcsReferenceNumber\",                   \"Value\": \"3DS_LOA_ACS_PPFU_020100_00009\"               },               {                    \"Name\":  \"ProcessedAsDataOnly\",                   \"Value\": \"false\"               }           ]          }               ] </br> Para el caso de DUKPT-eGlobal, <b>Track2</b>, <b>SecurityCode</b> y <b>Track1</b> se cifraran formando parte del mismo Bloque, El mismo se debera formar con el Track2 ( reemplazando el signo = por el digito D ) completandolo hasta los 38 digitos con el digito F, luego el  SecurityCode completandolo hasta 10 digitos y por ultimo el Track1 padeado completando el bloque  de los 208 digitos.  </br> Este elemento <b>Security</b> sera utilizado para enviar cualquier dato de autenticacion del pagador por ejemplo 3DSecure, para el caso de que el proveedor de la Autenticacion sea SNAP se deberan contener como valores todos los elementos definidos en el objeto <b>ThreeDSInformation</b>.     </br> Este mecanismo podra utilizarse en el futuro para encriptar otros datos que sean sensibles pero no del medio de pago, si no de las personas. </br> <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 24px;\">Log de Cambios</h1></br> <span>&#8226;</span> <b>Versión 5.6.1</b> <span>&#8226;</span><span>&#8226;</span> Se añade el campo <b>MerchantCategory</b> en las respuestas de todas las transacciones. Sólo se enviará en caso de que la categoría de la compañia exista.</br> <span>&#8226;</span> <b>Versión 5.6.0</b> <span>&#8226;</span><span>&#8226;</span> Los campos <b>ResponseCode</b>, <b>ResponseMessage</b> y <b>ResponseActions</b> son <b>obligatorios</b> en las respuestas de todas las transacciones.</br> <span>&#8226;</span> <b>Versión 5.5.7</b> <span>&#8226;</span><span>&#8226;</span> Se añade el elemento <b>Notification</b>. El mismo se encuentra dentro de <b>SaleResponse</b> y <b>AuthorizeSaleResponse</b>. Notificación a generar alertas vía e-mail.</br> <span>&#8226;</span> <b>Versión 5.5.6</b> <span>&#8226;</span><span>&#8226;</span> Se añaden los elementos <b>CardAppLabel</b>, <b>CardAuthRequestCryptogram</b> y <b>CardAuthResponseCryptogram</b>, para facilitar el analisis de los POS y ReadingDevices, el contenido de dichos elementos se encontraba en Tag de los elementos CardCryptogram y CardCryptogramResponse.</br> <span>&#8226;</span>  <b>Versión 5.5.5</b> <span>&#8226;</span><span>&#8226;</span> Se modifican los elementos <b>AuthorizeSale</b> y <b>AuthorizeSaleResponse</b> para su correcta documentación. Además, se añade el campo <b>ReadingDeviceOperatingFrom</b> el cual indica desde cuando se encuentra operativo o encendido el dispositivo</br> <span>&#8226;</span> <b>Versión 5.5.4</b> <span>&#8226;</span><span>&#8226;</span> Se renombra el atributo <b>ReasonReverse</b> a <b>ReverseReason</b>. Dicho campo permite notificar en las Reversas la razón por la cual fue necesario generarla.</br> <span>&#8226;</span> <b>Versión 5.5.3</b> <span>&#8226;</span><span>&#8226;</span> Se agregan atributos al elemento <b>Configuration</b> para la operación <b>PaymentMethod</b>. Por otra parte, se añade el mismo en todas las operaciones donde no se encontraba documentado. </br><b>• Versión 5.5.2</b> <span>&#8226;</span><span>&#8226;</span> Se Agrega el elemento <b>Payer</b> con los datos del Pagador. Originalmente hasta esta version se envian los mismos en el elemento <b>Customer</b>, pero desde ahora se permite que se informen personas ( fisicas y juridicas ) como cliente comprador y como pagador. Si el elemento <b>Payer</b> no esta presente se tomaran los datos del elemento <b>Customer</b>. Se da soporte al Tipo de Ticket Payer.</br> <span>&#8226;</span> <b>Versión 5.5.1</b> </br> <span>&#8226;</span><span>&#8226;</span> Se completa la documentacion de los Elementos <b>Seller</b> y <b>Customer</b>, agregandose los atributos <b>City</b> y  <b>AbbreviatedName</b>.<br/>   <span>&#8226;</span><span>&#8226;</span> Se unifica la definicion del Elemento  <b>Customer</b> .<br/>   <span>&#8226;</span><span>&#8226;</span> Se agrega el Elemento <b>PaymentFacilitatorID</b> para indicar el Identificador de Facilitador de pagos o Payfac.</br> <span>&#8226;</span> <b>Versión 5.5.0</b> </br> <span>&#8226;</span><span>&#8226;</span> El elemento <b>ResponseActions</b> y <b>PosOrDeviceAction</b> de todas las operaciones deja de ser una lista.<br/>  de elementos en un string y se convierte en un array de string. Cada valor de la lista anterior está representada por un elemento del array.<br/>   <span>&#8226;</span><span>&#8226;</span> Se agregan los campos <b>ForeignIdentifier</b>, <b>SmallImage</b> y <b>LargeImage</b> en el campo <b>Wallets</b> de la operación <b>WalletsResponse</b>.<br/> <span>&#8226;</span><span>&#8226;</span> En el campo <b>PaymentMethods</b> de la operación <b>PaymentMethodsResponse</b> se agregan las properties <b>Imag</b>, <b>SmallImage</b> y <b>LargeImage</b>. Además se adiciona el campo <b>ID</b> en <b>Category</b> y el campo <b>ForeignIdentifier</b> en <b>Type</b>. <br/> <span>&#8226;</span><span>&#8226;</span> Se agrupan los campos relacionados con los datos del cliente y del vendedor en dos únicos campos de tipo objeto denominados <b>Customer</b> y <b>Seller</b>, respectivamente.<br/> <span>&#8226;</span><span>&#8226;</span> El elemento Layout del campo <b>Tickets</b> se convierte en un array de objetos que contiene elementos que permiten describir, dar formato y codificar los datos a imprimir. <br/> <span>&#8226;</span><span>&#8226;</span> Se documenta la operación <b>OrderStatus</b>.</br> <span>&#8226;</span><span>&#8226;</span> Los campos que refieren a tiempo y fecha se convierten en formato date-time. </br> <span>&#8226;</span><span>&#8226;</span> Se agrega el campo <b>ForeignResponseCode</b> en todas las respuestas de las operaciones, como un código de para el sistema externo, es decir, para la aplicación cliente que se comunica con el TEF.</br> <span>&#8226;</span><span>&#8226;</span> Se adiciona el campo <b>CardGetMode</b> que permite indicar por cada elemento que contiene los datos sensibles, si están encriptados y también el algoritmo usado. En caso de no estar especificado se asume PLAIN.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega el campo <b>OrigReference</b> en aquellas operaciones que pueden referenciar a una transacción previa, como <b>Void</b>, <b>Return</b> y <b>GetTransaction</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se cambia la estrutura de la respuesta de la Operacion <b>GetTransacion</b> por errores. </br> <span>&#8226;</span><span>&#8226;</span> Se agregan las acciones Ok, Error y Retry en los campos <b>ResponseActions</b>.</br> <span>&#8226;</span><span>&#8226;</span> En aquellas operaciones financieras en las que se especifica la tarjeta se agrega en el requerimiento el campo <b>Pin</b>y en la respuesta el campo <b>WorkingKeys</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega el campo <b>Security</b> con el objetivo de indicar los datos sensibles de seguridad de una transacción tanto en los requerimientos como en las respuestas de las operaciones disponibles.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega la operacion <b>KeysRenewal</b> Las claves podran ser retornadas en el elemento <b>Security</b> y en caso de obtener como accion de respuesta <b>KeysRenewal</b> se esta indicando que esta nueva operacion debe ser ejecutada.<br/>      <span>&#8226;</span><span>&#8226;</span> Se agrega la opcion <b>Signature</b>  .<br/>     <span>&#8226;</span><span>&#8226;</span> Se agrega el elemento  <b>CategoryCode</b> para especificar el MCC del Vendedor y/o del Cliente  .<br/>     <span>&#8226;</span><span>&#8226;</span> Se agregan los Elementos <b>MerchantID</b>, <b>TerminalID</b>, <b>TraceNumber</b> y <b>SettlementBatchNumber</b> En los requerimientos, en caso que los mismos contengan valor los mismos seran utilizados para enviar al Host Resolutor de la Transaccion.</br>  <span>&#8226;</span><span>&#8226;</span> Se agregan los valores para pagos recurrentes a  los Elementos  <b>CardReadMode</b> y  <b>CardReadModeDescription</b> <span>&#8226;</span> <b>Versión 5.4.0</b> </br> <span>&#8226;</span><span>&#8226;</span> Se cambia la dirección IP por el nombre.</br> <span>&#8226;</span><span>&#8226;</span> Se contemplan los Datos del <b>Vendedor/Seller</b> y del <b>Cliente/Customer</b> en las operaciones  <b>WalletRequest</b>, <b>Sale</b>, <b>AuthorizeSale</b>, <b>DebtPayment</b>,  <b>Deposit</b>,  <b>Settlement</b>,  <b>Capture</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se Agregan los elementos <b>POSGEO</b> y <b>ReadingDeviceGEO</b> para que el dispositivo de lectura y el Punto de venta Notifiquen su coordenadas georefenciales en el momento de que se realiza la transacción.</br> <span>&#8226;</span><span>&#8226;</span> Se unifica y amplía el elemento <b>RequiredInformation</b>  tanto en los requerimientos como en las respuestas</br>  <span>&#8226;</span><span>&#8226;</span> Se cambia el tipo el elemento <b>CurrencyCode</b> a string para permitir cualquieras de la notaciones posibles.</br> <span>&#8226;</span><span>&#8226;</span> Se cambia el  elemento <b>Currency</b> por <b>CurrencyCode</b>  en el elemento <b>Plans</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se contemplan del detalle ( elemento <b>Products</b> ) de la venta en las operaciones  <b>WalletRequest</b>, <b>Sale</b>, <b>Void</b>, <b>Return</b>, <b>AuthorizeSale</b>, <b>DebtPayment</b>,  <b>VoidDebtPayment</b>, <b>Deposit</b>,  <b>Settlement</b>,  <b>Capture</b>.</br> <span>&#8226;</span><span>&#8226;</span> Agregamos la operación <b>DebtInquiry</b> que actua como sinónimo de <b>BalanceInquery</b>, la cual podía ser usada para consulta de Saldo y también de deuda.</br> <span>&#8226;</span><span>&#8226;</span> Se corrigen los tipos de Datos de Varios campos <b>Amount</b> que en lugar de string debían ser number.</br> <span>&#8226;</span><span>&#8226;</span> Se agregan las operaciones <b>QueryCompanies</b> y <b>QueryLineOfBusiness</b> para la consulta de Rubros y Empresas que se pueden utilizar para pagar Servicios/Deuda/Facturas con la operación <b>DebtPayment</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se adiciona el elemento <b>Companies</b> en la Operacion <b>BalanceInquiry</b> para el caso de que existan mas de una Compania para el mismo codigo o identificador de la deuda o factura a pagar y adicionalmente se agrega para ese caso la posibilidad de especificar a que compania corrende el Pago en el elemento <b>DebtCompanyIdentification</b> en la operación <b>DebtPayment</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se adiciona el elemento <b>BaseAmonut</b> en los requerimientos de las operación <b>Return</b>, el elemento <b>Reference</b>  en las operaciones <b>Sale</b>, <b>AuthorizeSale</b>, <b>Void</b>, <b>Return</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b>, <b>GetTransaction</b> y <b>WalletRequest</b>.  Además, se agregan los elementos <b>TaxFinancialCostAmount</b>, <b>TaxFinancialCostPercentage</b>, <b>FinancialCostAmount</b>, <b>FinancialCostPercentage</b> y <b>RequestAmount</b>  en las respuestas de dichas operaciones.</br> <span>&#8226;</span><span>&#8226;</span> En cada plan que se devuelve a través del <b>PaymentMethodResponse</b> estarán presentes <b>TaxFinancialCostAmount</b>,  <b>TaxFinancialCostPercentage</b>, <b>FinancialCostAmount</b> y <b>FinancialCostPercentage</b>. </br> <span>&#8226;</span><span>&#8226;</span> Se agregan los elementos  <b>CardAppName</b> y <b>CardAppIdentifier</b> en las peticiones de las operaciones <b>Sale</b>, <b>AuthorizeSale</b>,  <b>Void</b>, <b>Return</b>, <b>PaymentMethods</b>, <b>GetCard</b>, <b>Validate</b>, <b>DebtInquiery</b>, <b>BalanceInquiry</b>, <b>DebtPayment</b> y <b>VoidDebtPayment</b>.  Además, se agregan en las respuestas de algunas de ellas.</br> <span>&#8226;</span><span>&#8226;</span> Se cambia la estructura del elemento <b>Tickets</b> de las respuestas donde el elemento <b>Action</b>  hace referencia a las acciones que debe ejecutar el punto de venta, el elemento <b>DeviceAction</b> a las acciones que debe ejecutar el dispositivo y <b>ExecutedAction</b> a las acciones  que ejecutó la plataforma para sus <b>Tickets</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se adicionan los elementos <b>POSOrDeviceAction</b>, <b>OperationMode</b> y <b>OperationModeDescription</b> a la operación <b>Configure</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega el elemento <b>RemainderAmount</b> a la operación <b>GetBlockResponse</b> que hace referencia a la diferencia entre el monto total de la transacción y las devoluciones parciales realizadas.</br> <span>&#8226;</span><span>&#8226;</span> Se corrijen errores en la definición de varios campos, como <b>ReadingDeviceType</b> y <b>CardReadMode</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se reemplaza el campo <b>ApplicationIdentification</b> por <b>SystemIdentification</b> en las operaciones <b>EnableService</b>, <b>Wallets</b>, <b>QueryCompanies</b>,  <b>QueryLineOfBusiness</b> y sus respectivas respuestas. </br> <span>&#8226;</span><span>&#8226;</span> Se agregan el identifidor Tributario en <b>Sale</b>, <b>AuthorizeSale</b>, <b>Void</b>,  <b>Return</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b> y <b>Debtinquery</b> que permite transacciones con <b>Token</b> ( <b>CredentialToken</b> y  <b>CredentialIssuerToken</b> ). En estas operaciones se elimina de mandatorias al campo <b>BranchIdentification</b> y <b>POSIdentification</b><br/> <span>&#8226;</span><span>&#8226;</span> Se agrega la operación <b>Enrollment</b>, la cual permite transacciones con <b>Token</b> ( <b>CredentialToken</b> y  <b>CredentialIssuerToken</b> ) y pagos recurrentes.</br> <span>&#8226;</span><span>&#8226;</span> El campo <b>ResponseAction</b> deja de ser un enum y se convierte en string. Se indica en la descripción los posibles actions.</br> <span>&#8226;</span><span>&#8226;</span> Se agregan los campos <b>SellerIdentification</b> y <b>SellerIdentificationType</b> en aquellas operaciones en las que se especifican con los datos del vendedor.</br> <span>&#8226;</span><span>&#8226;</span> El campo <b>FacilityPayments</b> deja de ser mandatario en las operaciones <b>Enrollment</b> y <b>Sale</b>. </br> <span>&#8226;</span><span>&#8226;</span> Se elimina la posibilidad de envío en el header HTTP.<br/> <span>&#8226;</span><span>&#8226;</span> Se agregan los campos <b>CashbackAmount</b> y <b>TipAmount</b> en la operación <b>WalletRequest</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se adiciona en el campo <b>CardReadMode</b> la opción K de Token.<br/> <span>&#8226;</span><span>&#8226;</span> Se corrige el campo <b>Answertype</b> y se modifica por <b>AnswerType</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se agregan los campos referidos al vendedor en las operaciones <b>Void</b> y <b>Return</b>. <br/> <span>&#8226;</span><span>&#8226;</span> Se crea un primer nivel para cada operación de tipo objeto. <br/>  <span>&#8226;</span><span>&#8226;</span> Se crea el campo <b>InputTokens</b> como un array de objetos que contienen Name y Value como properties en las operaciones <b>Sale</b>, <b>AuthorizeSale</b>, <b>Void</b>, <b>Return</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b> y <b>DebtInquiry</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Los elementos <b>Action</b>, <b>DeviceAction</b> y <b>ExecutedAction</b> del campo <b>Tickets</b> dejan de ser de tipo string y se convierten en arrays.<br/>     <span>&#8226;</span><span>&#8226;</span> Se agrega el elemento <b>AdditionalInformation</b> en las respuestas de todas las operaciones.<br/>     </br> <span>&#8226;</span> <b>Versión 5.3.0</b> Se amplía la definición de la Operación <b>Configure</b> permitiendo tanto en la respuesta como en el requerimiento los elementos <b>Operations</b>, <b>Tables</b> y <b>Files</b></br></br> Se agregan los elementos <b>VoidSupport</b>, <b>ReturnSupport</b>, <b>WalletUseInVoidTransaction</b> y <b>WalletUseInReturnTransaction</b> en las caracteristicas de un Wallet.<br/><br/> Se agrega el Valor <b>Display</b> en el elemento <b>ResponseActions</b> indicando que se debe mostrar en el Display del Dispositivo o Aplicativo el contenido del elemento <b>DisplayResponseMessage</b>.  En la respuesta de la operación  <b>BalanceInquery</b> se agregan los elementos <b>AmountAvailable</b> y <b>PointsAvailable</b> para indicar los saldos.</br> Se especifica en la documentación que el Cancel puede ser usado para Cancelar un Pago con Wallets en Curso.</br></br> Se agregan elementos en los Requerimientos y en las respuestas opcionales entre los POS* que permiten describir las características del punto de venta, los Device* que permiten especificar las características del Dispositivo de Lectura.<br/>   Se cambió el elemento <b>AnswerIdentification</b> por <b>AnswerKey</b>  para compatibilizar con el servicio de Pagos.<br/><br/>     Se agregaron <b>AccountNumber</b>, <b>AccountType</b> y <b>Balance</b> en las operaciones <b>BalanceInquiry</b> y <b>DebtPayment</b> .<br/><br/>     Se agregaron las Operaciones <b>Confirm</b> y  <b>Cancel</b>, donde la Operación <b>Confirm</b> es usada para confirmar un pago recibido por el POS o Aplicativo del comercio. Existen Wallets en los que la confirmación es automática y se indica en el Elemento  <b>AutoConfirm</b> de la respuesta del comando <b>Wallets</b>. La operación <b>Cancel</b> puede ser utilizada a partir de que la Plataforma retorne la acción <b>PaymentFlowIsCancelable</b> en la respuesta de una operación <b>WalletRequest</b>. El Wallet soporta Cancelación de Requerimiento lo cual está indicado con el Elemento <b>SupportRequestCancel</b> dentro de las propiedades de  los Wallets que son retornados por la Operación <b>Wallets</b>.<br/> Se agregó como carasterística de los Wallets también el elemento <b>SupportValidityOfTheRequest</b> que indica si en el primer requerimiento de la Operación <b>WalletRequest</b> se puede enviar el elemento <b>TransactionTimeout</b> que especifica el tiempo de vida de la intención de pago. Superado ese tiempo no se podrá pagar y el ciclo de reintento será detenido por la plataforma, indicado por las siguientes acciones: <b>Completed</b> y <b>Error</b>.<br/> Se agrega el Elemento <b>Tickets</b> en la respuesta de una Operación <b>WalletRequest</b>. El elemento estará presente si como acción está presente el Valor <b>Tickets</b>, indicando que los mismos deberán ser Impresos, capturados digitalmente, etc. según se indique. <br/><br/> Se permite en la Operación <b>PaymentMethod</b> la búsqueda por el Id o el ForeignIdentification<br/><br/> <span>&#8226;</span> <b>Versión 5.2.6</b> Se cambia el nombre del elemento <b>DateTime</b> por <b>TransactionDateTime</b> en la operación <b>WalletRequest</b>.<br/><br/> <span>&#8226;</span> <b>Versión 5.2.5</b> Se agregan en los Planes el atributo <b>POSOrDeviceActions</b> que permite indecarle al Dispositivo que debe solicitar  PIN para esa transacción y eso lo indica enviando la acción <b>RequestPIN</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se agrega el <b>ResponseActions</b> <b>Configure</b> que indica que se debe ejecutar una reconfiguración para obtener  parámetros nuevos ya que hay alguna actualización. <span>&#8226;</span><span>&#8226;</span> Se agregan las Operaciones <b>Wallets</b>, <b>WalletRequest</b> y <b>EnableService</b>, las mismas pueden formar parte  de un Block y forman parte de la ruptura de Secuencia.<br/><br/> <span>&#8226;</span> <b>Versión 5.2.4</b> Se agrega el identifidor Tributario en <b>OrderInitial</b>, que permite transacciones con <b>Token</b> ( <b>CredentialToken</b> y  <b>CredentialIssuerToken</b> ).<br/> <span>&#8226;</span><span>&#8226;</span> Se completa el <b>GetCardResponse</b> para que contenga los  elementos <b>PaymentMethod</b> y <b>Plans</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se completa el <b>PaymentMethodResponse</b> para que contenga los elementos <b>PaymentMethod</b> y <b>Plans</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se agrega en el <b>GetCard</b>: permite forzar un modo de lectura y permite solicitar los datos leídos al POS <b>CardGetMode</b>. <br/><br/> <span>&#8226;</span><span>&#8226;</span> Se permite el envío de datos del cliente <b>Customer*</b> en las operaciones Financieras.<br/><br/> <span>&#8226;</span> <b>Versión 5.2.3</b> Se cambian los valores posibles para <b>ResponseActionCancel</b> en las operaciones <b>GetBlock</b> y <b>GetTransaction</b>.<br/>   <br/> <span>&#8226;</span> <b>Versión 5.2.2</b> Se agrega el Atributo <b>ReasonReverse</b> que permite notificar en las Reversas la razón por la cual fue necesario  generarla, el atributo <b>ReasonSequenceBreak</b> que permite indicar la razón por la cual se produce la ruptura de secuencia que podrá generar una reversa si  fuese necesario, y el atributo </b>Reason</b> en la operación <b>Cancel</b>.<br/>   <br/> <span>&#8226;</span> <b>Versión 5.2.1</b> Se agrega el Atributo <b>IsReverse</b> en todos las operaciones reversables.<br/>   <br/><br/> <br/><br/> <br/><p style=\"color:Blue;\">&copy;2019-2021 EVO Payments Inc. All rights reserved.</p>The EVO Payments name, logo and related trademarks and service marks, owned<br /> by EVO Payments, are registered and/or used in the<br /> United States and many foreign countries. All other trademarks,<br /> service marks and trade names referenced in this site are the property<br /> of their respective owners.<br /> <br /> <br /> ANY USE, COPYING OR REPRODUCTION OF THE TRADEMARKS, LOGOS, INFORMATION,<br />  IMAGES OR DESIGNS CONTAINED IN THIS SITE IS STRICTLY<br />  PROHIBITED WITHOUT THE PRIOR WRITTEN PERMISSION OF EVO Payments Inc.<br /> <br />   # noqa: E501

    The version of the OpenAPI document: 5.6.1
    Contact: integrations@evopayments.mx
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.sale_object_sale_customer import SaleObjectSaleCustomer
    from openapi_client.model.sale_object_sale_input_tokens import SaleObjectSaleInputTokens
    from openapi_client.model.sale_object_sale_payer import SaleObjectSalePayer
    from openapi_client.model.sale_object_sale_security import SaleObjectSaleSecurity
    from openapi_client.model.sale_response_object_sale_response_additional_information import SaleResponseObjectSaleResponseAdditionalInformation
    from openapi_client.model.sale_response_object_sale_response_card_category import SaleResponseObjectSaleResponseCardCategory
    from openapi_client.model.sale_response_object_sale_response_configuration import SaleResponseObjectSaleResponseConfiguration
    from openapi_client.model.sale_response_object_sale_response_merchant_category import SaleResponseObjectSaleResponseMerchantCategory
    from openapi_client.model.sale_response_object_sale_response_payment_method import SaleResponseObjectSaleResponsePaymentMethod
    from openapi_client.model.sale_response_object_sale_response_plans import SaleResponseObjectSaleResponsePlans
    from openapi_client.model.sale_response_object_sale_response_products import SaleResponseObjectSaleResponseProducts
    from openapi_client.model.sale_response_object_sale_response_required_information import SaleResponseObjectSaleResponseRequiredInformation
    from openapi_client.model.sale_response_object_sale_response_tickets import SaleResponseObjectSaleResponseTickets
    from openapi_client.model.sale_response_object_sale_response_working_keys import SaleResponseObjectSaleResponseWorkingKeys
    globals()['SaleObjectSaleCustomer'] = SaleObjectSaleCustomer
    globals()['SaleObjectSaleInputTokens'] = SaleObjectSaleInputTokens
    globals()['SaleObjectSalePayer'] = SaleObjectSalePayer
    globals()['SaleObjectSaleSecurity'] = SaleObjectSaleSecurity
    globals()['SaleResponseObjectSaleResponseAdditionalInformation'] = SaleResponseObjectSaleResponseAdditionalInformation
    globals()['SaleResponseObjectSaleResponseCardCategory'] = SaleResponseObjectSaleResponseCardCategory
    globals()['SaleResponseObjectSaleResponseConfiguration'] = SaleResponseObjectSaleResponseConfiguration
    globals()['SaleResponseObjectSaleResponseMerchantCategory'] = SaleResponseObjectSaleResponseMerchantCategory
    globals()['SaleResponseObjectSaleResponsePaymentMethod'] = SaleResponseObjectSaleResponsePaymentMethod
    globals()['SaleResponseObjectSaleResponsePlans'] = SaleResponseObjectSaleResponsePlans
    globals()['SaleResponseObjectSaleResponseProducts'] = SaleResponseObjectSaleResponseProducts
    globals()['SaleResponseObjectSaleResponseRequiredInformation'] = SaleResponseObjectSaleResponseRequiredInformation
    globals()['SaleResponseObjectSaleResponseTickets'] = SaleResponseObjectSaleResponseTickets
    globals()['SaleResponseObjectSaleResponseWorkingKeys'] = SaleResponseObjectSaleResponseWorkingKeys


class DepositResponseObjectDepositResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('response_actions',): {
            'OK': "OK",
            'APPROVE': "Approve",
            'REFUSE': "Refuse",
            'ISSUERCALL': "IssuerCall",
            'WITHHOLD': "WithHold",
            'GETCARD': "GetCard",
            'USETERMINALTOAUTHORIZE': "UseTerminalToAuthorize",
            'CONFIGURATIONERROR': "ConfigurationError",
            'SYSTEMERROR': "SystemError",
            'RESOURCEERROR': "ResourceError",
            'PROCESSERROR': "ProcessError",
            'ENABLESERVICE': "EnableService",
            'COMPLETED': "Completed",
            'CONFIGURE': "Configure",
            'TICKETS': "Tickets",
            'DISPLAY': "Display",
            'PRINT': "Print",
            'ERROR': "Error",
            'RETRY': "Retry",
            'KEYSRENEWAL': "KeysRenewal",
        },
        ('was_reverse_previous',): {
            '0': 0,
            '1': 1,
        },
        ('currency_code',): {
            '152': "152",
            '484': "484",
            '878': "878",
            '840': "840",
            '858': "858",
            '986': "986",
            'CLP': "CLP",
            'MXN': "MXN",
            'EUR': "EUR",
            'USD': "USD",
            'UYU': "UYU",
            'BRL': "BRL",
        },
        ('card_read_mode',): {
            'C': "C",
            'B': "B",
            'M': "M",
            'L': "L",
            'S': "S",
            'T': "T",
            'E': "E",
            'F': "F",
            'K': "K",
            'R': "R",
        },
        ('card_read_mode_description',): {
            'EMV_CHIP': "EMV CHIP",
            'MAGNETIC_STRIPE': "MAGNETIC STRIPE",
            'MANUAL': "MANUAL",
            'CONTACTLESS': "CONTACTLESS",
            'CONTACTLESS_STRIPE': "CONTACTLESS STRIPE",
            'TYPED': "TYPED",
            'ECOMMERCE': "ECOMMERCE",
            'FALLBACK': "FALLBACK",
            'RECURRING': "RECURRING",
        },
    }

    validations = {
        ('response_code',): {
        },
        ('sequence',): {
            'max_length': 128,
        },
        ('block',): {
            'max_length': 128,
        },
        ('request_key',): {
            'max_length': 128,
        },
        ('answer_key',): {
            'max_length': 128,
        },
        ('public_answer_key',): {
            'max_length': 128,
        },
        ('reversed_answer_key',): {
            'max_length': 128,
        },
        ('reversed_sequence',): {
            'max_length': 128,
        },
        ('committed_block',): {
            'max_length': 128,
        },
        ('reversed_block',): {
            'max_length': 128,
        },
        ('host_result_code',): {
        },
        ('host_code',): {
            'max_length': 8,
            'min_length': 6,
        },
        ('auth_result_code',): {
            'max_length': 16,
        },
        ('auth_host_process_code',): {
            'max_length': 6,
        },
        ('auth_host_msg_type',): {
            'max_length': 16,
        },
        ('host_msg_type',): {
            'max_length': 16,
        },
        ('auth_code',): {
            'max_length': 8,
            'min_length': 2,
        },
        ('auth_ticket',): {
        },
        ('merchant_id',): {
            'max_length': 15,
        },
        ('terminal_id',): {
            'max_length': 8,
        },
        ('terminal_trace',): {
        },
        ('settlement_batch_number',): {
        },
        ('card_number',): {
            'max_length': 19,
            'min_length': 10,
        },
        ('card_exp',): {
            'max_length': 4,
            'min_length': 4,
        },
        ('orig_answer_key',): {
            'max_length': 128,
        },
        ('orig_auth_ticket',): {
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'response_code': (int, str),  # noqa: E501
            'response_actions': ([str],),  # noqa: E501
            'response_message': (str,),  # noqa: E501
            'company_identification': (str,),  # noqa: E501
            'system_identification': (str,),  # noqa: E501
            'branch_identification': (str,),  # noqa: E501
            'pos_identification': (str,),  # noqa: E501
            'foreign_response_code': (str,),  # noqa: E501
            'request_type': (str,),  # noqa: E501
            'service_version': (str,),  # noqa: E501
            'sequence': (str,),  # noqa: E501
            'security': ([SaleObjectSaleSecurity],),  # noqa: E501
            'block': (str,),  # noqa: E501
            'request_key': (str,),  # noqa: E501
            'working_keys': ([SaleResponseObjectSaleResponseWorkingKeys],),  # noqa: E501
            'required_information': ([SaleResponseObjectSaleResponseRequiredInformation],),  # noqa: E501
            'answer_type': (str,),  # noqa: E501
            'answer_key': (str,),  # noqa: E501
            'public_answer_key': (str,),  # noqa: E501
            'was_reverse_previous': (int,),  # noqa: E501
            'reversed_answer_key': (str,),  # noqa: E501
            'reversed_sequence': (str,),  # noqa: E501
            'committed_block': (str,),  # noqa: E501
            'reversed_block': (str,),  # noqa: E501
            'message_id': (str,),  # noqa: E501
            'server_address': (str,),  # noqa: E501
            'server_instance': (str,),  # noqa: E501
            'server_node_name': (str,),  # noqa: E501
            'adapter_input_version': (str,),  # noqa: E501
            'adapter_input_address': (str,),  # noqa: E501
            'adapter_input_node_name': (str,),  # noqa: E501
            'adapter_output_version': (str,),  # noqa: E501
            'adapter_output_address': (str,),  # noqa: E501
            'adapter_output_node_name': (str,),  # noqa: E501
            'additional_information': ([SaleResponseObjectSaleResponseAdditionalInformation],),  # noqa: E501
            'printer_response_message': ([str],),  # noqa: E501
            'display_response_message': ([str],),  # noqa: E501
            'currency_code': (str,),  # noqa: E501
            'currency_description': (str,),  # noqa: E501
            'transaction_description': (str,),  # noqa: E501
            'transaction_resolution_mode': (str,),  # noqa: E501
            'currency_symbol': (str,),  # noqa: E501
            'facility_payments': (int,),  # noqa: E501
            'facility_type': (int,),  # noqa: E501
            'value_facility_payments': (float,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'alternative_amount': (float,),  # noqa: E501
            'amount_charged': (float,),  # noqa: E501
            'amount_to_apply': (float,),  # noqa: E501
            'cashback_amount': (float,),  # noqa: E501
            'tip_amount': (float,),  # noqa: E501
            'request_amount': (float,),  # noqa: E501
            'promoted_amount': (float,),  # noqa: E501
            'credential_token': (str,),  # noqa: E501
            'credential_issuer_token': (str,),  # noqa: E501
            'input_tokens': ([SaleObjectSaleInputTokens],),  # noqa: E501
            'output_tokens': ([SaleObjectSaleInputTokens],),  # noqa: E501
            'tax_financial_cost_amount': (float,),  # noqa: E501
            'tax_financial_cost_percentage': (float,),  # noqa: E501
            'financial_cost_amount': (float,),  # noqa: E501
            'financial_cost_percentage': (float,),  # noqa: E501
            'host_result_code': (int,),  # noqa: E501
            'host_message': (str,),  # noqa: E501
            'host_code': (str,),  # noqa: E501
            'host_id': (int,),  # noqa: E501
            'user_id': (str,),  # noqa: E501
            'issuer_name': (str,),  # noqa: E501
            'host_date_time': (datetime,),  # noqa: E501
            'transmition_date_time': (datetime,),  # noqa: E501
            'auth_result_code': (str,),  # noqa: E501
            'auth_host_process_code': (str,),  # noqa: E501
            'auth_host_msg_type': (str,),  # noqa: E501
            'auth_host_message': (str,),  # noqa: E501
            'host_msg_type': (str,),  # noqa: E501
            'auth_code': (str,),  # noqa: E501
            'auth_date_time': (datetime,),  # noqa: E501
            'auth_ticket': (int,),  # noqa: E501
            'auth_rrn': (str,),  # noqa: E501
            'transaction_authentication_type': (str,),  # noqa: E501
            'identifier_for_the_adquirer': (str,),  # noqa: E501
            'identifier_for_the_resolutor': (str,),  # noqa: E501
            'payment_facilitator_id': (str,),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'terminal_id': (str,),  # noqa: E501
            'terminal_trace': (int,),  # noqa: E501
            'settlement_batch_number': (int,),  # noqa: E501
            'card_read_mode': (str,),  # noqa: E501
            'card_read_mode_description': (str,),  # noqa: E501
            'card_description': (str,),  # noqa: E501
            'card_type_description': (str,),  # noqa: E501
            'card_category': (SaleResponseObjectSaleResponseCardCategory,),  # noqa: E501
            'card_number': (str,),  # noqa: E501
            'card_number_masked': (str,),  # noqa: E501
            'card_hashing': (str,),  # noqa: E501
            'card_exp': (str,),  # noqa: E501
            'card_cryptogram_response': (str,),  # noqa: E501
            'card_app_name': (str,),  # noqa: E501
            'card_app_identifier': (str,),  # noqa: E501
            'card_app_label': (str,),  # noqa: E501
            'card_auth_request_cryptogram': (str,),  # noqa: E501
            'card_auth_response_cryptogram': (str,),  # noqa: E501
            'payer': (SaleObjectSalePayer,),  # noqa: E501
            'customer': (SaleObjectSaleCustomer,),  # noqa: E501
            'merchant_category': (SaleResponseObjectSaleResponseMerchantCategory,),  # noqa: E501
            'products': ([SaleResponseObjectSaleResponseProducts],),  # noqa: E501
            'payment_method': (SaleResponseObjectSaleResponsePaymentMethod,),  # noqa: E501
            'plans': (SaleResponseObjectSaleResponsePlans,),  # noqa: E501
            'plan_description': (str,),  # noqa: E501
            'plan_config_version': (int,),  # noqa: E501
            'tickets': ([SaleResponseObjectSaleResponseTickets],),  # noqa: E501
            'configuration': (SaleResponseObjectSaleResponseConfiguration,),  # noqa: E501
            'card_holder_name': (str,),  # noqa: E501
            'orig_answer_key': (str,),  # noqa: E501
            'orig_auth_date_time': (datetime,),  # noqa: E501
            'orig_auth_ticket': (int,),  # noqa: E501
            'orig_auth_terminal_trace': (int,),  # noqa: E501
            'orig_auth_code': (str,),  # noqa: E501
            'payment_method_id': (int,),  # noqa: E501
            'payment_method_description': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'response_code': 'ResponseCode',  # noqa: E501
        'response_actions': 'ResponseActions',  # noqa: E501
        'response_message': 'ResponseMessage',  # noqa: E501
        'company_identification': 'CompanyIdentification',  # noqa: E501
        'system_identification': 'SystemIdentification',  # noqa: E501
        'branch_identification': 'BranchIdentification',  # noqa: E501
        'pos_identification': 'POSIdentification',  # noqa: E501
        'foreign_response_code': 'ForeignResponseCode',  # noqa: E501
        'request_type': 'RequestType',  # noqa: E501
        'service_version': 'ServiceVersion',  # noqa: E501
        'sequence': 'Sequence',  # noqa: E501
        'security': 'Security',  # noqa: E501
        'block': 'Block',  # noqa: E501
        'request_key': 'RequestKey',  # noqa: E501
        'working_keys': 'WorkingKeys',  # noqa: E501
        'required_information': 'RequiredInformation',  # noqa: E501
        'answer_type': 'AnswerType',  # noqa: E501
        'answer_key': 'AnswerKey',  # noqa: E501
        'public_answer_key': 'PublicAnswerKey',  # noqa: E501
        'was_reverse_previous': 'WasReversePrevious',  # noqa: E501
        'reversed_answer_key': 'ReversedAnswerKey',  # noqa: E501
        'reversed_sequence': 'ReversedSequence',  # noqa: E501
        'committed_block': 'CommittedBlock',  # noqa: E501
        'reversed_block': 'ReversedBlock',  # noqa: E501
        'message_id': 'MessageID',  # noqa: E501
        'server_address': 'ServerAddress',  # noqa: E501
        'server_instance': 'ServerInstance',  # noqa: E501
        'server_node_name': 'ServerNodeName',  # noqa: E501
        'adapter_input_version': 'AdapterInputVersion',  # noqa: E501
        'adapter_input_address': 'AdapterInputAddress',  # noqa: E501
        'adapter_input_node_name': 'AdapterInputNodeName',  # noqa: E501
        'adapter_output_version': 'AdapterOutputVersion',  # noqa: E501
        'adapter_output_address': 'AdapterOutputAddress',  # noqa: E501
        'adapter_output_node_name': 'AdapterOutputNodeName',  # noqa: E501
        'additional_information': 'AdditionalInformation',  # noqa: E501
        'printer_response_message': 'PrinterResponseMessage',  # noqa: E501
        'display_response_message': 'DisplayResponseMessage',  # noqa: E501
        'currency_code': 'CurrencyCode',  # noqa: E501
        'currency_description': 'CurrencyDescription',  # noqa: E501
        'transaction_description': 'TransactionDescription',  # noqa: E501
        'transaction_resolution_mode': 'TransactionResolutionMode',  # noqa: E501
        'currency_symbol': 'CurrencySymbol',  # noqa: E501
        'facility_payments': 'FacilityPayments',  # noqa: E501
        'facility_type': 'FacilityType',  # noqa: E501
        'value_facility_payments': 'ValueFacilityPayments',  # noqa: E501
        'amount': 'Amount',  # noqa: E501
        'alternative_amount': 'AlternativeAmount',  # noqa: E501
        'amount_charged': 'AmountCharged',  # noqa: E501
        'amount_to_apply': 'AmountToApply',  # noqa: E501
        'cashback_amount': 'CashbackAmount',  # noqa: E501
        'tip_amount': 'TipAmount',  # noqa: E501
        'request_amount': 'RequestAmount',  # noqa: E501
        'promoted_amount': 'PromotedAmount',  # noqa: E501
        'credential_token': 'CredentialToken',  # noqa: E501
        'credential_issuer_token': 'CredentialIssuerToken',  # noqa: E501
        'input_tokens': 'InputTokens',  # noqa: E501
        'output_tokens': 'OutputTokens',  # noqa: E501
        'tax_financial_cost_amount': 'TaxFinancialCostAmount',  # noqa: E501
        'tax_financial_cost_percentage': 'TaxFinancialCostPercentage',  # noqa: E501
        'financial_cost_amount': 'FinancialCostAmount',  # noqa: E501
        'financial_cost_percentage': 'FinancialCostPercentage',  # noqa: E501
        'host_result_code': 'HostResultCode',  # noqa: E501
        'host_message': 'HostMessage',  # noqa: E501
        'host_code': 'HostCode',  # noqa: E501
        'host_id': 'HostID',  # noqa: E501
        'user_id': 'UserID',  # noqa: E501
        'issuer_name': 'IssuerName',  # noqa: E501
        'host_date_time': 'HostDateTime',  # noqa: E501
        'transmition_date_time': 'TransmitionDateTime',  # noqa: E501
        'auth_result_code': 'AuthResultCode',  # noqa: E501
        'auth_host_process_code': 'AuthHostProcessCode',  # noqa: E501
        'auth_host_msg_type': 'AuthHostMsgType',  # noqa: E501
        'auth_host_message': 'AuthHostMessage',  # noqa: E501
        'host_msg_type': 'HostMsgType',  # noqa: E501
        'auth_code': 'AuthCode',  # noqa: E501
        'auth_date_time': 'AuthDateTime',  # noqa: E501
        'auth_ticket': 'AuthTicket',  # noqa: E501
        'auth_rrn': 'AuthRRN',  # noqa: E501
        'transaction_authentication_type': 'TransactionAuthenticationType',  # noqa: E501
        'identifier_for_the_adquirer': 'IdentifierForTheAdquirer',  # noqa: E501
        'identifier_for_the_resolutor': 'IdentifierForTheResolutor',  # noqa: E501
        'payment_facilitator_id': 'PaymentFacilitatorID',  # noqa: E501
        'merchant_id': 'MerchantID',  # noqa: E501
        'terminal_id': 'TerminalID',  # noqa: E501
        'terminal_trace': 'TerminalTrace',  # noqa: E501
        'settlement_batch_number': 'SettlementBatchNumber',  # noqa: E501
        'card_read_mode': 'CardReadMode',  # noqa: E501
        'card_read_mode_description': 'CardReadModeDescription',  # noqa: E501
        'card_description': 'CardDescription',  # noqa: E501
        'card_type_description': 'CardTypeDescription',  # noqa: E501
        'card_category': 'CardCategory',  # noqa: E501
        'card_number': 'CardNumber',  # noqa: E501
        'card_number_masked': 'CardNumberMasked',  # noqa: E501
        'card_hashing': 'CardHashing',  # noqa: E501
        'card_exp': 'CardExp',  # noqa: E501
        'card_cryptogram_response': 'CardCryptogramResponse',  # noqa: E501
        'card_app_name': 'CardAppName',  # noqa: E501
        'card_app_identifier': 'CardAppIdentifier',  # noqa: E501
        'card_app_label': 'CardAppLabel',  # noqa: E501
        'card_auth_request_cryptogram': 'CardAuthRequestCryptogram',  # noqa: E501
        'card_auth_response_cryptogram': 'CardAuthResponseCryptogram',  # noqa: E501
        'payer': 'Payer',  # noqa: E501
        'customer': 'Customer',  # noqa: E501
        'merchant_category': 'MerchantCategory',  # noqa: E501
        'products': 'Products',  # noqa: E501
        'payment_method': 'PaymentMethod',  # noqa: E501
        'plans': 'Plans',  # noqa: E501
        'plan_description': 'PlanDescription',  # noqa: E501
        'plan_config_version': 'PlanConfigVersion',  # noqa: E501
        'tickets': 'Tickets',  # noqa: E501
        'configuration': 'Configuration',  # noqa: E501
        'card_holder_name': 'CardHolderName',  # noqa: E501
        'orig_answer_key': 'OrigAnswerKey',  # noqa: E501
        'orig_auth_date_time': 'OrigAuthDateTime',  # noqa: E501
        'orig_auth_ticket': 'OrigAuthTicket',  # noqa: E501
        'orig_auth_terminal_trace': 'OrigAuthTerminalTrace',  # noqa: E501
        'orig_auth_code': 'OrigAuthCode',  # noqa: E501
        'payment_method_id': 'PaymentMethodId',  # noqa: E501
        'payment_method_description': 'PaymentMethodDescription',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, response_code, response_actions, response_message, *args, **kwargs):  # noqa: E501
        """DepositResponseObjectDepositResponse - a model defined in OpenAPI

        Args:
            response_code (int): Código de Respuesta Interno de la plataforma, el POS debe actuar por lo que indican las acciones especificadas en ResponseActions y no por el código de respuesta informado en este campo o elemento, pero es una buena práctica que sea persistido por el mismo.
            response_actions ([str]): Acciones a realizar por parte del POS y/o PINPAD en base al resultado de la operación que ha sido procesada. Cada uno de estos actions o acciones están concatenadas por comas. Los posibles actions son OK, Approve, Refuse, IssuerCall, Tickets, WithHold, GetCard, UseTerminalToAuthorize, ConfigurationError, SystemError, ResourceError, ProcessError, Completed, Configure, Display, EnableService y Print.
            response_message (str): Descripción del resultado del proceso del requerimiento recibido. Esta descripción es generada por la plataforma, no por el Host que termine resolviendo la transacción.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            company_identification (str): ID que identifica la companía desde donde proviene la petición.. [optional]  # noqa: E501
            system_identification (str): ID que identifica el sistema desde donde proviene la petición.. [optional]  # noqa: E501
            branch_identification (str): ID que identifica la sucursal desde donde proviene la petición. Esta sucursal pertenece a una determinada companía.. [optional]  # noqa: E501
            pos_identification (str): ID que identifica la caja o punto de venta desde donde proviene la petición. Este punto de venta pertenece a una determinada sucursal y companía.. [optional]  # noqa: E501
            foreign_response_code (str): Código de respuesta para el sistema externo, es decir, para la aplicación cliente que se comunica con el TEF.. [optional]  # noqa: E501
            request_type (str): Tipo de Operación que se requirió, contendrá el mismo valor que se recibió en el requerimiento, sobre formatos que no soportan elementos complejos o compuestos.. [optional]  # noqa: E501
            service_version (str): Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible.. [optional]  # noqa: E501
            sequence (str): Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma.. [optional]  # noqa: E501
            security ([SaleObjectSaleSecurity]): Datos asociados a la seguridad de la transacción o de elementos sensibles.. [optional]  # noqa: E501
            block (str): ID que identifica a un grupo de transacciones que serán confirmadas o canceladas. [optional]  # noqa: E501
            request_key (str): ID generado para la identificación por parte del Plataforma de la información generada en la ejecución de un GetCard o un Payment Method. Será necesario para que un mensaje de Sale, Void, Payment Method o Enrollment identifique el contexto generado y lo utilice para esa operación.. [optional]  # noqa: E501
            working_keys ([SaleResponseObjectSaleResponseWorkingKeys]): Nueva forma de enviar las llaves disponibles para esta caja.. [optional]  # noqa: E501
            required_information ([SaleResponseObjectSaleResponseRequiredInformation]): En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente.. [optional]  # noqa: E501
            answer_type (str): Tipo de Operación que se está requiriendo, solo necesario sobre formatos que no soportan elementos complejos o compuestos.. [optional]  # noqa: E501
            answer_key (str): Código de identificación, generado por Plataforma, de la operación realizada'.. [optional]  # noqa: E501
            public_answer_key (str): Código público de identificación, generado por Plataforma, de la operación realizada'.. [optional]  # noqa: E501
            was_reverse_previous (int): Flag indicador de generación de reversa para la última operación reversable.. [optional]  # noqa: E501
            reversed_answer_key (str): ID que identifica a la operación que acaba de ser reversada.. [optional]  # noqa: E501
            reversed_sequence (str): Secuencia de la transacción que fue reversada.. [optional]  # noqa: E501
            committed_block (str): ID del bloque de transacciones que ha sido confirmado de forma automática (es decir, sin recibir un requerimiento de BlockClose). Este escenario se presentará si el Plataforma así se ha configurado para actuar bajo esa circunstancia.. [optional]  # noqa: E501
            reversed_block (str): ID del bloque de transacciones que ha sido cancelado de forma automática (es decir, sin recibir un requerimiento de BlockClose). Este escenario se presentara si el Plataforma así se ha configurado para actuar bajo esa circunstancia.. [optional]  # noqa: E501
            message_id (str): Identificador Unívoco del Mensaje ( UUID v5 ).. [optional]  # noqa: E501
            server_address (str): Dirección IP del Server que atiende el requerimiento.. [optional]  # noqa: E501
            server_instance (str): Instancia de Server que atiende el requerimiento.. [optional]  # noqa: E501
            server_node_name (str): Nombre del Nodo que atendió el requerimiento.. [optional]  # noqa: E501
            adapter_input_version (str): Versión del  Adaptador de Protocolo Entrante que atiende el Requerimiento.. [optional]  # noqa: E501
            adapter_input_address (str): Dirección IP del Adaptador de Protocolo Entrante que atiende el requerimiento.. [optional]  # noqa: E501
            adapter_input_node_name (str): Nombre del Nodo del Adaptador de Protocolo Entrante que atiende el requerimiento.. [optional]  # noqa: E501
            adapter_output_version (str): Versión del  Adaptador de Protocolo Saliente que atiende el Requerimiento.. [optional]  # noqa: E501
            adapter_output_address (str): Dirección IP  del  Adaptador de Protocolo Saliente que atiende el Requerimiento.. [optional]  # noqa: E501
            adapter_output_node_name (str): Nombre del Nodo  del  Adaptador de Protocolo Saliente que atiende el Requerimiento.. [optional]  # noqa: E501
            additional_information ([SaleResponseObjectSaleResponseAdditionalInformation]): En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente.. [optional]  # noqa: E501
            printer_response_message ([str]): Información adicional/Mensaje promocional/Leyenda de respuesta a imprimir en el ticket de la operación. Cada línea de este mensaje sera un elemento dentro del array.. [optional]  # noqa: E501
            display_response_message ([str]): Información adicional/Mensaje promocional/Leyenda de respuesta a mostrar en pantalla en el ticket de la operación. Cada línea de este mensaje será un elemento dentro del array.. [optional]  # noqa: E501
            currency_code (str): código de Moneda - ISO 4217 <https://en.wikipedia.org/wiki/ISO_4217 Se puede utilizar la Codificación Alfabética o Numérica <br />   * Num   - Alpha - Description <br />   * '032' - 'ARS' - Pesos Argentinos <br />   * '152' - 'CLP' - Pesos Chilenos <br/>   * '484' - 'MXN' - Pesos Mexicanos <br/>   * '840' - 'USD' - dólares Americanos <br/>   * '878' - 'EUR' - Euros <br/>   * '858' - 'UYU' - Pesos Uruguayos <br/>   * '878' - 'EUR' - Euros <br/>   * '986' - 'BRL' - Real Brasileño. [optional]  # noqa: E501
            currency_description (str): Descripción del tipo de cambio utilizado en la transacción.. [optional]  # noqa: E501
            transaction_description (str): Tipo de transacción. [optional]  # noqa: E501
            transaction_resolution_mode (str): Modo en que fue realizada la transacción. [optional]  # noqa: E501
            currency_symbol (str): Símbolo monetario del tipo de cambio utilizado en la transacción.. [optional]  # noqa: E501
            facility_payments (int): Cantidad de cuotas utilizadas para realizar la operación. [optional]  # noqa: E501
            facility_type (int): Tipo de plan utilizado para para realizar la operación. [optional]  # noqa: E501
            value_facility_payments (float): Monto final a pagar en cada una de las cuotas en las que se divida la compra. [optional]  # noqa: E501
            amount (float): Importe o Monto de la Transacción.. [optional]  # noqa: E501
            alternative_amount (float): Monto con la que se realizó transacción. Si este valor es recibido, la búsqueda de los planes será limitada con este criterio.. [optional]  # noqa: E501
            amount_charged (float): Importe o Monto de la Transacción que efectivamente se cobró.  Si se envía en Void o Return en lugar de Amount, se genera un Ajuste si el Host lo soporta.. [optional]  # noqa: E501
            amount_to_apply (float): Importe o Monto de la Transacción a aplicar.. [optional]  # noqa: E501
            cashback_amount (float): Monto del dinero en efectivo (cashback).. [optional]  # noqa: E501
            tip_amount (float): Importe o Monto de la Propina.. [optional]  # noqa: E501
            request_amount (float): Monto libre de costos financerios e impuestos por el que la venta se realizó. El monto cobrado realmente no es este, dado que no incluye las tasas e impuestos. [optional]  # noqa: E501
            promoted_amount (float): Monto Sujeto a Promoción monto de la operación. [optional]  # noqa: E501
            credential_token (str): Token asociado a la Credencial Enrolada. [optional]  # noqa: E501
            credential_issuer_token (str): Emisor del Token asociado a la credencial enrolada. [optional]  # noqa: E501
            input_tokens ([SaleObjectSaleInputTokens]): Tokens.. [optional]  # noqa: E501
            output_tokens ([SaleObjectSaleInputTokens]): Tokens.. [optional]  # noqa: E501
            tax_financial_cost_amount (float): Monto del recargo impositivo aplicado al costo financiero que la transacción tiene. [optional]  # noqa: E501
            tax_financial_cost_percentage (float): Porcentaje de recargo impositivo a aplicar sobre el monto del costo financiero. [optional]  # noqa: E501
            financial_cost_amount (float): Monto del Costo financiero total generado en base al plan elegido. [optional]  # noqa: E501
            financial_cost_percentage (float): Porcentaje del costo financiero a aplicar al monto de la transacción. [optional]  # noqa: E501
            host_result_code (int): Código de Resultado retornado por el Host Adquirente.. [optional]  # noqa: E501
            host_message (str): Mensaje Retornado por el Host Adquirente, normalmente asociado al valor de HostResultCode. [optional]  # noqa: E501
            host_code (str): Código de autorización retornado por el Host que resuelve la transacción.. [optional]  # noqa: E501
            host_id (int): Número de identificación del host al cual fue enviada la petición, y por el cual fue finalmente procesada.. [optional]  # noqa: E501
            user_id (str): Identificador del usuario que está realizando la Transacción.. [optional]  # noqa: E501
            issuer_name (str): Nombre del Emisor de la Credencial o Tarjeta que se usó en la transacción.. [optional]  # noqa: E501
            host_date_time (datetime): Fecha y Hora de la transacción retornada por el Host que resuelve la Transacción - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14. [optional]  # noqa: E501
            transmition_date_time (datetime): Fecha y hora de transmisión de la operación hacia el host - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14. [optional]  # noqa: E501
            auth_result_code (str): Código de Resultado retornado por el Host Adquirente.. [optional]  # noqa: E501
            auth_host_process_code (str): Código de procesamiento de la operación enviada al host. Elemento 3 del protocolo de comunicaciones ISO 8583, formato de mensajes utilizado por los hosts para realizar operaciones financieras.. [optional]  # noqa: E501
            auth_host_msg_type (str): Elemento 0 del protocolo de comunicaciones ISO 8583, formato de mensajes utilizado por los hosts para realizar operaciones financieras. El valor de este campo es el que devuelve el host en una respuesta a una petición.. [optional]  # noqa: E501
            auth_host_message (str): Mensaje Retornado por el Host Adquirente, normalmente asociado al valor de AuthResultCode. [optional]  # noqa: E501
            host_msg_type (str): Elemento 0 del protocolo de comunicaciones ISO 8583, formato de mensajes utilizado por los hosts para realizar operaciones financieras. El valor de este campo es el que se envio al host en el envio de una petición.. [optional]  # noqa: E501
            auth_code (str): Código de autorización retornado por el Host que resuelve la transacción.. [optional]  # noqa: E501
            auth_date_time (datetime): Fecha y Hora de la transacción retornada por el Host que resuelve la Transacción - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14. [optional]  # noqa: E501
            auth_ticket (int): Número Ticket  o Voucher Generado para la Plataforma.. [optional]  # noqa: E501
            auth_rrn (str): Número de identificación de la transacción, utilizado por la mayoría de los hosts para realizar anulaciones y devoluciones.. [optional]  # noqa: E501
            transaction_authentication_type (str): Tipo de autenticación. [optional]  # noqa: E501
            identifier_for_the_adquirer (str): Identificador que genera el Host Adquirente para la Transacción. En algunos podrá ser igual al AuthRRN.. [optional]  # noqa: E501
            identifier_for_the_resolutor (str): Identificador que genera el Host o Plataforma que resuelve la transacción.. [optional]  # noqa: E501
            payment_facilitator_id (str): Identificador de facilitador de pagos o Payfac.. [optional]  # noqa: E501
            merchant_id (str): Número de comercio utilizado para realizar la transacción. Este Número es asignado por el host, y parametrizado en la BD, relacionado a cada uno de los planes disponibles.. [optional]  # noqa: E501
            terminal_id (str): Identificador de Terminal por el cual se envía la Transacción al Host.. [optional]  # noqa: E501
            terminal_trace (int): Número de Trace/Secuencia que genera la plataforma para la transacción asociado al TerminalID.. [optional]  # noqa: E501
            settlement_batch_number (int): Para aquellos host que exista el concepto de lote, es el número de lote al cual pertenece la transacción.. [optional]  # noqa: E501
            card_read_mode (str): Modo de ingreso de los datos de la tarjeta. Los posibles valores significan: C - EMV Chip / B - Banda magnética / L - Contactless Chip / S - Contactless Banda / M - Manual (Tarjeta Presente) / T - Digitada (Tarjeta no Presente) / E - ECOMMERCE (Ventas por Internet)  / F - FALLBACK (Banda por falla en Chip) / K - TOKEN / R - Recurring ( Pagos Recurrentes ). [optional]  # noqa: E501
            card_read_mode_description (str): Descripción del modo de ingreso con el que fue leída la tarjeta. [optional]  # noqa: E501
            card_description (str): Nombre de la Tarjeta que se usó en la transacción, usado para la impresión del voucher.. [optional]  # noqa: E501
            card_type_description (str): Descripción del modo de ingreso utilizado para capturar los datos de la tarjeta.. [optional]  # noqa: E501
            card_category (SaleResponseObjectSaleResponseCardCategory): [optional]  # noqa: E501
            card_number (str): Número de Tarjeta. En el caso de las respuestas el mismo estará enmascarado.. [optional]  # noqa: E501
            card_number_masked (str): Número de tarjeta enmascarado, según indica la parametrización en la base de datos. Se utilizará para imprimir en el cupón.. [optional]  # noqa: E501
            card_hashing (str): Hash de la tarjeta generado por la plataforma.. [optional]  # noqa: E501
            card_exp (str): Fecha de vencimiento de la tarjeta. Este dato sera necesario si el modo de ingreso fue manual/digitada.. [optional]  # noqa: E501
            card_cryptogram_response (str): Tags EMV en format TLV recibidos desde el Host.. [optional]  # noqa: E501
            card_app_name (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            card_app_identifier (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            card_app_label (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            card_auth_request_cryptogram (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            card_auth_response_cryptogram (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            payer (SaleObjectSalePayer): [optional]  # noqa: E501
            customer (SaleObjectSaleCustomer): [optional]  # noqa: E501
            merchant_category (SaleResponseObjectSaleResponseMerchantCategory): [optional]  # noqa: E501
            products ([SaleResponseObjectSaleResponseProducts]): Detalle de Productos de la Operación.. [optional]  # noqa: E501
            payment_method (SaleResponseObjectSaleResponsePaymentMethod): [optional]  # noqa: E501
            plans (SaleResponseObjectSaleResponsePlans): [optional]  # noqa: E501
            plan_description (str): Descripción del plan utilizado para para realizar la operación. [optional]  # noqa: E501
            plan_config_version (int): Identificador de Versión utilizada por Plataforma en la evaluación del Plan. [optional]  # noqa: E501
            tickets ([SaleResponseObjectSaleResponseTickets]): Elemento Compuesto que indica qué Tickets intervienen en la transacción y si deben ser digitalizados o impresos.. [optional]  # noqa: E501
            configuration (SaleResponseObjectSaleResponseConfiguration): [optional]  # noqa: E501
            card_holder_name (str): Nombre del tarjetahabiente obtenido de la tarjeta.. [optional]  # noqa: E501
            orig_answer_key (str): Identificador Unívoco de la Transacción que se quiere Referenciar, usado en Deposit, Void, Return, etc. O sea en las transacciones que hacen referencia a una Transacción previa. El valor fue obtenido en el campo o elemento AnswerKey de la Respuesta de la transacción referenciada. . [optional]  # noqa: E501
            orig_auth_date_time (datetime): Fecha y Hora de la Transacción previa que se está referenciando. - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14. [optional]  # noqa: E501
            orig_auth_ticket (int): Número de Ticket o Voucher de la Transacción Original Referenciada.. [optional]  # noqa: E501
            orig_auth_terminal_trace (int): Número de terminal de la Transacción previa que se está referenciando.. [optional]  # noqa: E501
            orig_auth_code (str): Código de autorización de la transacción original.. [optional]  # noqa: E501
            payment_method_id (int): ID de la marca con la cual la tarjeta fue identificada. [optional]  # noqa: E501
            payment_method_description (str): Descripción o nombre de la marca con la cual la tarjeta fue identificada. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.response_code = response_code
        self.response_actions = response_actions
        self.response_message = response_message
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, response_code, response_actions, response_message, *args, **kwargs):  # noqa: E501
        """DepositResponseObjectDepositResponse - a model defined in OpenAPI

        Args:
            response_code (int): Código de Respuesta Interno de la plataforma, el POS debe actuar por lo que indican las acciones especificadas en ResponseActions y no por el código de respuesta informado en este campo o elemento, pero es una buena práctica que sea persistido por el mismo.
            response_actions ([str]): Acciones a realizar por parte del POS y/o PINPAD en base al resultado de la operación que ha sido procesada. Cada uno de estos actions o acciones están concatenadas por comas. Los posibles actions son OK, Approve, Refuse, IssuerCall, Tickets, WithHold, GetCard, UseTerminalToAuthorize, ConfigurationError, SystemError, ResourceError, ProcessError, Completed, Configure, Display, EnableService y Print.
            response_message (str): Descripción del resultado del proceso del requerimiento recibido. Esta descripción es generada por la plataforma, no por el Host que termine resolviendo la transacción.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            company_identification (str): ID que identifica la companía desde donde proviene la petición.. [optional]  # noqa: E501
            system_identification (str): ID que identifica el sistema desde donde proviene la petición.. [optional]  # noqa: E501
            branch_identification (str): ID que identifica la sucursal desde donde proviene la petición. Esta sucursal pertenece a una determinada companía.. [optional]  # noqa: E501
            pos_identification (str): ID que identifica la caja o punto de venta desde donde proviene la petición. Este punto de venta pertenece a una determinada sucursal y companía.. [optional]  # noqa: E501
            foreign_response_code (str): Código de respuesta para el sistema externo, es decir, para la aplicación cliente que se comunica con el TEF.. [optional]  # noqa: E501
            request_type (str): Tipo de Operación que se requirió, contendrá el mismo valor que se recibió en el requerimiento, sobre formatos que no soportan elementos complejos o compuestos.. [optional]  # noqa: E501
            service_version (str): Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible.. [optional]  # noqa: E501
            sequence (str): Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma.. [optional]  # noqa: E501
            security ([SaleObjectSaleSecurity]): Datos asociados a la seguridad de la transacción o de elementos sensibles.. [optional]  # noqa: E501
            block (str): ID que identifica a un grupo de transacciones que serán confirmadas o canceladas. [optional]  # noqa: E501
            request_key (str): ID generado para la identificación por parte del Plataforma de la información generada en la ejecución de un GetCard o un Payment Method. Será necesario para que un mensaje de Sale, Void, Payment Method o Enrollment identifique el contexto generado y lo utilice para esa operación.. [optional]  # noqa: E501
            working_keys ([SaleResponseObjectSaleResponseWorkingKeys]): Nueva forma de enviar las llaves disponibles para esta caja.. [optional]  # noqa: E501
            required_information ([SaleResponseObjectSaleResponseRequiredInformation]): En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente.. [optional]  # noqa: E501
            answer_type (str): Tipo de Operación que se está requiriendo, solo necesario sobre formatos que no soportan elementos complejos o compuestos.. [optional]  # noqa: E501
            answer_key (str): Código de identificación, generado por Plataforma, de la operación realizada'.. [optional]  # noqa: E501
            public_answer_key (str): Código público de identificación, generado por Plataforma, de la operación realizada'.. [optional]  # noqa: E501
            was_reverse_previous (int): Flag indicador de generación de reversa para la última operación reversable.. [optional]  # noqa: E501
            reversed_answer_key (str): ID que identifica a la operación que acaba de ser reversada.. [optional]  # noqa: E501
            reversed_sequence (str): Secuencia de la transacción que fue reversada.. [optional]  # noqa: E501
            committed_block (str): ID del bloque de transacciones que ha sido confirmado de forma automática (es decir, sin recibir un requerimiento de BlockClose). Este escenario se presentará si el Plataforma así se ha configurado para actuar bajo esa circunstancia.. [optional]  # noqa: E501
            reversed_block (str): ID del bloque de transacciones que ha sido cancelado de forma automática (es decir, sin recibir un requerimiento de BlockClose). Este escenario se presentara si el Plataforma así se ha configurado para actuar bajo esa circunstancia.. [optional]  # noqa: E501
            message_id (str): Identificador Unívoco del Mensaje ( UUID v5 ).. [optional]  # noqa: E501
            server_address (str): Dirección IP del Server que atiende el requerimiento.. [optional]  # noqa: E501
            server_instance (str): Instancia de Server que atiende el requerimiento.. [optional]  # noqa: E501
            server_node_name (str): Nombre del Nodo que atendió el requerimiento.. [optional]  # noqa: E501
            adapter_input_version (str): Versión del  Adaptador de Protocolo Entrante que atiende el Requerimiento.. [optional]  # noqa: E501
            adapter_input_address (str): Dirección IP del Adaptador de Protocolo Entrante que atiende el requerimiento.. [optional]  # noqa: E501
            adapter_input_node_name (str): Nombre del Nodo del Adaptador de Protocolo Entrante que atiende el requerimiento.. [optional]  # noqa: E501
            adapter_output_version (str): Versión del  Adaptador de Protocolo Saliente que atiende el Requerimiento.. [optional]  # noqa: E501
            adapter_output_address (str): Dirección IP  del  Adaptador de Protocolo Saliente que atiende el Requerimiento.. [optional]  # noqa: E501
            adapter_output_node_name (str): Nombre del Nodo  del  Adaptador de Protocolo Saliente que atiende el Requerimiento.. [optional]  # noqa: E501
            additional_information ([SaleResponseObjectSaleResponseAdditionalInformation]): En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente.. [optional]  # noqa: E501
            printer_response_message ([str]): Información adicional/Mensaje promocional/Leyenda de respuesta a imprimir en el ticket de la operación. Cada línea de este mensaje sera un elemento dentro del array.. [optional]  # noqa: E501
            display_response_message ([str]): Información adicional/Mensaje promocional/Leyenda de respuesta a mostrar en pantalla en el ticket de la operación. Cada línea de este mensaje será un elemento dentro del array.. [optional]  # noqa: E501
            currency_code (str): código de Moneda - ISO 4217 <https://en.wikipedia.org/wiki/ISO_4217 Se puede utilizar la Codificación Alfabética o Numérica <br />   * Num   - Alpha - Description <br />   * '032' - 'ARS' - Pesos Argentinos <br />   * '152' - 'CLP' - Pesos Chilenos <br/>   * '484' - 'MXN' - Pesos Mexicanos <br/>   * '840' - 'USD' - dólares Americanos <br/>   * '878' - 'EUR' - Euros <br/>   * '858' - 'UYU' - Pesos Uruguayos <br/>   * '878' - 'EUR' - Euros <br/>   * '986' - 'BRL' - Real Brasileño. [optional]  # noqa: E501
            currency_description (str): Descripción del tipo de cambio utilizado en la transacción.. [optional]  # noqa: E501
            transaction_description (str): Tipo de transacción. [optional]  # noqa: E501
            transaction_resolution_mode (str): Modo en que fue realizada la transacción. [optional]  # noqa: E501
            currency_symbol (str): Símbolo monetario del tipo de cambio utilizado en la transacción.. [optional]  # noqa: E501
            facility_payments (int): Cantidad de cuotas utilizadas para realizar la operación. [optional]  # noqa: E501
            facility_type (int): Tipo de plan utilizado para para realizar la operación. [optional]  # noqa: E501
            value_facility_payments (float): Monto final a pagar en cada una de las cuotas en las que se divida la compra. [optional]  # noqa: E501
            amount (float): Importe o Monto de la Transacción.. [optional]  # noqa: E501
            alternative_amount (float): Monto con la que se realizó transacción. Si este valor es recibido, la búsqueda de los planes será limitada con este criterio.. [optional]  # noqa: E501
            amount_charged (float): Importe o Monto de la Transacción que efectivamente se cobró.  Si se envía en Void o Return en lugar de Amount, se genera un Ajuste si el Host lo soporta.. [optional]  # noqa: E501
            amount_to_apply (float): Importe o Monto de la Transacción a aplicar.. [optional]  # noqa: E501
            cashback_amount (float): Monto del dinero en efectivo (cashback).. [optional]  # noqa: E501
            tip_amount (float): Importe o Monto de la Propina.. [optional]  # noqa: E501
            request_amount (float): Monto libre de costos financerios e impuestos por el que la venta se realizó. El monto cobrado realmente no es este, dado que no incluye las tasas e impuestos. [optional]  # noqa: E501
            promoted_amount (float): Monto Sujeto a Promoción monto de la operación. [optional]  # noqa: E501
            credential_token (str): Token asociado a la Credencial Enrolada. [optional]  # noqa: E501
            credential_issuer_token (str): Emisor del Token asociado a la credencial enrolada. [optional]  # noqa: E501
            input_tokens ([SaleObjectSaleInputTokens]): Tokens.. [optional]  # noqa: E501
            output_tokens ([SaleObjectSaleInputTokens]): Tokens.. [optional]  # noqa: E501
            tax_financial_cost_amount (float): Monto del recargo impositivo aplicado al costo financiero que la transacción tiene. [optional]  # noqa: E501
            tax_financial_cost_percentage (float): Porcentaje de recargo impositivo a aplicar sobre el monto del costo financiero. [optional]  # noqa: E501
            financial_cost_amount (float): Monto del Costo financiero total generado en base al plan elegido. [optional]  # noqa: E501
            financial_cost_percentage (float): Porcentaje del costo financiero a aplicar al monto de la transacción. [optional]  # noqa: E501
            host_result_code (int): Código de Resultado retornado por el Host Adquirente.. [optional]  # noqa: E501
            host_message (str): Mensaje Retornado por el Host Adquirente, normalmente asociado al valor de HostResultCode. [optional]  # noqa: E501
            host_code (str): Código de autorización retornado por el Host que resuelve la transacción.. [optional]  # noqa: E501
            host_id (int): Número de identificación del host al cual fue enviada la petición, y por el cual fue finalmente procesada.. [optional]  # noqa: E501
            user_id (str): Identificador del usuario que está realizando la Transacción.. [optional]  # noqa: E501
            issuer_name (str): Nombre del Emisor de la Credencial o Tarjeta que se usó en la transacción.. [optional]  # noqa: E501
            host_date_time (datetime): Fecha y Hora de la transacción retornada por el Host que resuelve la Transacción - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14. [optional]  # noqa: E501
            transmition_date_time (datetime): Fecha y hora de transmisión de la operación hacia el host - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14. [optional]  # noqa: E501
            auth_result_code (str): Código de Resultado retornado por el Host Adquirente.. [optional]  # noqa: E501
            auth_host_process_code (str): Código de procesamiento de la operación enviada al host. Elemento 3 del protocolo de comunicaciones ISO 8583, formato de mensajes utilizado por los hosts para realizar operaciones financieras.. [optional]  # noqa: E501
            auth_host_msg_type (str): Elemento 0 del protocolo de comunicaciones ISO 8583, formato de mensajes utilizado por los hosts para realizar operaciones financieras. El valor de este campo es el que devuelve el host en una respuesta a una petición.. [optional]  # noqa: E501
            auth_host_message (str): Mensaje Retornado por el Host Adquirente, normalmente asociado al valor de AuthResultCode. [optional]  # noqa: E501
            host_msg_type (str): Elemento 0 del protocolo de comunicaciones ISO 8583, formato de mensajes utilizado por los hosts para realizar operaciones financieras. El valor de este campo es el que se envio al host en el envio de una petición.. [optional]  # noqa: E501
            auth_code (str): Código de autorización retornado por el Host que resuelve la transacción.. [optional]  # noqa: E501
            auth_date_time (datetime): Fecha y Hora de la transacción retornada por el Host que resuelve la Transacción - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14. [optional]  # noqa: E501
            auth_ticket (int): Número Ticket  o Voucher Generado para la Plataforma.. [optional]  # noqa: E501
            auth_rrn (str): Número de identificación de la transacción, utilizado por la mayoría de los hosts para realizar anulaciones y devoluciones.. [optional]  # noqa: E501
            transaction_authentication_type (str): Tipo de autenticación. [optional]  # noqa: E501
            identifier_for_the_adquirer (str): Identificador que genera el Host Adquirente para la Transacción. En algunos podrá ser igual al AuthRRN.. [optional]  # noqa: E501
            identifier_for_the_resolutor (str): Identificador que genera el Host o Plataforma que resuelve la transacción.. [optional]  # noqa: E501
            payment_facilitator_id (str): Identificador de facilitador de pagos o Payfac.. [optional]  # noqa: E501
            merchant_id (str): Número de comercio utilizado para realizar la transacción. Este Número es asignado por el host, y parametrizado en la BD, relacionado a cada uno de los planes disponibles.. [optional]  # noqa: E501
            terminal_id (str): Identificador de Terminal por el cual se envía la Transacción al Host.. [optional]  # noqa: E501
            terminal_trace (int): Número de Trace/Secuencia que genera la plataforma para la transacción asociado al TerminalID.. [optional]  # noqa: E501
            settlement_batch_number (int): Para aquellos host que exista el concepto de lote, es el número de lote al cual pertenece la transacción.. [optional]  # noqa: E501
            card_read_mode (str): Modo de ingreso de los datos de la tarjeta. Los posibles valores significan: C - EMV Chip / B - Banda magnética / L - Contactless Chip / S - Contactless Banda / M - Manual (Tarjeta Presente) / T - Digitada (Tarjeta no Presente) / E - ECOMMERCE (Ventas por Internet)  / F - FALLBACK (Banda por falla en Chip) / K - TOKEN / R - Recurring ( Pagos Recurrentes ). [optional]  # noqa: E501
            card_read_mode_description (str): Descripción del modo de ingreso con el que fue leída la tarjeta. [optional]  # noqa: E501
            card_description (str): Nombre de la Tarjeta que se usó en la transacción, usado para la impresión del voucher.. [optional]  # noqa: E501
            card_type_description (str): Descripción del modo de ingreso utilizado para capturar los datos de la tarjeta.. [optional]  # noqa: E501
            card_category (SaleResponseObjectSaleResponseCardCategory): [optional]  # noqa: E501
            card_number (str): Número de Tarjeta. En el caso de las respuestas el mismo estará enmascarado.. [optional]  # noqa: E501
            card_number_masked (str): Número de tarjeta enmascarado, según indica la parametrización en la base de datos. Se utilizará para imprimir en el cupón.. [optional]  # noqa: E501
            card_hashing (str): Hash de la tarjeta generado por la plataforma.. [optional]  # noqa: E501
            card_exp (str): Fecha de vencimiento de la tarjeta. Este dato sera necesario si el modo de ingreso fue manual/digitada.. [optional]  # noqa: E501
            card_cryptogram_response (str): Tags EMV en format TLV recibidos desde el Host.. [optional]  # noqa: E501
            card_app_name (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            card_app_identifier (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            card_app_label (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            card_auth_request_cryptogram (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            card_auth_response_cryptogram (str): Disponible solo con Tarjetas Chip (Incluye Contacless Chip), se debe imprimir en los Tickets/Vouchers.. [optional]  # noqa: E501
            payer (SaleObjectSalePayer): [optional]  # noqa: E501
            customer (SaleObjectSaleCustomer): [optional]  # noqa: E501
            merchant_category (SaleResponseObjectSaleResponseMerchantCategory): [optional]  # noqa: E501
            products ([SaleResponseObjectSaleResponseProducts]): Detalle de Productos de la Operación.. [optional]  # noqa: E501
            payment_method (SaleResponseObjectSaleResponsePaymentMethod): [optional]  # noqa: E501
            plans (SaleResponseObjectSaleResponsePlans): [optional]  # noqa: E501
            plan_description (str): Descripción del plan utilizado para para realizar la operación. [optional]  # noqa: E501
            plan_config_version (int): Identificador de Versión utilizada por Plataforma en la evaluación del Plan. [optional]  # noqa: E501
            tickets ([SaleResponseObjectSaleResponseTickets]): Elemento Compuesto que indica qué Tickets intervienen en la transacción y si deben ser digitalizados o impresos.. [optional]  # noqa: E501
            configuration (SaleResponseObjectSaleResponseConfiguration): [optional]  # noqa: E501
            card_holder_name (str): Nombre del tarjetahabiente obtenido de la tarjeta.. [optional]  # noqa: E501
            orig_answer_key (str): Identificador Unívoco de la Transacción que se quiere Referenciar, usado en Deposit, Void, Return, etc. O sea en las transacciones que hacen referencia a una Transacción previa. El valor fue obtenido en el campo o elemento AnswerKey de la Respuesta de la transacción referenciada. . [optional]  # noqa: E501
            orig_auth_date_time (datetime): Fecha y Hora de la Transacción previa que se está referenciando. - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14. [optional]  # noqa: E501
            orig_auth_ticket (int): Número de Ticket o Voucher de la Transacción Original Referenciada.. [optional]  # noqa: E501
            orig_auth_terminal_trace (int): Número de terminal de la Transacción previa que se está referenciando.. [optional]  # noqa: E501
            orig_auth_code (str): Código de autorización de la transacción original.. [optional]  # noqa: E501
            payment_method_id (int): ID de la marca con la cual la tarjeta fue identificada. [optional]  # noqa: E501
            payment_method_description (str): Descripción o nombre de la marca con la cual la tarjeta fue identificada. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.response_code = response_code
        self.response_actions = response_actions
        self.response_message = response_message
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")