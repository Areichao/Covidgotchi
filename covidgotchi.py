# here is where our main functions n shit will go. feel free to work in a separate ide, but move function name into "doing"
# on trello so we dont have two people working on the same thing. Try not to forget to use trello or it could get confusing.
# ask emily for pngs, png names
# screen size is x = 1000, y = 700

import pygame

pygame.init()

brenden = false = True
# HES NOT REAL HE CANT HURT YOU

checkCount = 0  # which task they checked
health = 4
imageFilePath = 'C:/Users/Brenden/Pictures/Covidgotchi/'

# **************************header stuff**************************
pygame.display.set_caption("Covidgotchi")
icon = pygame.image.load(imageFilePath + 'icon32.png')  # png needed
pygame.display.set_icon(icon)

size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
black = (0, 0, 0)  # constants
white = (255, 255, 255)  # constants
transparent = (0, 0, 0, 0)  # constants
currentScreen = 'Title'
global game
game = True

# **************************title screen stuff**************************
exitButtonLocation = (325, 500)  # "location of exit button" DIMENSIONS: (612.5, 625)
startButtonLocation = (200, 250)  # "location of start button" DIMENSIONS: (482.5,400)
instructionButtonLocation = (512.5, 325)  # "location of instructions button" DIMENSIONS: (775,475)

# **************************character selection screen**************************
# loaded all images
happyShark = pygame.image.load(imageFilePath + 'shark.png')
happyCat = pygame.image.load(imageFilePath + 'cat.png')
happyBird = pygame.image.load(imageFilePath + 'bird.png')
happyDog = pygame.image.load(imageFilePath + 'dog.png')
sadShark = pygame.image.load(imageFilePath + 'sharksad.png')
sadCat = pygame.image.load(imageFilePath + 'catsad.png')
sadBird = pygame.image.load(imageFilePath + 'birdsad.png')
sadDog = pygame.image.load(imageFilePath + 'dogsad.png')
# dictionary with pngs as values
charactersHappy = {'shark': happyShark, 'cat': happyCat, 'bird': happyBird, 'dog': happyDog, }
charactersSad = {'shark': sadShark, 'cat': sadCat, 'bird': sadBird, 'dog': sadDog}

characterLocations = [(82.5, 400), (312.5, 387.5), (575, 387.5), (800, 400)]
global activeCharacter
activeCharacter = 'cat'

# **************************main game stuff**************************
checkmarkLocation = [(670, 155), (670, 220), (670, 285), (670, 350)]  # coordinates of checkmarks go in here (730, 210)
checkmarkSize = (60, 55)  # "put dimensions of checkmark (x, y)"

characterLocation = (262.5, 362.5)  # location of character in game screen
heartLocation = (12.5, 12.5)  # location of hearts in game screen

greenCheck = pygame.image.load(imageFilePath + 'greenCheck.png')
redCheck = pygame.image.load(imageFilePath + 'redCheck.png')
hearts = pygame.image.load(imageFilePath + 'healthbar{}.png'.format(health + 1))

global taskChecks
taskChecks = [True, True, True, True]

# **************************exit screen stuff**************************
yesLocation = [(380, 355), (495, 410)]
noLocation = [(505, 355), (615, 410)]

# **************************timers**************************
currentTime = 0
staticStretch = staticDrink = staticEat = staticOutside = 0


# **************************game functions**************************
def slapChecks(task):
    global staticOutside, staticEat, staticDrink, staticStretch, taskChecks, escp

    if (task == 0):
        if (taskChecks[0] == True):
            if (currentTime - staticStretch) < 5000:
                screen.blit(greenCheck, checkmarkLocation[0])
            elif (currentTime - staticStretch) < 10000:
                screen.blit(redCheck, checkmarkLocation[0])

    if (task == 1):
        if (taskChecks[1] == True):
            if (currentTime - staticDrink) < 5000:
                screen.blit(greenCheck, checkmarkLocation[1])
            elif (currentTime - staticDrink) < 15000:
                screen.blit(redCheck, checkmarkLocation[1])

    if (task == 2):
        if (taskChecks[2] == True):
            if (currentTime - staticEat) < 5000:
                screen.blit(greenCheck, checkmarkLocation[2])
            elif (currentTime - staticEat) < 20000:
                screen.blit(redCheck, checkmarkLocation[2])

    if (task == 3):
        if (taskChecks[3] == True):
            if (currentTime - staticOutside) < 5000:
                screen.blit(greenCheck, checkmarkLocation[3])
            elif (currentTime - staticOutside) < 25000:
                screen.blit(redCheck, checkmarkLocation[3])
                
    if task == -1:
        screen.blit(pygame.image.load(imageFilePath + 'exitScreen.png'), (375, 262.5))




