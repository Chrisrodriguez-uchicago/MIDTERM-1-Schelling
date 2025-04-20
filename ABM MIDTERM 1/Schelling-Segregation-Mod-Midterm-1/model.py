from mesa import Model
from mesa.space import SingleGrid
from agents import SchellingAgent
from mesa.datacollection import DataCollector

class SchellingModel(Model):
    ## Define initiation, requiring all needed parameter inputs
    def __init__(self, width = 50, height = 50, density = 0.7, desired_share_alike_white = 0.5, desired_share_alike_black = 0.25, desired_share_alike_asian = 0.4, desired_share_alike_latino = 0.3,  group_one_share = 0.29, group_two_share = .36,  group_three_share =.28, radius = 1, seed = None):
        ## Inherit seed trait from parent class
        super().__init__(seed=seed)
        ## Define parameter values for model instance
        self.width = width
        self.height = height
        self.density = density
        self.desired_share_alike_latino = desired_share_alike_latino
        self.desired_share_alike_asian = desired_share_alike_asian
        self.desired_share_alike_black = desired_share_alike_black
        self.desired_share_alike_white = desired_share_alike_white

        self.group_one_share = group_one_share
        self.group_two_share = group_two_share
        self.group_three_share = group_three_share

        self.radius = radius
        ## Create grid
        self.grid = SingleGrid(width, height, torus = True)
        ## Instantiate global happiness tracker
        self.happy = 0
        ## Define data collector, to collect happy agents and share of agents currently happy
        self.datacollector = DataCollector(
            model_reporters = {
                "happy" : "happy",
                "share_happy" : lambda m : (m.happy / len(m.agents)) * 100
                if len(m.agents) > 0
                else 0
            }
        )

        # store the groupshares for readibility of assignment below.
        g1 = self.group_one_share   # Latino
        g2 = self.group_two_share   # White
        g3 = self.group_three_share # Black
        g4 = max(0, 1.0 - (g1 + g2 + g3))  # Asian calculated as remainder of population

        ## Place agents randomly around the grid, randomly assigning them to agent types.
        for cont, pos in self.grid.coord_iter():
            if self.random.random() < self.density:
                r = self.random.random()
                #If-else statement segements  agents into 4 categories
                #approximating a rough distribution of Black, Latino, Asian,
                #and White people in Chicago.

                #The demographics are as follows:
                #type 1 = Latinos (29% of Chicago)
                #type 2 = Whites (36% of Chicago)
                #type 3 = Black (28% of Chicago)
                #type 0 = Asian (7% of Chicago)

                if r < g1:
                    agent_type = 1 #Latino
                elif r < g1 + g2:
                    agent_type = 2 #White
                elif r < g1 + g2 +  g3:
                    agent_type = 3 #Black
                else:
                    agent_type = 0 #Asian

                self.grid.place_agent(SchellingAgent(self, agent_type), pos)


                '''
                if self.random.random() < self.group_one_share:
                    self.grid.place_agent(SchellingAgent(self, 1), pos)
                else:
                    self.grid.place_agent(SchellingAgent(self, 0), pos)

                '''

        ## Initialize datacollector
        self.datacollector.collect(self)

    ## Define a step: reset global happiness tracker, agents move in random order, collect data
    def step(self):
        self.happy = 0
        self.agents.shuffle_do("move")
        self.datacollector.collect(self)
        ## Run model until all agents are happy
        self.running = self.happy < len(self.agents)
