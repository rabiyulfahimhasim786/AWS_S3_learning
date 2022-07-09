from functools import reduce
import boto3

ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
#ses = Session(aws_access_key_id=ACCESS_KEY,
#              aws_secret_access_key=SECRET_KEY)
#s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

import boto3
#s3_client = s3
s3=boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
list=s3.list_objects(Bucket='bucket_name',  Prefix='foldername')['Contents']
for s3_key in list:
    s3_object = s3_key['Key']
    if not s3_object.endswith("/"):
        s3.download_file('bucket_name', s3_object, s3_object)
    else:
        import os
        if not os.path.exists(s3_object):
            os.makedirs(s3_object)