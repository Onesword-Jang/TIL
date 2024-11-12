# 5-5 fastapi.vision
# pip install fastai

from fastapi.vision.all import *

path = untar_data(URLs.PETS)
path_imgs = path/'images'

def is_cat(x): return x[0].isupper()

dls = ImageDataLoaders.from_name_func(
    path_imgs, get_image_files(path_imgs), valid_pct=0.2, seed=42,
    label_func=is_cat, item_tfms=Resize(224)
)

dls.show_batch(max_n=9, figsize=(7, 6))

learn = cnn_learner(dls, resnet34, metrics=error_rate)

learn.lr_find()

learn.find_tune(3)

learn.show_results()

interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()