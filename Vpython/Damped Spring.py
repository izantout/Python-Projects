GlowScript 3.1 VPython
from vpython import *

scene = canvas(background = color.white) # create a scene with whatever color i want

ground = box(pos = vec(0, -0.02, 0), size = vec(3, 0.02, 0.4), color = color.green)

g = 9.8
mu = 0.01 # kinetic friction coefficent between spring box and ground

l = 2.5

b_box = box(pos = vec(-1, 0.1, 0), size = vec(0.4, 0.2, 0.1), color = color.red, make_trail = True)


s_box = box(pos = vec(b_box.pos.x + 1, 0.1, 0), v = vec(0, 0, 0), m = 1, size = vec(0.2, 0.2, 0.1), color = color.red)


spring = helix(pos = b_box.pos, axis = s_box.pos - b_box.pos, k = 5, l_0 = 2, radius = 0.05, color = color.orange)


vgraph = graph(title = 'Velocity', xtitle = 't', ytitle = 'v(t)') # create graph object with title 'Velocity', xtitle = 't', and y title = 'v(t)'
vx_a = gcurve(graph = vgraph, color = color.cyan) # create gcurve associated with vgraph and a color of cyan

scene.waitfor('click')

myrate = 200

s_box.p = s_box.m * s_box.v # initialize the momentum of the s_box (use s_box.p)

t = 0
dt = 0.01

s_box.old_v = s_box.v # create old velocity variable 
s_box.T = 0 # create period time and set it to 0

while t < 30:
    rate(myrate)
    
    spring.pos = b_box.pos
    
    spring.axis = s_box.pos - b_box.pos # calculate spring axis
    
    l = s_box.pos - b_box.pos # recalculate spring length
    
    spring.s = l.mag - spring.l_0 # difference between total length minus equilibrium length
    
    F_s = -spring.k * spring.s * spring.axis.hat # calculate the spring force
    F_f = -mu * s_box.m * g * s_box.v.hat # finish the equation
    
    F = F_s + F_f
    
    s_box.p = s_box.p + F * dt # calculate the momentum of s_box
    s_box.v = s_box.p / s_box.m # calculate the velocity
    s_box.pos += s_box.v * dt # calculate the position
    
    vx_a.plot(pos = (t,s_box.v.x))
    
    t = t + dt # update time
    
    if s_box.old_v.x > 0 and s_box.v.x < 0:
        print('Period: ', s_box.T, 2*pi*sqrt(s_box.m/spring.k))
        s_box.T = 0
    
    s_box.old_v = s_box.v # update old box velocity
    s_box.T = s_box.T + dt # update periode timer
   
