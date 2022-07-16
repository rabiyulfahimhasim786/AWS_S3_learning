
import boto3
from botocore.exceptions import ClientError
import datetime
#from datetime import datetime, timedelta
from datetime import timedelta


ACCESS_KEY = "ACCESS_KEY" # replace with your ACCESS_KEY
SECRET_KEY = "SECRET_KEY" # replace with your SECRET_KEY
from functools import reduce
import boto3
#import boto3

s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
response = s3_client.list_objects_v2(Bucket='bucket_name', Prefix='subfoldername') # replace with your bucket name and folder name
all = response['Contents']        
latest = max(all, key=lambda x: x['LastModified'])
#print(latest)
#print(latest.values())
list(reduce(lambda x, y: x + y, latest.items()))
a = list(reduce(lambda x, y: x + y, latest.items()))
#print(a[1])

#file downloading 
#print(latest.values())
list(reduce(lambda x, y: x + y, latest.items()))
a = list(reduce(lambda x, y: x + y, latest.items()))
#print(a[1])
urllink = a[1]
testurl = urllink[0:72]
print(testurl)
prefix = testurl
#prefix = "subfolder1/subfolder2/"
s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)#)
bucket = s3.Bucket(name="bucket_name") # replace with your bucket name
filtered_file_names =[]
FilesNotFound = True
for obj in bucket.objects.filter(Prefix=prefix):
     #print('{0}:{1}'.format(bucket.name, obj.key))
     #full_s3_file = '{0}/{1}'.format(bucket.name, obj.key)
     #filtered_file_names.append('{0}/{1}'.format(bucket.name, obj.key))
     #full_s3_file = 'https://{0}.s3.amazonaws.com/{1}'
     filtered_file_names.append('https://{0}.s3.amazonaws.com/{1}'.format(bucket.name, obj.key))
     #https://{0}.s3.amazonaws.com/{1}
     #print(filtered_file_names)
     FilesNotFound = False
print(filtered_file_names)
if FilesNotFound:
     print("ALERT", "No file in {0}/{1}".format(bucket, prefix))
