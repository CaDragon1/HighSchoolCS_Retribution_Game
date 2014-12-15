#Characters you can talk to:
#Panther of the fresh breath
#

#Bosses:
#The Phantom Revenant (Malfectorum Reditum)

#Monsters:
#

damage = 0
HP = 100
block = 0
minionHP = 35
bossHP = 200
Wut = False
boss = False
#Minion attacks
def Swipe():
        global damage
        global HP
        global block
        damage = 3
        HP = HP - damage + block
        if block > damage:
            block = block - 3
            print 'The undead minion tries to swipe at you, but you block with your shield. You now have ' + str(block) + ' shield points.'
        elif block < damage and block > 0:
            block = 0
            HP = HP - (damage - block) 
            print 'The undead minion grazes you, breaking through your defenses. You have 0 shield points left and ' + str(HP) + ' HP left.'
        else:
            HP = HP - damage
            print 'The undead minion swipes at you, striking you in the chest. You have ' + str(HP) + ' HP left.'
        return
def Bite():
        global damage
        global HP
        global block
        print 'The undead minion bites your arm, but your undead ward prevents you from getting infected.'
        print 'You knock it off of your arm and it stumbles back.'
        damage = 5
        HP = HP - damage + block
        if block > damage:
            block = block - 5
            print "Fortunately, it didn't bite through your tunic. You now have " + str(block) + " shield points."
        elif block < damage and block > 0:
            block = 0
            HP = HP - (damage - block)
            print 'You examine the wound, but it is not bad. You now have 0 shield points and ' + str(HP) + ' HP.'
        else:
            HP = HP - damage
            print 'You examine the wound and see it bleeding out. You are left with ' + str(HP) + ' HP.'
        return
def Tackle():
    global minionHP
    global damage
    global HP
    global block
    global Wut
    if minionHP > 0:
        if Wut == False:
            print 'The undead minion does its best impression of a leap, somehow managing to catch you.'
        if Wut == True:
            print 'The undead minion does its best impression of a leap, somehow managing to catch you... AGAIN.'
        damage = 7
        if block < damage:
            HP = HP - (damage - block)
            print 'He bites you, but you throw him off before he can hang on.'
            block = 0
            print 'You now have 0 shield points and ' + str(HP) + ' HP.' 
        elif block > damage and block > 0:
            block = block - 7
            print 'However, you swing your shield and knock it back before it can do any damage. You now have ' + str(block) + ' shield points.'
        else:
            HP = HP - damage
            print 'He clings and starts inflicting damage, and you struggle for a moment until you throw him off.'
            print 'You get up with ' + str(HP) + ' health.'
        Wut = True
    return
#Boss moves
def darkPulse():
    global damage
    global HP
    global block
    global bossHP
    if bossHP > 0:
        if bossHP > 50:
            damage = 6
        else:
            damage = 10
        print "A wave of darkness sweeps out from the revenant. You struggle in the suffocating, crushing shadow."
        if damage < block:
            block = block - damage
            print "Your shield protected you against the attack and the darkness recedes, leaving you with " + str(block) + " shield points."
        elif damage > block and block > 0:
            HP = HP - (damage - block)
            block = 0
            print "Your shield blocks some of the attack, but your shield points dropped to 0 and you are forced to take a knee to endure the rest. The darkness recedes and you stand up with " + str(HP) + "HP left."
        else:
            HP = HP - (damage - block)
            print "The darkness damages you, knocking you to the ground. You lay there as the shadows press around you until they recede. You pick yourself off the ground with " + str(HP) + "HP left."
    return
def bonePierce():
    global damage
    global HP
    global block
    global BossHP
    if bossHP > 0:
        damage = 8
        print 'The revenant summons a sharp spear of bone and hurls it at you.'
        if damage < block:
            block = block - damage
            print 'You lift your shield just in time and the spear clatters against the shield. You have ' + str(block) + ' shield points.'
        elif damage > block and block > 0:
            HP = HP - (damage - block)
            block = 0
            print 'You start to raise your shield, but it merely deflects it, causing it to graze you. You have 0 shield points and ' + str(HP) + ' health points.'
        else:
            HP = HP - damage
            print 'The spear hits you. You now have ' + str(HP) + ' HP left.'
    return
def condemn():
    global damage
    global HP
    global block
    global BossHP
    if bossHP > 0:
        damage = 10
        if damage < block:
            block = block - damage
            print "You see a dangerous glint in the Revenant's eyes, but you quickly throw off the foreboding feeling that accompanied it. You see it swing its scythe and you raise your shield, blocking it."
            print "You now have " + str(block) + " shield points left."
        elif damage > block and block > 0:
            HP = HP - (damage - block)
            block = 0
            print "The revenant's eyes flash and you feel condemmed. You look up and see the revenant's scythe falling. It glances off of your just raised shield and scrapes you."
            print 'You have 0 shield points and ' + str(HP) + ' HP left.'
        else:
            HP = HP - damage
            print "The revenant's eyes flash and you get a feeling of impending doom. You look up just in time to see his scythe swipe down on you. You now have " + HP + ' HP left.'
    return
