import turtle   
import winsound
import random

#Criando variaveis
caneta01 = turtle.Turtle()
janela = turtle.Screen()

def musicLoad():
    lista_musica =["Alok_-Ilkay-Sencan_-Tove-Lo-Don_t-Say-Goodbye.wav","Blinding-Lights-_Instrumental_.wav","Vintage-Culture_-Adam-K-ft.-MKLA-Save-Me-Karaoke-Instrumental.wav","Vintage-Culture_-Rooftime-I-Will-Find-Instrumental.wav"]
    
    musica = random.choice(lista_musica)
   
    return musica

#tela de load
def Tela_load():
    winsound.PlaySound(musicLoad(), winsound.SND_ASYNC)

    loading = turtle.Turtle()
    loading.shape("square")
    loading.color("White")
    loading.penup()
    loading.goto(0,-130)
    
    turtle.setup(width=800, height=600)
    turtle.title("PINGPOW")
    turtle.bgpic("loadTela.png")
    

    texto = turtle.Turtle()
    texto.speed(0)
    texto.penup()
    texto.hideturtle()
    texto.goto(0,-100)
    texto.color("White")

    for i in range(22):
        loading.shapesize(stretch_wid=1,stretch_len=1+(i/4))
        texto.clear()
        texto.write("{}%".format(i*5),align="center",font=(20))
        turtle.delay(500)
       
    janela.clear()
    
Tela_load()


# gera os cenarios de forma aleatoria
def gera_cenario():
    lista =["1.png","2.png","3.png","fundo4.png"]
    
    n = random.choice(lista)
   
    return n

#criando área da janela do game

janela.bgpic(gera_cenario())
janela.title("PINGPOW")
janela.setup(width=800, height=600)
janela.tracer(0)
caneta01.speed(0)
caneta01.shapesize(5)
caneta01.up()
caneta01.shape("blank")

#criando jogador A
jogador_A = turtle.Turtle()
jogador_A.speed(0)
jogador_A.shape("square")
jogador_A.color("Red")
jogador_A.shapesize(stretch_wid=10, stretch_len=1)
jogador_A.penup()
jogador_A.goto(-350,0)

#criando jogador B
jogador_B = turtle.Turtle()
jogador_B.speed(0)
jogador_B.shape("square")
jogador_B.color("Blue")
jogador_B.shapesize(stretch_wid=10, stretch_len=1)
jogador_B.penup()
jogador_B.goto(350,0)

#criando a Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("White")
bola.penup()
bola.goto(0,0)

bola.dx = 1.1
bola.dy = 1.1

#placar
placar_A = 0
placar_B = 0

placar = turtle.Turtle()
placar.speed(0)
placar.color("White")
placar.penup()
placar.hideturtle()
placar.goto(0,260)
placar.write(" VERMELHO: 0   AZUL: 0 ",align="center",font=("courier",20, "normal","bold"))


#funções 
def jogador_A_up():
    y = jogador_A.ycor()
    y += 30
    jogador_A.sety(y)

def jogador_A_down():
    y = jogador_A.ycor()
    y -= 30
    jogador_A.sety(y)


def jogador_B_up():
    y = jogador_B.ycor()
    y += 30
    jogador_B.sety(y)

def jogador_B_down():
    y = jogador_B.ycor()
    y -= 30
    jogador_B.sety(y) 
#Movimentação do jogador A
janela.listen()
janela.onkeypress(jogador_A_up,"w") 
janela.onkeypress(jogador_A_down,"s") 

#Movimentação do jogador B
janela.onkeypress(jogador_B_up,"Up") 
janela.onkeypress(jogador_B_down,"Down") 

def som_colisao():
    winsound.PlaySound('impacto.wav', winsound.SND_ASYNC)

def som_torcida():
    winsound.PlaySound('torcida.wav', winsound.SND_ASYNC)
    

def live_music():
    winsound.PlaySound(musicLoad(), winsound.SND_ASYNC)


#live_music()
#Game loop

while True:
    janela.update()
    #Movimento da bola


    bola.setx(bola.xcor()+bola.dx)
    bola.sety(bola.ycor()+bola.dy)

    #colisão com o limite da tela de cimas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    #colisão que gera o ponto
    if bola.xcor() > 390:
        bola.color("White")
        bola.dx *=-1
        placar.clear()
        placar_A +=1
        som_torcida()
        placar.write(f" VERMELHO: {placar_A}   AZUL: {placar_B} ",align="center",font=("courier",20, "normal","bold"))
        



    if bola.xcor() < -390:
        bola.color("White")
        bola.dx *=-1
        placar.clear()
        placar_B +=1
        som_torcida()
        placar.write(f" VERMELHO: {placar_A}   AZUL: {placar_B} ",align="center",font=("courier",20, "normal","bold"))
        
        


    #colisão do jogador com a tela cima/baixo
    if jogador_A.ycor() < -240:
        jogador_A.sety(-240)

    if jogador_A.ycor() > 240:
        jogador_A.sety(240)

    if jogador_B.ycor() < -240:
        jogador_B.sety(-240)

    if jogador_B.ycor() > 240:
        jogador_B.sety(240)

    #colião da bola com os jogadores
    if (bola.xcor() > 340 and bola.xcor() < 350 ) and (bola.ycor() < jogador_B.ycor() + 140 and bola.ycor() > jogador_B.ycor() -140):
        som_colisao()
        bola.setx(340)
        bola.color("Blue")
        bola.dx *= -1
    
    if (bola.xcor() < -340 and bola.xcor() > -350 ) and (bola.ycor() < jogador_A.ycor() + 140 and bola.ycor() > jogador_A.ycor() -140):
        som_colisao()
        bola.setx(-340)
        bola.color("Red")
        bola.dx *= -1
    
    if placar_A == 3:
        janela.clear()
        turtle.bgpic("rosa.png")
        turtle.delay(700)
        
        

    if placar_B == 3:
        janela.clear()
        turtle.bgpic("verde.png")
        turtle.delay(700)     
        
    
