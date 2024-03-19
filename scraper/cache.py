from setup import CACHE
import pickle

def cache(file, data, mode="wb"):
    with open(CACHE + '/' + file, mode) as f:
        pickle.dump(data, f)

def load(file, mode="rb"):
    with open(CACHE + '/' + file, mode) as f:
        return pickle.load(f)
