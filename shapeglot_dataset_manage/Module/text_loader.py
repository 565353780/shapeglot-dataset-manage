import os
import csv
from tqdm import tqdm


class TextLoader(object):
    def __init__(self, dataset_root_folder_path: str) -> None:
        self.dataset_root_folder_path = dataset_root_folder_path

        self.shapenet_chairs_csv_file_path = self.dataset_root_folder_path + 'main_data_for_chairs/language/shapenet_chairs.csv'

        self.text_dict = {}
        return

    def reset(self) -> bool:
        self.text_dict = {}
        return True

    def loadTexts(self) -> bool:
        if not os.path.exists(self.shapenet_chairs_csv_file_path):
            print('[ERROR][TextLoader::loadTexts]')
            print('\t shapenet chairs csv file not exist!')
            print('\t shapenet_chairs_csv_file_path:', self.shapenet_chairs_csv_file_path)
            return False

        self.reset()

        with open(self.shapenet_chairs_csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in tqdm(reader, total=94120):
                if not row['correct']:
                    continue

                text = row['text']

                target_chair = row['target_chair']
                if target_chair == '0':
                    chair_id = row['chair_a']
                elif target_chair == '1':
                    chair_id = row['chair_b']
                else:
                    chair_id = row['chair_c']

                if chair_id not in self.text_dict:
                    self.text_dict[chair_id] = [text]
                else:
                    self.text_dict[chair_id].append(text)

        return True
