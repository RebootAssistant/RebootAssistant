import os

i = 1

config = open("config.txt","w+")

nameText = input("Type in your name here: ")
nameAudio = input("Now type in your name as it is pronounced, so Geoff would be 'Jeff': ")
config.write(nameText)
config.write("\n")
config.write(nameAudio)
config.write("\n")
print("Changed name.")

location = input("Type in your city here: ")
config.write(location)
config.write("\n")
print("Changed location.")

emailaddress = input("Type in your email address here: ")
emailpassword = input("Type in your email password here: ")
config.write(emailaddress)
config.write("\n")
config.write(emailpassword)
config.close()
print("Changed email.")
print("Configuration is done.")


        
