# Smartphone-Image-Super-Resolution

Here, we developed a Super Resolution Generative Adversarial Network (SRGAN) to enhance the quality of Smartphone Images. While using our model for the first time, training should be done.

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

