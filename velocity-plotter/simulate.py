def simulate(m1, m2):
  a = {
    'm': m1,
    'v': -10
  }

  b = {
    'm': m2,
    'v': 0
  }

  # setup data
  aData, bData = [], []

  # add initial data
  aData.append(a['v'] * a['m'] ** 0.5)
  bData.append(b['v'] * b['m'] ** 0.5)

  print('Simulating for mass ratio ' + str(a['m']) + ':' + str(b['m']) + '...')

  # run simulation until a is moving away from b faster than b is moving towards a
  while not (a['v'] >= b['v'] >= 0):
    
    # if heading towards wall, reflect velocity of b
    if b['v'] < 0:
      b['v'] = -b['v']
      
    # if collision between cubes, calculate velocities accordingly  
    else:
      a['v'], b['v'] = (a['m'] - b['m']) / (a['m'] + b['m']) * a['v'] + (2 * b['m']) / (b['m'] + a['m']) * b['v'], (b['m'] - a['m']) / (b['m'] + a['m']) * b['v'] + (2 * a['m']) / (a['m'] + b['m']) * a['v']

    # add data
    aData.append(a['v'] * a['m'] ** 0.5)
    bData.append(b['v'] * b['m'] ** 0.5)
  
  return [aData, bData]

