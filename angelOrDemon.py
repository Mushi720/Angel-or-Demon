import pygame
import json

#Colors
BLACK = (0, 0, 0)
GRAY = (100,100,100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SKIN = (196, 98, 0)

#Start Pygame
pygame.init()

#Definitions
size = (700, 500)
clock = pygame.time.Clock()
done = False

#More definitions
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Angel or Demon")

#Status Class
class GameStatus():
    def getStatus(self):
        return self.status
    def setStatus(self, value):
        self.status = value 
    def getMissao(self):
        return self.missao
    def setMissao(self, value):
        self.missao = value           
    def getStatusDialog(self):
        return self.statusDialog
    def setStatusDialog(self, value):
        self.statusDialog = value
    def getFree(self):
        return self.free
    def setFree(self, value):
        self.free = value
    def getJail(self):
        return self.jail
    def setJail(self, value):
        self.jail = value
    def getMoney(self):
        return self.money
    def setMoney(self, value):
        self.money = value   
    def getInjustice(self):
        return self.injustice
    def setInjustice(self, value):
        self.injustice = value
    def getWitnessChanged(self):
        return self.witnessChanged
    def setWitnessChanged(self, value):
        self.witnessChanged = value 
        
#Set Initial Classes     
game = GameStatus()
game.setStatus(1)
game.setMissao(1)
game.setFree(0)
game.setJail(0)
game.setMoney(3000)
game.setInjustice(0)
game.setStatusDialog(0)
game.setWitnessChanged(True)

#Load Json 
file = open("script.txt", "r")
falas = file.read()
file.close() 
falas = json.loads(falas)   

#Game Classes    
class HomeScreen():
    def screen(self):
        #Title
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen,BLACK,[100,50,500,100], 5)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Angel or Demon",True,BLACK)
        screen.blit(text, [270, 90])
        #Start Button
        startButton = pygame.draw.rect(screen,BLACK,[250,300,200,50])        
        if (startButton.collidepoint(pos)):
            startButton = pygame.draw.rect(screen,GRAY,[250,300,200,50])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Start",True,WHITE)
        screen.blit(text, [320, 315])    
        #Quit Button
        quitButton = pygame.draw.rect(screen,BLACK,[250,377,200,50])
        if (quitButton.collidepoint(pos)):
            quitButton = pygame.draw.rect(screen,GRAY,[250,377,200,50])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Quit",True,WHITE)
        screen.blit(text, [318, 390])
        #Mouse Event
        if (event.type == pygame.MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            if (startButton.collidepoint(pos)):
                game.setStatus(2)
            elif (quitButton.collidepoint(pos)):
                global done
                done = True
                
class GameScreen:   
    person = ""
    def printOnWindow(self):
        y = 240
        for text in falas["st"+ str(game.getMissao())][self.person]:
            y+=20
            font = pygame.font.SysFont('Calibri', 20, True, False)
            text = font.render(text,True,GREEN)
            screen.blit(text, [20, y])             
    def screen(self):
        pos = pygame.mouse.get_pos()
        missao = "st"+ str(game.getMissao())
        #Table
        pygame.draw.rect(screen,BLACK,[200,350,500,150], 5)
        #Suspeito
        pygame.draw.rect(screen,GREEN,[400,200,100,150])
        suspect = pygame.draw.circle(screen, SKIN, (450, 160), 40)
        pygame.draw.rect(screen,RED,[440,180,20,10])
        pygame.draw.circle(screen, BLACK, (440, 150), 5)
        pygame.draw.circle(screen, BLACK, (460, 150), 5)
        pygame.draw.line(screen, BLACK, [450,160], [450,170], 5)
        pygame.draw.line(screen, YELLOW, [440,122], [460,122], 5)
        pygame.draw.line(screen, GREEN, [350,300], [410,210], 20)
        pygame.draw.line(screen, GREEN, [550,300], [490,210], 20)
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text = font.render("2448",True,BLACK)
        screen.blit(text, [430, 230])         
        #Option Bar
        pygame.draw.rect(screen,BLACK,[0,0,700,40], 5)
        text = font.render("R$ "+str(game.getMoney()),True,BLACK)
        screen.blit(text, [20, 10])           
        text = font.render("Caso: "+str(game.getMissao()),True,BLACK)
        screen.blit(text, [220, 10])          
        #Suspect Screen
        pygame.draw.rect(screen,BLACK,[200,40,500,310], 5)
        #Window
        pygame.draw.rect(screen,BLACK,[0,250,200,250], 5)
        #Buttons
        #FreeButton
        freeButton = pygame.draw.rect(screen,GREEN,[500,7,75,25])
        if freeButton.collidepoint(pos):
            freeButton = pygame.draw.rect(screen,(0, 200, 0),[500,7,75,25])
        text = font.render("Angel",True,WHITE)
        screen.blit(text, [511, 12])        
        #JailButton
        jailButton = pygame.draw.rect(screen,RED,[600,7,75,25])
        if jailButton.collidepoint(pos):
            jailButton = pygame.draw.rect(screen,(200, 0, 0),[600,7,75,25])
        text = font.render("Demon",True,WHITE)
        screen.blit(text, [607, 12])         
        #Police Officer A
        policeA = pygame.draw.rect(screen,BLACK,[0,40,200,70], 5)
        text = font.render("Policial A",True,BLACK)
        if (policeA.collidepoint(pos)):
            text = font.render("Policial A",True,GRAY)
        screen.blit(text, [50, 70])
        #Police Officer B
        policeB = pygame.draw.rect(screen,BLACK,[0,110,200,70], 5)
        text = font.render("Policial B",True,BLACK)
        if (policeB.collidepoint(pos)):
            text = font.render("Policial B",True,GRAY)
        screen.blit(text, [50, 140])
        #Witness
        witness = pygame.draw.rect(screen,BLACK,[0,180,200,70], 5)
        text = font.render("Testemunha",True,BLACK)
        if (game.getMoney() < 1):
            text = font.render("Testemunha",True,GRAY)
        if (witness.collidepoint(pos)):
            text = font.render("Testemunha",True,GRAY)
        screen.blit(text, [40, 210])        
        #Basket
        basket = pygame.draw.rect(screen,BLACK,[250,380,50,90],5)
        #Computer
        pygame.draw.rect(screen,BLACK,[550,355,80,80],5)
        computerScreen = pygame.draw.rect(screen,BLUE,[565,370,50,50])
        pygame.draw.rect(screen,BLACK,[550,445,80,40],5)
        pygame.draw.line(screen, BLACK, [550,465], [630,465], 5)
        pygame.draw.circle(screen, BLACK, (650, 460),10,5)
        #Mouse Event
        if (event.type == pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            #computerScreen
            if (computerScreen.collidepoint(pos)):
                game.setStatusDialog(1)
            #basket
            if (basket.collidepoint(pos)):
                game.setStatusDialog(2)
            #freeButton
            if (freeButton.collidepoint(pos)):
                pygame.time.wait(1000)
                if(falas[missao]["Inocente"] == "False"):
                    game.setInjustice(game.getInjustice()+1)
                if (game.getMissao() >= 10):
                    game.setStatus(3)
                game.setWitnessChanged(True)
                game.setFree(game.getFree()+1)
                game.setMissao(game.getMissao()+1)
                missao = "st"+ str(game.getMissao())
                self.person = ""
            #jailButton
            if (jailButton.collidepoint(pos)):
                pygame.time.wait(1000)
                if(falas[missao]["Inocente"] == "True"):
                    game.setInjustice(game.getInjustice()+1)              
                if (game.getMissao() >= 10):
                    game.setStatus(3)
                game.setWitnessChanged(True)
                game.setJail(game.getJail()+1)
                game.setMissao(game.getMissao()+1)
                missao = "st"+ str(game.getMissao())
                self.person = ""
            #policeA
            if (policeA.collidepoint(pos)):
                self.person = 'PolicialA'
            #policeB
            if (policeB.collidepoint(pos)):
                self.person = 'PolicialB'
            #witness
            if (witness.collidepoint(pos)):
                pygame.time.wait(1000)
                if (game.getMoney() > 0 and game.getWitnessChanged()==True):
                    game.setWitnessChanged(False)
                    game.setMoney(game.getMoney() - 1000)
                    self.person = 'Testemunha'
            #suspect
            if (suspect.collidepoint(pos)):
                self.person = 'Suspeito'            
        
        if self.person != "":        
            self.printOnWindow()
        
        #Open a Dialog
        if (game.getStatusDialog() == 1):
            dialogInfo = DialogInfo()
            dialogInfo.dialog()  
        if (game.getStatusDialog() == 2):
            dialogThings = DialogThings()
            dialogThings.dialog()          

class ResultScreen():
    def screen(self):
        #Status PCC
        if game.getFree() > 5:
            statusPCC = "ALTA"
            statusPopulacao = "BAIXA"
        else:
            statusPCC = "BAIXA"
            statusPopulacao = "ALTA"
        #Title
        pygame.draw.rect(screen,BLACK,[50,50,600,100], 5)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Missao Completa",True,BLACK)
        screen.blit(text, [270, 90])
        #Right Box
        pygame.draw.rect(screen,BLACK,[50,170,200,260], 5)
        #Data
        text = font.render("Numero de casos: 10",True,BLACK)  
        screen.blit(text, [270, 180])
        text = font.render("Condenados: "+str(game.getJail()),True,BLACK)  
        screen.blit(text, [270, 210])
        text = font.render("Inocentados: "+str(game.getFree()),True,BLACK) 
        screen.blit(text, [270, 240])   
        text = font.render("Satisfacao da Populacao: "+statusPopulacao,True,BLACK) 
        screen.blit(text, [270, 270])   
        text = font.render("Satisfacao do PCC: "+statusPCC,True,BLACK) 
        screen.blit(text, [270, 300])     
        text = font.render("Injusticas: "+str(game.getInjustice()),True,BLACK) 
        screen.blit(text, [270, 330])         
        #Next Button
        nextButton = pygame.draw.rect(screen,BLACK,[570,400,80,30])
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text = font.render("NEXT",True,WHITE)        
        screen.blit(text, [587, 407])       
        #Mouse Event
        if (event.type == pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            if (nextButton.collidepoint(pos)):
                game.setStatus(4)        
            
class MessageScreen():
    def screen(self):
        pygame.draw.rect(screen,BLACK,[50,50,600,400], 5)
        #Message
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Obrigado por atrapalhar os planos do PCC na cidade",True,RED)        
        screen.blit(text, [70, 70]) 
        text = font.render("do Recife. Esta eh uma versao beta de Angel or",True,RED)        
        screen.blit(text, [70, 100])   
        text = font.render("Demon. Para ficar por dentro das novidades sobre",True,RED)        
        screen.blit(text, [70, 130]) 
        text = font.render("o jogo acesse mushiworld.azurewebsites.net",True,RED)        
        screen.blit(text, [70, 160])
        #Menu Button
        menuButton = pygame.draw.rect(screen,BLACK,[570,453,80,30])
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text = font.render("MENU",True,WHITE)
        screen.blit(text, [587, 460])
        pos = pygame.mouse.get_pos()
        if menuButton.collidepoint(pos):
            if (event.type == pygame.MOUSEBUTTONUP):
                game.setStatus(1)
            
class DialogInfo():
    def dialog(self):
        missao = "st"+ str(game.getMissao())
        pygame.draw.rect(screen,WHITE,[100,50,500,400])
        pygame.draw.rect(screen,BLACK,[100,50,500,400], 5)
        pygame.draw.line(screen, BLACK, [100,80], [600,80], 5)
        closeButton = pygame.draw.rect(screen,RED,[560,55,20,20])
        pygame.draw.rect(screen,BLACK,[120,110,100,100],5)      
        pygame.draw.rect(screen,BLACK,[120,250,460,180],5)
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text = font.render("Ficha do Suspeito",True,BLACK)
        screen.blit(text, [120, 57])
        #Suspect Photo
        pygame.draw.circle(screen, SKIN, (170, 160), 40)
        pygame.draw.rect(screen,RED,[160,180,20,10])
        pygame.draw.circle(screen, BLACK, (160, 150), 5)
        pygame.draw.circle(screen, BLACK, (180, 150), 5)
        pygame.draw.line(screen, BLACK, [170,160], [170,170], 5)
        pygame.draw.line(screen, YELLOW, [160,122], [180,122], 5)          
        #Write on Dialog
        text = font.render(falas[missao]['Info'][0],True,BLACK)
        screen.blit(text, [230, 110])        
        text = font.render(falas[missao]['Info'][1],True,BLACK)
        screen.blit(text, [230, 130])   
        x = 0
        y = 220
        for text in falas[missao]['Info']:
            if x > 1:
                text = font.render(falas[missao]['Info'][x],True,BLACK)
                screen.blit(text, [130, y])  
            y+=20
            x+=1
        #Mouse Event
        if (event.type == pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            if (closeButton.collidepoint(pos)):
                game.setStatusDialog(0)


class DialogThings():
    def dialog(self):
        missao = "st"+ str(game.getMissao())
        things = falas[missao]['Pertences']
        pygame.draw.rect(screen,WHITE,[100,50,500,400])
        pygame.draw.rect(screen,BLACK,[100,50,500,400], 5)
        pygame.draw.line(screen, BLACK, [100,80], [600,80], 5)
        closeButton = pygame.draw.rect(screen,RED,[560,55,20,20])
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text = font.render("Pertences do Suspeito",True,BLACK)
        screen.blit(text, [120, 57])
        #Things
        #Celular
        if 1 in things:
            pygame.draw.rect(screen,BLACK,[130,90,50,100], 5)
            pygame.draw.rect(screen,BLUE,[135,95,40,40])
            pygame.draw.line(screen, BLACK, [130,140], [180,140], 5)
            pygame.draw.line(screen, BLACK, [130,150], [180,150], 5)
            pygame.draw.line(screen, BLACK, [130,160], [180,160], 5)
            pygame.draw.line(screen, BLACK, [130,170], [180,170], 5)
            pygame.draw.line(screen, BLACK, [130,180], [180,180], 5)
            pygame.draw.line(screen, BLACK, [155,140], [155,190], 5)
        #Revolver
        if 2 in things:
            pygame.draw.rect(screen,BLACK,[200,90,100,30], 5)
            pygame.draw.rect(screen,BLACK,[240,95,30,20], 5)
            pygame.draw.rect(screen,BLACK,[198,120,20,40])
            pygame.draw.rect(screen,BLACK,[220,120,20,10],5)
        #Maconha
        if 3 in things:
            pygame.draw.rect(screen,GREEN,[320,90,100,50])
        #Faca
        if 4 in things:
            pygame.draw.line(screen, BLACK, [470,90], [470,130], 5)
            pygame.draw.line(screen, BLACK, [460,130], [480,130], 5)
            pygame.draw.rect(screen,BLACK,[466,130,10,30])
        #Mouse Event
        if (event.type == pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            if (closeButton.collidepoint(pos)):
                game.setStatusDialog(0)
                 
#Classes
homeScreen = HomeScreen()        
gameScreen = GameScreen()  
resultScreen = ResultScreen()
messageScreen = MessageScreen()

"""
#Sound
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
"""

#Main loop
while not done:
    #Exit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #To fill the screen
    screen.fill(WHITE)
    
    if game.getStatus() == 1:
        homeScreen.screen()
    if game.getStatus() == 2:
        gameScreen.screen()   
    if game.getStatus() == 3:
        resultScreen.screen()          
    if game.getStatus() == 4:
        messageScreen.screen()  
               
    #To draw
    pygame.display.flip()
    #Time
    clock.tick(60)

#End Game
pygame.quit()
