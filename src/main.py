import sys

import typer

from databuilder.data_builder import DataBuilder
from train.linear_regression import LinearRegression as tlr
from predictor.linear_regression import LinearRegression as plr

app = typer.Typer()

@app.command()
def build():
    DataBuilder.build()

@app.command()
def train():
    tlr.train()

@app.command()
def predict():
    plr.predict()

if __name__ == "__main__":
    app()