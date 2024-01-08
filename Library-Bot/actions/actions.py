# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


#from gpt3_fallback import ActionGPT3Fallback

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideBookInfo(Action):
    def name(self):
        return "action_provide_book_info"

    def read_book_info(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            book_info = file.read()
        return book_info

    def extract_book_title(self, book_info):
        # Mencari baris yang dimulai dengan "TITLE"
        title_line = next(line for line in book_info.split('\n') if line.startswith("TITLE"))
        # Mengambil teks setelah ":"
        title = title_line.split(": ")[1].strip()
        return title

    def extract_book_synopsis(self, book_info):
        # Mencari baris yang dimulai dengan "SYNOPSIS"
        synopsis_start = book_info.find("SYNOPSIS :") + len("SYNOPSIS :")
        # Mengambil teks setelah "SYNOPSIS :"
        synopsis = book_info[synopsis_start:].strip()
        return synopsis
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        book_info = self.read_book_info("BOOK_DATA.txt")
        book_title = self.extract_book_title(book_info)
        book_synopsis = self.extract_book_synopsis(book_info)
        
        if intent == 'ask_synopsis':
            if book_title:
                dispatcher.utter_message(template="utter_provide_synopsis", book_title=book_title, synopsis=book_synopsis)
            else:
                dispatcher.utter_message(text="I'm sorry, but I couldn't find information about that book.")

        elif intent == 'ask_book_from_synopsis':
            if book_synopsis:
                dispatcher.utter_message(template="utter_provide_book_title", book_title=book_title)
            else:
                dispatcher.utter_message(text="I'm sorry, but I couldn't find the synopsis of that book.")

        return []

    
    
# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
