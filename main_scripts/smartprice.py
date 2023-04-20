from DataOps.feature_engg import feature_engg_class
from Model.model_fit import *
feat=feature_engg_class()
num_df,cat_df,output=feat.load_data()
fin_df=feat.min_max_scaling(cat_df,num_df)
X_train,X_test,y_train,y_test=feat.split(fin_df,output)
print(f"length of the train set:{len(X_train)}")

l_reg=model_fit()
metric=l_reg.model(X_train,X_test,y_train,y_test)
