GlowScript 3.1 VPython
from vpython import *

scene = canvas(background = color.white) # Make a scene with whatever color you want. 

fixed_point = sphere(pos = vec(0,6,0), radius = 0.5, color = color.red)

l_0 = 8
theta_0 = 30 * pi / 180
omega_0 = 0
g = 10

ball = sphere(pos = fixed_point.pos + vec(l_0*sin(theta_0), l_0 * cos(theta_0), 0), mass = 0.5, radius = 0.2, color = color.blue)

spring = helix(pos = fixed_point.pos, axis = ball.pos - fixed_point.pos, radius = 0.2, color = color.orange)# position of fixed_point.pos, make an axis (this connects the flucrum to the end), radius = 0.2, color = color.orange)

ball.omega = omega_0
ball.p = ball.mass * l_0 * ball.omega
a_graph = graph(title = 'Theta - Omega', xtitle = 't', ytitle = 'theta - omega') # create graph object with title' Theta - omega', xtitle 't', ytitle ;theta - omega'

theta_plot = gcurve(graph = a_graph, color = color.red) # gcurve associated with a_graph with color red
omega_plot = gcurve(graph = a_graph, color = color.green) # gcurve associated with a_graph with colo green

scene.waitfor('click')

myrate = 200

ball.theta = theta_0
t = 0 # initialize the time 
dt = 0.01 # create time step of 0.01

ball.omega_old = ball.omega
ball.T = 0

while t < 20:
    rate(myrate)
    
    spring.pos = fixed_point.pos
    spring.axis = ball.pos - fixed_point.pos # update spring axis
    
    F = -ball.mass * g * sin(ball.theta)
    
    ball.p = ball.p + F * dt # calculate moentum
    ball.omega = ball.p / (ball.mass * l_0)
    ball.theta = ball.theta + ball.omega * dt
    
    ball.pos = fixed_point.pos + vec(l_0*sin(ball.theta), -l_0*cos(ball.theta), 0)
    
    theta_plot.plot(pos = (t, ball.theta))# plot ball.theta versus time
    omega_plot.plot(pos = (t, ball.omega))# plot ball.omega versus time
    
    t = t + dt
    
    
    if ball.omega_old > 0 and ball.omega < 0:
        print(ball.T, 2*pi*sqrt(l_0/g))
        ball.T = 0
        
    ball.omega_old = ball.omega
    ball.T = ball.T + dt                                       
