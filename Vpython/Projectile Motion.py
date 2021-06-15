GlowScript 3.1 VPython
from vpython import *

scene = canvas(background = color.white)

ground = box(pos = vec(0, -0.02, 0), size = vec(3, 0.02, 0.4), color = color.green)

# Initial variables - Physics

v0 = 4.0
g = 9.81
h = 0.5
x0 = -1
alpha = 35 * pi/180     # works in radiants so converte the number in degrees to radiants. 

ball = sphere(pos = vec(x0, h, 0), mass = 0.5, angle = alpha, radius = 0.1, color = color.red, make_trail = True)


ball.v = v0 * vec(cos(ball.angle), sin(ball.angle), 0) # Initial Ball Velocity
ball.p = ball.mass * ball.v                            # Initial Ball Momentum

stone = sphere(pos = vec(x0, h, 0), mass = 0.5, angle = alpha, radius = 0.1, color = color.purple, make_trail = True)


stone2 = sphere(pos = vec(x0, h, 0), mass = 0.5, angle = alpha, radius = 0.1, color = color.cyan, make_trail = True)


stone.v = v0 * vec(cos(stone.angle), sin(stone.angle), 0) # Initial Stone Velocity
stone.p = stone.mass * stone.v                            # Initial Stone Momentum

v_graph = graph(title = 'Velocity', xtitle = 't', ytitle = 'v')

v_b_x = gcurve(graph = v_graph, color = color.red)  # Create gcurve with color red
v_b_y = gcurve(graph = v_graph, color = color.green)  # Create gcurve with color green

v_s_x = gcurve(graph = v_graph, color = color.blue)  # Create gcurve with color blue
v_s_y = gcurve(graph = v_graph, color = color.cyan)  # Create gcurve with color cyan

myrate = 200

t = 0
dt = 0.001

while stone.pos.y >0 :
    
    rate(myrate)  # Just for the animation(the rate of the animation refreshes)
    
    F_ball = vec(0, 0, 0)
    
    ball.p += F_ball * dt
    ball.v = ball.p/ball.mass   # Find the velocity
    ball.pos += ball.v * dt
    
    F_stone = stone.mass * vec(0, -g, 0)
    
    stone.p += F_stone * dt
    stone.v = stone.p/stone.mass
    stone.pos += stone.v * dt # Find the position
    
    # Can also calculate the position using kinematic equations - textbook - Google
    stone2.pos = vec(x0 + v0 * cos(alpha) * t, h + v0 * sin(alpha) * t - g/2 * t ** 2, 0)
    
    v_b_x.plot(pos = (t, ball.v.x))
    v_b_y.plot(pos = (t, ball.v.y))
    
    v_s_x.plot(pos = (t, stone.v.x))
    v_s_y.plot(pos = (t, stone.v.y))
    
    t += dt

d = stone.pos.x - x0   # Called the range
print('distance: ', d)








