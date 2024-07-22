# src/mushroom_model.py
import joblib
import pandas as pd

PATH = "./models/artifacts.joblib"
ARTIFACT = joblib.load(PATH)
MODEL = None
PREPROCESSOR = None

def predict_mushroom(df):
    """
    Returns ndarray of predictions (poisonous=1) 
    given a properly formatted DataFrame of observations.
    """
    pass

if __name__ == "__main__":
    observation = {
        'cap-diameter': [50],
        'stem-height': [20],
        'stem-width': [30],
        'has-ring': ['t'],
        'cap-shape': ['c']
    }

    single_obs_df = pd.DataFrame(observation)
    print(predict_mushroom(single_obs_df))
