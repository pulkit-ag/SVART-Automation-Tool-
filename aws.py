import pyttsx3
import os
import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

pyttsx3.speak("Welcome to this application ! I'm your Personal Computer Assistant. I can perform following tasks at the moment.")
print("\t\t\t\t\tWelcome to AWS Automation ")
print("\t\t\t------------------------------------")
print()

print("\t\t\t1.Creating key pair ")
print("\t\t\t2.Checking available key pair ")
print("\t\t\t3.Deleting key pair ")
print("\t\t\t4.Creating security group ")
print("\t\t\t5.Deleting security group ")
print("\t\t\t6.Checking available instances")
print("\t\t\t7.Creating Instances ")
print("\t\t\t8.Starting Instance ")
print("\t\t\t9.Stopping Instance ")
print("\t\t\t10.Terminating Instance ")

print()

while True:
    pyttsx3.speak("What do you want me to do? ")
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Recognising...")
        data = r.recognize_google(audio)
    if (("key" in data)) and (("create" in data)):
        key_name=input("Enter key-name : ")
        pyttsx3.speak("Creating key pair in AWS..")
        os.system("aws ec2 create-key-pair --key-name {} --output text > {}.pem".format(key_name,key_name))
        pyttsx3.speak("key pair created successfully.")
    elif (("key" in data)) and (("check" in data)):
        pyttsx3.speak("Checking key pair in AWS..")
        os.system("aws ec2 describe-key-pairs")
    elif (("key" in data)) and (("delete" in data)):
        key_name = input("Enter key-name : ")
        pyttsx3.speak("Deleting key pair in AWS..")
        os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
        pyttsx3.speak("key pair deleted successfully")
    elif(("security group" in data)) and (("create" in data)):
        sg_name = input("Enter sg-name : ")
        desc = input("Enter sg description : ")
        pyttsx3.speak("Creating security group in AWS..")
        os.system("aws ec2 create-security-group --group-name {} --description {}".format(sg_name, desc))
        pyttsx3.speak("security group created successfully")
    elif (("security group" in data)) and (("delete" in data)):
        sg_name = input("Enter sg-name : ")
        pyttsx3.speak("Deleting Security group in AWS..")
        os.system("aws ec2 delete-security-group --group-name {}".format(sg_name))
        pyttsx3.speak("Security group deleted successfully")
    elif (("instances" in data) or ("instance" in data)) and (("check" in data) or ("available" in data)):
        pyttsx3.speak("Checking instances in AWS..")
        os.system("aws ec2 describe-instances")
    elif (("instances" in data) or ("instance" in data)) and (("launch" in data) or ("create" in data)):
        image = input("Enter image-id : ")  # ami-052c08d70def0ac62
        inst_type = input("Enter instance-type : ")  # t2.micro
        subnet = input("Enter subnet id : ")  # subnet-710f0619
        sg_id = input("Enter sg-id : ")
        key = input("Enter key-name : ")
        pyttsx3.speak("Launching new instance in AWS..")
        os.system(
            "aws ec2 run-instances --image-id {} --instance-type {} --count 1 --subnet-id {} --security-group-ids {} --key-name {}".format(
                image, inst_type, subnet, sg_id, key))
        pyttsx3.speak("new instance launched suucessfully")
    elif (("instances" in data) or ("instance" in data)) and (("start" in data)):
        instance_id = input("Enter instance-id : ")
        pyttsx3.speak("starting instance..")
        os.system("aws ec2 start-instances --instance-ids {} ".format(instance_id))
        pyttsx3.speak("Instance started successfully")
    elif (("instances" in data) or ("instance" in data)) and (("stop" in data)):
        instance_id = input("Enter instance-id : ")
        pyttsx3.speak("stopping instance..")
        os.system("aws ec2 stop-instances --instance-ids {} ".format(instance_id))
        pyttsx3.speak("Instance stopped successfully")
    elif (("instances" in data) or ("instance" in data)) and (("terminate" in data) or ("delete" in data)):
        inst_id = input("Enter instance id : ")
        pyttsx3.speak("terminating instance..")
        os.system("aws ec2 terminate-instances --instance-ids {}".format(inst_id))
        pyttsx3.speak("instance terminated successfully")
    elif ("exit" in data) or ("quit" in data):
        break
    else:
        pyttsx3.speak("This service is not supported yet!")
pyttsx3.speak("Thank you for using me ! Have a nice day.")
print("Thank you ! ")