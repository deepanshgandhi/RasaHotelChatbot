# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime
#from rasa.sdk_events import SlotSet

class Action_Return_time(Action):
   def name(self) -> Text:
      return "action_return_time"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      tim=tracker.get_slot("time")
      tim=int(tim)
      now=datetime.datetime.now()
      final_time=now.hour+tim
      if(final_time>12):
         dispatcher.utter_message("Sure, I have scheduled a cleaning for {} pm today".format(final_time-12))
      else:
         dispatcher.utter_message("Sure, I have scheduled a cleaning for {} am today".format(final_time))

      return []
