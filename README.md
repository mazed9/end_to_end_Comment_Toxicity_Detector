---
title: Comment Toxicity Detector
emoji: 📈
colorFrom: red
colorTo: pink
sdk: gradio
sdk_version: 4.31.5
app_file: app.py
pinned: false
license: mit
---
# Comment Toxicity Detector

This project implements a sentiment analysis  model that’s capable of detecting different types of toxicity like threats, obscenity, insults, and identity-based hate of a given comment. An LSTM-based model has been trained on 153 thousand sequence.

## Project Structure

- __01. Data Preparation:__
  * `Data Collection`: The [dataset](https://www.kaggle.com/datasets/julian3833/jigsaw-toxic-comment-classification-challenge) has been collected from the [Toxic Comment Classificatio Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) held on Kaggle.
  * `Data Cleaning & Preprocessing`: 
    - Vectorized the  data utilizing "TextVectorization" from keras
    - Prepared a tensorflow dataset for model training
  
- __02. Model Training:__
  * A Bidirectional LSTM model with an embedding layer has been trained on the preprocessed data.
  
- __03. App Deployment:__
  * Developed a web-app with Gradio interface
  * Deployed the [App](https://huggingface.co/spaces/mazed/Comment_Toxicity_Detector) in HuggingFace Spaces.

- `requirements.txt`: Contains the dependencies needed for the project:
  - `pandas`
  - `gradio`
  - `tensorflow==2.15.0`

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
