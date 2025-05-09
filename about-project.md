# About My Project

Student Name:  Kiritu Gachuki
Student Email:  kgachuki@syr.edu

### What it does
This project was inspired by my senior capstone research project analyzing the ongoing 
civil war in Sudan. Although that research focused mostly on arms trafficking, I wanted
to create a dashboard that highlights the humanitarian situation in Sudan, including human
rights violations. This dashboard shows a map of violent events towards civilians sourced from
ACLED, while giving the option to filter by state and by event type. This also shows some statistics on
internal displacement in Sudan, with the option to look at the origins of displaced people and
the percent of each state.

### How you run my project
The datasets cannot be distributed without permission, so the cache is intially empty.
1. First run the extract.py script to retrieve the data from the APIs (note that API keys are not provided in the script).
2. Then run import_and_clean.py to get the data prepared for the visualization. 
3. Then, use Streamlit Run on dashboard.py to see and interact with the dashboard.
Make sure to run requirements.txt, especially for the Humanitarian Data Exchange API

### Other things you need to know
Since I cannot push the script with the API Key included, I will send an email with the key.
The key is associated with my student email, so make sure that field is also filled in extract.py.