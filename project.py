import math
#MVP
y = float(input ("What height are you falling from?"))
g = 9.81
t=math.sqrt(2*y/g) 
print ("this is how long it will take for the ball to fall "+str(t)+" s")
Vx = float (input("How fast are you kicking the ball?"))
x= Vx*t 
print ("this is how far the ball will go: " +str(x)+" m/s")
Vy = math.sqrt(2*g*y)
Vf = math.sqrt(Vx**2+Vy**2) 
print ("this is the final velocity of the ball: " +str(Vf)+" m/s")

#STARTING SECOND PART HERE-Projectile Motion 
def projectile_motion(g):
    theta = float(input("What angle, from 0-90 do you want to kick the ball at?"))
    while theta > 90:
        theta = float(input("What angle, from 0-90 do you want to kick the ball at?"))
    while theta < 0:
        theta = float(input("What angle, from 0-90 do you want to kick the ball at?"))
    Vi = Vx
    H = (Vi**2 * math.sin(theta)**2) / (g*2)
    Height = H + y
    t1 = math.sqrt(2 * Height / g)
    t2 = Vi*math.sin(theta)/g
    t_total = t1 + t2
    Final_v = math.sqrt (Vi* math.cos(theta) + ((Vi*math.sin(theta))**2 + 2*g*y))
    distance = t_total * Vi * math.cos(theta)
    print ("this is the peak height of the ball: " +str(Height)+" m")
    print ("this is the time it will take for the ball the land: " +str(t_total)+" s")
    print ("this is the final velocity of the ball: " +str(Final_v)+" m/s")
    print ("this is the total horizontal distance the ball travels: "+ str(distance)+ " m")
print (projectile_motion(g))

#print ("Imagine you're kicking a ball on another planet")

# print float(input("Imagine you're kicking a ball on another planet, hat other planet in our solar system would you be on?"))
# if input== sun:
#     g= gsun=274
# if input== mercury:
#     g= gmercury = 3.7
# if input== venus:
#     g= gvenus = 8.87
# if input==
 #   gmars = 3.71
# gjupiter = 24.79
# guranus = 11.15
# gpluto = 0.62
