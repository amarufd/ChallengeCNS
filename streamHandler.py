from utils.IsMutateError import *
import time, json
import sys, traceback
import boto3

def actualiza_contador(event, context):
    try:
        print("INI:")
        print(event)
        print("-------------------------")
        
        eventoJson = json.loads(event['Records'])

        print("-------------------------")
        print(eventoJson)
        
        # se carga body
        # jsonADN = json.loads(event['body'])
        # jsonADN = jsonADN['dna']
        # mxADN = [list(item) for item in jsonADN]
       
        esMutante = True
        mutante = int(esMutante)
        humano = int(not esMutante)
        
        dynamodb = boto3.client('dynamodb')
        response = dynamodb.update_item(Key={'id': 1},
            UpdateExpression="set count_mutant_dna=count_mutant_dna+:m, count_human_dna=count_human_dna+:h",
            ExpressionAttributeValues={
                ':m': mutante,
                ':h': humano
            },
            ReturnValues="UPDATED_NEW"
        )

        body = {
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        # return response
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
        # return response