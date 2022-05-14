# Computing Pi with Bouncing Cubes
This git contains my exteneded essay and software used to generate the necessary visualizations.

## Plot Graphs

To generate a graph of the configuration space of velocities given two masses:
```
python3 velocity-plotter/main.py [m1] [m2] [-p or -pair for single pair of collisions, -f for full] [filepath]
```

eg.
```
python3 velocity-plotter/main.py 16 1 -p graphs/16-1-pair.png
```

An animated simulation of the cube bouncing process is located in `/simulation`. It is also running at https://bouncing-cubes.snowboardsheep.repl.co/.

You can find all graphs used in the paper in `/graphs`. 

## Credit
All software in this repo was written by Liam Ilan (https://www.liamilan.com/).