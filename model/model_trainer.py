from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

def train_and_save_model():
    df = pd.read_csv("Iris.csv")
    df = df.drop('Id',axis=1)
    X = df.drop('Species', axis=1)
    y = df['Species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, 'model/iris_clf_model.pkl')

if __name__ == "__main__":
    train_and_save_model()