# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_core_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
#from rasa.sdk_events import SlotSet

class ActionCheckWeather(Action):
   def name(self) -> Text:
      return "action_check_weather"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      dispatcher.utter_message("Hello World! from custom action")
      return []
