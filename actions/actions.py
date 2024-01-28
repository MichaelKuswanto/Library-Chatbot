# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Dict, Text, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import json

from difflib import SequenceMatcher

class ActionProvideSynopsisByTitle(Action):
    def name(self) -> Text:
        return "action_provide_synopsis"

    def calculate_similarity(self, str1, str2):
        # Menggunakan SequenceMatcher untuk menghitung similarity score
        similarity_ratio = SequenceMatcher(None, str1, str2).ratio()
        return similarity_ratio

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Ambil judul buku dari entitas 'book_title'
        user_book_title = tracker.latest_message['entities'][0]['value']

        # Baca data dari file JSON
        with open('BOOK_DATA.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Cari sinopsis berdasarkan judul buku dengan tingkat kesamaan tertinggi
        max_similarity = 0
        matching_book_synopsis = None

        for book in data['books']:
            book_title = book['title']
            similarity_score = self.calculate_similarity(user_book_title, book_title)

            if similarity_score > max_similarity:
                max_similarity = similarity_score
                matching_book_synopsis = book['synopsis']

        # Tentukan batas similarity yang diterima
        threshold_similarity = 0.6

        if max_similarity >= threshold_similarity:
            # Ambil templat dari domain.yml
            template = "utter_provide_synopsis"

            # Gantilah nilai placeholder dengan nilai yang sesuai
            response = domain["responses"][template][0]["text"]
            response = response.format(book_title=user_book_title, synopsis=matching_book_synopsis)

            # Berikan respons
            dispatcher.utter_message(text=response)
        else:
            # Jika similarity tidak mencapai threshold
            dispatcher.utter_message(text=f'Maaf, saya tidak dapat menemukan sinopsis untuk buku dengan judul "{user_book_title}".')

        return []

class ActionProvideAuthorByTitle(Action):
    def name(self) -> Text:
        return "action_provide_author"

    def calculate_similarity(self, str1, str2):
        # Menggunakan SequenceMatcher untuk menghitung similarity score
        similarity_ratio = SequenceMatcher(None, str1, str2).ratio()
        return similarity_ratio

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Ambil judul buku dari entitas 'book_title'
        user_book_title = tracker.latest_message['entities'][0]['value']

        # Baca data dari file JSON
        with open('BOOK_DATA.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Cari penulis berdasarkan judul buku dengan tingkat kesamaan tertinggi
        max_similarity = 0
        matching_book_author = None

        for book in data['books']:
            book_title = book['title']
            similarity_score = self.calculate_similarity(user_book_title, book_title)

            if similarity_score > max_similarity:
                max_similarity = similarity_score
                matching_book_author = book['author']

        # Tentukan batas similarity yang diterima
        threshold_similarity = 0.6

        if max_similarity >= threshold_similarity:
            # Ambil templat dari domain.yml
            template = "utter_provide_author"

            # Gantilah nilai placeholder dengan nilai yang sesuai
            response = domain["responses"][template][0]["text"]
            response = response.format(book_title=user_book_title, author=matching_book_author)

            # Berikan respons
            dispatcher.utter_message(text=response)
        else:
            # Jika similarity tidak mencapai threshold
            dispatcher.utter_message(text=f'Maaf, saya tidak dapat menemukan informasi penulis untuk buku dengan judul "{user_book_title}".')

        return []

class ActionProvideGenreByTitle(Action):
    def name(self) -> Text:
        return "action_provide_genre"

    def calculate_similarity(self, str1, str2):
        # Menggunakan SequenceMatcher untuk menghitung similarity score
        similarity_ratio = SequenceMatcher(None, str1, str2).ratio()
        return similarity_ratio

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Ambil judul buku dari entitas 'book_title'
        user_book_title = tracker.latest_message['entities'][0]['value']

        # Baca data dari file JSON
        with open('BOOK_DATA.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Cari genre berdasarkan judul buku dengan tingkat kesamaan tertinggi
        max_similarity = 0
        matching_book_genre = None

        for book in data['books']:
            book_title = book['title']
            similarity_score = self.calculate_similarity(user_book_title, book_title)

            if similarity_score > max_similarity:
                max_similarity = similarity_score
                matching_book_genre = book['genre']

        # Tentukan batas similarity yang diterima
        threshold_similarity = 0.6

        if max_similarity >= threshold_similarity:
            # Ambil templat dari domain.yml
            template = "utter_provide_genre"

            # Gantilah nilai placeholder dengan nilai yang sesuai
            response = domain["responses"][template][0]["text"]
            response = response.format(book_title=user_book_title, genre=matching_book_genre)

            # Berikan respons
            dispatcher.utter_message(text=response)
        else:
            # Jika similarity tidak mencapai threshold
            dispatcher.utter_message(text=f'Maaf, saya tidak dapat menemukan informasi genre untuk buku dengan judul "{user_book_title}".')

        return []

class ActionProvideTitleBySynopsis(Action):
    def name(self) -> Text:
        return "action_provide_book_title"

    def calculate_similarity(self, str1, str2):
        # Menggunakan SequenceMatcher untuk menghitung similarity score
        similarity_ratio = SequenceMatcher(None, str1, str2).ratio()
        return similarity_ratio

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Ambil sinopsis dari entitas 'synopsis'
        user_synopsis = next((entity['value'] for entity in tracker.latest_message['entities'] if entity['entity'] == 'synopsis'), None)

        # Baca data dari file JSON
        with open('BOOK_DATA.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Cari judul berdasarkan sinopsis buku dengan tingkat kesamaan tertinggi
        max_similarity = 0
        matching_book_title = None

        for book in data['books']:
            book_synopsis = book['synopsis']
            similarity_score = self.calculate_similarity(user_synopsis, book_synopsis)

            if similarity_score > max_similarity:
                max_similarity = similarity_score
                matching_book_title = book['title']

        # Tentukan batas similarity yang diterima
        threshold_similarity = 0.6

        if max_similarity >= threshold_similarity:
            # Ambil templat dari domain.yml
            template = "utter_provide_book_title"

            # Gantilah nilai placeholder dengan nilai yang sesuai
            response = domain["responses"][template][0]["text"]
            response = response.format(book_title=matching_book_title)

            # Berikan respons
            dispatcher.utter_message(text=response)
        else:
            # Jika similarity tidak mencapai threshold
            dispatcher.utter_message(text='Maaf, saya tidak dapat menemukan buku dengan sinopsis yang sesuai.')

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
