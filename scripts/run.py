import os

compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

run = './bin/tp1 0 input/test-prob-1.in output/outttt'
os.system(run)
