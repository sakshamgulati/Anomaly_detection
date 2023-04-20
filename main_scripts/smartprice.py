from DataOps.feature_engg import feature_engg_class
feat=feature_engg_class()
num_df,cat_df,output=feat.load_data()
fin_df=feat.min_max_scaling(cat_df,num_df)
X_train,X_test,y_train,y_test=feat.split(fin_df,output)
print(f"length of the train set:{len(X_train)}")

