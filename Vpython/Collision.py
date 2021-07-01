GlowScript 3.1 VPython
from vpython import *

scene = canvas(background = color.white)

ground = box(pos = vec(0, -0.05, 0), size = vec(7, 0.02, 0.4), color = color.green)

ball = sphere(pos = vec(-2.5, 0, 0), mass = 0.5, v = vec(1, 0, 0), radius = 0.05, color = color.red, make_trail = True, trail_type = 'points')


ball.p = ball.mass * ball.v

stone = sphere(pos = vec(3, 0, 0), mass = 5, v = vec(-0.5, 0, 0), radius = 0.05, color = color.blue, make_trail = True, trail_type = 'points')


stone.p = stone.mass * stone.v

l_0 = 0.5
k = 50

vx = graph(title = 'Velocity', xtitle = 't', ytitle = 'v_x (t)')
v_b_x = gcurve(graph = vx, color = color.red, width = 1)
v_s_x = gcurve(graph = vx, color = color.blue, width = 1)

px = graph(title = 'Momentum', xtitle = 't', ytitle = 'v_x (t)')
p_b_x = gcurve(graph = px, color = color.red, width = 1)
p_s_x = gcurve(graph = px, color = color.blue, width = 1)
p_total_x = gcurve(graph=px, color=color.purple, width = 1 )


en_g = graph(title = 'Energy', xtitle = 't', ytitle = 'E(t)')
K_1_g = gcurve(graph = en_g, color = color.red, width = 1)
K_2_g = gcurve(graph = en_g, color = color.blue, width = 1)
P_g = gcurve(graph = en_g, color = color.green, width = 1)
E_tot_g = gcurve(graph = en_g, color = color.purple, width = 1)

myrate = 1000

t = 0
dt = 0.001
r = stone.pos - ball.pos

p_tot = ball.p + stone.p # calculate total momentum
k_ball = 0.5 * ball.mass * ball.v.mag2
k_stone = 0.5 * stone.mass * stone.v.mag2
pe_total = 0
E_tot =  k_ball + k_stone + pe_total # calculate total energy
print('P_before: ',p_tot, 'E_before :', E_tot)

while abs(ball.pos.x) < 3.2:
    rate(myrate)
    
    F_b = vec(0, 0, 0)
    F_s = vec(0, 0, 0)
    pe_total = 0
    r = stone.pos - ball.pos
    if r.mag < l_0:
        F_b = -k * (l_0 - r.mag) * vec(1,0,0) # Calculate spring force
        F_s = - F_b # Calculate spring force
        pe_total = 0.5 * k * (l_0 - r.mag)**2 # Calculate spring force
        
    ball.p = ball.p + F_b * dt # update momentum
    ball.v = ball.p / ball.mass # calculate velocity
    ball.pos += ball.v * dt # update position
    
    stone.p = stone.p + F_s * dt # update momentum
    stone.v = stone.p / stone.mass # calculate velocity
    stone.pos += stone.v * dt    # update momentum
    
    v_b_x.plot(pos = (t, ball.v.x))
    v_s_x.plot(pos = (t, stone.v.x)) # plot the velocities of ball and stone
    
    p_b_x.plot(pos = (t, ball.p.x)) # plot the momenta of the ball and the stone
    p_s_x.plot(pos = (t, stone.p.x))
    p_total_x.plot(pos = (t, stone.p.x + ball.p.x)) # plot the total momentum
    
    E1 = 0.5 * ball.mass * ball.v.mag2 # calculate the ball energy
    E2 = 0.5 * stone.mass * stone.v.mag2
    
    K_1_g.plot(pos = (t, E1))
    K_2_g.plot(pos = (t, E2))
    
    P_g.plot(pos = (t, pe_total))
    E_tot_g.plot(pos = (t, E1 + E2 + pe_total))
    
    # calculate the stone energy
    
    t += dt

p_tot = stone.p + ball.p
E_tot = k_ball + k_stone + pe_total

print('P_after: ',p_tot, 'E_after :', E_tot)
    
