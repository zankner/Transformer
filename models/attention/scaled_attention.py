import tensorflow as tf

def scaled_attention(queries, keys, values, mask):
  attention_logits = tf.matmul(queries, keys, transpose_b=True)
  dk = tf.math.sqrt(tf.cast(tf.shape(keys)[-1], tf.float32))
  scaled_attention_logits = attention_logits / dk
  if mask is not None:
    scaled_attention_logits += (mask * -1e9)
  normalized_attention = tf.nn.softmax(scaled_attention_logits)
  scaled_values = tf.matmul(normalized_attention, values)
  return scaled_values
