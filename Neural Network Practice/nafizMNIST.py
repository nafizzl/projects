# Steps for making a neural network model and training it:
#     1. Import all necessary packages and dependencies from your ML framework (PyTorch in this case)
#     2. Get the data and set training size (batch)
#     3. Make the neural network
#     4. Create instances of your neural network and additional tools like an optimizer and loss 
#     5. Engage your neural network in a training loop
#           a. Calculate the losses in each training cycle
#           b. Use them to adjust and optimize your model for better results
#     6. Observe the outputs your model delivers and carry out any necessary changes


# imports for beginner MNIST training using PyTorch
import torch                                            # get the full package to use things like assigning computation platform
from PIL import Image                                   # get the ability to load images and have the trainer anyalyze and conclude on them
from torch import nn, load, save                        # neural network package, contains helpful classes
from torch.optim import Adam                            # optimization algorithm efficient in training
from torch.utils.data import DataLoader                 # tool to help load data from a dataset and do various actions
from torchvision import datasets                        # package of datasets ready for use (DataSets in util.data is an alternative)
from torchvision.transforms import ToTensor             # convert data to tensors processable by PyTorch
import time                                             # This is for adding sensible delays to terminal messages

# get data from dataset package, set its root, tell PyTorch to download, train, and convert data to a tensor for processing
trainingData = datasets.MNIST(
    root="data", 
    download=True, 
    train=True, 
    transform=ToTensor()
    )
# tell PyTorch to get and train images in batches of 32 
trainingDataset = DataLoader(trainingData, 32)

# # Trying out these methods to determine MNIST set size, and try to view labels and tensor representations of images 
# print(len(trainingData))                         # length of MNIST is 60,000
# image = trainingData[10][0]                      # first index of an entry is the image of the digit itself
# label = trainingData[10][1]                      # second index of an entry is the image's label (what the number written is)
# print(label)                                     # gives the number 
# print(image.size())                              # gives size of image (28 x 28 pixels)
# print(image)                                     # in terminal, gives tensor of image, in other IDE like Google Collab, shows actual image

# create neural network using a base class in the nn package, Module 
class numberClassifier(nn.Module):
    def __init__(self):                                 # initialize the layers of our neural network using components from nn package
        super().__init__()                              # invoke the super constructor of parent, allowing for correct initialization of a functional PyTorch neural network
        self.model = nn.Sequential(
            # nn's 2D convolutional layer method, which defines a neural network's layer's input channels, output channels, and size of kernels (matrices) 
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3),        
            ## nn's Rectified Linear Unit function, introduces non-linearity by converting any negative values to 0, allowing neural network to learn complex patterns
            nn.ReLU(),
            ## Repeat the previous two in order to build up the layers of the neural network, adjusting channel numbers mainly
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
            nn.ReLU(),
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3),
            nn.ReLU(),
            ## nn's Flatten method which converts the multi-channel value to a single tensor/vector
            nn.Flatten(),
            ## nn's Linear function, which takes the calculated output and tries to identify a class (take worked on image, say which digit it is from 0 to 9)
            nn.Linear(64*1*(28-6)*(28-6), 10)
            # The -6 is to account for shaved pixels from the paired Conv2d and ReLU functions.
        )
    def forward(self, x):                               # define how data is processed as it passes through the layers of our neural network
        return self.model(x)

# create instances of the neural network, the optimizer (for improving the neural network), and loss (for difference between neural network's output and true output)

# set the computation platform of the nueral network to NVIDIA's CUDA parallel computing platform if available on device, else use the device's CPU (if there's no NVIDIA GPU, use CPU)
device = ('cuda' if torch.cuda.is_available() else 'cpu')
trainer = numberClassifier().to(device) 

# give the optimization algorithm the neural network's parameters and set the learning rate (step size) to 0.001, which makes the optimization slower but more precise results
optimizer = Adam(trainer.parameters(), lr=1e-3)

# use the nn package's CrossEntropyLoss method for loss calculation, a common way for multi-class classification problems like MNIST
findLoss = nn.CrossEntropyLoss()

if __name__ == "__main__":
    choice = -1
    print("Welcome to nafizzl's MNIST training model.")
    while choice != 1 and choice != 2:
        time.sleep(2)
        print("Press 1 to train the model and get a PyTorch file.")
        time.sleep(2)
        print("Press 2 to view the results of a trained model.")
        time.sleep(2)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            for epoch in range(10):                             # train model for 10 epochs, or 10 full run-throughs of the entire database 
                for batch in trainingDataset:                   # We use the DataLoader instance rather than the MNIST dataset itself
                    x,y = batch                                 # Get the batch for model to work with (x is image, y is label)
                    x,y = x.to(device),y.to(device)             # Send your data to device, whether CPU or GPU 
                    yhat = trainer(x)                           # Get the result from the neural network
                    loss = findLoss(yhat, y)                    # Compute the difference between the neural network's output and the real output
                    
                    # Take the previous results and start optimizing and "upgrading" your model to later output accurate results
                    # First apply the gradient function to your optimizer results to determine how your model should improve
                    optimizer.zero_grad()
                    # Next, apply backpropagation calculations using the loss function
                    loss.backward()
                    # Increment the optimizer's step and 
                    optimizer.step()

                print(f"Epoch {epoch} loss: {loss.item()}")     # This line just prints the loss calcualted in each epoch, or full dataset cycle
            
            with open("nafizModel.pt", "wb") as f:              # This creates a PyTorch file that saves important information like losses and gradients
                save(trainer.state_dict(), f)                   # The model will directly record results using this function
            
        elif choice == 2:
            with open("nafizModel.pt", "rb") as f:              # open up the PyTorch file which contains training data
                trainer.load_state_dict(load(f))                # tell the model to load its contents
            
            # Let the user select any random image out of the 60000 available
            index = int(input("Enter the index of the image to predict (0-59999): ")) 
            image, label = trainingData[index]

            time.sleep(2)
            print(f"Label: {label}")                            # Take note of the actual label

            image = image.unsqueeze(0).to(device)               # Unsqueeze adds a dimension to the tensor (used for single inputs when the model expects a batch)

            # The no_grad method is used to make the model only evaluate and not update its learning parameters
            with torch.no_grad():
            # The argmax methods looks for which class has the highest probability of being true and returns that number as an output with the help of the item method
                prediction = torch.argmax(trainer(image)).item()

            time.sleep(2)
            print(f"Prediction: {prediction}")

            time.sleep(2)
            if label == prediction:
                print("The trained model delivered the correct answer.")
            else:
                print("The trained model did not deliver the correct answer.")    
        else:
            print("Invalid number, please try again.")
            time.sleep(2)