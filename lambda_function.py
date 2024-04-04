import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    print("Data")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World!')
    }
