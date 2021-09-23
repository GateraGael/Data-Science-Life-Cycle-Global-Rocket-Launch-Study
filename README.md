# Global Rocket Launch Data Analysis

![This is a alt text.](images/ASIG_Logo.PNG)

[www.nsbe-aerospace.org](https://www.nsbe-aerospace.org/)

# Table of contents
1. [Introduction](#Introduction)
2. [Purpose](#Purpose)
    1. [Approach](#Approach)
3. [Phase 1](#Phase1)

<!--
see how to make table of contents in markdown: https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents

2. [Some paragraph](#paragraph1)
    1. [Sub paragraph](#subparagraph1)
3. [Another paragraph](#paragraph2)
-->
## Introduction to East Africa Spaceport Concept<a name="Introduction"></a>

The East Africa Spaceport Feasibility Study Research Team of the Aerospace Special Interest Group (SIG) at National Society of Black Engineers (NSBE) is currently involved in a 9 year research project whose aim is to make various arguments supporting the case for an equatorial launch site in the East African Community. A spaceport, also called a launch site, is a complex with multiple facilities for launching spacecraft into trajectories around the Earth and beyond.  The concept of the East African Community (EAC) Spaceport nicknamed “Uhuru”, a Swahili word that means “freedom” was first suggested during the 2012 NSBE Aerospace Systems Conference in Los Angeles. The NSBE Space SIG partnered with Futron Corporation, Phezu Space LLC, and Isibizo Phezu Space (Pty) Ltd South Africa, and performed a preliminary study of this concept. The preliminary study highlighted the following: geo-physical advantages and possible sites for spaceport, science and technology advancement, economic benefits, space market competitiveness, South African spaceport collaboration, and public safety and asset protection. Several operational conveniences exist with building an equatorially located spaceport in East Africa. Rocket launch physics indicates that an equatorial launch to Geostationary Earth Orbit (GEO), Low Earth Orbit (LEO), or interplanetary trajectories uses less fuel than a launch from other latitudes for the same payload mass. The ability to either launch larger payloads or manifest more payloads for the same cost is an attractive option to space industry businesses. Alternatively, the ability to launch the same payload at a reduced cost versus launching from other latitudes is equally attractive.


## Purpose<a name="Purpose"></a>

The purpose of this global rocket launch business study is to provide members of the mentioned East African Spaceport research team an analytical framework based on the Data Science lifecycle proposed by the "Data Science and Big Data Analytics - Discovering, Analyzing, Visualizing and Presenting Data" book by EMC Education Services. This project aims at providing insight of gloabl rocket launches based on current and past trends in order for the mentioned team to be able to predict the future of the industry. Stakeholders of the hypothetical Spaceport in East Africa can also gain some industry insights to better understand and plan to use the near-equatorial location as a launch as a service platform.
Statistical insights and Machine Learning models can be applied on available open source datasets containing historical rocket launches to prove the "low cost", "reliability" and other aspects of what would constitute an ideal launch site depending on the desired application and target orbits for customers.

Much is written generally about analytics, it is important to make a clear distinction between BI and Data Science. One way to evaluate the type of analysis being performed is to examine the time horizon and the kind of analytical approaches being used.  

In sales and for a typical company, BI systems make it easy to answer questions related to quarter-to-date revenue, progress toward quarterly targets, and understand how much of a given product was sold in a prior quarter or year.  These questions tend to be closed-ended and explain current or past behavior, typically by aggregating historical data and grouping it in some way. 

This approach is not really fit for research!

By comparison, Data Science tends to use disaggregated data in a more forward-looking, exploratory way, focusing on analyzing the present and enabling informed decisions about the future. Rather than aggregating historical data to look at how many of a given product sold in the previous quarter, a team may employ models such as time series analysis. Data Science tends to be more exploratory in nature and may use scenario optimization to deal with more open-ended questions such as what is the optimal scenario for our business? What will happen next? Why are these trends happening? What will happen next?

### Approach <a name="Approach"></a>

The 6 Phases of the Data Science Lifecycle:

**Phase 1 — Discovery:** In Phase 1, the team learns the business domain, including relevant history such as whether the organization or business unit has attempted similar projects in the past from which they can learn.

**Phase 2 – Data Preparation:** In this phase, the team gathers as much data as possible store it in an easy to access database and take steps to condition the data for the next phase.

**Phase 3 – Model Planning:** In this phase, the team explores the data to learn about the relationships between variables and subsequently selects key variables and the most suitable models.

**Phase 4 – Model Building:** The team develops datasets for testing, training, and production purposes. In addition, in this phase the team builds and executes models based on the work done in the model planning phase.

**Phase 5 – Communicate Results:** The team should identify key findings, quantify the business value, and develop a narrative to summarize and convey findings to stakeholders.

**Phase 6 – Operationalize:** The team delivers final reports, briefings, code, and technical documents

![This is a alt text.](images/DataLifecycle-6phases.PNG){ width=50% height=50% }


## Phase 1 <a name="Phase 1"></a>
From Previous Study done by the EAC Spaceport Feasibility Study Team framed the problem statement & Identified Key Stakeholders 

Our initial Hypothesis is that from a business standpoint launching from an as near to the equator as often as possible provides a cost reduction to identified stakeholders.

Lastly, we have gathered several open source data that should help give us the insight that we need. That will be refered to in this repository.

Here is four of the open source data that we have found for our project: Spacex.csv file from a Kaggle profile, Space x rest API, Rocket Launch Sites Page from Wikipedia, Spreadsheet from Union for Concerned Scientists detailing the over 2,218 satellites which is a research group website


<!--
## Some paragraph <a name="paragraph1"></a>
The first paragraph text

### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="paragraph2"></a>
The second paragraph text

-->



