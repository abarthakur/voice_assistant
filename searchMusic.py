# The aim of this file is to search a music file by name and play it randomly
import os
import subprocess

sample_input=raw_input("Enter the command : ")
sample_input=sample_input.lower()
gutter=["play ","music ","song ","listen ","hear "];
for gt in gutter:
	sample_input=sample_input.replace(gt,'');
print sample_input;