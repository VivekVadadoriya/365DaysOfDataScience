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