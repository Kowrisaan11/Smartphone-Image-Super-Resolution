# Smartphone-Image-Super-Resolution

Here, we used the Super Resolution Generative Adversarial Network (SRGAN).

## To train our model using the train.py file, follow these steps:

1. **Ensure you have the necessary Python libraries installed:**

   ```bash
   pip install torch torchvision tensorboard tqdm
   ```

2. **Configure **``** as follows:**

   ```python
   LOAD_MODEL = False
   SAVE_MODEL = True
   ```

3. **Configure **``** as follows:**

   - At line 139, set:
     ```python
     try_model = False
     ```

4. **In the terminal, type the following command:**

   ```bash
   python train.py
   ```

