# Chinese-Swatter

Flask Web application that provides resources to help students study/practice Chinese 

## Objectives

1. Build functional system that provides a resource in which students can learn chinese characters

2. Build a fully functional graphical interface using bootstrap. 

3. Use of async javascript to update MCQ porition of /practice endpoint

## Project Structure

1. Front-end
    - practice page
    - about page
    - Use of ajax to handle game

2. Back-end
    - Routing endpoints
    - Character Models
        - id
        - hanzi
        - pinyin
        - english
        - book_volume
        - character_set

3. Script to create character sets
    - Query first google translate API using pinyin to get characters
    - Query official google translate API to ensure character matches english translation
    - Create new Chinese Character Model 
    - Append new model to list
    - After retrieving all requested characters for a given set commit to database

## Documentation 

## Contribution 

1. Fork repository
2. Make changes to repository (**Following google python style guide**)
3. Commit changes to forked repository
4. Make pull request, were a review will be done
5. Changes will be made accordingly to upstream repository whether to a sub-branch or master branch 



