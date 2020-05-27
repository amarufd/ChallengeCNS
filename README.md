# Lambda isMutate y statistic  #

### Descripción ###

Ejercicio que analiza si el DNA recibido por el servicio es de un mutante o humano y crea estadistica de ello

### endpoints

post - https://tkx47lnfx9.execute-api.us-east-2.amazonaws.com/dev/ismutate

```json
{
    "dna": [
        "ATGTGA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCGTA",
        "TCACTG"
    ]
}

```

get - https://tkx47lnfx9.execute-api.us-east-2.amazonaws.com/dev/statistic

### Instalación y configuración ###

#### Dependencias: 
* [AWS-Cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

##### Instrucciones de deploy:

Para que los servicios logren conexión con la base de datos en el archivo **serverless.yaml** se deben completar las siguientes variables:
* **awsSecretStoreArn**: storage donde se encuentran las llaves de acceso a la base de datos
* **database**: nombre de la base de datos
* **dbClusterOrInstanceArn**: arn del cluster de base de datos


Ejecutar el comando deploy
```sh
$ serverless deploy

```
El comando anterior ejecuta la creacion de los lambdas y la creacion de cluster de base de datos


