# Computing Pi with Bouncing Cubes
This repo contains my IB Mathematics exteneded essay and software used to generate the necessary visualizations. The essay can be found [here](https://github.com/liam-ilan/extended-essay/blob/master/computing-pi-with-bouncing-cubes.pdf).

## The Paper
This paper is my International Baccalaureate Extended Essay in Mathematics, written for the May 2023 session. It can be found in this repo in `computing-pi-with-bouncing-cubes.pdf`. (Link [here](https://github.com/liam-ilan/extended-essay/blob/master/computing-pi-with-bouncing-cubes.pdf)).

## Development
One major task for this paper was writing software to generate the nescacary graphs and visuals.

To generate the graphs found in the paper (located under `./graphs`), run

```python
python main.py
```

`graphers.py` provides 3 methods, used by `main.py` for generating graphs:

1. `graphDisplacement(path, scale, opts)` - generates `public/displacement-100-1.png` and `public/displacement-100-1-scale.png`
  * path - path to save to
  * pair - boolean, render only pair of collisions, or whole thing
  * opts - options for sim
2. `graphVelocity(path, pair, opts)` - generates `public/velocity-100-1.png` and `public/velocity-100-1-pair.png`
  * path - path to save to
  * scale - boolean, scale by root m1 and m2 or don't
  * opts - options for sim
3. `graphMirrors(path, opts)` - generates `public/mirrors-100-1.png`
  * path - path to save to
  * opts - options for sim

The `opts` argument in the 3 methods provided by `graphers.py` is a dictionary, structured as follows:
```python
opts = { 
  'timeStep': simulation time step, 
  'postSteps': number of time steps to simulate after the last collision, 
  'mA': mass of cube A,
  'mB': mass of cube B, 
  'vA': initial velocity of cube A, 
  'vB': initial velocity of cube B, 
  'dA': initial displacement of cube A, 
  'dB': intial displacement of cube B, 
  'wA': width of cube A, 
  'wB': width fo cube B
}
```

An animated simulation of the bouncing cubes is located in `/interactive-simulation`. It is also running at https://bouncing-cubes.snowboardsheep.repl.co/.

You can find all graphs used in the paper under `/graphs`. 

## Credit
All software in this repo was written by Liam Ilan (https://www.liamilan.com/).