import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Arc
from simulators import getVelocityData
from simulators import getDisplacementData

# graphs configuration space of velocities
# path - path to save to
# pair - boolean, render only pair of collisions, or whole thing
# opts - options for sim
def graphVelocity(path, pair, opts):
  mA = opts['mA']
  mB = opts['mB']
  [aData, bData] = getVelocityData(opts)

  # graph
  print('Graphing ' + path + '...')
    
  # create figure
  plt.figure(figsize=(7, 7), dpi=300)

  # get radius of energy conservation circle
  radius = -aData[0]

  # set axis to be with 5 unit padding
  plt.axis([-radius - 5, radius + 5, -radius - 5, radius + 5])

  # modify data if single set of lines
  if pair:
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
    
  if pair:
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
    plt.gca().add_patch(
      Arc(
        (aData[1], bData[1]),
        radius / 2,
        radius / 2,
        0,
        fullAngle1 / math.pi * 180,
        fullAngle2 / math.pi * 180,
        color='tab:pink',
        linewidth=1,
        fill=False
      )
    )
    
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
  plt.xlabel(r'$v_{1}\sqrt{m_{1}}$')
  plt.ylabel(r'$v_{2}\sqrt{m_{2}}$')
  plt.title('Configuration Space of Velocities for Cubes with Mass Ratio ' + str(mA) + ':' + str(mB))

  # save
  print('Saving ' + path + '...')
  plt.savefig(path)
  
  print('Finished ' + path)

# graphs configuration space of displacements
# path - path to save to
# pair - boolean, scale by root m1 and m2 or don't
# opts - options for sim
def graphDisplacement(path, scale, opts):
  # simulate
  [aData, bData] = getDisplacementData(opts)

  # setup scale factors
  aScaleFactor = opts['mA'] ** 0.5 if scale else 1
  bScaleFactor = opts['mB'] ** 0.5 if scale else 1

  aData = [x * aScaleFactor for x in aData]
  bData = [x * bScaleFactor for x in bData]

  # graph
  print('Graphing ' + path + '...')
  
  # create figure
  plt.figure(figsize=(7 * aScaleFactor, 7 * bScaleFactor), dpi=300)
  plt.margins(0)

  # plot labels and title
  plt.xlabel(r'$d_{1}\sqrt{m_{1}}$' if scale else r'$d_{1}$')
  plt.ylabel(r'$d_{2}\sqrt{m_{2}}$' if scale else r'$d_{2}$')
  plt.title('Configuration Space of Displacements for Cubes with Mass Ratio ' + str(opts['mA']) + ':' + str(opts['mB']))

  # plot data
  plt.plot(aData, bData, color='tab:blue', lw=2)

  # plot collision lines
  plt.plot(
    [0, max(aData)], 
    [opts['wB'] * bScaleFactor, opts['wB'] * bScaleFactor], 
    color='tab:orange'
  )
  plt.plot(
    [0, max(aData)], 
    [0, max(aData) / aScaleFactor * bScaleFactor], 
    color='tab:green'
  )

  # create legend
  # create legend symbols
  legend_symbols = [
    Line2D([0], [0], color='tab:blue', lw=1),
    Line2D([0], [0], color='tab:green', lw=1),
    Line2D([0], [0], color='tab:orange', lw=1)
  ]

  # titles for legend
  legend_titles = [
    'State',
    r'$d_{1} = d_{2}$',
    r'$d_{2} = $Cube B Width'
  ]

  # plot legend
  plt.legend(legend_symbols, legend_titles, loc="upper left")

  # download figure
  print('Saving ' + path + '...')
  plt.savefig(path)

  print('Finished ' + path)

# graphs configuration space of displacements
# path - path to save to
# opts - options for sim
def graphMirrors(path, opts):

  # simulate
  [aData, bData] = getDisplacementData(opts)

  # setup scale factors
  aScaleFactor = opts['mA'] ** 0.5
  bScaleFactor = opts['mB'] ** 0.5

  aData = [x * aScaleFactor for x in aData]
  bData = [x * bScaleFactor for x in bData]

  # radius of green lines
  r = (max(aData) ** 2 + max(bData) ** 2) ** 0.5

  # graph
  print('Graphing ' + path + '...')

  # create figure
  plt.figure(
    figsize = (
      max([*aData, r]) / 200, 
      max([*bData, r / 2]) / 200
    ),
    dpi=300
  )

  # drop margins
  plt.margins(0)

  # plot labels and title
  plt.xlabel(r'$d_{1}\sqrt{m_{1}}$')
  plt.ylabel(r'$d_{2}\sqrt{m_{2}}$')
  plt.title('Configuration Space of Displacements for Cubes with Mass Ratio ' + str(opts['mA']) + ':' + str(opts['mB']))

  # find slope of mirror
  mirrorSlope = (max(aData) / aScaleFactor * bScaleFactor) / max(aData)

  # shift data down to corner
  yDiff = opts['wB'] * bScaleFactor
  xDiff = (1 / mirrorSlope) * yDiff

  bData = [y - yDiff for y in bData]
  aData = [x - xDiff for x in aData]

  angleStep = math.atan(mirrorSlope)

  # plot "light"
  plt.plot(
    [-r, r],
    [bData[0], bData[0]],
    color='tab:grey',
    lw = 3
  )

  # plot data
  plt.plot(aData, bData, color='tab:blue', lw=2)

  # plot mirrors
  for n in range(int(math.ceil(math.pi / angleStep))):
    angle = n * angleStep
    slope = math.tan(angle)

    # plot collision lines (mirror lines):
    plt.plot(
      [0, math.copysign(1, slope) * ((r ** 2) / (slope ** 2 + 1)) ** 0.5], 
      [0, math.copysign(1, slope) * slope * ((r ** 2) / (slope ** 2 + 1)) ** 0.5], 
      color='tab:green'
    )

    # collision points
    if math.tan(angle) != 0:
      plt.plot(bData[0] / math.tan(angle), bData[0], 'o', color='tab:pink')

  # create legend
  # create legend symbols
  legend_symbols = [
    Line2D([0], [0], color='tab:blue', lw=1),
    Line2D([0], [0], color='tab:green', lw=1),
    Line2D([0], [0], color='tab:grey', lw=1),
    Line2D([], [], marker='o', color='tab:pink', lw=1),
  ]

  # titles for legend
  legend_titles = [
    'State',
    '"Mirrors" (Collision Lines)',
    '"Ray of Light" (State Reflected Across Mirrors)',
    'Collision'
  ]

  # plot legend
  plt.legend(legend_symbols, legend_titles, loc="upper left")

  # download figure
  print('Saving ' + path + '...')
  plt.savefig(path)

  print('Finished ' + path)

