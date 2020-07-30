import boto3
s3=boto3.client('s3')
file_name=input("enter the name of the file with extension:")
bucket_name=input('enter the bucket name:')
target_file_name=input('enter the target file name:')
s3.upload_file(file_name,bucket_name,target_file_name)
print("File Uploaded Successfully in the bucket:",bucket_name)
