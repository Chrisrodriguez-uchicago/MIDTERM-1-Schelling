from mesa import Agent

class SchellingAgent(Agent):
    ## Initiate agent instance, inherit model trait from parent class
    def __init__(self, model, agent_type):
        super().__init__(model)
        ## Set agent type
        self.type = agent_type

        if self.type == 0: #Asian
            self.tolerance = model.desired_share_alike_asian
        elif self.type == 1: #Latino
            self.tolerance = model.desired_share_alike_latino
        elif self.type == 2: # white
            self.tolerance = model.desired_share_alike_white
        elif self.type == 3: #black
            self.tolerance = model.desired_share_alike_black

    ## Define basic decision rule
    def move(self):
        ## Get list of neighbors within range of sight
        neighbors = self.model.grid.get_neighbors(self.pos,
            moore =True, include_center =False, radius =self.model.radius)
        ## Count neighbors of same type as self
        similar_neighbors = len([ent for ent in neighbors if ent.type == self.type])
        ## If an agent has any neighbors (to avoid division by zero), calculate share of neighbors of same type
        if len(neighbors) > 0:
            share_alike = similar_neighbors / len(neighbors)
        else:
            share_alike = 0
        ## If unhappy with neighbors, move to random empty slot. Otherwise add one to model count of happy agents.
        if share_alike < self.tolerance:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1
