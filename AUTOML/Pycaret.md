import pandas
dataset=pd.read_csv(path)

from pycaret.classification import *
model_setup = setup(data=dataset, target='Survived',session_id=1,silent = True)

#compare different models 
compare_models()

