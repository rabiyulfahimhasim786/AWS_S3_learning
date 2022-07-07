from boto3 import Session
import string
import random

#ACCESS_KEY = "your access key"
#SECRET_KEY = "your_secret_key"
#REGION_NAME = "your bucket's region name"
#BUCKET_NAME = "your bucket name"

ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
#REGION_NAME = "your bucket's region name"
#BUCKET_NAME = "tesxtractkvtable-us-east-1-660866612853"
#prefix = 'async-kv-table/'
BUCKET_NAME = "bucket_naem"
#prefix = 'json/'
ses = Session(aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY)
              #region_name=REGION_NAME)
key = 'json/filename.format'
#key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
file = 'filename.format'
content_type = 'application/json'#format name example - json formats
s3 = ses.resource('s3')

s3.Bucket(BUCKET_NAME).put_object(Key=key, Body=open(file, 'rb'),  ContentType=content_type)
#s3.Bucket(BUCKET_NAME).put_object(Key=key, Body=open(file, 'rb'),  ACL='public-read', ContentType=content_type)