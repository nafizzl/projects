from flask import Flask, render_template, request, redirect, url_for

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
            return redirect(url_for("test"))
        elif request.form['button'] == "Train":
            return redirect(url_for("train"))
    else:
        return render_template("home.html")

@webTrainer.route("/train", methods=["GET", "POST"])
def train():
    if request.method == "POST":
        if request.form['button'] == "Test":
            return redirect(url_for("test"))
        elif request.form['button'] == "Home":
            print("home")
            return redirect(url_for("home"))
    else:
        return render_template("train.html")
    
@webTrainer.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        if request.form['button'] == "Train":
            return redirect(url_for("train"))
        elif request.form['button'] == "Home":
            return redirect(url_for("home"))
    else:
        return render_template("test.html")

if __name__ == "__main__":
    webTrainer.run(debug=True)