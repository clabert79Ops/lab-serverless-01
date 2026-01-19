def handler(event, context):
    print("Event:", event)
    return {
        "statusCode": 200,
        "body": "Deployed with AWS CDK"
    }