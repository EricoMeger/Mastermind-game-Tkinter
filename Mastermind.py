from tkinter import * 
from random import choice

class window():

    def __init__(self):
        self.janela = Tk()
        self.width = int(self.janela.winfo_screenwidth()/2 - 600/2)#Isso aqui é pra centralizar a janela no meio do monitor
        self.height = int(self.janela.winfo_screenheight()/2 - 400/2)
        self.canvas = Canvas(self.janela, width=600, height=400)
        self.canvas.pack()
        self.usrInput = []
        self.secret = []
        self.tentativas = 0
        self.x1 = 210
        self.x2 = 235
        self.y1 = 225
        self.y2 = 250
    
    def btnCallback(self, event):
        #Para que seja possível limpar somente a linha de bolas que o usuário está mexendo no momento, damos uma tag única para esta linha, no caso, a primeira linha será a bola0, a segunda bola1 e assim por diante. Segue abaixo
        tag = "bola" + str(self.tentativas)
        
        if event == "clear":
            #Zeramos a lista de input do usuário
            self.usrInput = []
            #Dessa forma, quando o usuário clicar no botão clear, podemos deletar somente os circulos mais recentes, da ultima linha colocada
            self.canvas.delete(tag)
            #Retornamos x para sua posição inicial
            self.x1 = 210
            self.x2 = 235
            
        else:
            #Adicionamos à lista de inputs do usuario a cor selecionada
            self.usrInput.append(event)
            #criamos um circulo com essa cor, para representar a escola
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=event, tags=tag)
            self.x1 = self.x2 + 5
            self.x2 = self.x1 + 25
            #caso o usuário tenha selecionado quatro cores, chamamos a função que checa a sequência inserida
            if len(self.usrInput) == 4:
                self.checkWin()

    def setSecret(self):
        #Se cria uma lista com as cores disponíveis
        colors = ["red", "green", "blue", "yellow", "purple", "brown", "gray", "orange"]
        for i in range(4):
            if colors:
                color = choice(colors)
                self.secret.append(color)
                #Adiciona-se na lista da senha a cor sorteada, removendo a mesma cor, para que não haja repetições
                colors.remove(color)
        print(self.secret)

    def checkWin(self):
    	#zeramos a lista de acertos e o contador
        acertos = []
        contadorAcertos = 0
       
        #Compara as duas listas (agradeço prof)
        for i, s in zip(self.usrInput, self.secret):
            if i == s: # mesma posição
                acertos.append("black") #Adiciona a um vetor para que possa imprimir os circulos depois
                contadorAcertos += 1 #incrementa a variável usada para checar a vitoria
            elif i in self.secret: # está no vetor, mas não mesma posição
                acertos.append("white")

        for i in range(len(acertos)):
            self.x1 = self.x2 + 5
            self.x2 = self.x1 + 25
            #Usamos o sort para ajeitar a lista em ordem alfabetica, dessa forma os pretos serão impressos primeiro e os brancos por ultimo, sem uma ordem que o usuario consiga se basear para saber qual cor é a correta
            acertos.sort()
            #Criamos um circulo com as cores presentes na lista
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=acertos[i])
            
        #Se tiver 4 circulos pretos
        if contadorAcertos == 4:
            self.endingScreen("vitoria")
         
        elif self.tentativas == 6:
            self.endingScreen("derrota")
    
        #após as checagens zeramos a lista de inputs do usuário, retornamos as coordenadas x para a posição inicial e diminuimos as coordenadas y para subir a posição dos circulos
        self.usrInput = []
        self.x1 = 210
        self.x2 = 235
        self.y1 -= 30
        self.y2 -= 30
        self.tentativas += 1

    def endingScreen(self, fim):
        x1 = 240 
        x2 = 265 
        y1 = 200
        y2 = 225
        #limpamos o canvas para mostrar a tela final
        self.canvas.delete("all")
        self.canvas.create_text(300, y1-10, text="A resposta era:", fill="black")
        self.canvas.create_text(300, y1+80, text="Sua última tentativa foi:", fill='black')
        #espero que você tenha comic sans baixado
        font = ('Comic Sans MS', 20, 'bold')
        
        if fim == "vitoria":
            self.canvas.create_text(300, 50, text="Parabéns!! Você ganhou!", fill="black", font=font)
        
        elif fim == "derrota":
            self.canvas.create_text(300, 50, text="Que pena!! Você perdeu...", fill="black", font=font)

        for i in range(len(self.secret)):
            #Criamos os círculos da senha e da última resposta inserida pelo usuário
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.secret[i])
            self.canvas.create_oval(x1, y1+90, x2, y2+90, fill=self.usrInput[i])
            x1 = x2 + 5
            x2 = x1 + 25

    def chamaJanela(self):
        self.janela.title("Mastermind")
        #o geometry da tela passamos os parametros largura, altura, posxInicial, posyInicial. Lá no construtor da classe é feito um calculo nas variaveis width e height que pega o centro da tela. (em teoria é pra funcionar em qualquer monitor)
        self.janela.geometry(f"600x400+{self.width}+{self.height}")
        #chamamos a função que sorteia a senha
        self.setSecret()
        #criamos as bolas clicáveis
        self.createBalls()
        #mantemos a janela aberta
        self.janela.mainloop()        

    def createBalls(self):
        #Aqui cria os botões com as cores que o usuário pode clicar para usar
        red = self.canvas.create_oval(210, 290, 235, 315, fill='red')
        #para ficar mais fácil de entender: variavel = create_oval(x1, y1, x2, y2, sendo o 1 o ponto de inicio e o 2 o ponto de fim do desenho do circulo)
        green = self.canvas.create_oval(239, 290, 264, 315, fill='green')
        blue = self.canvas.create_oval(269, 290, 294, 315, fill='blue')
        yellow = self.canvas.create_oval(299, 290, 324, 315, fill='yellow') 
        purple = self.canvas.create_oval(210, 325, 235, 350, fill='purple')
        brown = self.canvas.create_oval(239, 325, 264, 350, fill='brown') 
        orange = self.canvas.create_oval(269, 325, 294, 350, fill='orange')
        gray = self.canvas.create_oval(299, 325, 324, 350, fill='gray')
       
        self.canvas.create_text(365, 300, text="Clear", fill='black')
        clear = self.canvas.create_oval(353, 307, 378, 332, fill='white')

        
        #aqui a gente fala pro tkinter que a variável x que representa uma das bolas vai poder ser interagida usando o botão 1, significando o botão esquerdo do mouse, ou seja, pode ser clicada.
        #depois disso, definimos a função que o botão vai chamar quando for clicado, não me pergunte sobre o lambda, só sei que sem ele o bagulho não funciona
        self.canvas.tag_bind(red, '<Button-1>', lambda callback: self.btnCallback("red"))
        self.canvas.tag_bind(green, '<Button-1>', lambda callback: self.btnCallback("green"))
        self.canvas.tag_bind(blue, '<Button-1>', lambda callback: self.btnCallback("blue"))
        self.canvas.tag_bind(yellow, '<Button-1>', lambda callback: self.btnCallback("yellow"))
        self.canvas.tag_bind(purple, '<Button-1>', lambda callback: self.btnCallback("purple"))
        self.canvas.tag_bind(brown, '<Button-1>', lambda callback: self.btnCallback("brown"))
        self.canvas.tag_bind(orange, '<Button-1>', lambda callback: self.btnCallback("orange"))
        self.canvas.tag_bind(gray, '<Button-1>', lambda callback: self.btnCallback("gray"))
        self.canvas.tag_bind(clear, '<Button-1>', lambda callback: self.btnCallback("clear"))


#main
#criamos o objeto da classe
janela = window()
#chamamos a função que cria a janela
janela.chamaJanela()
