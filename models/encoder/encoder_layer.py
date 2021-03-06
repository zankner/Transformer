import tensorflow as tf
from tensorflow.keras.layers import (
  Dense, LayerNormalization, Dropout, Layer
)
from models.attention.multi_head_attention import MultiHeadAttention

class EncoderLayer(Layer):
  def __init__(self, ff_dim, d_model, dk, dv, heads):
    super(EncoderLayer, self).__init__()
    
    self.multiHeadAttention = MultiHeadAttention(d_model, dk, dv, heads)

    self.ff = Dense(ff_dim)
    self.o = Dense(d_model)

    self.layernorm1 = LayerNormalization()
    self.layernorm2 = LayerNormalization()

    self.dropout1 = Dropout(.1)
    self.dropout2 = Dropout(.1)


  def call(self, x, mask, training=False):
    attention = self.multiHeadAttention(x, x, x, mask)
    attention = self.dropout1(attention, training=training)
    res_norm_attention = self.layernorm1(x + attention)

    ff_h = self.ff(res_norm_attention)
    ff_o = self.o(ff_h)
    ff_o = self.dropout2(ff_o)
    res_norm_ff = self.layernorm2(res_norm_attention + ff_o)
    return res_norm_ff 
