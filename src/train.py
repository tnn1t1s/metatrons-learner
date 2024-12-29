import torch
import torch.nn as nn
import pandas as pd
from torch.utils.data import DataLoader, TensorDataset
from model import MetatronNet

def load_data(file_path):
    data = pd.read_csv(file_path)
    X = data[["x1", "x2", "x3", "x4", "x5"]].values
    y = data["label"].values
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)

def train_model():
    # Load data
    X_train, y_train = load_data("data/train_data.csv")
    dataset = TensorDataset(X_train, y_train)
    loader = DataLoader(dataset, batch_size=32, shuffle=True)

    # Model, loss, optimizer
    model = MetatronNet()
    criterion = nn.BCELoss()  # Binary cross-entropy loss
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    # Training loop
    epochs = 20
    for epoch in range(epochs):
        for batch in loader:
            inputs, labels = batch
            outputs = model(inputs).squeeze()
            loss = criterion(outputs, labels)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
    
    # Save model
    torch.save(model.state_dict(), "src/metatron_net.pth")

if __name__ == "__main__":
    train_model()

