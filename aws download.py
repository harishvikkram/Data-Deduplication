import boto3
s3=boto3.client('s3')
bucket_name=input("Enter the name of the bucket:")
file_name=input("Enter the name of the file with extension:")
target_name=input("Enter the target file name:")
s3.download_file(bucket_name,file_name,target_name)
print("File Downloaded successfully...")