def showHealth():
    """ shows health bar """
    hearts = pygame.image.load(imageFilePath + 'healthbar{}.png'.format(health + 1))
    screen.blit(hearts, heartLocation)


def addGreenCheckmark(task):
    """adds green checkmark for when timer is good"""
    if task == 0:
        # stretch
        global staticStretch
        screen.blit(greenCheck, checkmarkLocation[0])
        taskChecks[0] = True
        staticStretch = currentTime
    if task == 1:
        # water
        global staticDrink
        screen.blit(greenCheck, checkmarkLocation[1])
        taskChecks[1] = True
        staticDrink = currentTime
    if task == 2:
        # food
        global staticEat
        screen.blit(greenCheck, checkmarkLocation[2])
        taskChecks[2] = True
        staticEat = currentTime
    if task == 3:
        # outdoor
        global staticOutside
        screen.blit(greenCheck, checkmarkLocation[3])
        taskChecks[3] = True
        staticOutside = currentTime


def addRedCheckmark(task):
    """adds red checkmark when timer is running low"""
    global taskChecks
    if task == 0:
        # stretch
        screen.blit(redCheck, checkmarkLocation[0])
    elif task == 1:
        # water
        screen.blit(redCheck, checkmarkLocation[1])
    elif task == 2:
        # food
        screen.blit(redCheck, checkmarkLocation[2])
    elif task == 3:
        # outdoor
        screen.blit(redCheck, checkmarkLocation[3])


def removeCheckmark(task):
    """removes checkmark for when timer ded"""
    global taskChecks
    if task == 0:
        # stretch
        #        screen.blit(redCheck.image.fill(transparent), checkmarkLocation[0])
        taskChecks[0] = False
        characterDie()
        slapChecks(0)
    if task == 1:
        # water

        #        screen.blit(redCheck.image.fill(transparent), checkmarkLocation[1])
        taskChecks[1] = False
        characterDie()
        slapChecks(1)
    if task == 2:
        # food

        #        screen.blit(redCheck.image.fill(transparent), checkmarkLocation[2])
        taskChecks[2] = False
        characterDie()
        slapChecks(2)
    if task == 3:
        # outdoor

        #        screen.blit(redCheck.image.fill(transparent), checkmarkLocation[3])
        taskChecks[3] = False
        characterDie()
        slapChecks(3)


def characterDie():
    """character loses health, triggered by time limit"""
    # subtract health
    global health
    if health > 0: health -= 1
    # if health = 2, scrin.blit(characterdie)
    if health <= 2: screen.blit(charactersSad[activeCharacter], characterLocation)



def characterUndie():
    """character gains health, triggered by checkmarking completed tasks"""
    # add health
    global health
    if health < 4: health += 1
    # if health = 3, screen.blit(characterunded)
    if health > 2: screen.blit(charactersHappy[activeCharacter], characterLocation)


def updateHealth():
    """Update the health of player to show how many hearts"""
    showHealth()


def checkIfOnBox(x, y):
    """Checks if the cursor location is on a check mark box"""
    global checkCount
    checkCount = 0
    # go through all check boxes and see if they click on any
    for checkmark in checkmarkLocation:
        # get bottom left coordinates of the checkmark box
        topLeftX = checkmark[0]
        topLeftY = checkmark[1]
        # get top right coordinates of the checkmark box
        btmRightX = checkmark[0] + checkmarkSize[0]
        btmRightY = checkmark[1] + checkmarkSize[1]
        # if mouse pos coordinates lie within box size, they clicked on a box; return true
        if ((x > topLeftX and x < btmRightX) and (y > topLeftY and y < btmRightY)):
            return True
        checkCount += 1
    # they did not click on a box, return false
    return False


def slapPlayer():
    global activeCharacter
    if health > 2:
        screen.blit(charactersHappy[activeCharacter], characterLocation)
    else:
        screen.blit(charactersSad[activeCharacter], characterLocation)


