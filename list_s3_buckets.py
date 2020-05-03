import boto3
import os
"""connect AWS and list all the bucket names"""
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_ACCESS_KEY_SECRET = os.environ['AWS_ACCESS_KEY_SECRET']

s3_obj = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,  aws_secret_access_key=AWS_ACCESS_KEY_SECRET)

for bucket in s3_obj.buckets.all():
    print(bucket.name)
