# Smartphone-Image-Super-Resolution

Here, we used the Super Resolution Generative Adversarial Network (SRGAN).

To train our model using the train.py file, follow these steps:
1) Ensure you have the necessary Python libraries installed
   pip install torch torchvision tensorboard tqdm
2) Configure config.py as follows
   LOAD_MODEL = False
   SAVE_MODEL = True
3) Configure train.py as follows
   At 139th line, set as try_model = False
4) In the terminal,
   Type as python train.py 
