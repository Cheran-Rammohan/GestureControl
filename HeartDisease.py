import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

x_ready = pd.read_csv(r'C:\Users\chera\OneDrive\Documents\SPRING 2022\ENGR 3398\refined_x.csv')
y_ready = pd.read_csv(r'C:\Users\chera\OneDrive\Documents\SPRING 2022\ENGR 3398\refined_y.csv')
print(x_ready.head())

x_train,x_test,y_train,y_test = train_test_split(x_ready, y_ready, random_state=42)

clf_dt = DecisionTreeClassifier(random_state=42)
clf_dt = clf_dt.fit(x_train, y_train)

#plt.figure(figsize= (10, 5))
plot_tree(clf_dt, class_names=["Heart Disease: Yes","Heart Disease: NO"], feature_names=x_ready.columns)

plot_confusion_matrix(clf_dt, x_test, y_test, display_labels=["Heart Disease: Yes","Heart Disease: NO"])

path = clf_dt.cost_complexity_pruning_path(x_train,y_train)
ccp_alphas = path.ccp_alphas
ccp_alphas = ccp_alphas[:-1]


clf_dts = []
alpha_loop_values = []
for ccp_alphas in ccp_alphas:
    clf_dt = DecisionTreeClassifier(random_state=0, ccp_alpha= ccp_alphas)
    scores = cross_val_score(clf_dt, x_train, y_train, cv = 6)
    alpha_loop_values.append([ccp_alphas, np.mean(scores), np.std(scores)])

alpha_results = pd.DataFrame(alpha_loop_values,columns=['alpha', 'mean_accuracy', 'std'])
max_acc_ideal_ccp_alpha = alpha_results['mean_accuracy'].max()
max_acc_col = alpha_results['mean_accuracy']
size = len(alpha_results.index)
for i in range(1, size):
    if max_acc_col.iloc[i] == max_acc_ideal_ccp_alpha:
        ideal_alpha_index = i
ideal_ccp_alpha = alpha_results.at[ideal_alpha_index, 'alpha']
ideal_ccp_alpha = float(ideal_ccp_alpha)
print(ideal_ccp_alpha)