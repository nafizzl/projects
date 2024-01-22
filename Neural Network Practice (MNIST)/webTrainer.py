from flask import Flask, render_template

import torch                                            
from PIL import Image                                   
from torch import nn, load, save                        
from torch.optim import Adam                            
from torch.utils.data import DataLoader                 
from torchvision import datasets                        
from torchvision.transforms import ToTensor             
import time                                             

webTrainer = Flask(__name__)

@webTrainer.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    webTrainer.run(debug=True)