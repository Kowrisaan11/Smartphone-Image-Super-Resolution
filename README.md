# Smartphone-Image-Super-Resolution

Here, we developed an ESRGAN (Enhanced Super-Resolution Generative Adversarial Network) to enhance the quality of Smartphone Images. While using our model for the first time, training should be done.

**Ensure that necessary Python libraries are installed:**

   ```bash
   pip install torch torchvision tensorboard tqdm
   ```

## To train our model using the train.py file, follow these steps:
1. **Configure **config.py** as follows:**

   ```python
   LOAD_MODEL = False
   SAVE_MODEL = True
   ```

2. **Configure **train.py** as follows:**

   - At line 139, set:
     ```python
     try_model = False
     ```

3. **In the terminal, type the following command:**

   ```bash
   python train.py
   ```
After the training, gen.pth & disc.pth files will be generated.

## To test our model using the train.py file, follow these steps:
1) **Configure **config.py** as follows:**

   ```python
   LOAD_MODEL = True
   SAVE_MODEL = False
   ```
   
2) **Configure **train.py** as follows:**

   - At line 139, set:
     ```python
     try_model = True
     ```
     
3. **In the terminal, type the following command:**

   ```bash
   python train.py
   ```

