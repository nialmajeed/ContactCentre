import boto3
import json

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Extract phone number from Contact Flow event
    phone_number = event['Details']['ContactData']['CustomerEndpoint']['Address']
    print(phone_number)

    # Query DynamoDB table
    try:
        TableName= dynamodb.Table('C-Foundation-Table')  # Replace with your table name
        dbResponse = TableName.get_item( Key = {'PhoneNumber': str(phone_number)})
        dbFname = dbResponse['Item']['FirstName']
        return {'FirstName': dbFname}


    except Exception as e:
        print(f"Error: {e}")
        return {'FirstName': 'Error'}