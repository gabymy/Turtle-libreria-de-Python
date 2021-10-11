# import package
import turtle
import random

col = ['red', 'yellow', 'green', 'blue', 'white', 'black', 'orange', 'pink']
  
#pantalla
sc=turtle.Screen()
sc.setup(500,350)

print('-----------------------------')
print('AL FINALIZAR TOCA LA PANTALLA')
print('-----------------------------')
  
#turtle
turtle.speed(1)
turtle.up()
turtle.setpos(-50,100)
turtle.down()
turtle.shape("circle")
turtle.color('purple')
turtle.width(2)


def fxn(x,y):
    global col
    ind = random.randint(0, 7)
    sc.bgcolor(col[ind])

   
  
# bucle para construccion
for i in range(6):
    
    
    turtle.forward(100)
      
    # angulo de giro
    turtle.tilt(180)
      
    # pantalla
    turtle.stamp()
      
    # movimiento a la derecha
    turtle.right(60)
      

turtle.ht()
turtle.onscreenclick(fxn)
