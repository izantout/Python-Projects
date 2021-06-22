GlowScript 3.1 VPython
from vpython import *

scene = canvas(background = color.white)

fix_point = sphere(pos = vec(0,6,0), radius = 0.5, color = color.red)

l_0 = 6                     # initial length
alpha = 90 * pi / 180       
l_0_spring = 1.5 * l_0
k_spring = 10
g = 10
mu = 0.01

ball = sphere(pos = fix_point.pos + vec(l_0*sin(alpha), -l_0*cos(alpha), 0), mass = 0.5, v = vec(0, 0, 0), radius = 0.1, color = color.blue, make_trail = True, trail_radius = 0.01)



spring = helix(pos = fix_point.pos, axis = ball.pos - fix_point.pos, radius = 0.2, color = color.orange)


ball.p = ball.mass * ball.v

vg = graph(title = 'Velocity', xtitle = 't', ytitle = 'v(t)')
vx_b = gcurve(graph = vg, color = color.cyan)
vy_b = gcurve(graph = vg, color = color.red)

work_g = graph(title = 'Work', xtitle = 't', ytitle = 'W(t)')
w_g = gdots(graph = work_g, color = color.cyan, size = 2)
e_g = gcurve(graph = work_g, color = color.green)
w_s = gdots(graph = work_g, color = color.magenta, size = 2)
e_s = gcurve(graph = work_g, color = color.blue)

l = ball.pos - fix_point.pos # total spring displacement (vector)
spring.s = l.mag - l_0_spring # difference between total spring length and the equilibrium spring length
spring_e_0 = 0.5 * k_spring * spring.s ** 2 # initialize spring potential energy
work_s = 0

grav_e_0 = ball.mass * g * ball.pos.y
work_g = 0

energy_g = graph(title = 'Energy', xtitle = 't', ytitle = 'E(t)')
kin_e_g = gcurve(graph = energy_g, color = color.red)
grav_e_g = gcurve(graph = energy_g, color = color.green)
spring_e_g = gcurve(graph = energy_g, color = color.purple)
total_e_g = gcurve(graph = energy_g, color = color.blue)

myrate = 1600

t = 0
dt = 0.002

while t < 10:
    rate(myrate)
    
    # fix_point.pos.y = l_0 + sin(7*t) don't need to include it in your report
    
    spring.pos = fix_point.pos
    
    spring.axis = ball.pos - fix_point.pos # calculate spring axis
    
    l = ball.pos - fix_point.pos # calculate total spring length
    
    spring.s = l.mag - l_0_spring # calculate the difference between total spring length and equilibrium spring length
    
    F_s = k_spring * spring.s * -l.hat
    F_g = ball.mass * vec(0, -g, 0)
    
    # F_d = -mu * ball.v.mag2 * ball.v.hat
    F_d = -mu * ball.v.mag * ball.v.hat
    
    F = F_g + F_s + F_d
    
    ball.p = ball.p + F * dt # update momentum
    ball.v = ball.p / ball.mass # update velocity
    ball.pos += ball.v * dt # update position
    
    work_g = work_g + dot(F_g, ball.v) * dt 
    work_s = work_s + dot(F_s, ball.v) * dt 
    
    spring.axis = ball.pos - fix_point.pos
    
    vx_b.plot(pos = (t,ball.v.x))
    vy_b.plot(pos = (t,ball.v.y)) # plot the x and y velocities as functions of time
    
    grav_e = ball.mass * g * ball.pos.y
    spring_e = 0.5 * k_spring * spring.s ** 2 # calculate spring energy
    kin_e = 0.5 * ball.mass * ball.v.mag2 # calculate kinetic energy 
    total_e = grav_e + kin_e + spring_e # calculate total energy 
    
    w_g.plot(pos = (t, -work_g))
    e_g.plot(pos = (t,grav_e - grav_e_0 ))# use e_g to plot final minus initial gravitational energy as a function of time
    
    w_s.plot(pos = (t, -work_s))
    e_g.plot(pos = (t,spring_e - spring_e_0 )) # use e_s to plot final minus initial spring energy as a function of time
    
    grav_e_g.plot(pos = (t, grav_e)) # plot grav_e vs time 
    spring_e_g.plot(pos = (t, spring_e)) # plot spring_e vs time
    kin_e_g.plot(pos = (t, kin_e)) # plot kin_e vs time
    total_e_g.plot(pos = (t, total_e)) # plot total_e vs time
    
    t = t + dt
