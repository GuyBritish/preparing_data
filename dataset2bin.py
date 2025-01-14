import mxnet as mx
from mxnet import ndarray as nd
import argparse
import pickle
import sys
import os
import joblib

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'eval'))
import lfw

parser = argparse.ArgumentParser(description='Package LFW images')
# general
parser.add_argument('--pairs-dir', default='', help='')
parser.add_argument('--image-size', type=str, default='112,112', help='')
parser.add_argument('--output', default='', help='path to save.')
parser.add_argument('--data-dir', default='', help='path to data')
args = parser.parse_args()
lfw_dir = args.data_dir
lfwpairs_dir = args.pairs_dir
image_size = [int(x) for x in args.image_size.split(',')]
lfw_pairs = lfw.read_pairs(os.path.join(lfwpairs_dir, 'pairs.txt'))
lfw_paths, issame_list = lfw.get_paths(lfw_dir, lfw_pairs) # or jpg
lfw_bins = []
#lfw_data = nd.empty((len(lfw_paths), 3, image_size[0], image_size[1]))
i = 0

for path in lfw_paths:
  with open(path, 'rb') as fin:
    _bin = fin.read()
    lfw_bins.append(_bin)
    #img = mx.image.imdecode(_bin)
    #img = nd.transpose(img, axes=(2, 0, 1))
    #lfw_data[i][:] = img
    i+=1
    if i%1000==0:
      print('loading dataset', i)
with open(args.output, 'ab') as f:
  joblib.dump((lfw_bins, issame_list), f)
#with open(args.output, 'wb') as f:
#  pickle.dump((lfw_bins, issame_list), f, protocol=pickle.HIGHEST_PROTOCOL)
