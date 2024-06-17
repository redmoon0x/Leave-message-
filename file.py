import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://bbhcca21020:qQ1XnGQ9XmOZZCVQ@cluster0.qzlwovv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.message_board_db
collection = db.messages

# Set up the page title
st.title("Anonymous Message Board - Submit Messages")

# Input box for new messages
message = st.text_area("Leave a message for me anonymously:")

# Button to submit the message
if st.button("Submit"):
    if message:
        # Insert message into MongoDB collection
        collection.insert_one({"message": message})
        st.success("Your message has been submitted!")
    else:
        st.error("Please enter a message before submitting.")
