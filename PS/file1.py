import numpy as np
import matplotlib.pyplot as plt

# Choose number of chords to draw in the simulation:
num_chords = 10000
count=0

def draw_circle_and_triangle(ax):
    circle = plt.Circle((0, 0), 1, color='w', linewidth=2, fill=False)
    ax.add_patch(circle)  # Draw circle
    ax.plot([np.cos(np.pi / 2), np.cos(7 * np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(np.pi / 2), np.cos(- np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(- np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(- np.pi / 6), np.cos(7 * np.pi / 6)],
            [np.sin(- np.pi / 6), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    plt.show()


def bertrand_simulation(method_number):
    # Simulation initialisation parameters
    count = 0

    # Figure initialisation
    plt.style.use('dark_background')  # use dark background
    ax = plt.gca()
    ax.cla()  # clear things for fresh plot
    ax.set_aspect('equal', 'box')
    ax.set_xlim((-1, 1))  # Set x axis limits
    ax.set_ylim((-1, 1))  # Set y axis limits

    # Repeat the following simulation num_chords times:
    
        # Step 1: Construct chord coordinates according to chosen method
    for k in range(0, num_chords):
      x, y = bertrand_methods[method_number]()
      lenChord=np.sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)
      if(lenChord>np.sqrt(3)):
         count+=1
      print(count/num_chords)
      if(k<1000):
         if(lenChord>np.sqrt(3)):
           plt.plot(x, y, color='red', alpha=0.1)
         else:
           plt.plot(x, y, color='cyan', alpha=0.1)
        # Step 2: Compute length of chord and compare it with triangle side
        # Display probability after each simulation
        # Plot the first 1000 chords
        # Hint: Use different colors for chords longer than the triangle side
        # and make the chords more transparent by setting alpha = 0.1

    draw_circle_and_triangle(plt.gca())
    plt.show()
    
#An illustration of Bertrand's Paradox
def bertrand1():
    argx=np.random.rand()
    argy=np.random.rand()
    argx=argx*2*(np.pi)
    argy=argy*2*(np.pi)
    x=[np.cos(argx), np.cos(argy)]
    y=[np.sin(argx), np.sin(argy)]
    return x, y
def bertrand2():
   radius=np.random.rand()
   theta=np.random.rand()
   theta=theta*2*(np.pi)
   mid=[radius*np.cos(theta), radius*np.sin(theta)]
   bisectorAngle=np.arccos(radius)
   x=[np.cos(theta+bisectorAngle), np.cos(theta-bisectorAngle)]
   y=[np.sin(theta+bisectorAngle), np.sin(theta-bisectorAngle)]
   return x, y
def bertrand3():
   x=np.random.rand()
   y=np.random.rand()
   x=x*(np.sqrt(1-y*y))
   radius=np.sqrt(x*x+y*y)
   theta=np.atan2(x, y)
   bisectorAngle=np.arccos(radius)
   x=[np.cos(theta+bisectorAngle), np.cos(theta-bisectorAngle)]
   y=[np.sin(theta+bisectorAngle), np.sin(theta-bisectorAngle)]
   return x, y
bertrand_methods = {1: bertrand1, 2: bertrand2, 3: bertrand3}

# method_choice = input('Choose method to simulate: ')
bertrand_simulation(2)
