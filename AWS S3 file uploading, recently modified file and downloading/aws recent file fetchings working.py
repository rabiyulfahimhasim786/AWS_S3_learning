from datetime import datetime

import boto3
ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
#ses = Session(aws_access_key_id=ACCESS_KEY,
#              aws_secret_access_key=SECRET_KEY)
s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

#my_bucket = s3.Bucket('ocr-textract-key-value-output')
my_bucket = s3.Bucket('bucket_name')
last_modified_date = datetime(1939, 9, 1).replace(tzinfo=None)
for file in my_bucket.objects.all():
    file_date = file.last_modified.replace(tzinfo=None)
    if last_modified_date < file_date:
        last_modified_date = file_date

print(last_modified_date)

# you can have more than one file with this date, so you must iterate again
for file in my_bucket.objects.all():
    if file.last_modified.replace(tzinfo=None) == last_modified_date:
        print(file.key)
        #print(last_modified_date)