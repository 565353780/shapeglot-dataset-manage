from shapeglot_dataset_manage.Module.text_loader import TextLoader

def demo():
    dataset_root_folder_path = '/home/chli/chLi/Dataset/ShapeGlot/data/'

    text_loader = TextLoader(dataset_root_folder_path)
    text_loader.loadTexts()

    print(len(text_loader.text_dict['03001627'].keys()))
    return True
