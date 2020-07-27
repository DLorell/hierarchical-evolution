# Hierarchical Evolution
An evolutionary algorithm which can automatically tune the amount of slack vs competition.

The concept of competition is well understood as the degree to which the superior features of a system cause it to triumph over or proliferate more than other systems. The inverse of this concept is less talked about, "slack." That is, the degree to which inferior features are able to persist. Intuitively, it would seem that in any optimization process, a fully competitive environment would produce systems with the most desirable features. However, with such strong competitive forces at play, it is easy to get hopelessly stuck in local (sub)optima. With the ability to increase/decrease the amount of slack in the environment, it may be possible to more optimally explore it. The investigation of that idea is the aim of this project.


## Stage 1: A Toy Model

Before jumping into anything too complicated, it would behoove us to establish the efficacy of this idea on a toy model. I will hand-design a simple hill-climbing task as a sanity check. 

###  Environment:
* 500x500 grid where each tile is associated with a fitness level. The fitness of each tile is proportional to it's "height." The topology of the environent is hilly in nature with hills of varying  height (and so of varying fitness.) The implicit goal is to find the top of the highest hill. 
* Agents spawn at the center of the map. The highest hills are near the edges, but a number of smaller hills are situated between.
* An epoch is defined as 1000 generations, after which the simulation ends.
     
###  Agents:
* The "agents" are really just points on the environment. 
* An agent has a lifespan of one iteration. 
* The "genetic" info of the agents are simply their positions. At each iteration, a new agent attempts to spawn on every tile adjacent to some living agents from the previous round. This movement amounts to reproduction with mutations. 
* The order in which the agents are given a chance to reproduce or not is random each round. 
* Each agent has a probability P(i) of reproducing. P is calculated by first applying a softmax over agent's heights to get the raw relative probability distribution S. P(i) is then calculated as P(i) = ((1-K)S(i) + K*(1/N) where N is the number of agents being considered and K linearly interpolates between the softmax distribution and the uniform distribution.
* K then represents the slack. Low K means high competition and high K means high slack (i.e. reproduction is totally random).
    
With any luck, the average fitness of the population and the maximum fitness within the population will vary with the level of slack.

## Installation
## Create Conda Env
    conda create -q -n test-environment --file hill-climber/requirements.txt
    conda activate test-environment
## Install Additional Dependencies
    pip install git+https://github.com/okken/pytest-check
