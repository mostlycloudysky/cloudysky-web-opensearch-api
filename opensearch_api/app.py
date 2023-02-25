import json
# import requests

def lambda_handler(event, context):
    
    queryString = event['queryStringParameters']['q']
    print(queryString)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": queryString,
        }),
    }
