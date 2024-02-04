from flask import Flask, render_template, request

import torch                                            
from PIL import Image                                   
from torch import nn, load, save                        
from torch.optim import Adam                            
from torch.utils.data import DataLoader                 
from torchvision import datasets                        
from torchvision.transforms import ToTensor             
import time                                             

webTrainer = Flask(__name__)

@webTrainer.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form['button'] == "Test":
            return render_template("test.html")
        elif request.form['button'] == "Train":
            return render_template("train.html")
    else:
        return render_template("home.html")

@webTrainer.route("/train")
def train():
    return render_template("train.html")

@webTrainer.route("/test")
def test():
    return render_template("test.html")
if __name__ == "__main__":
    webTrainer.run(debug=True)