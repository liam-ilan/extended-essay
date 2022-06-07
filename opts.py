opts = {
  'paths': {
    './graphs/velocity-100-1-pair.png': {
      'type': 'velocity',
      'variation': 'pair'
    },
    './graphs/velocity-100-1-full.png': {
      'type': 'velocity',
      'variation': 'full'
    },
    './graphs/displacement-100-1.png': {
      'type': 'displacement',
      'timeStep': 1 / 1000,
      'postSteps': 10000
    }
  },
  'data': {
    'mA': 100,
    'mB': 1,
    'vA': -10,
    'vB': 0,
    'dA': 200,
    'dB': 100,
    'wA': 20,
    'wB': 20
  }
}