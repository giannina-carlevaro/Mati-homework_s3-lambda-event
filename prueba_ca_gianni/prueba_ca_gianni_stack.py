from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_lambda as lambda_,
    aws_lambda_event_sources as eventsources,
    RemovalPolicy,
    )
from constructs import Construct

PROJECT = 'hello-cdk'

class PruebaCaGianniStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # Crear el bucket S3
        bucket = s3.Bucket(self, "MyFirstBucket",
                       bucket_name=f"{PROJECT}-bucket-cagianni",
                       block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                       encryption=s3.BucketEncryption.S3_MANAGED,
                       versioned=True,
                       auto_delete_objects=True,
                       removal_policy=RemovalPolicy.DESTROY)

        # Crear la función Lambda
        lambda_function = lambda_.Function(self, "lambda-hello-cdk",
                                           function_name=f"{PROJECT}-function",
                                           description="Lambda function to handle S3 events",
                                           runtime=lambda_.Runtime.PYTHON_3_9,
                                           handler="lambda_function.lambda_handler",
                                           code=lambda_.Code.from_asset("scripts/lambdas"),
                                           )

        # Asociar la función Lambda con el bucket S3
        # notification = s3n.LambdaDestination(lambda_function)
        # notification.bind(self, bucket)
        # bucket.add_event_notification(s3.EventType.OBJECT_CREATED, notification)

        # Evento sobre bucket Content para la activacion de la segunda Lambda 'read_textract_function'
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            # s3n.LambdaDestination(read_textract_function),
            s3n.LambdaDestination(lambda_function),
        )