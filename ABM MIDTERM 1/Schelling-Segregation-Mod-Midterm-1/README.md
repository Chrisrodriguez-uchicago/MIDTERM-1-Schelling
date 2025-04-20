# Schelling Segregation Model (Modified: Multi-Group Version)

*Code adapted from the given schelling model*

## Summary

This project is a modified version of the classic Schelling segregation model, implemented in Python using Mesa and Solara. The original model simulated how even small preferences for same-type neighbors can lead to large-scale segregation, despite agents being willing to live in mixed neighborhoods.

In this version, I extend the model from two agent types (Red and Blue) to four ethnoracial groups**, allowing for the representation of more realistic urban demographic dynamics. I additionally extended the model to allow distinct thereshold proportionss of neighbors allowed for each group. Each agent belongs to one of four groups (visualized by color), and seeks to live near a distinct threshold proportion of neighbors from their own group.

This modification enables the exploration of questions around multi-group segregation, racial hierarchies, and asymmetric preferences in urban environments.

## Modification

The base model has been extended to support four distinct agent types instead of two. The threshold has been changed from the same for both groups to distinct for all 4 groups. This allows for the simulation of segregation in a multi-group context, mimicking real-world cities like Chicago or Los Angeles, where multiple racial and ethnic communities interact simultaneously and with differing levels of tolerance.

Each group is assigned a unique color (e.g., orange, black, brown, blue), and the proportions of each group as well as their tolerances can be configured via the interactive GUI. The model tracks how agents move and cluster over time to maximize satisfaction with their neighbors, demonstrating how segregation can still emerge in a multi-ethnic setting.

This change adds enables more complex, asymmetric social modeling.

## Installation

Install required Python packages using the included `requirements.txt` file:

```bash
$ pip install -r requirements.txt

## How to Run

To run the model interactively once you have a complete agents file, run the following code in this directory:

```
    $ solara run app.py
```

## Files

* ``agents.py``: Contains the agent class, with modification to their attributes now allowing them to be one of 3 types wit the remainingg fourth group being the remainderof generated agents
* ``model.py``: Contains the model class, with modification of rules that place and assign type to agents
* ``app.py``: Defines classes for visualizing the model in the browser via Solara, and instantiates a visualization server. This has a slight modification whichh defines the way in which the new two groups of agents are viaulized
