# aws-local
An example repo allowing AWS development locally

## Requirements
- Use https://github.com/localstack/localstack to create a local aws project env
- Create a lambda with your language of choice that allows a `GET` at `/counter` returning the times the services has been invoked
- Store the current count in a DynamoDB and retrieve it with your lambda
- the above should work on your machine and should be recreatable by anyone cloning the repo

## Bonus
- Deploy the above to AWS with Terraform
