# Project Amendments

This document aims to provide context and reasoning behind the amendments made after the initial project was completed.


## Database Schema

### game_id Field

To support with viewing the distribution for each of the Round the World practice games, a game_id field was added to the respective tables.

This was implemented using a UUID4 string giving each game a unique ID in the table. This meant that multiple games of Round the World could be separated easily to be able to use GROUP BY to aggregate figures.

The steps to make this change included:
- Export current data to .csv
- Amend database schema
- Generate game_id values for current data
- Re-add data to tables
- Amend data entry logic to include game_id field


## Data Analysis

### Round the World Distribution

With the changes made in the database schema, a new visualisation was created for the report for the Round the World pages. This new visualisation provided insight into the distribution of attempts/hits to assess overall performance.

This distribution analysis replaced the summary tables on the report. This was because the summary table provided similar insights to the heatmap visual making it redundant.

The new chart was implemented using a histogram. The median and 25th/75th percentile were then also added as vertical lines to help assess average performance. The bin size was determined as below:
- Singles:
    - Bin size = 3
    - Corresponds to the number of darts in hand at start of attempt 
- Doubles:
    - Bin size = 1
    - Due to limited performance at hitting doubles, smaller bin size allowed for more granular analysis against objective of practice game