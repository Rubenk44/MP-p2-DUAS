import numpy as np
import pandas as pd
import os
import cv2 as cv
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

def flatten_image(image):
    # Flatten the image using NumPy
    return image.flatten()

def process_image(file_path, terrain):
    # Load and preprocess the image
    image = cv.imread(file_path)
    image = cv.resize(image, (25, 25))
    flattened_image = flatten_image(image)
    return [terrain] + flattened_image.tolist()

def get_train():
    data = []
    # Iterate over the images for each terrain type folder in 'trainset' and append the flattened tile and terrain type to the dataframe
    for terrain in os.listdir("trainset"):
        terrain_path = os.path.join("trainset", terrain)
        for file in os.listdir(terrain_path):
            file_path = os.path.join(terrain_path, file)
            data.append(process_image(file_path, terrain))
    
    # Convert data to DataFrame
    columns = ["terrain"] + [f"pixel{i}" for i in range(25 * 25 * 3)]  # Assuming RGB images
    df = pd.DataFrame(data, columns=columns)
    
    # Save the dataframe to a csv file
    df.to_csv("trainset.csv", index=False)

def train_model():
    df = pd.read_csv("trainset.csv")
    df.dropna(inplace=True)
    X = df.drop("terrain", axis=1)
    NaN_rows = np.argwhere(np.isnan(X))
    y = df["terrain"]
    model = RandomForestClassifier(n_estimators=100, n_jobs=-1, max_depth=10, random_state=42)
    model.fit(X, y)
    dump(model, "model.joblib")

if __name__ == "__main__":
    get_train()
    train_model()