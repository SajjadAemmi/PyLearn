# 7-7 Face Recognition
Face recognition using python

- Framework: TensorFlow2 and Keras
- Backbone net: MobileNetV2 
- Face detector: MTCNN

## Performance
| Model | train Accuracy | test Accuracy |
---|---|---|
| MobileNetV2 | 99.22% | 92.50% |

## PreTrain Model
If you do not wish to train the model, we also provide trained model. Pretrain model and trained model are put in
[Google Drive](https://drive.google.com/drive/folders/1otgK5wd7axsLtDjvB2JcZ8xQ9kKLXZrj?usp=sharing)

## Dataset
7-7 Faces dataset: 14 human (7 Males / 7 Females) with 1.2K labeled images.
Get dataset from [Google Drive](https://drive.google.com/drive/folders/1WGSotRtFPYGuxPEGkWWRsBPlVXFSvl7p?usp=sharing)

## Train
Run `Face_Recognition_Train.ipynb`

## Test
Evaluate the trained model using:
```
python inference_image.py --input input/obamas.jpg
python inference_video.py --input input/kim.mp4
```

![screen shot](output/result.jpg)
