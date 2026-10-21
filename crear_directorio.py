import boto3
import json

def lambda_handler(event, context):

    body = json.loads(event["body"])

    bucket = body["bucket"]
    directorio = body["directorio"]

    s3 = boto3.client("s3")

    s3.put_object(
        Bucket=bucket,
        Key=directorio + "/"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "mensaje": "Directorio creado correctamente",
            "bucket": bucket,
            "directorio": directorio
        })
    }
