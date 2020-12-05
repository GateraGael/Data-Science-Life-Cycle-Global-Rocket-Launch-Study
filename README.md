# Aerospace Launch Business Data Analysis
## 

Provide an analytical framework that is part of the Data Science lifecycle that can prove to be give an advantage to the EAC Spaceport Feasibility Study research team.

This project is an application of Data-Driven business intelligent tools and techniques to study global launch business using various available sources of data.

Apply methodologies in data science to prove the "low cost", "reliability" and other aspects of what would constitute an ideal launch site depending on the desired application for stakeholders.

The objective of this project is to provide the EAC Spaceport Feasibility Study team insight into launch business based on past data and current trends and better able to predict the future of the industry using statistical insight, or whichever predictive model that proves to be the most accurate and reliable.

Although much is written generally about analytics, it is important to make a clear distinction between BI and Data Science One way to evaluate the type of analysis being performed is to examine the time horizon and the kind of analytical approaches being used.  In sales and for a typical company, BI systems make it easy to answer questions related to quarter-to-date revenue, progress toward quarterly targets, and understand how much of a given product was sold in a prior quarter or year.  These questions tend to be closed-ended and explain current or past behavior, typically by aggregating historical data and grouping it in some way. 

This approach is not really fit for research!

By comparison, Data Science tends to use disaggregated data in a more forward-looking, exploratory way, focusing on analyzing the present and enabling informed decisions about the future. Rather than aggregating historical data to look at how many of a given product sold in the previous quarter, a team may employ models such as time series analysis. Data Science tends to be more exploratory in nature and may use scenario optimization to deal with more open-ended questions such as what is the optimal scenario for our business? What will happen next? Why are these trends happening? What will happen next?

The 6 Phases of the Data Science Lifecycle:
Phase 1—Discovery: In Phase 1, the team learns the business domain, including relevant history such as whether the organization or business unit has attempted similar projects in the past from which they can learn.
Phase 2 – Data Preparation: In this phase, the team gathers as much data as possible store it in an easy to access database and take steps to condition the data for the next phase.
Phase 3 – Model Planning: In this phase, the team explores the data to learn about the relationships between variables and subsequently selects key variables and the most suitable models.
Phase 4 – Model Building: The team develops datasets for testing, training, and production purposes. In addition, in this phase the team builds and executes models based on the work done in the model planning phase.
Phase 5 – Communicate Results:  The team should identify key findings, quantify the business value, and develop a narrative to summarize and convey findings to stakeholders.
Phase 6 – Operationalize: The team delivers final reports, briefings, code, and technical documents


The key roles for our analytics project are the following:
Users: EAC Spaceport Feasibility Study Team
Project Sponsor: NSBE/ Aerospace SIG
Project Manager: Gael Gatera
BI Analyst: EAC Spaceport Feasibility Study Team
Database Admin: Jibri Tolen
Data Engineer: Jibri Tolen
Data Scientist: Gael Gatera


Phase 1 review:
From Previous Study done by the EAC Spaceport Feasibility Study Team framed the problem statement & Identified Key Stakeholders 

Our initial Hypothesis is that from a business standpoint launching from an as near to the equator as often as possible provides a cost reduction to identified stakeholders.

Lastly, we have gathered several open source data that should help give us the insight that we need. That will be refered to in this repository.

Here is four of the open source data that we have found for our project: Spacex.csv file from a Kaggle profile, Space x rest API, Rocket Launch Sites Page from Wikipedia, Spreadsheet from Union for Concerned Scientists detailing the over 2,218 satellites which is a research group website


Phase 2 review:
This phase typically starts with ETL which is an acronym for:
Extract: read the data in our case from multiple sources 
Transform: clean and structure the data into the desired form 
Load: Is to write the data into a database for storage 

Successfully deployed a SQL Linux based Server deployed by AWS that will house the previously mentioned open source data and will be used to make queries.

A brief look into the specifications of our server:
Deployed an EC2 instance that hosts a SQL Server with the data normalized to make our BI reports a lot easier to produce.
EC2 instance allow DBA to have full control of the database and allows us to choose what Operating System and other utilities to add for the most optimal performance.
Typical RDS (Relational Database Systems) choses the previously mentioned for us which is a negative.
We used a Linux Based instead of Microsoft in order to save up to 3x the space on our VDK (Virtual Hard Disk) for basic kernel needs

We are currently in somewhat of a phase 2.5 as the data still needs to be cleaned up quite a bit. However, we jumped the gun a bit and started doing some a priori analysis just for the sake of it and started making some plots as the one shown in this slide. 
This is a plot made from the UCS satellites database of the longitudinal location from where a satellite was launched from vs. the respective launch mass. Here we can see that there are quite a lot of satellites launched very near the equator however it is still not enough make clear conclusions.
