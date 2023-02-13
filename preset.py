import os

def create_preset_list() -> list:
    '''make a list of all subdirectories in directory "sounds" '''
    presets = []
    rootdir = 'sounds'
    for rootdir, dirs, files in os.walk(rootdir):
        for subdir in dirs:
            print(os.path.join(rootdir, subdir))
            presets.append(os.path.join(rootdir, subdir))
    return presets

def choose_preset(n, num_presets) -> int:
    if n + 1 <= num_presets:
        n += 1
    else:
        n = 0
    return n