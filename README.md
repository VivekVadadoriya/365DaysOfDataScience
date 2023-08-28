# 365DaysOfDataScience
> This repository contains my daily tasks and resources for the #365DaysOfDataScience Challenge.

## Day 1: Learn Airflow
- [Install Airflow Using Docker](https://www.youtube.com/watch?v=Sva8rDtlWi4&ab_channel=Philodiscite) : This approch does not work as it is giving an error "docker daemon is not running".
- [Install Docker](https://www.youtube.com/watch?v=aCRMnDLnWmU&ab_channel=ProgrammingKnowledge) : Follow this video to install docker on your windows 11.
- [Install Airflow W/O Using Docker](https://www.youtube.com/watch?v=Va_NMDoDqLQ&ab_channel=TechAdvice) : Tried this method and it works, but after all installation i didn't get username and password.
- [Install/Uninstall WSL](https://youtu.be/CV6SKGbUv5Q) : Used to Install/Uninstall WSL.
- [How to Delete Linux Distro](https://youtu.be/Q5bLGgW_U0Y) : Used to delete unused WSL System.
- [Install Airflow - FreeCodeCamp](https://www.freecodecamp.org/news/install-apache-airflow-on-windows-without-docker/) : This is the best guide to follow.
- [Airflow For Beginners](https://youtu.be/p0vZedMl93c) : Must Video for Installation and creating first project. Learn to create first dag and see it's log. Commmand used while creating this project are [cat fileName, sudo vi fileName, airflow dags list, airflow standalone]
  
## Day 2: Did Some Airflow Projects
- [Edit/Save file in Ubuntu](https://stackoverflow.com/questions/17535428/how-to-edit-save-a-file-through-ubuntu-terminal) : How to edit/save a file through Ubuntu Terminal
- [Getting Started with Apache Airflow](https://www.youtube.com/watch?v=iKGdg4MDEBI&ab_channel=AIEngineering) : Best video to learn airflow concept. [Download Code](https://github.com/Sri-nidhi/airflow2.0-demo)  
- [Airflow Download Podcast](https://www.youtube.com/watch?v=s-r2gEr7YW4&ab_channel=Dataquest) : Step by Step Guide - [Link](https://github.com/dataquestio/project-walkthroughs/blob/master/podcast_summary/steps.md). **Some Command :**
  - nano ~/airflow/airflow.cfg : To edit config file and set dag path and other changes.
  - sqlite3 databaseName.db : To create sqlite database.
  - airflow connections add 'connectionName' --conn-type 'sqlite' --conn-host 'databasePath/databaseName.db' : To add connection in airflow.
  - airflow connections get connectionName : Get all the connection by the name connectionName.
  - pwd : To get current file path.
  - Learn how to pass data from one task to other in airflow.
  - Learn how to download audio file.
- [Webinar on Airflow](https://youtu.be/Fy6oRT-8GlY) : Good for beginners, But not worth time if you have already created dag.

## Day 3: Learn DBT and Some Maths
- [DBT Fundamental Course](https://courses.getdbt.com/courses/fundamentals) : **Learnings :**
  - ETL is the process of creating new database objects by extracting data from multiple data sources, transforming it on a local or third party machine, and loading the transformed data into a data warehouse.
  - ELT is a more recent process of creating new database objects by first extracting and loading raw data into a data warehouse and then transforming that data directly in the warehouse.
  - The new ELT process is made possible by the introduction of cloud-based data warehouse technologies.
- [Linera Algebra](https://www.3blue1brown.com/topics/linear-algebra) : **Topics Covered :**
  - Essence of linear algebra preview
  - Vectors, what even are they?
  - Linear combinations, span, and basis vectors
  - Linear transformations and matrices

## Day 4: Continue Learning DBT
- [DBT Fundamental Course](https://courses.getdbt.com/courses/fundamentals) : **Learnings :**
  - dbt Cloud is a hosted version that streamlines development with an online Integrated Development Environment (IDE) and an interface to run dbt on a schedule.
  - dbt Core is a command line tool that can be run locally.
  - dbt is designed to handle the transformation layer of the ‘extract-load-transform’ framework for data platforms. dbt creates a connection to a data platform and runs SQL code against the warehouse to transform data.
  - Quickstart for dbt Cloud and Snowflake: [Link](https://docs.getdbt.com/quickstarts/snowflake?step=4)
  - Models : 
    - Models are .sql files that live in the models folder.
    - Models are simply written as select statements - there is no DDL/DML that needs to be written around this. This allows the developer to focus on the logic.
    - The materialization can be configured as a table with the following configuration block at the top of the model file: `{{ config(materialized='table') }}`
    - When dbt run is executing, dbt is wrapping the select statement in the correct DDL/DML to build that model as a table/view. If that model already exists in the data warehouse, dbt will automatically drop that table or view before building the new database object.
  - Modularity :
    - Modularity is the degree to which a system's components may be separated and recombined, often with the benefit of flexibility and variety in use. This allows us to build data artifacts in logical steps.
  - ref Macro:
    - Models can be written to reference the underlying tables and views that were building the data warehouse. Example: `{{ ref('stg_customers') }}` compiles to analytics.dbt_jsmith.stg_customers.
  - Command - If `dbt run -s staging` will run all models that exist in models/staging.
  - Sources:
    - Sources represent the raw data that is loaded into the data warehouse.
    - We can reference tables in our models with an explicit table name (raw.jaffle_shop.customers).
    - However, setting up Sources in dbt and referring to them with the source function enables a few important tools.
      - Multiple tables from a single source can be configured in one place.
      - Sources are easily identified as green nodes in the Lineage Graph.
      - You can use dbt source freshness to check the freshness of raw tables.
    - The ref function is used to build dependencies between models.
    - Similarly, the source function is used to build the dependency of one model to a source. Example : {{ source('jaffle_shop','customers') }}
  - Source freshness:
    -  Freshness thresholds can be set in the YML file where sources are configured. For each table, the keys loaded_at_field and freshness must be configured.
    - A threshold can be configured for giving a warning and an error with the keys warn_after and error_after.
    - The freshness of sources can then be determined with the command dbt source freshness.

## Day 5: Continue Learning DBT
- [DBT Fundamental Course](https://courses.getdbt.com/courses/fundamentals) : **Learnings :**
  - 