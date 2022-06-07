from velocity import graphVelocity
from displacement import graphDisplacement
from opts import opts

def generateGraphs(opts):
  # convert opts from user to opts for graphers
  for path in opts['paths'].keys():

    # opts to pass to graphers
    newOpts = {'path': path}

    # opts passed sepcifically for given type
    specificOpts = opts['paths'][path]

    # handle data for velocity graphs
    if specificOpts['type'] == 'velocity':
      newOpts['variation'] = specificOpts['variation']

      # update options and graph
      newOpts = {**newOpts, **opts['data']}
      graphVelocity(newOpts)

    # handle data for displacement graphs
    elif specificOpts['type'] == 'displacement':
      newOpts['timeStep'] = specificOpts['timeStep']
      newOpts['postSteps'] = specificOpts['postSteps']

      # update options and graph
      newOpts = {**newOpts, **opts['data']}
      graphDisplacement(newOpts)

if __name__ == '__main__':
  generateGraphs(opts)