from graphers import graphVelocity, graphDisplacement

opts = { 
  'timeStep': 0.001, 
  'postSteps': 10000, 
  'mA': 100, 
  'mB': 1, 
  'vA': -10, 
  'vB': 0, 
  'dA': 200, 
  'dB': 100, 
  'wA': 20, 
  'wB': 20
}

graphDisplacement('./graphs/displacement-100-1.png', False, opts)
graphDisplacement('./graphs/displacement-100-1-scale.png', True, opts)

graphVelocity('./graphs/velocity-100-1.png', False, opts)
graphVelocity('./graphs/velocity-100-1-pair.png', True, opts)