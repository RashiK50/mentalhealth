import streamlit as st
import pandas as pd


data = pd.read_csv("D:\pro2\Student Mental health.csv")

# Filter data for males
male_data = data[data['Choose your gender'] == 'Male']

# Count the number of 'Yes' responses for each question
questions = ['Do you have Anxiety?', 'Do you have Depression?', 'Do you have Panic attack?', 'Did you seek any specialist for a treatment?']
yes_counts = male_data[questions].apply(lambda x: (x == 'Yes').sum())

# Create the bar chart
st.bar_chart(yes_counts)

# Optionally, display the counts for clarity
st.write("Number of males responding 'Yes' to each question:")
st.write(yes_counts)

st.divider()
st.divider()
st.divider()


female_data = data[data['Choose your gender'] == 'Female']

# Count the number of 'Yes' responses for each question
questions = ['Do you have Anxiety?', 'Do you have Depression?', 'Do you have Panic attack?', 'Did you seek any specialist for a treatment?']
yes_counts_female = female_data[questions].apply(lambda x: (x == 'Yes').sum())

# Create the bar chart
st.bar_chart(yes_counts_female)

# Optionally, display the counts for clarity
st.write("Number of females responding 'Yes' to each question:")
st.write(yes_counts_female)

st.divider()
st.divider()
st.divider()


female_data = data[data['Choose your gender'] == 'Female']
male_data = data[data['Choose your gender'] == 'Male']

# List of questions
questions = ['Do you have Anxiety?', 'Do you have Depression?', 'Do you have Panic attack?', 'Did you seek any specialist for a treatment?']

# Count the number of 'Yes' responses for each question for females and males
yes_counts_female = female_data[questions].apply(lambda x: (x == 'Yes').sum())
yes_counts_male = male_data[questions].apply(lambda x: (x == 'Yes').sum())

# Combine the 'Yes' counts for males and females into a single DataFrame
combined_counts = pd.DataFrame({
    'Female': yes_counts_female,
    'Male': yes_counts_male
})

# Create a bar chart with the combined counts
st.bar_chart(combined_counts)

# Optionally, display the counts for clarity
st.write("Number of 'Yes' responses for each question by gender:")
st.write(combined_counts)