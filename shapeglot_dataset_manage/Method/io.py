from six.moves import cPickle

def unpickle_data(file_name: str):
    in_file = open(file_name, 'rb')
    size = cPickle.load(in_file, encoding='latin1')

    for _ in range(size):
        yield cPickle.load(in_file, encoding='latin1')
    in_file.close()
