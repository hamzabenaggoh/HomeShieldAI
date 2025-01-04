import warnings
import sys
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,precision_recall_fscore_support
from sklearn.metrics import f1_score,roc_auc_score
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
from xgboost import plot_importance
from joblib import load

# Ensure a CSV file argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]


# Get model
rf = load('/Users/hamzabenaggoun/Desktop/HomeShieldAI/snort_ml/model/models/clf_rf.joblib')

# Read dataset
# df = pd.read_csv("../pcap_output/testing2.pcap_Flow.csv")

try:
    df = pd.read_csv(csv_file)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    sys.exit(1)

#Get selected features
selected_features = load('/Users/hamzabenaggoun/Desktop/HomeShieldAI/snort_ml/model/features/selected_features.joblib')

# Get the scaler
scaler = load('/Users/hamzabenaggoun/Desktop/HomeShieldAI/snort_ml/model/scalers/scaler.joblib')

#Get training features
# training_features = load('../model/features/training_features.joblib')
training_features = scaler.feature_names_in_




column_mapping = {
        'Flow Duration': 'Flow Duration',
        'Total Fwd Packet': 'Total Fwd Packets',
        'Total Bwd packets': 'Total Backward Packets',
        'Total Length of Fwd Packet': 'Total Length of Fwd Packets',
        'Total Length of Bwd Packet': 'Total Length of Bwd Packets',
        'Fwd Packet Length Max': 'Fwd Packet Length Max',
        'Fwd Packet Length Min': 'Fwd Packet Length Min',
        'Fwd Packet Length Mean': 'Fwd Packet Length Mean',
        'Fwd Packet Length Std': 'Fwd Packet Length Std',
        'Bwd Packet Length Max': 'Bwd Packet Length Max',
        'Bwd Packet Length Min': 'Bwd Packet Length Min',
        'Bwd Packet Length Mean': 'Bwd Packet Length Mean',
        'Bwd Packet Length Std': 'Bwd Packet Length Std',
        'Flow Bytes/s': 'Flow Bytes/s',
        'Flow Packets/s': 'Flow Packets/s',
        'Flow IAT Mean': 'Flow IAT Mean',
        'Flow IAT Std': 'Flow IAT Std',
        'Flow IAT Max': 'Flow IAT Max',
        'Flow IAT Min': 'Flow IAT Min',
        'Fwd IAT Total': 'Fwd IAT Total'
    }


# Apply column mapping to standardize column names
df.rename(columns=column_mapping, inplace=True)

# print(df.columns)

# Handle missing features (not in the dataset but required for training)
missing_features = [feature for feature in training_features if feature not in df.columns]
if missing_features:
    # print(f"Warning: The following features are missing in the dataset: {missing_features}")
    for feature in missing_features:
        df[feature] = 0 

# Drop extra features not required by the model
extra_features = [feature for feature in df.columns if feature not in training_features]
if extra_features:
    # print(f"Warning: Dropping extra features not used during training: {extra_features}")
    df.drop(columns=extra_features, inplace=True)

# Ensure column order matches training data
df = df[training_features]

# Scale numeric features
numeric_features = df.select_dtypes(include=[float, int]).columns
df[numeric_features] = scaler.transform(df[numeric_features])

# Handle invalid values (NaN, inf)
df = df.fillna(0) 
df = df.replace([float('inf'), float('-inf')], 0) 

df = df[selected_features]


# print(df.head())
# print()
# print(df.columns)
# print()
# print(selected_features)


# Testing pretrained prediction
# new_row = np.array([
#     0.74212177,  1.58145868, -0.04606245, -0.04606245, -0.55972423, -0.59874409,
#     -0.59874409, -0.56950241,  3.46884699, -0.04834351, -0.04839057, -0.0779658,
#     -0.62799905, -0.63124783, -0.24866129, -0.03430633, -0.03430633, -0.2478958,
#     -0.06677185, -0.06677185
# ])
# df.loc[len(df)] = new_row
# print(df.tail())

# Make predictions
predictions = rf.predict(df.to_numpy())
print(predictions)



"""

Possible issues:

make sure that the sklearn versions are the same


"""