import aws_cdk as core
import aws_cdk.assertions as assertions

from traffic_api.traffic_api_stack import TrafficApiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in traffic_api/traffic_api_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TrafficApiStack(app, "traffic-api")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
