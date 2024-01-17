# Steps for making a neural network model and training it:
#     1. Import all necessary packages and dependencies from your ML framework (PyTorch in this case)
#     2. Get the data and set training size
#     3. Make the neural network
#     4. Create instances of your neural network and additional tools like an optimizer and loss 
#     5. Engage your neural network in a training loop
#     6. Observe the outputs your model delivers and carry out any necessary changes


# imports for beginner MNIST training using PyTorch
from torch import nn                                    # neural network package, contains helpful classes
from torch.optim import Adam                            # optimization algorithm efficient in training
from torch.utils.data import DataLoader                 # tool to help load data from a dataset and do various actions
from torchvision import datasets                        # package of datasets ready for use (DataSets in util.data is an alternative)
from torchvision.transforms import ToTensor             # convert data to tensors processable by PyTorch

# get data from dataset package, set its root, tell PyTorch to download, train, and convert data to a tensor for processing
trainingData = datasets.MNIST(
    root="data", 
    download=True, 
    train=True, 
    transform=ToTensor()
    )
# tell PyTorch to get and train images in batches of 32 
trainingDataset = DataLoader(trainingData, 32)

# create neural network using a base class in the nn package, Module 
class numberClassifier(nn.Module):
    def __init__(self):                                 # initialize the layers of our neural network using components from nn package
    
    def forward(self, x):                               # define how data is processed as it passes through the layers of our neural network

# create instances of the neural network, the optimizer (for improving the neural network), and loss (for difference between neural network's output and true output)

# set the computation platform of the nueral network to NVIDIA's CUDA parallel computing platform if available on device, else use the device's CPU (if there's no NVIDIA GPU, use CPU)
trainer = numberClassifier().to(torch.device('cuda' if torch.cuda.is_available() else 'cpu')) 

# give the optimization algorithm the neural network's parameters and set the learning rate (step size) to 0.001, which makes the optimization slower but more precise results
optimizer = Adam(trainer.parameters(), lr=1e-3)

# use the nn package's CrossEntropyLoss method for loss calculation, a common way for multi-class classification problems like MNIST
findLoss = nn.CrossEntropyLoss()
