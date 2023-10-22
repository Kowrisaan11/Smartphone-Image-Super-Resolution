import torch
from PIL import Image
import albumentations as A
from albumentations.pytorch import ToTensorV2

LOAD_MODEL = True   #set to True, for load pre-trained models during training.
SAVE_MODEL = True   #set to True, for save checkpoint files for both the generator and discriminator during training.

# These variables specify the filenames for saving and loading checkpoints for the generator and discriminator, respectively.
CHECKPOINT_GEN = "gen.pth"
CHECKPOINT_DISC = "disc.pth"

# This variable determines whether the code should use the CPU or GPU for computations. It checks for GPU availability and sets the device accordingly.
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

LEARNING_RATE = 1e-4    #The learning rate used for training the generator and discriminator.
NUM_EPOCHS = 10000
BATCH_SIZE = 16
LAMBDA_GP = 10
NUM_WORKERS = 4

# These variables specify the resolution for high-resolution and low-resolution images. 
# For example, HIGH_RES is set to 32, and LOW_RES is set to 8, indicating that high-resolution images have a size of 32x32 pixels, and low-resolution images are 8x8 pixels.
HIGH_RES = 32
LOW_RES = HIGH_RES // 4

IMG_CHANNELS = 3    # The number of image channels. In this case, it is set to 3 for RGB images.

highres_transform = A.Compose(
    [
        A.Normalize(mean=[0, 0, 0], std=[1, 1, 1]),
        ToTensorV2(),
    ]
)

lowres_transform = A.Compose(
    [
        A.Resize(width=LOW_RES, height=LOW_RES, interpolation=Image.BICUBIC),
        A.Normalize(mean=[0, 0, 0], std=[1, 1, 1]),
        ToTensorV2(),
    ]
)

both_transforms = A.Compose(
    [
        A.RandomCrop(width=HIGH_RES, height=HIGH_RES),
        A.HorizontalFlip(p=0.5),
        A.RandomRotate90(p=0.5),
    ]
)

test_transform = A.Compose(
    [
        A.Normalize(mean=[0, 0, 0], std=[1, 1, 1]),
        ToTensorV2(),
    ]
)
