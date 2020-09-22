IMAGE_FORMAT = "channels_last"
BACKBONE = 'vgg16'
BATCH_SIZE = 1
LR = 0.00001
EPOCHS = 100
OPTIMIZER = "adam"
INPUT_SHAPE = (360, 480, 3) #(h,w,3) 
NUM_CLASSES = 6
LABEL_PATH = "F:\TF2-Semantic-Segmentation\dataset\labels.csv"
CKP_PATH = "F:\TF2-Semantic-Segmentation\checkpoint"