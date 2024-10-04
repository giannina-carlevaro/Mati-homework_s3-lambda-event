import aws_cdk as core
import aws_cdk.assertions as assertions

from prueba_ca_gianni.prueba_ca_gianni_stack import PruebaCaGianniStack

# example tests. To run these tests, uncomment this file along with the example
# resource in prueba_ca_gianni/prueba_ca_gianni_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PruebaCaGianniStack(app, "prueba-ca-gianni")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
