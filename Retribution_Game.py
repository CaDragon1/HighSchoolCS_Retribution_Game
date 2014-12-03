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

#Bosses:
#The Phantom Revenant (Malfectorum Reditum)
damage = 0
HP = 100
def Minion():
    def Swipe():
        global damage
        global HP
        print 'The undead Minion swipes at you, striking you in the chest.'
        damage = 3
        HP = HP - damage
        print 'You now have ' + HP + ' health left.'
    def Bite():
        global damage
        global HP
        print 'The undead Minion bites your arm, but your undead ward prevents you from getting infected.'
        print 'You knock it off of your arm and it stumbles back.'
        damage = 5
        HP = HP - damage
        print 'You are left with ' + HP + ' HP.'
    def Scream():
        global damage
        global HP



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


