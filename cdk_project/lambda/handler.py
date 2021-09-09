def handler(event, context):
    return {
        'body': 'Hello from the new staged Lambda!',
        'statusCode': '200'
    }