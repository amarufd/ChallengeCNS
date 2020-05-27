# Lambda isMutate an statistic  #

### Descripción ###

* Ejercicio que analiza si el DNA recibido por el servicio es de un mutante o humano.
* Creando estadistica de ello

### endpoints

isMutate
statistic



### Instalación y configuración ###

#### Dependencias: 
* [AWS-Cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

##### Instrucciones de deploy:

Al momento de deployar los lambdas deben estar definidas las siguientes variables:
* **awsSecretStoreArn**: storage donde se encuentran las llaves de acceso a la base de datos
* **database**: nombre de la base de datos
* **dbClusterOrInstanceArn**: arn del cluster de base de datos


Ejecutar el comando deploy
```sh
$ serverless deploy

```



