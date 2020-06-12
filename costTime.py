import os
import re
import cv2
import torch
import torch.nn as nn
from torchvision import transforms
import numpy as np
import argparse
from BagData import test_dataset
from torch.utils.data import DataLoader
import time

class MyTimer(object):       
    def __enter__(self):
        self.start = time.time()
        return self
        
    def __exit__(self, *unused):
        self.end = time.time()
        print("elapsed time: %f s" % (self.end-self.start))

test_dataloader = DataLoader(test_dataset, batch_size=8, shuffle=False, num_workers=8)

def test():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    segnet = torch.load("./checkpoints_attention/SegNet_2.pt")
    unet = torch.load("./checkpoints_unet/unet_11.pt")
    myModel = torch.load("./checkpoints_attention/SpoonNetspretral3_12.pt")
    myModel = myModel.to(device).float()
    myModel.eval()
    unet = unet.to(device).float()
    unet.eval()
    segnet = segnet.to(device).float()
    segnet.eval()

    for (names, bag, bag_msk, qa) in test_dataloader:
        bag = bag.to(device)
        with MyTimer():
            for i in range(1000):
                m_output = myModel(bag)
            torch.cuda.synchronize()
        with MyTimer():
            for i in range(1000):
                m_output = unet(bag)
            torch.cuda.synchronize()
        with MyTimer():
            for i in range(1000):
                m_output = segnet(bag)
            torch.cuda.synchronize()
        break



if __name__ == "__main__":
   test()
