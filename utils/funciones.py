import json
import boto3
import os
import sys, traceback
from utils.IsMutateError import *

awsSecretStoreArn = os.environ['awsSecretStoreArn'],
database = os.environ['database']
dbClusterOrInstanceArn = os.environ['dbClusterOrInstanceArn']

#Funciones
# GuardarRegistro
def guardarRegistro(respuesta,jsonADN):
    try:
        client = boto3.client('rds-data')

        strADN = jsonADN[0]
        for ele in range(len(jsonADN)-1):
            strADN += "-"+jsonADN[ele+1]

        sqlInsert = ("""insert into `CONSULTASDNA` (`ISMUTANT`, `DNA`) values( %s, '%s')""" % (respuesta, strADN))
        print(sqlInsert)
        
        response = client.execute_statement(
            continueAfterTimeout=False,
            secretArn = os.environ['awsSecretStoreArn'],
            database = "isMutant",
            resourceArn = os.environ['dbClusterOrInstanceArn'],
            sql = sqlInsert
        )
    except ServicioError as e:
        print("error de servicio")

        body = {
            "mensaje": str(e)
        }

        response = {
            "statusCode": 500,
            "body": json.dumps(body)
        }
        return response

    except IsMutateError as e:
        print("error de negocio")

        body = {
           "mensaje": str(e)
        }

        response = {
           "statusCode": 409,
           "body": json.dumps(body)
        }
        return response
        
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())


        print (e)
        body = {
            "mensaje": "Error al realizar la consulta",
            "ex": str(e)
        }

        response = {
            "statusCode": 500,
            "body": json.dumps(body)
        }
        return response
        

def selectRegistros():
    client = boto3.client('rds-data')
        
    response = client.execute_statement(
        continueAfterTimeout=False,
        secretArn = os.environ['awsSecretStoreArn'],
        database = database,
        resourceArn = os.environ['dbClusterOrInstanceArn'],
        sql = "SELECT * FROM CONSULTASDNA"
    )
        
        
        
    for user in response['records']:
        Rid     = user[0]['longValue']
        RisMut = user[1]['booleanValue']
        Rdna  = user[2]['stringValue']
        print(Rid , ' ' , RisMut , ' ' , Rdna)
