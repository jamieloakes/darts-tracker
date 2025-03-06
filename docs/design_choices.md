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


## Data Entry

The data entry was decided to be done via a Command Line Interface. The reasons for this include:
- Less development work to set-up meaning faster time to be able to use tracker
- Simplicity of data being recorded
- This project is intended for personal use so no other end-users to support

The data entry was set-up using a set of menus. This was done for two main benefits:
- More modular approach allowing new practice games to be added easily
- Able to break down each practice game into its own logic/functions

The menus created are:
- Main menu
    - Initial screen to select other menus
- Round the World (Singles)
    - Menu/data entry form for Round the World (Singles) practice game
- Round the World (Doubles)
    - Menu/data entry form for Round the World (Doubles) practice game
- 501
    - Menu/data entry form for legs of 501

To help with data validation, the inputs were wrapped in a Try/Except block within a While loop. This allowed the data to be re-inputted rather than the program stopping in case of a ValueError.


## Data Analysis

The research questions for analysis were defined as:
- Which singles typically require more attempts to hit?
    - Use to improve scoring/setup play for problem targets
- Which doubles are more favourable?
    - Use to plan route for checkout
    - Use to improve performance for problem targets
- Is the current practice routine improving performance in 501?
    - Increase in 3 Dart Average?
    - Reduction in number of darts required to finish leg?
        - Can be used as a proxy for 3 Dart Average
    - Reduction in checkout attempts?

Matplotlib was used to create the visualisations. This was for two reasons:
- Extensive documentation and online support
- Compatability with DataFrames in its plotting functions
    - Results from database get read into a DataFrame meaning less work to prepare data

The visualisations created were:
- Round the World (Singles & Doubles)
    - Data Table
        - Show the raw data for the number of attempts/hits at each target
        - Easy to understand and quickly assess performance
    - Heatmap
        - Visually show performance on actual dartboard
            - Implemented using pie chart
        - Format colour of each target relative to the number of attempts
            - Singles: More attempts (i.e worse performance) means more vibrant colour
            - Doubles: Less hits (i.e worse performance) means more vibrant colour
        -  Easier to see specific problem areas of board (Top right, Bottom left etc.)

To collate these graphs into a report, many different solutions were considered. One solution was using a HTML template and then converting this into PDF format. The concern with this was content spreading across pages affecting readability of the report.

It was decided to use FPDF, a python library for creating PDFs, and embedding the PNGs of the graphs. This provided two main benefts:
- Ability to manage and configure pages to ensure related content fits on a single page
- Less work required to style report due to FPDF's built-in formatting functions