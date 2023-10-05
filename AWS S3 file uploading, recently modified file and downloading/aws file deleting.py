import boto3
from boto3.session import Session

ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
session = Session(ACCESS_KEY,
                  SECRET_KEY)

# s3_client = session.client('s3')
s3_resource = session.resource('s3')
my_bucket = s3_resource.Bucket(BUCKET_NAME)

response = my_bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': 'json/page_2.pdf'   # the_name of_your_file #the foldername with file name
            }
        ]
    }
)
