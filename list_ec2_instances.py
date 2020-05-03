import boto3
import os
"""list all the EC2 instances and their status. This can be done by using both resource object and client object. 
For client object, values are retrieved from the dictionary 
"""
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_ACCESS_KEY_SECRET = os.environ['AWS_ACCESS_KEY_SECRET']

session_obj = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,  aws_secret_access_key=AWS_ACCESS_KEY_SECRET)

#using resource object
ec2_res_obj = session_obj.resource(service_name='ec2')
for instance in ec2_res_obj.instances.all():
    print(instance.id, instance.state['Name'])

#using client object
ec2_client_obj = session_obj.client(service_name='ec2')

for reservation in ec2_client_obj.describe_instances()['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance['State']['Name'])