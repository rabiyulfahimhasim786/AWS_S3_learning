import boto3
from botocore.exceptions import ClientError
import datetime
#from datetime import datetime, timedelta
from datetime import timedelta
 
 

ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
def Fetch_url(last_modified_timestamp):
    s3_files_path = "s3://bucketname/tables"
    if 's3://' not in s3_files_path:
        raise Exception('Given path is not a valid s3 path.')

    session = boto3.session.Session()
    s3_resource = session.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    bucket_token = s3_files_path.split('/')
    bucket = bucket_token[2]
    folder_path = bucket_token[3:]
    prefix = ""
    for path in folder_path:
        prefix = prefix + path + '/'
    try:
        result = s3_resource.meta.client.list_objects(Bucket=bucket, Prefix=prefix)
    except ClientError as e:
        raise Exception("boto3 client error in list_all_objects_based_on_last_modified function: " + e.__str__())
    except Exception as e:
        raise Exception(
            "Unexpected error in list_all_objects_based_on_last_modifiedfunction of s3 helper: " + e.__str__())
    filtered_file_names = []
    for obj in result['Contents']:
        if str(obj["LastModified"]) >= str(last_modified_timestamp):
            full_s3_file = "s3://" + bucket + "/" + obj["Key"] #for S3 browser URL fetching
            #full_s3_file = "https://" + bucket + ".s3.amazonaws.com/" + obj["Key"] #For https URL fetching
            filtered_file_names.append(full_s3_file)
    return filtered_file_names

#x = datetime.datetime.now()
#print(x)
#print(Fetch_url(x)) 
newTime = datetime.datetime.now() - datetime.timedelta(days=2)
#vTime = datetime.datetime.now() - datetime.timedelta(minutes=2)

print(Fetch_url(newTime))
#print(Fetch_url("2022-07-01 12:19:56.986445+00:00")) 
