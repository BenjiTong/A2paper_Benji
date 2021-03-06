# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:   
# https://aws.amazon.com/developers/getting-started/python/

import boto3
import json
import base64
from botocore.exceptions import ClientError
import mysql.connector


class Sec_Mysql:

    global conn 
    conn = None

    def get_mysql_conn():

        global conn
        if conn != None and conn.is_connected():
            return conn

        secret_name = "MyRDSInstanceRotationSecret-8guDf8SkolUm"
        region_name = "us-east-1"


        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
        # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        # We rethrow the exception by default.

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            # if e.response['Error']['Code'] == 'DecryptionFailureException':
            #     # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            #     # Deal with the exception here, and/or rethrow at your discretion.
            #     raise e
            # elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            #     # An error occurred on the server side.
            #     # Deal with the exception here, and/or rethrow at your discretion.
            #     raise e
            # elif e.response['Error']['Code'] == 'InvalidParameterException':
            #     # You provided an invalid value for a parameter.
            #     # Deal with the exception here, and/or rethrow at your discretion.
            #     raise e
            # elif e.response['Error']['Code'] == 'InvalidRequestException':
            #     # You provided a parameter value that is not valid for the current state of the resource.
            #     # Deal with the exception here, and/or rethrow at your discretion.
            #     raise e
            # elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            #     # We can't find the resource that you asked for.
            #     # Deal with the exception here, and/or rethrow at your discretion.
                                
            print("Database client error due to {}".format(e))          
            raise e
        else:
            # Decrypts secret using the associated KMS CMK.
            # Depending on whether the secret is a string or binary, one of these fields will be populated.
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                 # Your code goes here. 
                # {
                #   "password": "assdfDaRU'",
                #   "engine": "mysql",
                #   "port": 3306,
                #   "dbInstanceIdentifier": "a2onlinemaindb",
                #   "host": "a2onlinemaindb.czthotmsn29q.ap-southeast-1.rds.amazonaws.com",
                #   "username": "admin"
                # }
                data = json.loads(secret)
                try:
                    conn =  mysql.connector.connect(host=data['host'], user=data['username'], passwd=data['password'], port=data['port'], database='main')
                    print('db connected!')
                except Exception as e:
                    print("Database connection failed due to {}".format(e))          
                return conn
            else:
                decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])