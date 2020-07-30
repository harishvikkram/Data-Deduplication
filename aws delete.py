import boto3
s3 = boto3.resource("s3")
bucket_name=input("Enter the Bucket Name:")
file_name=input("Enter the Name of File:")
obj = s3.Object(bucket_name,file_name)
obj.delete()
print("File deleted from cloud..")
