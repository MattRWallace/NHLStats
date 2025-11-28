import sys

import typer

from databuilder.data_builder import DataBuilder
from train.linear_regression import Trainer
from predictor.linear_regression import Predictor

app = typer.Typer()

@app.command()
def build():
    DataBuilder.build()

@app.command()
def train():
    Trainer.train()

@app.command()
def predict():
    Predictor.predict()

if __name__ == "__main__":
    app()