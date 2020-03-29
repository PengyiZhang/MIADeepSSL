# Weakly supervised deep learning 

We build two demos. One is weakly supervised object localization based on CAM and Grad-CAM introduced in [00_Interpretability](../00_Interpretability). The other one is weakly supervised semantic segmentation.


## Weakly supervised object localization
CAMs generate heatmaps highlighting class-specific discriminative regions. Heatmaps are good for qualitative analysis of the approach. However, for the evaluation of the localization results, well defined region proposals are required. To achieve this, heatmaps (CAMs) are first normalized between 0 and 1, assigning each pixel a value according to its intensity. The high intensity regions are then selected using binary segmentation, giving us the predicted regions as shown below. ([Weakly-supervised localization of diabetic retinopathy lesions in retinal fundus images](https://arxiv.org/abs/1706.09634))


1. CAM built on the output of 4-st dense block

![img](./images/image2_cam.png)
![img](./images/image2_cam_p.png)

2. Grad-CAM built on the output of 4-st dense block

![img](./images/image2_grad_cam3.png)
![img](./images/image2_grad_cam3_p.png)


## Weakly supervised semantic segmentation

A representive framework for weakly supervised semantic segmentation:

![img](./images/Figure_framework.png)

Besides, prior knowledge, such as target's size, shape, can be very useful for training deep models especially when facing weakly supervised situation. 

Here, we show how to embed prior knowledge into the training of deep models on weak labels and achieve similar segmentation results with those trained with fully supervision. The demo is based on [Constrained-CNN losses for weakly supervised segmentation](https://arxiv.org/abs/1805.04628).


### Methods

We build the demo of weakly supervised semantic segmentation on two methods：

- [] method 1: representive framework: pre-processing (region growing / K-means clustering) + ENet + post-processin (DenseCRF / Graph Search)

- [] method 2: [Size Constrained-CNN](https://arxiv.org/abs/1805.04628): size constrained loss + ENet


### Dataset
We used the training set from the publicly available data of [the 2017 ACDC Challenge](https://www.creatis.insa-lyon.fr/Challenge/acdc/) . This set consists of 100 cine magneticresonance (MR) exams covering well defined pathologies:  dilated cardiomyopathy, hypertrophiccardiomyopathy, myocardial infarction with altered left ventricular ejection fraction and abnormalright ventricle.  It also included normal subjects.  The exams were acquired in breath-hold with aretrospective or prospective gating and a SSFP sequence in 2-chambers, 4-chambers and in short-axisorientations. A series of short-axis slices cover the LV from the base to the apex, with a thickness of 5 to 8 mm and an inter-slice gap of 5 mm. The spatial resolution goes from 0.83 to 1.75 mm2/pixel. For all the experiments, we employed the same 75 exams for training and the remaining 25 forvalidation. To increase the variability of the data, we augmented the dataset by randomly rotating, flipping, mirroring and scaling the images. 

### Results

#### 1. Weak labels

![img](./images/Figure_fs.png)

(a) Full supervision: gt

----


![img](./images/Figure_ep.png)

(b) weak supervision 1： erosion operation on gt

----

![img](./images/Figure_rand.png)

(c) weak supervision 2： random point supervision 

----

![img](./images/Figure_centroid.png)

(d) weak supervision 3： centroid point supervision 

----

![img](./images/Figure_box.png)

(e) weak supervision 4： box supervision


------
