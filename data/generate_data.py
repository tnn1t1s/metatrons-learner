import numpy as np
import pandas as pd

def generate_data(samples=1000):
    np.random.seed(42)  # For reproducibility

    # Generate 5 input features
    x1 = np.random.rand(samples)
    x2 = np.random.rand(samples)
    x3 = np.random.rand(samples)
    x4 = np.random.rand(samples)
    x5 = np.random.rand(samples)

    # Generate labels based on a "cool" rule:
    # Combine weighted sums and a nonlinear term
    y = (0.3 * x1 + 0.2 * x2 - 0.4 * x3 + 0.1 * np.sin(5 * x4) + 0.5 * x5 > 0.5).astype(int)

    # Save data to a pandas DataFrame
    data = pd.DataFrame({
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "x4": x4,
        "x5": x5,
        "label": y
    })

    # Split into train and test datasets
    train_data = data.sample(frac=0.8, random_state=42)
    test_data = data.drop(train_data.index)

    # Save to CSV files
    train_data.to_csv("data/train_data.csv", index=False)
    test_data.to_csv("data/test_data.csv", index=False)

    print("Training and testing datasets generated and saved to 'data/' directory.")

if __name__ == "__main__":
    generate_data()

