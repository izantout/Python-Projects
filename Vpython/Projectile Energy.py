GlowScript 3.1 VPython
from vpython import *

scene = canvas(background = color.white) # make a scene with whatever background color

ground = box(pos = vec(0,-0.02,0), size = vec(6,0.02,0.4),  color = color.green)

ball = sphere(pos=vec(-3,1,0), mass = 0.5, alpha = 30 * pi / 180,  radius = 0.03,color = color.red, make_trail = True, trail_type = 'points') 
# sphere object with poition(-3,1,0), mass = 0.5, launching angle alpha = 30, radius = 0.03, color=color.red, make_trail = True, trail_type = 'points'

ball.v = vec(1, sin(ball.alpha), 0)
ball.p = ball.mass * ball.v

stone = sphere(pos=vec(-3,1,0), mass = 0.5, radius = 0.03, alpha = 30 * pi / 180, color = color.blue, mass = 0.5, make_trail = True, trail_type = 'points') # sphere object with poition(-3,1,0), mass = 0.5, launching angle alpha = 30, radius = 0.03, color=color.red, make_trail = True, trail_type = 'points'


stone.v = vec(1, sin(stone.alpha), 0)
stone.p = stone.mass * stone.v

vx = graph(title = 'Veloctiy', xtitle = 't', ytitle = 'v_x (t)') # create graph with title Veloctiy, xtitle of t and ytitle of v_x (t)
vx_b = gcurve(graph = vx, color = color.red, width = 1)
vx_s = gcurve(graph = vx, color = color.blue, width = 1)

vy = graph(title = 'Veloctiy', xtitle = 't', ytitle = 'v_y (t)') # create graph with title Veloctiy, xtitle of t and ytitle of v_x (t)
vy_b = gcurve(graph = vy, color = color.red)
vy_s = gcurve(graph = vy, color = color.blue)

work_g = graph(title = 'Work', xtitle = 't', ytitle = 'W(t)')
w_b = gcurve(graph = work_g, color = color.red)
w_s = gcurve(graph = work_g, color = color.blue) # ask
ke_b = gcurve(graph = work_g, color = color.green)
ke_s = gcurve(graph = work_g, color = color.cyan)


total_e = graph(title = 'Total energy', xtitle = 't', ytitle = 'E')
tot_e_b = gcurve(graph = total_e, color = color.blue)
tot_e_s = gcurve(graph = total_e, color = color.red)



myrate = 100

g = 0.2
mu = 0.05

t = 0
dt = 0.01 

ball.kinetic_energy_i = ball.p.mag2 / (2*ball.mass)
stone.kinetic_energy_i = stone.p.mag2 / (2*stone.mass)

ball.work = 0
stone.work = 0

while ball.pos.y > 0: 
    
    rate(myrate)
    
    F_s = vec(0, 0, 0) 
    
    stone.p = stone.p + F_s * dt # update momentum for the stone
    stone.v = stone.p/stone.mass # update velocity
    stone.pos += stone.v * dt # update position
    
    
    F_b = vec(0,ball.mass * -g,0) + -mu * ball.v.mag2 * ball.v.hat # define gravitational force on ball
    
    ball.p = ball.p + F_b * dt # update momentum for the ball
    ball.v = ball.p/ball.mass # update velocity
    ball.pos += ball.v * dt # update position
    
    
    vx_b.plot(pos = (t,ball.v.x)) # plot the x velocity of the ball as a function of time
    vx_s.plot(pos = (t,stone.v.x)) # plot the x velocity of the stone as a function of time
    
    vy_b.plot(pos = (t,ball.v.y)) # plot the y velocity of the ball as a function of time
    vy_s.plot(pos = (t,stone.v.y)) # plot the y velocity of the stone as a function of time
    
    
    ball.work = ball.work + dot(F_b, ball.v) * dt # use the work update equation
    stone.work = stone.work + dot(F_s, ball.v) * dt # use the work update equation
    
    ball.kinetic_energy_f = ball.p.mag2 / (2*ball.mass) # calculate the kenetic energy at curent loop iterration
    stone.kinetic_energy_f = stone.p.mag2 / (2*stone.mass) # calculate the kenetic energy at curent loop iterration
    
    
    ball.e = ball.kinetic_energy_f + (F_b.mag * ball.pos.y) # add gravitational potential energy mgball.pos.y
    stone.e = stone.kinetic_energy_f 
    
    w_b.plot(pos = (t,ball.work)) # plot work for ball as a function of time
    w_s.plot(pos = (t,stone.work)) # plot work for stone as a function of time
    
    ke_b.plot(pos=(t,ball.kinetic_energy_f-ball.kinetic_energy_i)) # use the work energy theorem - plot the energy difference for the ball as a function of time
    ke_s.plot(pos=(t,stone.kinetic_energy_f-stone.kinetic_energy_i)) # do the same for the stone
    
    tot_e_b.plot(pos = (t,ball.e))
    tot_e_s.plot(pos = (t,stone.e))
    t += dt
