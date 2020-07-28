
# Lambda invocation count

A toolkit to run lambda functions and keep a counter on the number of invocations

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python
Pip
awscli


### Installing

In your local repository, 

zip the python file to invoke into the lambda

Note: Python modules used in the code work in Lambda. If there is any error with the modules, before zipping the code, please run the following in your local repository

pip install -t . boto3
pip install -t . flask


### If you are running with lockstack


Arrange the localstack environment by following the steps from - https://github.com/localstack/localstack 

Suggested solution is running docker-compose up by downloading the docker-compose.yaml file from the localstack repository

Create a Lambda function in the localstack environment using the following command:

aws --endpoint-url=http://localhost:4574 lambda create-function \
    --region {preferred region} \
    --function-name {give a valid function name}  \
    --runtime {python runtime in your local} \
    --handler {app.handler} \
    --memory-size 128  \
    --zip-file fileb://{zip_file} \
    --role arn:aws:iam::tmp:role/lambda-ex

Create a dynamodb table in the localstack environment using the following command for stroing the count:

aws --endpoint-url=http://localhost:4569  dynamodb create-table   \
    --table-name {table_name}     \
    --attribute-definitions         \
    AttributeName={attribute_name},AttributeType=S    \
    --key-schema         \
    AttributeName=(attribute_name),KeyType=HASH \
    --provisioned-throughput      \
    ReadCapacityUnits=10,WriteCapacityUnits=5

Once lambda function and dynamodb table are created, please follow the below steps to invoke a function

aws --endpoint-url=http://localhost:4574/ lambda invoke --function-name {function name} {local_file}







