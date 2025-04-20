import solara
from model import SchellingModel
from mesa.visualization import (
    SolaraViz,
    make_space_component,
    make_plot_component,
)

## Define agent portrayal: color, shape, and size
def agent_portrayal(agent):

    #MODIFICATION: defining olor scheme for additional groups
    if agent.type == 0:
        color = "blue" #Asians appear as Blue
    elif agent.type == 1:
        color = "#895129" #Latinos appear as Brown
    elif agent.type == 2:
        color = "orange" #White people appear as Orange
    elif agent.type == 3:
        color = "black" #Black people appear as Black
    else:
        #This is a fail safe to see if any agents are somehow assigned another type.
        color = "gray"


    return {
        "color": color,
        "marker": "s",
        "size": 40,
        "x": agent.pos[0],
        "y": agent.pos[1],
    }

## Enumerate variable parameters in model: seed, grid dimensions, population density, agent preferences, vision, and relative size of groups.
## MODIFICATION: Added sliders to GUI for both group shares and tolerance thersolds
#for easy manipulation of demographics disperate prefernces.
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "width": {
        "type": "SliderInt",
        "value": 50,
        "label": "Width",
        "min": 5,
        "max": 100,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 50,
        "label": "Height",
        "min": 5,
        "max": 100,
        "step": 1,
    },
    "density": {
        "type": "SliderFloat",
        "value": 0.7,
        "label": "Population Density",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "desired_share_alike_white": {
        "type": "SliderFloat",
        "value": 0.6,
        "label": "White Desired Share Alike",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "desired_share_alike_asian": {
        "type": "SliderFloat",
        "value": 0.4,
        "label": "Asian Desired Share Alike",
        "min": 0,
        "max": 1,
        "step": 0.01,
        },
    "desired_share_alike_black": {
        "type": "SliderFloat",
        "value": 0.25,
        "label": "Black Desired Share Alike",
        "min": 0,
        "max": 1,
        "step": 0.01,
        },
    "desired_share_alike_latino": {
        "type": "SliderFloat",
        "value": 0.3,
        "label":  "Latino Desired Share Alike",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "group_one_share": {
        "type": "SliderFloat",
        "value": 0.29,
        "label": "Share Latino Agents",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "group_two_share": {
        "type": "SliderFloat",
        "value": 0.36,
        "label": "Share White Agents",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "group_three_share": {
        "type": "SliderFloat",
        "value": 0.28,
        "label": "Share Black Agents",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "radius": {
        "type": "SliderInt",
        "value": 1,
        "label": "Vision Radius",
        "min": 1,
        "max": 5,
        "step": 1,
    },
}

## Instantiate model
schelling_model = SchellingModel()

## Define happiness over time plot
HappyPlot = make_plot_component({"share_happy": "tab:blue"})

## Define space component
SpaceGraph = make_space_component(agent_portrayal, draw_grid=False)

## Instantiate page inclusing all components
page = SolaraViz(
    schelling_model,
    components=[SpaceGraph, HappyPlot],
    model_params=model_params,
    name="Schelling Segregation Model",
)
## Return page
page
