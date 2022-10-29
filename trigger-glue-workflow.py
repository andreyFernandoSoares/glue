import json
import boto3

glue = boto3.client(service_name='glue', region_name='us-east-1') 

def lambda_handler(event, context):
    # TODO implement
    workflow_run_id = glue.start_workflow_run(Name = 'best-plataform-workflow')
    
    return {
        'statusCode': 200,
        'body': json.dumps(workflow_run_id)
    }
