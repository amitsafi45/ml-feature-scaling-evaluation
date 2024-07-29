import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    df = pd.read_csv(file_path)
    df = df.iloc[:,2:]
    return df

def split_data(df):
    X_train, X_test, y_train, y_test = train_test_split(df.drop('Purchased', axis=1),
                                                        df['Purchased'],
                                                        test_size=0.3,
                                                        random_state=0)
    return X_train, X_test, y_train, y_test

def scale_data(X_train, X_test):
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler.mean_
