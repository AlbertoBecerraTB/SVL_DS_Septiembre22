###############################################################
# Script para la generacion del minitrain y el minitest en el
# problema de CNN Cats & Dogs
###############################################################

import pandas as pd

# Ruta al directorio raiz
ROOT_PATH = "C:\\Users\\alber\\Downloads\\dogs-vs-cats\\"

# Ruta a la carpeta train que tenemos que dividir en MINITRAIN
# y MINITEST
TRAIN_PATH = ROOT_PATH + "train\\train\\"

# Ruta en la que se quieren guardar MINITRAIN y MINITEST
MINI_TRAIN_PATH = ROOT_PATH + "mini_train\\"
MINI_TEST_PATH = ROOT_PATH + "mini_test\\"

# CSVs conteniendo los nombres de los ficheros para minitrain
# y minitest generados por shuhffling
TRAINING_FILENAMES = '3-Machine Learning/4-Deep Learning/\
                        2-Redes Convolucionales/train_files.csv'

TEST_FILENAMES = '3-Machine Learning/4-Deep Learning/\
                    2-Redes Convolucionales/test_files.csv'

# Lectura y conversión en iterable
ls_train_files = pd.read_csv(TRAINING_FILENAMES)
ls_test_files = pd.read_csv(TEST_FILENAMES)

ls_train_files = ls_train_files['filename'].tolist()
ls_test_files = ls_test_files['filename'].tolist()

def copy_img(ls_files, from_path, to_path):
    '''
    Función que replica una serie de archivos de 
    la carpeta from_path a to_path
    '''
    import shutil
    for file in ls_files:
        shutil.copy(from_path + file, to_path)

# Copia de train a los MINIs
copy_img(ls_train_files, TRAIN_PATH, MINI_TRAIN_PATH)
copy_img(ls_test_files, TRAIN_PATH, MINI_TEST_PATH)