import sys
import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from simulate import simulate
from matplotlib.patches import Arc

# simulate
mA = int(sys.argv[1])
mB = int(sys.argv[2])
[aData, bData] = simulate(mA, mB)

# graph
print('Graphing...')
  
# create figure
plt.figure(figsize=(7, 7))

# get radius of energy conservation circle
radius = -aData[0]

# set axis to be with 5 unit padding
plt.axis([-radius - 5, radius + 5, -radius - 5, radius + 5])

# modify data if single set of lines
if sys.argv[3] == '-p' or sys.argv[3] == '-pair':
  midPoint = int(len(aData) / 2)
  aData = aData[midPoint - 1:midPoint + 2]
  bData = bData[midPoint - 1:midPoint + 2]

# plot energy conservation (1/2 m1 v1^2 + 1/2 m2 v2^2 = constant)
energy_conservation_circle = plt.Circle(
  (0, 0), 
  radius, 
  color='tab:orange', 
  linewidth=1, 
  fill=False
)
plt.gca().add_patch(energy_conservation_circle)

# plot collisions
plt.plot(aData, bData, color='tab:blue', lw=2)

# mark angles, and lines connecting to center, if using single set
def getFixedAngle(x, y, r):
  return ((x / abs(x)) - 1) / 2 * math.pi - (x / abs(x)) * math.asin(y / r) + math.pi / 2

def getDistance(x1, y1, x2, y2):
  return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def getTextPosition(angle1, angle2, l1, l2, oX, oY):
  y1 = math.sin(angle1) * l1
  y2 = math.sin(angle2) * l2
  x1 = math.cos(angle1) * l1
  x2 = math.cos(angle2) * l2

  return [(x1 + x2) / 2 + oX, (y1 + y2) / 2 + oY]
  
if sys.argv[3] == '-p' or sys.argv[3] == '-pair':
  # plot collisions
  plt.plot([aData[0], 0, aData[2]], [bData[0], 0, bData[2]], color='tab:gray', lw=2)

  # get angles
  midAngle1 = getFixedAngle(bData[0], aData[0], radius)
  midAngle2 = getFixedAngle(bData[2], aData[2], radius)

  fullAngle1 = getFixedAngle(bData[0] - bData[1], aData[0] - aData[1], getDistance(aData[0], bData[0], aData[1], bData[1]))
  fullAngle2 = getFixedAngle(bData[2] - bData[1], aData[2] - aData[1], getDistance(aData[2], bData[2], aData[1], bData[1]))

  if midAngle1 > midAngle2:
    midAngle1, midAngle2 = midAngle2, midAngle1

  if fullAngle1 > fullAngle2:
    fullAngle1, fullAngle2 = fullAngle2, fullAngle1

  # plot center angle
  plt.gca().add_patch(
    Arc(
      (0, 0), 
      radius / 2, 
      radius / 2,
      0,
      midAngle1 / math.pi * 180, 
      midAngle2 / math.pi * 180,  
      color='tab:pink', 
      linewidth=1, 
      fill=False
    )
  )

  # plot angle between two lines
  plt.gca().add_patch(Arc(
    (aData[1], bData[1]), 
    radius / 2, 
    radius / 2,
    0,
    fullAngle1 / math.pi * 180, 
    fullAngle2 / math.pi * 180,  
    color='tab:pink', 
    linewidth=1, 
    fill=False
  ))
  
  [centerTextX, centerTextY] = getTextPosition(midAngle1, midAngle2, radius / 2.5, radius / 2.5, 0, 0)
  [singleTextX, singleTextY] = getTextPosition(fullAngle1, fullAngle2, radius / 2.5, radius / 2.5, aData[1], bData[1])

  plt.gca().text(centerTextX, centerTextY, r'$2\theta$', {'color': 'tab:pink'},  horizontalalignment='center', verticalalignment='center')
  plt.gca().text(singleTextX, singleTextY, r'$\theta$', {'color': 'tab:pink'},  horizontalalignment='center', verticalalignment='center')

# plot stop condition
plt.fill_between(
  range(math.ceil(radius) + 1), # loop through points on x axis
  [0 for i in range(math.ceil(radius) + 1)], # from 0
  [i / (mA ** 0.5) * (mB ** 0.5) for i in range(math.ceil(radius) + 1)], # compute stop condition
  alpha=0.5,
  color='tab:green',
)
 
# create legend symbols
legend_symbols = [
  Line2D([0], [0], color='tab:blue', lw=1),
  Line2D([0], [0], color='tab:green', lw=1),
  Line2D([0], [0], color='tab:orange', lw=1)
]

# titles for legend
legend_titles = [
  'Collisions',
  r'$v_{1} \geq v_{2} \geq 0$',
  'Conservation of Energy'
]

# plot legend
plt.legend(legend_symbols, legend_titles, loc="upper left")

# add labels and title
plt.xlabel(r'$\sqrt{m_{1}} \cdot v_{1}$')
plt.ylabel(r'$\sqrt{m_{2}} \cdot v_{2}$')
plt.title('Configuration Space of Velocities for Cubes with Mass Ratio ' + str(mA) + ':' + str(mB))

# save
print('Saving...')
plt.savefig(sys.argv[4])
  
print('Finished')



