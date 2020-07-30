import hashlib
import boto3

# Python program to find MD5 hash value of a file

 
filename1 = input("Enter the file name: ")
with open(filename1,"rb") as f:
    bytes = f.read() # read file as bytes
    res1= hashlib.md5(bytes).hexdigest();
    print(res1)

filename2 = input("Enter the file name: ")
with open(filename2,"rb") as f:
    bytes = f.read() # read file as bytes
    res2= hashlib.md5(bytes).hexdigest();
    print(res2)

    
print("Comparing The Hash Values of The Numpy Arrays...")

if res1==res2:
    print("Duplicate File Found!!!..\nGoing To Delete The Redundant File in Cloud")
    s3 = boto3.resource("s3")
    bucket_name=input("Enter the Bucket Name:")
    file_name=input("Enter the Name of File:")
    obj = s3.Object(bucket_name,file_name)
    obj.delete()
    print("File deleted from cloud..\nRedundant File Successfully Removed from cloud..")
else:
    print("Not a Redundant File..")
    
