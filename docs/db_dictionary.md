# Database Dictionary

This document provides information regarding the tables and fields of the database.

Each section relates to a table in the database containing further explanations and field definitions.


## singles_rtw

Contains data for the Singles Round the World practice game.

Each record is the outcome of hitting the required target on the dartboard.

### Fields:
- (PK) event_id
    - Description: Unique ID for attempt
    - Type: INTEGER
- event_date
    - Description: Date of practice game
    - Type: TEXT
- target
    - Description: Single number attempting to hit
    - Type: TEXT
- attempts
    - Description: Number of attempts to hit target
    - Type: INTEGER


## doubles_rtw

Contains data for the Doubles Round the World practice game.

Each record is the outcome of throwing 9 darts at the required target on the dartboard. 


### Fields:
- (PK) event_id
    - Description: Unique ID for each attempt
    - Type: INTEGER
- event_date
    - Description: Date of practice game
    - Type: TEXT
- target
    - Description: Double number attempting to hit
    - Type: TEXT
- hits
    - Description: Number of hits of target
    - Type: INTEGER


## legs_stats

Contains data for 501 practice games.

Each entry is a leg of 501 and the key stats from it.

### Fields:
- (PK) leg_id
    - Description: Unique ID for leg of 501
    - Type: INTEGER
- event_date
    - Description: Date of practice game
    - Type: TEXT
- n_darts
    - Description: Number of darts thrown in leg
    - Type: INTEGER
- avg
    - Description: Three dart average of leg
    - Type: REAL
- checkout_attempts
    - Description: Number of darts thrown for check out
    - Type: INTEGER
- win
    - Description: Win outcome of leg (1 = Win, 0 = Lost)
    - Type: INTEGER