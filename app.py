import boto3
from flask import Flask
import json

app = Flask(_name_)

@app.route("/counter")

def hello():
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4569')
 
        table = dynamodb.Table('counter')

        count = 1
        response = table.get_item(Key={'Count': 'requestCount'})

        if 'Item' not in response:
            response_put = table.put_item(
                Item={
                    'Count': 'requestCount',
                    'Value': count
                }
            )
        else:
            count = int(response['Item']['value']) + 1
            response_put = table.put_item(
                Item={
                    'Count': "requestCount",
                    'Value': count
                }
            )
        
        get_request_count = table.get_item(Key={'Count': 'requestCount'})

        count = get_request_count['Item']['Value']

        return str(count)

def handler():
    if _name_ == "_main_":
        app.run(debug=True)

