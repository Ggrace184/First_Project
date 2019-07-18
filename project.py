import math
y = float(input ("What height are you falling from?"))
g = 9.81
#print (type (g))
t=math.sqrt(2*y/g) 
print ("this is how long it will take for the ball to fall "+str(t)+" s")
Vx = float (input("How fast are you kicking the ball?"))
x= Vx*t
print ("this is how far the ball will go: " +str(x)+" m/s")
Vy = math.sqrt(2*g*y)
Vf = math.sqrt(Vx**2+Vy**2)
print ("this is the final velocity of the ball: " +str(Vf)+" m/s")