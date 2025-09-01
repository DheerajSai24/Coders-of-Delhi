# Coders Of Delhi

## Overview
This project demonstrates fundamental data analysis techniques using pure Python, without relying on specialized data analysis libraries. It analyzes employee data from Coders Of Delhi, processing employee connections and page interactions from JSON data.

## Project Structure

- `data.json` - Original dataset containing employee and page information
- `data2.json` - Alternative dataset (used in some scripts)
- `cleaned_data.json` - Processed dataset after cleaning operations
- `Cleaning_data.py` - Script for data cleaning and preprocessing
- `FindingPeopleYouMayKnow.py` - Algorithm to suggest potential colleague connections
- `FindingPagesYouMightLike.py` - Algorithm to recommend pages based on employee interests
- `load_user_data.py` - Utility script to load and display employee information

## Data Structure

The dataset contains two main components:

### Employees
Each employee has:
- `id` - Unique identifier
- `name` - Employee's name
- `friends` - List of employee IDs representing connections
- `liked_pages` - List of page IDs the employee has liked

### Pages
Each page has:
- `id` - Unique identifier
- `name` - Name of the page

## Features

### Data Cleaning
The `Cleaning_data.py` script performs several data cleaning operations:
- Removes employees with missing values
- Eliminates duplicate friend connections
- Removes inactive employees (those without friends or liked pages)
- Removes duplicate pages

### Colleague Recommendations
The `FindingPeopleYouMayKnow.py` script implements a colleague recommendation algorithm that:
- Identifies colleagues-of-colleagues who aren't already connected
- Ranks potential connections based on the number of mutual colleagues
- Returns a sorted list of recommended connections

### Page Recommendations
The `FindingPagesYouMightLike.py` script implements a page recommendation algorithm that:
- Analyzes pages liked by employees with similar interests
- Ranks potential page recommendations based on shared interests
- Returns a sorted list of recommended pages

### Data Visualization
The `load_user_data.py` script provides a simple text-based visualization of:
- Employees and their connections
- Page information

## How to Use

1. Clone this repository
2. Run the scripts in the following order:
   ```
   python Cleaning_data.py
   python load_user_data.py
   python FindingPeopleYouMayKnow.py
   python FindingPagesYouMightLike.py
   ```

## Learning Objectives

This project demonstrates:
- Basic data processing techniques in Python
- JSON data handling
- Implementation of recommendation algorithms
- Data cleaning and preprocessing
- Employee network analysis concepts

## Requirements

- Python 3.x
- No external libraries required (uses only built-in Python modules)

## Note

This project is designed for educational purposes to understand the fundamentals of data analysis without relying on specialized libraries. The algorithms implemented are simplified versions of real-world recommendation systems.