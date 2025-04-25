import boto3
import json

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Extract phone number from Contact Flow event
    phone_number = event['Details']['ContactData']['CustomerEndpoint']['Address']

    # Query DynamoDB table
    try:
        response = dynamodb.query(
            TableName='C-Foundation-Table',  # Replace with your table name
            KeyConditionExpression='"Phone Number" = :p',
            ExpressionAttributeValues={
                ':p': {'S': "Phone Number"}
            }
        )

 if response['Items']:
            item = response['Items'][0]  # Assuming only one match per phone number
            customer_name = f"{item.get('FirstName', {}).get('S', '')} {item.get('LastName', {}).get('S', '')}"
            return {'customerName': customer_name}
        else:
            return {'customerName': ' '}

    except Exception as e:
        print(f"Error: {e}")
        return {'customerName': 'Error'}


    
