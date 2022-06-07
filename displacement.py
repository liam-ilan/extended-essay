import sys
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from simulators import getDisplacementData

def graphDisplacement(opts):
  # simulate
  [aData, bData] = getDisplacementData(opts)

  # graph
  print('Graphing ' + opts['path'] + '...')
  
  # create figure
  plt.figure(figsize=(7, 7))

  # plot labels and title
  plt.xlabel(r'$d_{1}$')
  plt.ylabel(r'$d_{2}$')
  plt.title('Configuration Space of Displacements for Cubes with Mass Ratio ' + str(opts['mA']) + ':' + str(opts['mB']))

  # plot data
  plt.plot(aData, bData, color='tab:blue', lw=2)

  # size of collision lines
  collisionLength = max(int(max(aData)), int(max(bData)))

  # plot collision lines
  plt.plot(range(collisionLength), [opts['wB'] for _ in range(collisionLength)], color='tab:orange')
  plt.plot(range(collisionLength), range(collisionLength), color='tab:green')

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
  print('Saving ' + opts['path'] + '...')
  plt.savefig(opts['path'])

  print('Finished ' + opts['path'])