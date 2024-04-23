import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
import torchvision
import prettytable
import sys

def versions():
    table = prettytable.PrettyTable()
    table.field_names = ["Component", "Version"]
    table.add_row(["Python", sys.version.split(' ')[0]])
    table.add_row(["pytorch", torch.__version__])
    table.add_row(["torchvision", torchvision.__version__])
    table.hrules = prettytable.ALL
    print(table)
