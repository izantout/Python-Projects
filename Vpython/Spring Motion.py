GlowScript 3.1 VPython
from vpython import *

scene = canvas(background = color.white)

fix_point = sphere(pos = vec(0,2,0), radius = 0.2, color = color.red)

# Physics constants

l_0 = 1.13          # initial value of x' 
l_0_spring = 1      # unstretched spring length - like x_0
k_spring = 5        # spring constant
m = 0.5
g = 10
mu = 0.1            # damping coeff

ball = sphere(pos = fix_point.pos + vec(0,-l_0,0), mass = m, radius = 0.1, color = color.blue, make_trail = True, v = vec(0,0,0)) # sphere object with pos equal to pos of fix_point + vec(0,-l_0,0)
        # mass = m, zero velocity, radius 0.1, color blue
        
spring = helix(pos = fix_point.pos, axis = ball.pos - fix_point.pos, 
                radius = 0.1, color = color.orange)
                
vg = graph(title = 'Velocity', xtitle = 't', ytitle = 'v(t)') # Create graph object with title 'Velocity', xtitle 't', ytitle 'v(t)'
vx_b = gcurve(graph = vg, color = color.cyan) # Create gcurve associated with vg with color cyan
vy_b = gcurve(graph = vg, color = color.magenta) # Create gcurve associated with vg with color magenta

scene.waitfor('click')

myrate = 200

ball.p = ball.mass * ball.v     # initialize momentum

t = 0                           # initialize time
dt = 0.01                       # initialize timestep

ball.old_v = ball.v
ball.T = 0

while t < 10:
    rate(myrate)
    
    spring.pos = fix_point.pos
    spring.axis = ball.pos - fix_point.pos
    
    l = ball.pos - fix_point.pos        # Total length of spring
    spring.s = abs(l_0_spring - l.mag) #me
    
    F_s = -k_spring * spring.s * spring.axis.hat  # Calculate spring force using spring.s
    F_g = ball.mass * vec(0,-g,0)       # grav force
    
    F_d = -mu * ball.v.mag2 * ball.v.hat        # quadratic drag
   #  F_d = -mu * ball.v.mag * ball.v.hat         # Linear drag
    
    F = F_s + F_g + F_d
    
    ball.p = ball.p + F * dt    # calculate momentum using total force
    ball.v = ball.p/ball.mass   # calculate velocity
    ball.pos += ball.v * dt     # calculate position
    
    spring.axis = ball.pos - fix_point.pos
    
    vx_b.plot(pos = (t,ball.v.x))
    vy_b.plot(pos = (t,ball.v.y)) # plot the y velocity using the other g curve
    
    t = t + dt              # update time
    
    if ball.old_v.y > 0 and ball.v.y < 0:
        print('period:', ball.T, 2 * pi * sqrt(ball.mass/k_spring))
        ball.T = 0
        
    ball.old_v = ball.v
    ball.T = ball.T + dt
        
        
    # 1) no drag - screenshot animation and graph and period information
    # 2) quadratic drag - screenshot animation and graph
    # 3) linear drag - screenshot animation and graph
    # 4) lab report - after including the code, include the 3 cases of no drag, quadratic drag, and linear drag
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
