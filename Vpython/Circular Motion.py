GlowScript 3.1 VPython
from vpython import *

scene = canvas(background = color.white) # create a scene 

ball = sphere(pos=vec(100,-200,0), mass = 1, v = vec(0,10,0), radius = 5, color = color.orange, make_trail = True) # create a sphere object with position of (100,-200,0), mass of 1, volcity of (0,10,0), radius of 5, color orange, set makeTrail to True.


center = sphere(pos=vec(0,0,0), radius = 5, color = color.red)

gr_v = graph(title = 'Velocity', xtitle = 'time(s)', ytitle = 'm/s') #  create graph object with title 'Velocity', xtitle 'time(s)', and ytitle 'm/s'


vx_plot = gcurve(graph = gr_v, color = color.red)
vy_plot = gcurve(graph = gr_v, color = color.cyan) # create gcurve for y velocity

gr_power = graph(title = 'Work - Energy', xtitle = 'time(s)', ytitle = 'N m/s')

p_plot = gcurve(graph = gr_power, color = color.red)
w_plot = gcurve(graph = gr_power, color = color.blue)

gr_ang_mom = graph(title = 'Angular Momentum', xtitle = 'time(s)', ytitle = 'kg m^2/s')

lx_plot = gcurve(graph = gr_ang_mom, color = color.orange)
ly_plot = gcurve(graph = gr_ang_mom, color = color.green)
lz_plot = gcurve(graph = gr_ang_mom, color = color.red)

start_pos = ball.pos
start_v = ball.v

ball.p = ball.mass * ball.v # initialize the momentum
work = 0

t = 0 # initialize time
dt = 0.005

myrate = 2500

while ball.pos.x <= 2*start_pos.x:
    rate(myrate)
    
    F = vec(0,0,0)
    if ball.pos.y >= 0 or ball.pos.x <= 0:
        r_vec = ball.pos
        F = (ball.mass * ball.v.mag2 / r_vec.mag) * (-r_vec.hat) # centripetal force
    
    work = work + dot(F, ball.v) * dt
    ke = ((ball.p.mag)**2)/2*ball.mass
    
    ball.L = cross(ball.pos,ball.p) # calculate angular momentum - use vector multiplication
        
    ball.p += F * dt # update the momentum
    ball.v = ball.p/ball.mass # calculate the velocity
    ball.pos += ball.v * dt # calculate the position
    
    vx_plot.plot(pos = (t,ball.v.x)) # plot the x velocity as a function of time
    vy_plot.plot(pos = (t,ball.v.y)) # plot the y veloctiy as a function of time
    p_plot.plot(pos = (t,ke))
    w_plot.plot(pos = (t,work)) # plot the work as a function of time
    lx_plot.plot(pos = (t,ball.L.x)) # plot the x component of the angular momentum as a function of time
    ly_plot.plot(pos = (t,ball.L.y)) # plot the y component of the angular momentum as a function of time
    lz_plot.plot(pos = (t,ball.L.z)) # plot the z component of the angular momentum as a function of time
    
    
    t += dt