#Your moves'
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
                print 'The revenant now has' + str(bossHP) + 'HP.'
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
                print 'The revenant now has' + str(bossHP) + 'HP.'
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
                print 'The revenant now has' + str(bossHP)+ 'HP.'
            else:
                bossHP = 0
def guard():
        global block
        if bossHP == 42:
            print "Using the meaning of life, your shield is strengthened, giving you extra defense."
            block = block + 36
        print "You raise your shield to defend yourself."
        block = block + 6
        print "You now have " + str(block) + " shield points."


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


#myfile=pickAFile("\Users\Public\Pictures\Sample Pictures\Ff14-class-archer.jpg")
#pict=makePicture("\Users\Public\Pictures\Sample Pictures\Ff14-class-archer.jpg")
#show(pict)


print "(Remember to advance text using the enter/return key!)"
print ''
print "Warden: So you're the lucky prisoner, " + name + "? You have been given an assignment. If you can complete it, then you can go free."
userInput = raw_input()
if userInput == "":
    print name + ": What is the assignment?"
print "Warden: You will be informed once you arrived. There is a carriage outside that will take you to Felador. Once you arrive, you will recieve further instructions."
userInput = raw_input()
if userInput == "":
    print ""
print " -About 15-20 minutes later, " + name + "appears at Felador.-"
userInput = raw_input()
if userInput == "":
    print ''
print name + " walks up to Felador Castle, where two guards meet him."
print 'Guard 1: What brings you here?'
userInput = raw_input()
if userInput == "":
    print ''
print name + ": My name is " + name + ". I was sent here from Regolith prison. They said that there was a task for me...?"
if userInput == "":
    print ''
print "Guard 2: Oh, you're the guy that we were told to bring you to the captain."
userInput = raw_input()
if userInput == "":
    print 'Guard 1: He should be right inside, go on ahead and talk to him.'
print name + " opens the huge door and walks through. Inside he spots an armored man wearing the red sash that signifies his rank."
print "It is because of this that you can tell that he is the captain."
userInput = raw_input()
if userInput == "":
    print ''
print 'Captain: Who are you?'
userInput = raw_input()
if userInput == "":
    print ""
print name + ': I am ' + name + ", I was sent from Regolith prison. Do you know what I am here for?"
print 'Captain: Right. Well, to answer your question, yes. You are here to run a mission for us. You see, we have recently had a revenant take up residence inside our dungeon.'
print 'Captain: We sent one of the cleaning staff to take care of it, but he has not returned. We decided that we would offer up your freedom if you could help us out.'
userInput = raw_input()
if userInput == "":
    print ""
print name + ': Why specifically me?'
print 'Captain: Well, you were one of our best behaved prisoners and we are short on cleaning staff. The door to the dungeon is down the hall to your left.'
print name + ': How will I beat it?'
print 'Captain: Here is a sword, a shield, and some leather armour. It should be sufficient.'
userInput = raw_input()
if userInput == "":
    print ''
print "You walk down the hall until you come across the dungeon door. You open it and descend the stone steps that are lit by the flickering wall torches."
userInput = raw_input()
if userInput == "":
    print ""
print "You reach the bottom after a short time, but you hear moans up ahead."
userInput = raw_input()
if userInput == "":
    print ""
print "You find an undead minion on the floor. It appears to not be able to get up. You shudder; fighting zombies is not your idea of fun."
userInput = raw_input()
if userInput == "":
    print ""
print "It's already bleeding out on the floor from the previos person.. and you just step on it to finish it off."
print "You continute walking.. and you see a bloody sign saying chamber of the Phantom Revenant."
print "You don't think anything of it. And you continue watching it"
print ""
print "You feel it getting a LOT hotter... and also getting gnawed on by a bunch of little creatures.. oh wait those are the undead minions.."
print "You beat the little grunts off of you as fast as you are able to, in disbelief aswell."
userInput = raw_input()
if userInput == "":
    print ""
print "You keep walking and you spot the phantom.. phantom revenant."
print "You... you are the one who has the items i need... you aren't leaving here alive.."
print "You have multiple attacks to attack the Revenant, use them wisely."
print "1- 2- 3- 4- 5-"
print ""
#you'll need it to print your hp, their hp and how much damage it did etc for each one.."
print "Wow... you defeated the revenant.. really..?"
print "You walk forward.. barely being able to walk, to go grab your items you need from the Revenant."
print "You pick up the items, and you feel accomplished..You take out the map and unscroll it"
print "You put it into your backpack.. zip it up and get ready to walk out to go back to the prison to give to your probation officer."
print "You walk towards the huge doors, and barely can open them because you are so tired.."
print "You open the door up and look towards the guards, who just watch as you walk away..."
print "You start walking back towards the prison and after a mile or so of walking.. you finally ending up at the prison."
print "Who the heck are you?? The guard said to Warden."
print "I have the items for the king so i can be free."
print "Fine.. go ahead..."
print "You walk in and find the officer. Sir.. here is your items as you hand them to him.."
print "What.. How did you.. Ehat"
print "Three days later... he wraps up the gift to give it to the king... Here you go sir"
print "He hands it over... he opens it.."
print "What.. How.. How did you.. Thank you.."