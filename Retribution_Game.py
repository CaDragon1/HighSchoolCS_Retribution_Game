# Retribution
#print "Congratulation,you are on probation period, now until you have done gotten the item, you will be a free man. task you have completed this task. You can be free whenever you have completed this task"
#print "ok sir!"


#from ImageLibrary import *
#myfile=pickAFile("\Users\Public\Pictures\Sample Pictures\Ff14-class-archer.jpg")
#pict=makePicture("\Users\Public\Pictures\Sample Pictures\Ff14-class-archer.jpg")
#show(pict)
            
#print "you open up the cell doors and walk out.. thinking about what you have just been told"

#Characters you can talk to:
#Panther of the fresh breath
#

#Monster List:
#Munitate Deer
#Basilisk
#Naga
#Pholos
#Sphinx
#
#Grunt
#
#

#Bosses:
#The Phantom Revenant (Malfectorum Reditum)
damage = 0
HP = 100
def Munitate():
    def Headbutt():
        global damage
        global HP
        print 'The Munitate Deer rushes forward, headbutting you.'
        damage = 6
        HP = HP - 6
        print 'You now have ' + HP + ' health left.'



# Name System
nameName = False
name = 'Mary'
while nameName == False:
    print 'What is your name?'
    name = str(raw_input())
    if name == 'Captain Falcon':
        print ' '
        print '*******************'
        print 'Show me your moves!'
        print '*******************'
        print ' '
    print "So your name is " + name + ", yes or no?"
    yesOrNo = str(raw_input())
    if yesOrNo == 'yes' or yesOrNo == 'Yes':
        nameName = True
    else:
        nameName = False


