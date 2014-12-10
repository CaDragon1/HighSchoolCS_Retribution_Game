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
Wut = False
block = 0
minionHP = 25
boss = False
bossHP = 200
def Minion():
    def Swipe():
        global damage
        global HP
        global block
        print 'The undead minion swipes at you, striking you in the chest.'
        damage = 3
        HP = HP - damage + block
        if block > 2:
            block = block - 3
        else:
            block = 0
        print 'You now have ' + HP + ' health left.'
        return
    def Bite():
        global damage
        global HP
        global block
        print 'The undead minion bites your arm, but your undead ward prevents you from getting infected.'
        print 'You knock it off of your arm and it stumbles back.'
        damage = 5
        HP = HP - damage + block
        if block > 4:
            block = block - 5
        else:
            block = 0
        print 'You are left with ' + HP + ' HP.'
        return
    def Tackle():
        global damage
        global HP
        global block
        global Wut
        if Wut == False:
            print 'The undead minion does its best impression of a leap, somehow managing to catch you.'
        if Wut == True:
            print 'The undead minion does its best impression of a leap, somehow managing to catch you... AGAIN.'
        print 'He clings and starts inflicting damage, and you struggle for a moment until you throw him off.'
        damage = 7
        HP = HP - damage + block
        if block > 6:
            block = block - 7
        else:
            block = 0
        print 'You get up with ' + HP + ' health.'
        Wut = True
        return
def UserAttack():
    def slash():
        global damage
        global minionHP
        global bossHP
        if boss == False:      
            if minionHP > 9:
                damage = 10
                minionHP = minionHP - damage
                print 'You swing your sword, giving a large gash to the minion and doing ' + str(damage) + ' damage. The minion now has ' + minionHP + ' HP.'
            else:
                minionHP = 0
                print "You cut off the minion's head and he staggers, falling to the ground in defeat."
        if boss == True:
            if bossHP > 11:
                if bossHP == 42:
                    print 'You strike the phantom revenant with the meaning of life. It sends off a blinding light and he withers before your eyes.'
                    bossHP = 15
                    print 'The light diminishes, leaving the revenant with 15 HP left. You follow that up with a sword strike.'
                damage = 12
                bossHP = bossHP - damage
                print 'Your sword slashes through the air in a wide arc. It strikes the revenant, taking some of the darkness with it.'
                print 'The revenant now has' + bossHP + 'HP.'
            else:
                bossHP = 0
        print 
    def shieldBash():
        global damage
        global minionHP
        global boss
        global bossHP
        if boss == False:
            if minionHP > 7:
                damage = 8
                minionHP = minionHP - damage
            else:
                minionHP = 0
        if boss == True:
            if bossHP > 11:
                if bossHP == 42:
                    print 'You smash your shield into the phantom revenant with the meaning of life. It sends off a blinding light and he withers before your eyes.'
                    bossHP = 16
                    print 'The light diminishes, leaving the revenant with 16 HP left. You follow that up with a shield bash.'
                damage = 14
                bossHP = bossHP - damage
                print 'You swing your shield and it smashes into the revenant, knocking him backwards.'
                print 'The revenant now has' + bossHP + 'HP.'
            else:
                bossHP = 0
    def stab():
        global damage
        global minionHP
        global boss
        global bossHP
        damage = 7
        if minionHP > 6:
            minionHP = minionHP - damage
        else:
            minionHP = 0
        if boss == True:
            if bossHP > 11:
                if bossHP == 42:
                    print "You thrust your sword into the revenant's body and infuse it with the meaning of life. The revenant starts dissolving internally, but it pulls away at the last second."
                    bossHP = 12
                    print 'The revenant has 12 HP left. You advance once more, hoping to stab it again.'
                damage = 11
                bossHP = bossHP - damage
                print 'You stab the revenant.'
                print 'The revenant now has' + bossHP + 'HP.'
            else:
                bossHP = 0
    def guard():
        global block
        if bossHP == 42:
            print "Using the meaning of life, your shield is strengthened, giving you extra defense."
            block = block + 36
        print "You raise your shield."
        block = block + 6
        print "You have " + block + " shield points."


# Name System
nameName = False
name = 'JonJacobJingleheimershmidt'
while nameName == False:
    print 'What is your name?'
    name = str(raw_input())
    if name == 'Captain Falcon':
        print ''
        print '*******************'
        print 'Show me your moves!'
        print '*******************'
        print ''
    print "So your name is " + name + ", yes or no?"
    yesOrNo = str(raw_input())
    if yesOrNo == 'yes' or yesOrNo == 'Yes':
        nameName = True
    else:
        nameName = False

# retribution
#print "Congratulation,you are on probation period, now until you have done gotten the item, you will be a free man. task you have completed this task. You can be free whenever you have completed this task"

#print "ok sir!"


#from ImageLibrary import *
#myfile=pickAFile("\Users\Public\Pictures\Sample Pictures\Ff14-class-archer.jpg")
#pict=makePicture("\Users\Public\Pictures\Sample Pictures\Ff14-class-archer.jpg")
#show(pict)
#undead ward so dont get infected
#print "you open up the cell doors and walk out.. thinking about what you have just been told"

    
print "(Remember to advance text using the enter/return key!)"
print ''
print "Warden- So you're the lucky prisoner, eh " + name + "? You have been given an assignment. If you can complete it, then you can go free."
userInput = raw_input()
if userInput == "":
    print name + "- What is the assignment?"
print "Warden- You will be informed once you arrived. There is a carriage outside that will take you to Felador. Once you arrive, you will recieve further instructions."
if userInput == "":
    print ""
print " -About 15-20 minutes later, " +name + "appears at Felador.-"
print " he walks up to a castle, there are 2 guards..."
print " with the muffleness of the mask, the guard asks, who comes here?"
print " my name is " + name, "i got told to come here as i am now on probation i was told to come here to retrieve my item for the final present."
print " which prison do you come from? "
userInput = raw_input()
if userInput == "":
    print ''
print " regolith prison "
userInput = raw_input()
if userInput == "":
    print ''
print " fine, you have 1 chance. we have our eyes on you" + name
userInput = raw_input()
if userInput == "":
    print ''
print " you open the huge door and walk thorugh the huge door"
userInput = raw_input()
if userInput == "":
    print ''
print " you can smell something but you disregard it.. but you follow the map to"
userInput = raw_input()
if userInput == "":
    print ''
print ""
print "you walk for around 10 minutes, following the map, and you finally find something interesting.."
userInput = raw_input()
if userInput == "":
    print ''
print ""
print "you find a grunt on the floor..."
userInput = raw_input()
if userInput == "":
    print ''
print ""
print "it's already bleeding out on the floor from the previos person.. and you just step on it to finish it off."
print "you continute walking.. and you see a bloody sign saying chamber of the Phantom Revenant."
print "You don't think anything of it. And you continue watching it"
print ""
print "You feel it getting a LOT hotter... and also getting gnawed on by a bunch of little creatures.. oh wait those are the grunts.."
print "you beat the little grunts off of you as fast as you are able to, in disbelief aswell."
userInput = raw_input()
if userInput == "":
    print ''
print ""
print "You keep walking and you spot the phantom.. phantom revenant."
print "you... you are the one who has the items i need... you aren't leaving here alive.."
print ""
print ""
print ""
print ""
print ""
print ""
print ""


