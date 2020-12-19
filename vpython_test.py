from vpython import *
import random

#constant declare
g = 9.8
size = 0.001
b = 0.47
height = 15

#background settings
scene = canvas(height = 800, width = 800, center = vec(0,0,0), background = vec(0.5,0.3,0.5))
people = box(height = 1.8, width = 0.1, length = 0.1, color = color.orange,pos = vec(0,-15,0))
floor = box(height = 0.1, width = 0.01, length = 20, color = color.black, pos = vec(0,-15.9,0))

#object
rains = [sphere(radius = 0.2,color = color.cyan, pos = vec(10*random.random(),height,0),v = vec(0,0,0)) for i in range(100)]


#collision detect
def collision(people_pos,rain_pos):
    if people_pos.x - 0.05 < rain_pos.x < people_pos.x + 0.05 and people_pos.z - 0.05 < rain_pos.z < people_pos.z + 0.05 and rain_pos.y < people_pos.y + 0.9 + size:return True
    elif rain_pos.x - people_pos.x < 0.05 + size and -15.9 < rain_pos.y < -14.1 and people_pos.z - 0.05 < rain_pos.z < people_pos.z + 0.05:return True
    
    else:
        return False



#motion
hit = 0
t,dt = 0, 0.001
while t<20:
    rate(1000)
    for rain in rains:
        if rain.pos.y > -15.9:
            rain.a = vec(0,-g,0)
            rain.v += rain.a * dt
            rain.pos += rain.v*dt
        if collision(people.pos,rain.pos) == True:
            hit += 1
            rain.visible = False
            del rain
        elif rain.pos.y < floor.pos.y + size:
            rain.visible = False
            del rain
    t+=dt
    #print(t)
    #if t > 3:
        #print(f'rain hit people:{hit}')
        #break
        