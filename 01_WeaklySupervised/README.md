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


