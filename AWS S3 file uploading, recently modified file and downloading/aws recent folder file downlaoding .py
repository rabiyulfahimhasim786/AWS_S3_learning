from functools import reduce
import boto3

ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
#ses = Session(aws_access_key_id=ACCESS_KEY,
#              aws_secret_access_key=SECRET_KEY)
#s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

import boto3
#s3_client = s3
s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
response = s3_client.list_objects_v2(Bucket='bucket_name', Prefix='foldername')
all = response['Contents']        
latest = max(all, key=lambda x: x['LastModified'])
print(latest)
#print(latest.values())
list(reduce(lambda x, y: x + y, latest.items()))
a = list(reduce(lambda x, y: x + y, latest.items()))
print(a[1])

#file downloading 

from boto3 import Session
import string
import random

#ACCESS_KEY = "your access key"
##SECRET_KEY = "your_secret_key"
#REGION_NAME = "your bucket's region name"
#BUCKET_NAME = "your bucket name"
ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
#REGION_NAME = "US East (N. Virginia)"
BUCKET_NAME = "bucket_name"
#prefix = 'json/'
ses = Session(aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY)
              #region_name=REGION_NAME)

key = a[1]
filename = 'filename.csv'

s3 = ses.resource('s3')
s3.Bucket(BUCKET_NAME).download_file(key, filename)