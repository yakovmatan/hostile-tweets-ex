from pandas import DataFrame

from app.fetcher import Fetcher
from app.processor import TextProcessing
from app.read_files import ReadFile


class Manager:

    def __init__(self):
        self.weapons = ReadFile(path='../data/weapon_list.txt').read_file().split('\n')
        self.data = Fetcher().get_data()

    def get_processed_data(self):
        return TextProcessing(DataFrame(self.data)).rarest_word().sentiment().weapons_detected(self.weapons).df