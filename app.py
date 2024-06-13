import gradio as gr
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

df = pd.read_csv('train.csv')

X=df['comment_text']

vectorizer = TextVectorization(max_tokens=250000,
                               output_sequence_length=300,
                               output_mode='int')
vectorizer.adapt(X)

#load the model
model = tf.keras.models.load_model('CT_epoch_3.h5')


def score_comment(comment):
    # Vectorize the input comment
    vectorized_comment = vectorizer([comment])
    # Predict using the loaded model
    results = model.predict(vectorized_comment)
    
    # Generate the output text based on predictions
    text = ''
    for idx, col in enumerate(df.columns[2:]):  # Adjust the range if necessary
        text += '{}: {}\n'.format(col, results[0][idx] > 0.5)
    
    return text

interface = gr.Interface(
    fn=score_comment,
    inputs=gr.Textbox(lines=2, placeholder='Comment to score'),
    outputs='text'
)

interface.launch()