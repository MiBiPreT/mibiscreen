# `mibipret` Natural Attenuation Screening

## General

`na_screening` provides tools for data analysis regarding ongoing biodegradation. Outcome of this "quick-scan" serve as starting point for evaluating if natural attenuation is a feasible strategy for remediation. The quick-scan is based on technical and scientific analysis of existing data. Goal is to determine whether natural attenuation is occurring and to identify what type of additional data is further necessary to prognosticate long-term behavior of a contaminant plume. The tools for the NA screening are based on the *First traffic light: Quick scan of historical data* as part of the NOBIS-report of Sinke et al., 2001[^1].

### What is Natural Attenuation (NA)?

*Natural Attenuation*(NA) or *monitored natural attenuation* (MAN) is a strategy for clean-up of contaminated groundwater based on allowing naturally occurring processes to reduce the toxic potential of contaminants. NA does not apply engineered solutions but builds on the recognition that certain subsurface pollutants can degrade naturally without
human intervention under appropriate conditions.

Processes involved in NA:
* hydro(geo)logy: Dilution of contaminant concentrations by spatial spreading due to dispersion and diffusion.
* biology: Reduction of contaminant mass by microbial degradation. 
* geochemistry: Immobilization of contaminants due to chemical reactions and adsorption.

All processes are linked as geochemical composition of the domain impacts microbial activity (availability of electron acceptors for their metabolism) and hydrogeological transport changes concentrations of contaminant, but also electron acceptors in space and time. 

## Assessment criteria
To decide if NA is suitable as remediation strategy, the most important questions that need to be answered are:

1) Does natural degradation of the contamination occur?
2) Is the degradation fast enough compared to the tolerated spread?
3) Is the process complete or is there stagnation in the long term?

If natural degradation of the contamination occurs, it is expected that a stable end situation will be reached in the short or long term. A remediation objective for the subsurface is for instance formulating a period of 30 years to achieve a stable end situation. Specifically, reaching acceptable concentrations of contaminants in the groundwater which are no threat to existing vulnerable objects and/or major impediments to the current or future use of the location or the environment. In many cases, but not always necessarily, there will be a sustainable equilibrium between supply and natural degradation and/or retention. Reaching a stable end situation my include temporary plume expansion. Modeling can help to evaluate for how long a plume will continue to expand until a stationary situation is reached. For the application of natural degradation, this has to be put in relation to the question if degradation is fast enough compared to the tolerated spread. If degradation stagnates, e.g. due to depletion of electron acceptors, with contaminant concentration levels exceeding acceptable levels, then NA is not a sustainable remediation strategy. 

## Traffic light principle

Data analysis provides decision support information in the form of *traffic lights*. They reflect the chances on natural attenuation as a remediation option: good with green light, fair chance with orange light, or no
chance with a red light. In case of an orange traffic light, additional information is needed.

Goal of the NA screening is to evaluate the probability that monitored natural attenuation is an appropriate strategy to achieve site specific remediation objectives within a reasonable time frame:
* at an early stage 
* with as little expenses as possible

The output can serve as decision support, while decisions on whether NA can be applied remain with problem owners and authorities. Relevant aspects in these discussions and decisions, such as political and practical considerations .. a role in the final decision and those aspects are listed and can be consulted at each traffic
light. A checklist with those aspects for the Netherlands conditions is added.

### Analysis Method/Workflow

Starting point is a spreadsheet/dataframe containing structured data. Raw data has to be brought into a template format with support routines provided in `data` to load, clean and standardize the data.

## References

[^1]: A.J.C. Sinke, T.J. Heimovaara, H. Tonnaer, J. Ter Meer (2001); Beslissingsondersteunend systeem voor de beoordeling van natuurlijke afbraak als sanieringsvariant, 
NOBIS 98-1-21, Gouda

