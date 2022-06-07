class Cube {
  constructor(element, m, d, v, w, dLimit, arrow) {
    // initial values
    this.element = element
    this.arrow = arrow
    this.m = m
    this.v = v
    this.d = d
    this.w = w
    this.dLimit = dLimit
    
    this.render()
  }
  
  render() {
    // update size and location of cube
    this.element.style.left = (this.d > this.dLimit ? this.d : this.dLimit) + 'px'
    this.element.style.width = this.w + 'px'
    this.element.style.height = this.w + 'px'

    if (this.v > 0) {
      this.arrow.className = 'arrow right-arrow'
    } else if (this.v < 0) {
      this.arrow.className = 'arrow left-arrow'
    } else {
      this.arrow.className = 'arrow'
    }
  }

  getVelocityPostCollision(otherCube) {
    return (this.m - otherCube.m) / (this.m + otherCube.m) * this.v + 
      (2 * otherCube.m) / (otherCube.m + this.m) * otherCube.v
  }
}
class World {
  constructor(opts) {
    // create cubes
    this.a = new Cube(document.getElementById('a'), opts.mA, opts.dA, opts.vA, opts.wA, opts.wB, document.getElementById('a-arrow'))
    this.b = new Cube(document.getElementById('b'), opts.mB, opts.dB, opts.vB, opts.wB, 0, document.getElementById('b-arrow'))

    // get counter element
    this.countElement = document.getElementById('count')

    // count collisions
    this.count = 0
    this.digits = opts.digits
    this.lastCollision = null
    
    // loop (make sure to bind 'this' outside interval to 'this' inside interval, as context for 'this' is window in interval)
    // ^ i hope 'this' make sense ;)
    setInterval(this.update.bind(this), opts.renderTimeStep * 1000, opts.timeStep, opts.renderTimeStep)
  }

  update(timeStep, renderTimeStep) {
    // run multiple simulation itterations per loop
    // calculate number of itterations based on render and simulation intervals
    for (let i = 0; i < Math.ceil(renderTimeStep / timeStep); i += 1) {
      // on collision between cubes
      if (this.a.d <= this.b.d + this.b.w && this.lastCollision !== 'cube') {
  
        // find and update velocities
        let newVA = this.a.getVelocityPostCollision(this.b)
        let newVB = this.b.getVelocityPostCollision(this.a)
  
        this.a.v = newVA
        this.b.v = newVB
  
        // count
        this.count += 1
  
        // flag collision for no duplicates
        this.lastCollision = 'cube'
      }
      
      // on collision with wall
      if (this.b.d <= 0 && this.lastCollision !== 'wall') {
        // on collision with wall, reflect block
        this.b.v = -this.b.v
        
        // count
        this.count += 1
        
        // flag collision for no duplicates
        this.lastCollision = 'wall'
      }
  
      // update displacements
      this.a.d += timeStep * this.a.v
      this.b.d += timeStep * this.b.v
  
      // render
      this.a.render(timeStep)
      this.b.render(timeStep)
  
      // update counter
      this.countElement.innerText = ('' + this.count).padStart(this.digits, 0)
    }
  }
}

// digits (to be converted to mass)
digits = parseInt(location.search.substring(1)) || 5

// options
const opts = {
  digits: digits,
  mA: 1 * (100 ** (digits - 1)),
  mB : 1,
  vA: -((digits - 1) * 50) - 100, // initial velocity start at 100, for ux increase for every digit 
  vB: 0,
  dA: 200,
  dB: 100, 
  wA: 20 + 10 * (digits - 1),
  wB: 20,
  timeStep: 1/1000000,
  renderTimeStep: 1/1000
}

// create world
const world = new World(opts)
