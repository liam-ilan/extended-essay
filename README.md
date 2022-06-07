# Computing Pi with Bouncing Cubes
This git contains my exteneded essay and software used to generate the necessary visualizations.

## Plot Graphs
To generate graphs, edit the configuration file (`opts.py`), then run

```
python main.py
```

`opts.py` contains a dictionary (`opts`) which gets used to pass arguments to the graphing software. This dictionary follows the following structure:

```
{
  'paths': {
    '<path name>': {
      'type': '<velocity or displacement>',
      'variation': '<full or pair>',                                    if type is velocity
      'timeStep': <length of simulation timestep>,                      if type is displacement
      'postSteps': <number of steps to simulate post last collision>    if type is displacement
    },
    ...
  }
  'data': {
    'mA': [mass of A],
    'mB': [mass of B],
    'vA': [velocity of A],
    'vB': [velocity of B],
    'dA': [displacement of A],
    'dB': [displacement of B],
    'wA': [width of A],
    'wB': [width of B]
  }
}
```

An animated simulation of the cube bouncing process is located in `/interactive-simulation`. It is also running at https://bouncing-cubes.snowboardsheep.repl.co/.

You can find all graphs used in the paper in `/graphs`. 

## Credit
All software in this repo was written by Liam Ilan (https://www.liamilan.com/).