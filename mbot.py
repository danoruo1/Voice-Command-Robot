import cyberpi,time,mbot2,event # Libraries Usesd

#Parameters for voice recognition (NavigateUrl, Accesstoken, etc.)
cyberpi.speech.set_recognition_address(url = "{NAVIGATEURL}")
cyberpi.speech.set_access_token(token = "{ACCESSTOKEN}")

# Initilize the variables
voiceCommand = 0
next = 0

@event.start
def on_start():
    global voiceCommand
    global next
    while not str(voiceCommand).find(str("stop")) > -1:
        cyberpi.console.print("Give me an instruction")
        cyberpi.cloud.listen("english", 3)
        voiceCommand = cyberpi.cloud.listen_result()
        if str(voiceCommand).find(str("red")) > -1 and next == 0:
            mbot2.forward(0)
            cyberpi.console.print("red")
            next +=1

        if str(voiceCommand).find(str("green")) > -1 and next == 0:
            mbot2.forward(50)
            cyberpi.console.print("green")
            next +=1

        if str(voiceCommand).find(str("yellow")) > -1 and next == 0:
            mbot2.forward(25)
            cyberpi.console.print("yellow")
            next +=1
        next = 0
