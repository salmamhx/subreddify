import io
import re
import string
import tqdm

import numpy as np

import tensorflow as tf
from tensorflow.keras import layers

%load_ext tensorboard

SEED = 42
AUTOTUNE = tf.data.AUTOTUNE