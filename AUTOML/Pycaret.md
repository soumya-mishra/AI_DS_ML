### Get the dataset
import pandas
dataset=pd.read_csv(path)

### pass the data annd Target column
from pycaret.classification import *

model_setup = setup(data=dataset, target='Survived',session_id=1,silent = True)

### compare different models 
compare_models()

### Creating and Tunning the model
model = create_model('gbc',fold=10)

### Tunning the models 
tuned_model = tune_model('gbc',fold=10)

### Model Performance's Visualization
plot_model(tuned_model,plot = 'auc')

#Precision-

plot_model(tuned_model,plot = 'pr')

#plotting confusion matrix

plot_model(tuned_model,plot = 'confusion_matrix')

### Ensembling of models
blend_all = blend_models(method='hard')

y_pred_blend = predict_model(blend_all, data=test_model)

### Stacking of models

lightgbm = create_model('lightgbm')

xgboost = create_model('xgboost')

catboost = create_model('catboost')

lda = create_model('lda')

ridge = create_model('ridge')

gbc = create_model('gbc')

lightgbm = create_model('lightgbm')


#Final stacking models - Pass a meta model as we pass in stacking 

stacker = stack_models(estimator_list = [lightgbm,xgboost,ridge,catboost,lda,gbc],meta_model = xgboost,method='hard')
