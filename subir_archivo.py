import boto3
import json
import base64

def lambda_handler(event, context):

    body = json.loads(event["body"])

    bucket = body["bucket"]
    directorio = body["directorio"]
    archivo = body["archivo"]

    contenido_base64 = body["contenido"]

    contenido = base64.b64decode(contenido_base64)

    s3 = boto3.client("s3")

    s3.put_object(
        Bucket=bucket,
        Key=f"{directorio}/{archivo}",
        Body=contenido
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "mensaje": "Archivo cargado correctamente",
            "archivo": archivo
        })
    }
