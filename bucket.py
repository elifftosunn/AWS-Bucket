import boto3
from boto3.session import Session

ACCESS_KEY = ''
SECRET_KEY = ''
bucket_name = ''

session = Session(aws_access_key_id=ACCESS_KEY,
                aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')

bucket = s3.Bucket(bucket_name)

def list_bucket():
    for s3_file in bucket.objects.all():
        print(s3_file.key)

list_bucket()



def download_file():
    bucket.download_file('6Aug_accessKeys.csv', './6Aug_accessKeys.csv')

download_file()


def upload_file():
    local_path = './t1.txt'
    bucket_path = 't1.txt'

    s3.meta.client.upload_file(Filename=local_path, Bucket=bucket_name, Key=bucket_path)

upload_file()


def delete_file():
    s3.Object(bucket_name, "t1.txt").delete()

delete_file()

# 1- buckets between file copy => any buket
def copy_file():
    copy_source = {
    'Bucket': 'elifbuckett',
    'Key': '6Aug_accessKeys.csv'
    }

    target_bucket = s3.Bucket('6auggg')

    target_bucket.copy(copy_source, 'newFile/6Aug_accessKeys.csv')

    print('File has been copied')

copy_file()

# 2- buckets between copy  => the buket you're working on now
def copy_file2():
    copy_source = {
    'Bucket': '',
    'Key': ''
    }

    bucket.copy(copy_source, '')

    print('File has been copied')

copy_file2()
