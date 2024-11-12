import os
import csv


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

            for row in reader:
                print(row)
                break
        return True
