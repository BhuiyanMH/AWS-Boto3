import boto3
import os
"""list all the EC2 instances and their status by Region."""

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_ACCESS_KEY_SECRET = os.environ['AWS_ACCESS_KEY_SECRET']
#create the session object
session_obj = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,  aws_secret_access_key=AWS_ACCESS_KEY_SECRET)

#get all the regions
ec2_client_obj = session_obj.client(service_name='ec2')
regions = ec2_client_obj.describe_regions()
region_names = []
for region in regions['Regions']:
    region_names.append(region['RegionName'])

for region_name in region_names:
    temp_session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,  aws_secret_access_key=AWS_ACCESS_KEY_SECRET, region_name=region_name)
    print("EC2 instance in region: ", region_name)
    resource = temp_session.resource(service_name='ec2')
    for instance in resource.instances.all():
        print(instance.id, instance.name, instance.state['Name'])
