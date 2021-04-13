Here's my adaptation of this repo for FRC. 

## Training:

First, get wpilib's data from here: https://app.supervise.ly/share-links/zU1hctCmBs4rkglGXRzsmh5GbeAeqQ50ZUsGxtI9JNNR2SSbTnbMHvOiyeUgYw10. You'll need to create an account. Find the "Images tagged as Valid" dataset, click the three dots in the lower right corner, and choose Download As > .json + images. Create an account at roboflow.com, and click "Create New Dataset." Give the dataset a name, make sure the Dataset Type is "Object Detection (Bounding Box)," and for the Annotation Group, just type "Powercell," (or whatever else you want to detect.) Click "Select Floder," and choose the Images Tagged as Valid dataset folder from supervisely. It should upload all of the images with annotations, but if it doesn't, adding annotations is easy enough. Once the RoboFlow dataset is all set up, follow the instructions on this blog: https://blog.roboflow.com/how-to-train-scaled-yolov4/. For best results with a Jetson Nano, augment the data with RoboFlow, and change the --img paramater to about 128, and the epochs to over 200. 

## Inference

Acquire an Nvida Jetson Nano with the latest ubuntu image. You'll need to install torch, torchvision, pynetworktables, and mish cuda as well as its dependencies. Clone this repo somewhere that is easily accessable. Add your trained model somewhere in the repo. Plug the Jetson into RCU via ethernet, and connect power. Plug a USB camera into a USB port on the Jetson. On the jetson, run the following command: 
```
cd ScaledYOLOv4-FRC
python3 detect_frc.py --source 0 --weights path/to/model.pt --img-size 128 --conf 0.6 --save-txt 
```
You can do this with a script that runs on startup, or just SSH into the Jetson and run it every time.

## On the robot

The coordinates of the bounding box that is closest to the bottom-center of the screen is sent through NetworkTables in the table "vision." You can change that in utils/send.py. The coordinates are sent in a normalized xywh format, like this:

![image](https://user-images.githubusercontent.com/72103122/114620798-cae91b00-9c60-11eb-9019-2823c93877ba.png)

The entries are labled as such:

Entry name|Type|Value
---|---|---
bv|bool|Whether or not there is a valid bounding box
bx|float|X position of the center of the bounding box, from 0 to 1
by|float|Y position of the center of the bounding box, from 0 to 1
bw|float|Width of the bounding box, from 0 to 1
bh|float|Height of the bounding box, from 0 to 1
bc|int|Class of nearest bounding box

## Citation

```
@article{wang2020scaled,
  title={{Scaled-YOLOv4}: Scaling Cross Stage Partial Network},
  author={Wang, Chien-Yao and Bochkovskiy, Alexey and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2011.08036},
  year={2020}
}
```
