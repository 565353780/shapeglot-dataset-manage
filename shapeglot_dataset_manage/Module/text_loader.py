import os
import csv
from tqdm import tqdm

from shapeglot_dataset_manage.Method.io import unpickle_data

class TextLoader(object):
    def __init__(self, dataset_root_folder_path: str) -> None:
        self.dataset_root_folder_path = dataset_root_folder_path

        self.shapenet_chairs_csv_file_path = self.dataset_root_folder_path + 'main_data_for_chairs/language/shapenet_chairs.csv'
        self.word_spell_pkl_file_path = self.dataset_root_folder_path + 'main_data_for_chairs/language/word_spell_manual_corrector_chairs.pkl'

        self.text_dict = {}
        return

    def reset(self) -> bool:
        self.text_dict = {}
        return True

    def loadTexts(self) -> bool:
        if not os.path.exists(self.word_spell_pkl_file_path):
            print('[ERROR][TextLoader::loadTexts]')
            print('\t word spell pkl file not exist!')
            print('\t word_spell_pkl_file_path:', self.word_spell_pkl_file_path)
            return False

        if not os.path.exists(self.shapenet_chairs_csv_file_path):
            print('[ERROR][TextLoader::loadTexts]')
            print('\t shapenet chairs csv file not exist!')
            print('\t shapenet_chairs_csv_file_path:', self.shapenet_chairs_csv_file_path)
            return False

        self.reset()

        chair_text_dict = {}

        spell_corrector = next(unpickle_data(self.word_spell_pkl_file_path))

        with open(self.shapenet_chairs_csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in tqdm(reader, total=94120):
                if not bool(row['correct']):
                    continue

                text = row['text']

                have_end = text[-1] == '.'
                if have_end:
                    text = text[:-1]

                word_list = text.split()

                for i, word in enumerate(word_list):
                    if word in spell_corrector.keys():
                        word_list[i] = spell_corrector[word]

                correct_text = ' '.join(word_list)
                if have_end:
                    correct_text += '.'

                target_chair = row['target_chair']
                if target_chair == '0':
                    chair_id = row['chair_a']
                elif target_chair == '1':
                    chair_id = row['chair_b']
                else:
                    chair_id = row['chair_c']

                if chair_id not in chair_text_dict:
                    chair_text_dict[chair_id] = [correct_text]
                else:
                    chair_text_dict[chair_id].append(correct_text)

        self.text_dict['03001627'] = chair_text_dict
        return True
