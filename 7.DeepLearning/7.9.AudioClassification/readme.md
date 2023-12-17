# Audio Classification

Audio classification is a fundamental problem in the field of audio processing. It is a challenging problem because there is no clear definition of what is a good representation of audio data. In this project, we will use a custom dataset to classify audio files into 29 classes.

## Installation

Run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

## Dataset

The dataset used in this project is a custom dataset. It contains 29 classes of audio files.

1. Download the dataset from [Google Drive](https://drive.google.com/drive/folders/12cXlHAgKRfUzfGp0Z2268AFRZ_ESV2j1?usp=sharing).

2. Extract it in the `./raw_audios` directory.

3. Use `make_dataset.ipynb` notebook to convert the data into a dataset with format that can be used by the model.

## Training

Use `train_tensorflow.ipynb` notebook to train the model.
