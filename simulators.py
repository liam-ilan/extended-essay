class Cube:
  def __init__(self, m, d, v, w, dLimit):
    # initial values
    self.m = m
    self.v = v
    self.d = d
    self.w = w
    self.dLimit = dLimit
    self.data = []

  def getVelocityPostCollision(self, otherCube):
    return (self.m - otherCube.m) / (self.m + otherCube.m) * self.v + (2 * otherCube.m) / (otherCube.m + self.m) * otherCube.v

class World:
  def __init__(self, opts):
    # create cubes
    self.a = Cube(opts['mA'], opts['dA'], opts['vA'], opts['wA'], opts['wB'])
    self.b = Cube(opts['mB'], opts['dB'], opts['vB'], opts['wB'], 0)

    # init data
    self.a.data.append(self.a.d)
    self.b.data.append(self.b.d + self.b.w)

    # count collisions
    self.count = 0
    self.lastCollision = None
    
    # loop sim
    while not (self.a.v >= self.b.v >= 0):
      self.update(opts['timeStep'])

    # run sim after last collision
    for i in range(opts['postSteps']):
      self.update(opts['timeStep'])

    self.a.data.append(self.a.d)
    self.b.data.append(self.b.d + self.b.w)

  def update(self, timeStep):
    # on collision between cubes
    if (self.a.d <= self.b.d + self.b.w and self.lastCollision != 'cube'):

      # find and update velocities
      newVA = self.a.getVelocityPostCollision(self.b)
      newVB = self.b.getVelocityPostCollision(self.a)

      self.a.v = newVA
      self.b.v = newVB

      # count
      self.count += 1

      # flag collision for no duplicates
      self.lastCollision = 'cube'

      # add data
      self.a.data.append(self.a.d)
      self.b.data.append(self.b.d + self.b.w)
    
    # on collision with wall
    if self.b.d <= 0 and self.lastCollision != 'wall':
      # on collision with wall, reflect block
      self.b.v = -self.b.v
      
      # count
      self.count += 1
      
      # flag collision for no duplicates
      self.lastCollision = 'wall'
      
      # add data
      self.a.data.append(self.a.d)
      self.b.data.append(self.b.d + self.b.w)

    # update displacements
    self.a.d += timeStep * self.a.v
    self.b.d += timeStep * self.b.v

def getDisplacementData(opts):
  world = World(opts)
  return [world.a.data, world.b.data]

def getVelocityData(opts):
  a = {
    'm': opts['mA'],
    'v': opts['vA']
  }

  b = {
    'm': opts['mB'],
    'v': opts['vB']
  }

  # setup data
  aData, bData = [], []

  # add initial data
  aData.append(a['v'] * a['m'] ** 0.5)
  bData.append(b['v'] * b['m'] ** 0.5)

  print('Simulating velocities for mass ratio ' + str(a['m']) + ':' + str(b['m']) + '...')

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
