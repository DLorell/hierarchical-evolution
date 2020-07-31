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
    max_pop         // int indicating the upper limit of how many agents can be active in each step

Public Methods:
    generate_new_heightmap(int: height, int: width)    // Generates a new heightmap and assigns it to heightmap attribute
    step()                                             // Updates the agent list and rel_fitnesses to reflect one iteration of reproduction / death
Private Methods:
    _get_relative_dist()  -> numpy.array               // Calculate the softmax distribution over agent fitnesses
    _get_reproduction_dist(float: k) -> numpy.array    // Calculate the final reproduction distribution, interpolated by k between softmax and uniform
    _mutate(Agent: agent) -> Agent[]                   // Gets a list of Agents mutated from a given parent Agent
    _is_legal(Tuple[int]) -> bool                      // Returns True iff the given position is a legal index pair of the heightmap
    _softmax1D(Array[float]) -> Array[float]           // Softmax function implemented in numpy

    
### view.py
Contains the classes which render a given enviroment. (Potentially add graphical user inputs later)

#### BoardView()
Attributes:
    target_resolution   // int resolution targeted, difference from board divisibility
    hill_color          // int[] RGB values representing the color of the map
    agent_color         // int[] RGB values representing the color of agents
    board_data          // np.array containing the color-map (height is RGB magnitude)
    agent_positions     // int[] list of (x,y) agent locations
    new_agent_positions // int[] list of (x,y) agent locations
    agents_need_update  // bool indicating whether agent positions have changed since the board's last update
    screen              // pygame.display where everything is rendered

Public Methods:

    get_resolution()                    // Returns the actual resolution based on target_resolution and board_data dimensions
    update_screen()                     // Resizes the screen if resolution has changed and updates the board
    set_agents(new_positions: int[])    // Toggles the agents_need-update flag and assigns new_positions to new_agent_positions
    update_board()                      // Redraws cells on the board as necessary based on update agent positions.



### controller.py
Contains the classes which allow the model and view to work in tandem.


## Roadmap

