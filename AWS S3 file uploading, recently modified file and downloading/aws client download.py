#s3_client = boto3.client('s3')
#open('hello.txt').write('Hello, world!')

# Upload the file to S3
#s3_client.upload_file('hello.txt', 'MyBucket', 'hello-remote.txt')

# Download the file from S3
#s3_client.download_file('MyBucket', 'hello-remote.txt', 'hello2.txt')
#print(open('hello2.txt').read())
import boto3

ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
#ses = Session(aws_access_key_id=ACCESS_KEY,
#              aws_secret_access_key=SECRET_KEY)
#s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3_client.download_file('bucket_name', 'foldername/filename.format', 'data.json') 
#data.json is a downloading file name with format