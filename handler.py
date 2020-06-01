from utils.IsMutateError import *
#import numpy as np
import time, json
import sys, traceback
import boto3
import os

def ismutate(event, context):
    try:
        start_time = time.time()

        print(event['body'])
        
        # se carga body
        jsonADN = json.loads(event['body'])
        jsonADN = jsonADN['dna']
        mxADN = [list(item) for item in jsonADN]

        respuesta,tiempoEjecucion = isMutateUnFor(mxADN)

        print("Respuesta: ",respuesta," - Tiempo Ejecucion: ",tiempoEjecucion)
        
        
        body = {
            "isMutate": respuesta,
            "tiempo": tiempoEjecucion
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        dynamodb = boto3.client('dynamodb')
        dynamodb.put_item(TableName=os.environ['DNAS_TABLE'], Item={'cadenaDna':{'S': event['body']}, 'esMutante':{'S': str(respuesta)}})

        return response


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


def stats(event, context):
    try:
        dynamodb = boto3.client('dynamodb')
        response = dynamodb.get_item(Key={'id': 1})

        return response['Item']
        
        # response = {
        #     "count_mutant_dna": 200,
        #     "count_human_dna": json.dumps(body),
        #     "ratio": 
        # }
    
    except Exception as e:
        print(traceback.format_exc())

def isMutateUnFor(mxADN):
    start_time = time.time()
    conteoMutate = 0

    for secuencia in range(len(mxADN)*len(mxADN[1])):
        # diagonal abajo atras
        col = secuencia % len(mxADN[1])
        fila = secuencia // len(mxADN[1])
    
        if(mxADN[fila][col] != 0):
            if(((col - 3)>=0) & ((fila + 3) < len(mxADN))):
                if((mxADN[fila][col] == mxADN[fila-1][col-1]) & (mxADN[fila][col] == mxADN[fila-2][col-2]) & (mxADN[fila][col] == mxADN[fila-3][col-3]) & (mxADN[fila][col] != 0)):
                    conteoMutate += 1
        
            # diagonal abajo adelante
            if(((col + 3) < len(mxADN[fila])) & ((fila + 3) < len(mxADN))):
                if((mxADN[fila][col] == mxADN[fila+1][col+1]) & (mxADN[fila][col] == mxADN[fila+2][col+2]) & (mxADN[fila][col] == mxADN[fila+3][col+3]) & (mxADN[fila][col] != 0)):
                    conteoMutate += 1
            
            # columna abajo
            if(((fila + 3) < len(mxADN))):
                if((mxADN[fila][col] == mxADN[fila+1][col]) & (mxADN[fila][col] == mxADN[fila+2][col]) & (mxADN[fila][col] == mxADN[fila+3][col]) & (mxADN[fila][col] != 0)):
                    conteoMutate += 1
                    
            # fila lado
            if(((col + 3) < len(mxADN[fila]))):
                if((mxADN[fila][col] == mxADN[fila][col+1]) & (mxADN[fila][col] == mxADN[fila][col+2]) & (mxADN[fila][col] == mxADN[fila][col+3]) & (mxADN[fila][col] != 0)):
                    conteoMutate += 1
            
            if conteoMutate >= 2:
                return conteoMutate >= 2, (time.time() - start_time)
    
    return conteoMutate >= 2, (time.time() - start_time)

