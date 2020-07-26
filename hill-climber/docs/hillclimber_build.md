# Build Docs for the Hillclimber Project

### Specifications
Design Pattern: MVC

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


## Implemenation Details

### model.py
Contains the classes governing the evolutionary environment and the agents within it.

#### Agent(x, y)
Attributes:
    x   // int representing the row of the agent
    y   // int representing the col of the agent

#### Environment(heightmap=None, agents=None)
Attributes:
    heightmap       // numpy.array (height, width) representing the optimization landscape for these agents
    agents          // Agent[] 
    rel_fitness     // numpy.array (num_agents) softmax based fitness distribution
    k               // float interpolating between softmax (competitive) and uniform (slack) reproduction distributions

Public Methods:
    generate_new_heightmap(int: height, int: width)    // Generates a new heightmap and assigns it to heightmap attribute
    step()                                             // Updates the agent list to reflect one iteration of reproduction / death
Private Methods:
    _get_relative_dist()  -> numpy.array               // Calculate the softmax distribution over agent fitnesses
    _get_reproduction_dist(float: k) -> numpy.array    // Calculate the final reproduction distribution, interpolated by k between softmax and uniform
    _mutate(Agent: agent) -> Agent[]                   // Gets a list of Agents mutated from a given parent Agent

    
### view.py
Contains the classes which render a given enviroment. (Potentially add graphical user inputs later)

#### BoardView()
Attributes:

Public Methods:

Private Methods:



### controller.py
Contains the classes which allow the model and view to work in tandem.


## Roadmap
