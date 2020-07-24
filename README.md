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
* The "agents" are really just points on the environment. At each iteration, a new agent is spawned on every tile adjacent to a living agent. If this results in more than K agents in the environment, then the (N - K) least fit agents despawn. (Where N is the # of agents.)  
* In order to avoid large populations suffering from lack of space, agents may spawn on top of other living agents.  
* K then represents the slack. Low K means high competition and high K means high slack.
    
With any luck, the average fitness of the population and the maximum fitness within the population will vary with the level of slack
      
