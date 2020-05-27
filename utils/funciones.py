import json
import boto3
import os
import sys, traceback
from utils.IsMutateError import *

awsSecretStoreArn = os.environ['awsSecretStoreArn'],
database = 
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
            database = database,
            resourceArn = os.environ['dbClusterOrInstanceArn'],
            sql = sqlInsert
        )

        return 0
    
    except ServicioError as e:
        print("error de servicio")

        return -1

    except IsMutateError as e:
        print("error de negocio")

        return -1
        
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())
        print (e)
        return -1
        

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


def consultaEstadisticas():
    try:
        client = boto3.client('rds-data')
        
        response = client.execute_statement(
            continueAfterTimeout=False,
            secretArn = os.environ['awsSecretStoreArn'],
            database = database,
            resourceArn = os.environ['dbClusterOrInstanceArn'],
            sql = "SELECT COUNT( * ) FROM CONSULTASDNA WHERE ISMUTANT IS TRUE"
        )

        mutantes = 0
        for user in response['records']:
            mutantes = user[0]['longValue']

        response = client.execute_statement(
            continueAfterTimeout=False,
            secretArn = os.environ['awsSecretStoreArn'],
            database = database,
            resourceArn = os.environ['dbClusterOrInstanceArn'],
            sql = "SELECT COUNT( * ) FROM CONSULTASDNA WHERE ISMUTANT IS FALSE"
        )

        humanos = 0
        for user in response['records']:
            humanos = user[0]['longValue']

        return mutantes,humanos


    except ServicioError as e:
        print("error de servicio")

        return -1,-1

    except IsMutateError as e:
        print("error de negocio")

        return -1,-1
        
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())
        print (e)
        return -1,-1