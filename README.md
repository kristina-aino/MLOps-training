# Overview

I want to create and document multiple low to medium intensity ml-ops integrations.

Important is that I want a full MLOps stack, from automation to monitoring to deployment, 
as well as added Data science, analysis and engineering to increase 
the learn effect for end to end ML Projects in the real world.

Every Projects stack is randomly generated with the `project-selector.py` script.
The generated categories are:
    `Orchestration` - what tool to use to automate pipelines, schedule ingress, start training/retraining, update visualizations, etc.
    `Framework` - Which framework to use for the models
    `Server` - What technology is used for serving the models (this might be restriced by the Framework selection)
    `Monitor` - The technology for monitoring training, model interations and deployments
    `Data storage` - The primary data storage used
    `Data Analysis` - how the data should be analyzed and visualized during the production
    `Wildcard` - A raondom technology that might or might not be applicable and can be left out