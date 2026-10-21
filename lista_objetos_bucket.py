import boto3
import json

def lambda_handler(event, context):

    body = json.loads(event["body"])

    nombre_bucket = body["bucket"]

    s3 = boto3.client("s3")

    respuesta = s3.list_objects_v2(
        Bucket=nombre_bucket
    )

    objetos = []

    for obj in respuesta.get("Contents", []):
        objetos.append(obj["Key"])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "objetos": objetos
        })
    }
