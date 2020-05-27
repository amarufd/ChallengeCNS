[![](https://www.consorcio.cl/documents/10180/13865848/logo-consorcio-home.png)](https://consorcio.cl)
# Lambda Cotizadores proyeccion ahorro.  #

### Descripción ###

* Proyecto Serverless Service cuya finalidad es entregar la proyección de ahorro.

### Backend (alias) asociado


on-crm-sales-negocio

### Instalación y configuración ###

#### Dependencias: 
* [AWS-Cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

##### Instrucciones de deploy:

Los parámetros para el deploy a tener en cuenta son los siguientes:
* **cc**: Centro de Costos asociado al ambiente donde se está instalando. Valor por defecto=55100
* **proyecto**: Nombre del proyecto asociado al requerimiento de desarrollo (se sugiere omitir y dejar por defecto)
* **layerStage**: ambiente en cual se está instalado, valores posibles: dev, qa, prod
* **urlBaseMicroservicios**: URL base de microservicios. 


Ejecutar el comando deploy en QA
```sh
$ serverless deploy --cc 26850 --layerStage QA

```

Ejecutar el comando deploy en dev
```sh
$ serverless deploy --cc 26850 --layerStage dev

```

##### Instrucciones para desarrollo local:
Para probar localmente ejecutar lo siguiente:
```sh
sls offline --noTimeout
```



