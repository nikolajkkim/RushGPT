# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet



# class ActionValidateMajor(Action):
#     def name(self):
#         return "action_validate_major"

#     def run(self, dispatcher, tracker, domain):
#         # List of required majors
#         required_majors = ["aerospace engineering", 
#                            "eiomedical engineering", 
#                            "biomedical engineering",
#                            "chemical engineering", 
#                            "civil engineering", 
#                            "computer engineering", 
#                            "computer science",  
#                            "computer science engineering", 
#                            "data science", 
#                            "electrical engineering", 
#                            "engineering",
#                            "engineerg undelcared", 
#                            "engineerg undecided", 
#                            "environmental engineering", 
#                            "material science", 
#                            "mechanical engineering", 
#                            "software engineering"]

#         # Get the user's major from the slot
#         user_major = tracker.get_slot("user_major")
#         dispatcher.utter_message(text=f"Debug: User's major is '{user_major}'")  # Debugging line


#         # Check if the major is valid
#         if user_major in required_majors:
#             dispatcher.utter_message(text=f"Great! {user_major} is a valid major. Let's continue.")
#         else:
#             dispatcher.utter_message(text=f"Sorry, {user_major} is not one of the required majors for Theta Tau. Please provide a valid major.")
#             return [SlotSet("user_major", None)]  # Reset the slot to ask again
#         return []

# class ActionSubmitMajorForm(Action):
#     def name(self):
#         return "action_submit_major_form"

#     def run(self, dispatcher, tracker, domain):
#         # You can add additional logic here if needed
#         dispatcher.utter_message(text="Thanks for sharing your major!")
#         return []