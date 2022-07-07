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
#print(latest.values())
list(reduce(lambda x, y: x + y, latest.items()))
a = list(reduce(lambda x, y: x + y, latest.items()))
#print(a[1])
urllink = a[1]
#https://ocr-textract-key-value-output.s3.amazonaws.com/json/data.json
url = f"https://bucket_name.s3.amazonaws.com/{urllink}" 
# please change url based on bucket_name accordingly
print(url)
