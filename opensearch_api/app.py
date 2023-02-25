import json
import boto3
from opensearchpy import OpenSearch, helpers


def lambda_handler(event, context):
    
    domain_endpoint = 'search-cloudysky-opensearch-pj37jyxci4bp3x4f2whstjdrx4.us-east-1.es.amazonaws.com'
    index = 'cloudysky-cms-data'
    queryString = event['queryStringParameters']['q']
    
    # Get Secrets from Secrets Manager
    def get_secrets(secret_name):
        region_name = "us-east-1"
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name)
        return get_secret_value_response
    # Get Connection String
    def get_connection_string():
        user = get_secrets(secret_name="os-username")['SecretString']
        password = get_secrets(secret_name="os-password")['SecretString']
        connection_string = "https://{}:{}@{}:443".format(
            user, password, domain_endpoint)
        return connection_string
    
    # Search Documents within OpenSearch
    def search_documents(data):
        connection_string = get_connection_string()
        client = OpenSearch([connection_string])
        response = client.search(index=index, body={
            "query": { "match_phrase_prefix": { "title": {
                "query": data, "slop": 3, "max_expansions": 5} } }")
        return response
        
    response = search_documents(queryString)   
    print(response) 
    

    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": queryString,
        }),
    }
