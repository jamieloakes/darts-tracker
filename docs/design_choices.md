# Design Choices

This document aims to provide context and reasoning behind the design decisions made for this project.


## Data Storage

The data was decided to be stored in a database. The reasons for this are:
- Structured nature of the data to be recorded
- Ability to enforce better data validity compared to a CSV file
- Perform aggregations directly with SQL

The particular DBMS used was SQLite. The reasoning for this was:
- Native support within python making it easy to setup
- Lightweight nature of SQLite made it a better fit for the small amount of data predicted to be stored

SQLite doesn't provide a native datatype for DATE/TIME fields which instead have to be stored as TEXT. This wasn't considered an issue due to the time-series functions SQLite provides to get around this.


## Database Schema

The database was set-up with three tables to reflect the three main practice games. These tables are:
- singles_rtw
- doubles_rtw
- legs_stats

While the __*singles_rtw*__ and __*doubles_rtw*__ tables contain similar fields, it was decided to put these in their own tables as the objectives of each are different. This helps to maintain separation of concerns making it easier in the analysis stage.

Furthermore, the database is not fully normalised which was done for the below reasons:
- Data management wasn't predicted to be a major concern due to the small number of fields 
- The savings in storage size from normalisation was not considered sufficient enough
- Less normalised data makes it easier to query through the use of less joins