import os

# Crear funcion "lambda_handler" que imprima en qué backet se desplegó y cuál es el nombre del archivo
def lambda_handler(event, context):
    print('Variables de entorno:', os.environ)
    print(f"Bucket: {event['Records'][0]['s3']['bucket']['name']}")
    print(f"File: {event['Records'][0]['s3']['object']['key']}")
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!!'
    }