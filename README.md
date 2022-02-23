# Contagious-Disease-Spread-Model
In this project the spread of a contagious disease is modeled through random movement of individuals (following certain probabilistic rules) and contagiousness factor of the disease. The model also takes into account whether the individual is masked or not and the effect that has on the spread.

There are P individuals, I0, ..., IP −1, each occupying a cell of an M × N grid (M (rows) ≤ 100; N(columns) ≤
100). Distance is measured in the conventional way: Euclidean distance. Individuals move from one cell to a
neighbouring cell with a certain probability. There are 8 possible neighbouring cells. The moves are
made in the order of the individuals (assuming that the individuals are numbered). For each individual,
their move depends on their previous move and the ‘probability’ and nothing else.

In one unit of time, after all the moves are performed, the rules of contamination apply: With a probability
which is inversely proportional to the distance between two individuals, if one of the individuals is infected, and
the other is not, they can transmit the disease to the other individual. This probability is effective only if the
distance between them is under a threshold value D. If an individual gets infected, they stays infected (i.e.
there is no cure) and starts to be infectious immediately in the next time frame.
The mutual infection probability of two individuals Ii
, Ij is as follows:
-minimum of (1, K/distance^2) if distance < D
-0 otherwise

Individuals may wear masks which reduce the infection probability by a factor of λ. This is explained in detail
below.
M, N, K, λ, D are system constants and are initialized in the test file, along with the initial state of the individuals.
The move probabilities are set according to the last move, depending on a grid of possible directions the individual can move in.

In case of attempting a move to a preoccupied position or outside of the arena, the attempting individual
will wait for one turn and hope the probability in the next turn will assign them to an empty neighbour
square that time. It is possible (with low probability) that an individual gets trapped and cannot move
at all, for more then one unit of time.

Individuals are set up as wearing a mask or not. This does not change over time in the simulation. If
an individual is wearing a mask, their probability to get infected or transmit their infection to another
individual is reduced by a dividing factor of λ. If the interaction is among two mask wearers, then the probability
is reduced by dividing it by a factor of λ^2 (1 < λ).

For each time step of the simulation, the function in model.py will be called by the test script
and will be expected to return the new coordinates for each individual (made into
a list).

draw.py visualizes the model.

Happy Coding :)