# **************************timer functions**************************
def timerStretch():  # task 0
    """ countdown till green checkmarks goes away for stretch (1 hour) """
    # current time is constantly running, static time is set when player presses task. distance between staticStretch and currentTime
    # will increase.
    global taskChecks
    global staticStretch

    if (currentTime - staticStretch) > 10000 and taskChecks[0] == True:  # 3000000: #50 minutes
        removeCheckmark(0)
        
    elif (currentTime - staticStretch) > 5000 and taskChecks[0] == True:  # 3600000: #60 minutes
        addRedCheckmark(0)
    slapChecks(0)


def timerDrink():  # task 1
    """ countdown for water (2 hour)"""
    # at 10 mins mark checkmark becomes red
    global taskChecks
    global staticStretch

    if (currentTime - staticDrink) > 15000 and taskChecks[1] == True:  # 6600000: # 110 minutes
        removeCheckmark(1)

    elif (currentTime - staticDrink) > 5000 and taskChecks[1] == True:  # 7200000: # 120 minutes
        addRedCheckmark(1)
    slapChecks(1)


def timerEat():  # task 2
    """ countdown for food (3.5 hours) """
    # at 10 mins mark checkmark becomes red
    global taskChecks
    global staticEat

    if (currentTime - staticEat) > 20000 and taskChecks[2] == True:  # 12000000: # 200 minutes
        removeCheckmark(2)
    elif (currentTime - staticEat) > 5000 and taskChecks[2] == True:  # 12600000: # 210 minutes
        addRedCheckmark(2)
    slapChecks(2)


def timerGoOutside():  # task 3
    """ cuntdown for fresh air (6 hours) """
    # at 10 mins mark checkmark becomes red
    global taskChecks
    global staticStretch

    if (currentTime - staticOutside) > 25000 and taskChecks[3] == True:  # 21000000: # 350 minutes
        removeCheckmark(3)
    elif (currentTime - staticOutside) > 5000 and taskChecks[3] == True:  # 21600000: # 360 minutes
        addRedCheckmark(3)
    slapChecks(3)


def timerCheck():
    """Check timer of each task to see if any should turn red"""

    timerStretch()
    timerDrink()
    timerEat()
    timerGoOutside()


# **************************switching screens**************************
def titleScreen():
    """Show title screen"""
    global currentScreen
    screen.blit(pygame.image.load(imageFilePath + 'titleScreen.png'), (0, 0))
    currentScreen = 'Title'


def instructionScreen():
    """switch screen to instructions"""
    global currentScreen
    screen.blit(pygame.image.load(imageFilePath + 'instructionScreen.png'), (0, 0))
    currentScreen = 'Instructions'


def characterSelectionScreen():
    """show character screen"""
    global currentScreen
    screen.blit(pygame.image.load(imageFilePath + 'characterSelection.png'), (0, 0))
    currentScreen = 'CharacterSelection'


def gameScreen():
    """Game screen"""
    global currentScreen
    screen.blit(pygame.image.load(imageFilePath + 'gameScreen.png'), (0, 0))
    currentScreen = 'Game'


#     def escapeMenuScreen():
#     """Shows the menu in game to exit and do other stuff¿"""
#     global currentScreen
#     screen.blit(pygame.image.load(imageFilePath + 'exitScreen.png'), (375, 262.5))
#     escape = True
#     pos = pygame.mouse.get_pos()
#     mousePosX, mousePosY = pygame.mouse.get_pos()
#     escapeMenu(mousePosX, mousePosY)


# characterLocations = [(100, 512.5), (312.5 , 462.5), (562.5 , 462.5), (887.5 , 487.5)]
def slapCharacters():
    """slaps lap smach the characters on top of the screen"""
    screen.blit(charactersHappy["shark"], characterLocations[0])
    screen.blit(charactersHappy["cat"], characterLocations[1])
    screen.blit(charactersHappy["bird"], characterLocations[2])
    screen.blit(charactersHappy["dog"], characterLocations[3])


# **************************title page**************************
def exitButton(x, y):
    btmX = exitButtonLocation[0] + 612.5
    btmY = exitButtonLocation[1] + 625

    if ((x > exitButtonLocation[0] and x < btmX) and (y > exitButtonLocation[1] and y < btmY)):
        # clicked on exit
        # escapeMenuScreen()
        global game
        game = False


