
#AWS s3
import boto3
import os
from functools import reduce
import boto3
ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"

s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
#def download_dir(prefix, local, bucket, client=s3_client):
def download_dir(request):
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = s3_client.list_objects_v2(Bucket='bucketname', Prefix='S3foldername')
    all = response['Contents']        
    latest = max(all, key=lambda x: x['LastModified'])
    print(latest)
        #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    b = list(reduce(lambda x, y: x + y, latest.items()))
    print(b[1])

        #file downloading 
        #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    bb = list(reduce(lambda x, y: x + y, latest.items()))
        #print(a[1])
    urllinks = bb[1]
    data = urllinks[0:71]
    prefix = data
    local = 'localfoldername'
    bucket = 'bucketname'
    client=s3_client
    keys = []
    dirs = []
    next_token = ''
    base_kwargs = {
        'Bucket':bucket,
        'Prefix':prefix,
    }
    while next_token is not None:
        kwargs = base_kwargs.copy()
        if next_token != '':
            kwargs.update({'ContinuationToken': next_token})
        results = client.list_objects_v2(**kwargs)
        contents = results.get('Contents')
        for i in contents:
            k = i.get('Key')
            if k[-1] != '/':
                keys.append(k)
            else:
                dirs.append(k)
        next_token = results.get('NextContinuationToken')
    for d in dirs:
        dest_pathname = os.path.join(local, d)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
    for k in keys:
        dest_pathname = os.path.join(local, k)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
        client.download_file(bucket, k, dest_pathname)
    #download_dir(urllinks[0:71], 'localfoldername', 'bucketname', client=s3_client)
    return HttpResponse("Hello world")
    #download_dir('S3foldername', 'localfoldername', 'bucketname', client=s3_client)
