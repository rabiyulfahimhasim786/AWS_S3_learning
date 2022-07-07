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

key = "foldername/filename.format"
filename = 'data1.json'# it is a downloading file format

s3 = ses.resource('s3')
s3.Bucket(BUCKET_NAME).download_file(key, filename)