def startButton(x, y):
    btmX = startButtonLocation[0] + 482.5
    btmY = startButtonLocation[1] + 400

    if ((x > startButtonLocation[0] and x < btmX) and (y > startButtonLocation[1] and y < btmY)):
        # clicked on character selection
        characterSelectionScreen()
        slapCharacters()


def instructionButton(x, y):
    btmX = instructionButtonLocation[0] + 775
    btmY = instructionButtonLocation[1] + 475

    if ((x > instructionButtonLocation[0] and x < btmX) and (y > instructionButtonLocation[1] and y < btmY)):
        # clicked on instructions selection
        instructionScreen()


def titleClicks(mousePosX, mousePosY):
    """Determine where player has clicked on the screen"""
    # check if mouse click was in start button
    startButton(mousePosX, mousePosY)
    # check if mouse click was in exit button
    exitButton(mousePosX, mousePosY)
    # check if mouse click was in instruction button
    instructionButton(mousePosX, mousePosY)


# **************************character selection functions**************************
def startFromCharacters():
    """Locks in the character choice and starts game"""
    # start game
    gameScreen()
    screen.blit(charactersHappy[activeCharacter], (characterLocation))


def getSpriteLocation(pos):
    """Get locations of the cursor relative to sprites, return which sprite is selected"""
    global activeCharacter
    if charactersHappy["shark"].get_rect(topleft=(characterLocations[0])).collidepoint(pos):
        activeCharacter = 'shark'
        startFromCharacters()
    elif charactersHappy["cat"].get_rect(topleft=(characterLocations[1])).collidepoint(pos):
        activeCharacter = 'cat'
        startFromCharacters()
    elif charactersHappy["bird"].get_rect(topleft=(characterLocations[2])).collidepoint(pos):
        activeCharacter = 'bird'
        startFromCharacters()
    elif charactersHappy["dog"].get_rect(topleft=(characterLocations[3])).collidepoint(pos):
        activeCharacter = 'dog'
        startFromCharacters()


# **************************Escape menu**************************
#                 top left,  bottom right
# yesLocation = [(380, 355), (495, 410)]
# noLocation = [(505, 355), (615, 410)]
# def escapeMenu(x, y): 
#     """Ask if they wanna really exit the game"""
#
#     if ((x > yesLocation[0][0] and x < yesLocation[1][0]) and (y > yesLocation[0][1] and y < yesLocation[1][1])):
#         # quit game
#         game = False
#     elif ((x > noLocation[0][0] and x < noLocation[1][0]) and (y > noLocation[0][1] and y < noLocation[1][1])):
#         # go back to previous page?
#         screen.blit(pygame.image.load(imageFilePath + 'exitScreen.png').image.fill(transparent), (375, 262.5))


# **************************game loop**************************

while game:

    # timer that constantly goes up
    # currentTime = pygame.time.get_ticks()
    # quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    # play game have
    #   print(currentScreen)
    # pygame.draw.rect(screen, black, pygame.Rect(60,60,40,40))
    pygame.draw.rect(screen, black, pygame.Rect(325, 500, 612.5, 625))  # (325, 500), (612.5, 625)
    if currentScreen == 'Title':
        titleScreen()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosX, mousePosY = pygame.mouse.get_pos()
                titleClicks(mousePosX, mousePosY)

    #               pygame.draw.rect(screen, black, pygame.Rect(30, 30, 60, 60))

    if currentScreen == 'Instructions':
        instructionScreen()
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    currentScreen = 'Title'

    if currentScreen == 'CharacterSelection':

        characterSelectionScreen()
        slapCharacters()
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN):
                # coordinate of mouse press
                pos = pygame.mouse.get_pos()
                getSpriteLocation(pos)

    """
    if currentScreen == 'Escape':
        escapeMenuScreen()
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouseX, mouseY = pygame.mouse.get_pos()
                escapeMenu(mouseX,mouseY) """

    if currentScreen == 'Game':


        currentTime = pygame.time.get_ticks()
        gameScreen()
        timerStretch()
        timerDrink()
        timerEat()
        timerGoOutside()
        slapPlayer()
        showHealth()
        slapChecks(0)
        slapChecks(1)
        slapChecks(2)
        slapChecks(3)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosX, mousePosY = pygame.mouse.get_pos()
                if checkIfOnBox(mousePosX, mousePosY):  # they clicked on a box
                    if taskChecks[checkCount] == False:
                        characterUndie()
                    addGreenCheckmark(checkCount)


    pygame.display.flip()  # update the screen