import turtle as t
t.speed(0) #pour aller plus vite
t.hideturtle() #cacher la tortue
t.setx(0)
t.sety(0)

#1- Des petites commandes pour tester les fonct de turtle
t.forward(60) #aller tout droit de 60
t.left(45) #tourner à gauche de 45 degrés
t.forward(30)
t.right(120) #tourner à droite de 120 degrés
t.penup() #lever le stylo
t.backward(50)#reculer de 50
t.pendown() #reposer le stylo
t.circle(30) #tracer un cercle de rayon 30
t.dot(12,'red') #tracer un point rouge de diamètre 12
t.penup()
t.setpos((0,0))

#2 Essayez de tracer un carré de 40x40




#2 On va maintenant faire une petite maison
#celle-ci doit faire 80 de côté, avoir une porte de 30 de côté, et un toit équilatéral
#compléter la fonction ci-dessous !


def maison():
    #tout d'abord, le carré qui compose les murs
    for i in range(...):
        t.forward(...)
        ...(...) #tourner à gauche
    t.penup() #on se déplace maintenant avec le stylo levé vers le point de départ de la porte
    t.forward(25)
    t.left(90)
    t.pendown()
    for i in range(...): #tracer les deux premiers côtés de la porte
        t.forward(...)
        ...(90)
    t.forward(30) #le dernier côté
    t.left(90)
    t.penup()
    # on se déplace maintenant vers le coin en haut à droite pour tracer le toit
    t.forward(...)
    t.left(...)
    t.forward(...)
    # on est dans le coin en haut, il faut maintenant se placer dans la bonne direction et tracer le toit
    # rappel, c'est un triangle équilatéral
    ...
    t.penup()
    t.home()



maison()


#On peut maintenant essayer de tracer plusieurs maisons côtes à côtes
#compléter la fonction village ci-dessous
def village(nb_maisons):
    x,y=0,0
    t.home() #revient à la position (0,0)
    for ... :
        ... #tracer une maison
        ... #on décale la tortue de façon à ce que la maison suivante soit dessinée à côté de la précédente


village(...)

t.exitonclick()
