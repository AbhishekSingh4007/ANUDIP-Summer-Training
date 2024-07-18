#Taking input as seconds 
sec = int(input("Enter the time : "))

#converting into hours, mkinutes and seconds
if (sec >= 0):
    hour = 0
    min = 0
    if(sec >=3600):
        hour = sec//3600
        sec= sec % 3600
    if(sec >=60):
        min = sec//60
        sec = sec%60
        
    #Printing the time in hour, minutes and seconds format.
    print(hour, " Hour ",min," minutes ", sec, "Seconds")  
else:  
    print("Time must be positive") 