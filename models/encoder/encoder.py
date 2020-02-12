import tensorflow as tf
from tensorflow.keras.layers import (
    Dense, LayerNormalization, Dropout, Layer
)
from models.encoder.encoder_layer import EncoderLayer
from models.pos_encoding.pos_encoding import PosEncoding

class Encoder(Layer):

  def __init__(self):
    super(Encoder, self).__init__(ff_dim, d_model, dk, dv, heads, encoder_dim)
    
    self.posEncoding = PosEncoding()

    self.embedding = Embedding()

    self.encoder_stack = []
    for i in range(encoder_dim):
      self.encoder_stack.apped(EncoderLayer(ff_dim, d_model, dk, dv, heads))

    self.dropout1 = Dropout()

  def call(self, x, training=False):
    input_embedding = self.embedding(x)
    pos_embedding = self.posEncoding(input_embedding)

    encoding = dropout1(pos_embedding)

    for encoder_layer in self.encoder_stack:
      encoding = encoder_layer(encoding)

    return encoding 
