import numpy as np
import scipy.io.wavfile
import boto3

file=input("Enter the name of the file or path:")
rate, data = scipy.io.wavfile.read(file)



print("The dimension of the array:",data.ndim)
print("The size of the array:",data.size)
print("The shape of the array:",data.shape)
print("The Contents of the array:",data)
print("The rate of file read:",rate)

dim=data.ndim

if dim==2:
    data2=[]
    for i in range(len(data)):     
        data2.append([data[i][0],data[i][1]])
    print("The Contents of the array:",data2)

    data2 = np.asarray(data2,dtype=np.int16)
    scipy.io.wavfile.write('output song.wav',rate,data2)


    print("Saving the contents as csv file...")
    np.savetxt('song contents.csv', data2, delimiter=',')
    print("Song saved as csv file..")

    print("Reading the data from csv file...")

    res= np.loadtxt('song contents.csv', delimiter=',') 
    print("Song values read from csv file",res)
    res=np.asarray(res,dtype=np.int16)
    print("Saving as a new song")
    scipy.io.wavfile.write('final song from csv.wav',rate,res)
    print("New Song saved from csv file")
else:
    data2=[]
    data2=np.append(data2,data)
    print("The Contents of the array:",data2)

    data2 = np.asarray(data2,dtype=np.int16)
    scipy.io.wavfile.write('output.wav',rate,data2)

    print("Saving the contents as csv file...")
    np.savetxt('song contents.csv', data2, delimiter=',')
    print("Song saved as csv file..")

    print("Reading the data from csv file...")

    res= np.loadtxt('song contents.csv', delimiter=',') 
    print("Song values read from csv file",res)
    res=np.asarray(res,dtype=np.int16)
    print("Saving as a new song")
    scipy.io.wavfile.write('final song from csv.wav',rate,res)
    print("New Song saved from csv file")

ch=input("Do you want to upload the file in aws cloud:")
if ch=="yes":
    s3=boto3.client('s3')
    file_name=input("enter the name of the file:")
    bucket_name=input('enter the bucket name:')
    target_file_name=input('enter the target file name:')
    s3.upload_file(file_name,bucket_name,target_file_name)
    print("File Uploaded Successfully in the bucket:",bucket_name)
else:
    print("Press ctrl+z to stop...")
    
