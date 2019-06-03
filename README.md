[//]: # (Image References)
[image1]: ./image/Schematic1.png
[image2]: ./image/Schematic2.png
[image3]: ./image/Schematic3.png

# ParCell
ParCell: A Parallel Cell Population Modeling Software

ParCell can simulate a cell population from single cell biochemical reactions and their environment (extracellular domain).

Documentation of Parcell is included in the file "Documentation ParCell.pdf".

![alt text][image1]

Schematic diagram of the population modeling framework. The framework uses multiprocessing parallelism to create a multiscale population model from a single-cell biochemical reaction network model. Each single cell is represented by a stand-alone parallel process. Intercellular communication is mediated in a server-client fashion. On the far right of the figure, an example set of biochemical network reactions associated with each cell is shown. The network consists of two intracellular species S and P and their synthesis, degradation, and inter-conversion in response to an extracellular cue I. The master process creates a population of cells, where each cell has this same set of biochemical reactions. However, the master process incorporates heterogeneity among the cells by sampling the protein copy number or parameter values from defined distributions (Input 1). In addition, the master process implements rules for cellular decision-making based on the intracellular species concentrations (Input 2). The master process also determines how the extracellular input I may change over time (t) or position (x,y,z
) based on some defined rules (Input 3).

![alt text][image2]

# Steps in parallel framework

The virtual master process takes 3 inputs: reaction rules, environment and constant. (1) The master spawns several parallel processes. Here, each cell is modeled as a memoryless process, termed cell process. In a large scale system several cell processes are assigned to a single core. (2) In each time intervals, master sends molecular concentration and environment information to each cell process and invokes Gillespie Algorithm. (3) Each cell process runs the Gillespie algorithm locally and (4) returns the updated molecular concentration to the master. Following this, the master node (5) updates environment variable, (6) population dynamics and (7) global time, before returning to first step. This cycle continues until simulation duration is reached.

![alt text][image3]

Schematic diagram of ParCell software.

This software is based on a published paper:

Islam, Mohammad, et al. "Multicellular Models Bridging Intracellular Signaling and Gene Transcription to Population Dynamics." Processes 6.11 (2018): 217.

