# Aewsome Medical Images

## 1. Modalities

### MR

#### [Transversal T2-weighted MR image of the prostate](https://promise12.grand-challenge.org/Details/)


There are 50 training cases available for download. These cases include a transversal T2-weighted MR image of the prostate. The training set is a representative set of the types of MR images acquired in a clinical setting. The data is multi-center and multi-vendor and has different acquistion protocols (e.g. differences in slice thickness, with/without endorectal coil). The set is selected such that there is a spread in prostate sizes and appearance. For each of the cases in the training set, a reference segmentation is also included.

Each downloaded file contains MR scans, stored in Meta (or MHD/RAW) format. This format stores an image as an ASCII readable header file with extension .mhd and a separate binary file for the image data with extension .raw. This format is ITK compatible. Documentation is available here. Applications that can read the data are MeVisLab, SNAP, Slicer or ParaView. If you want to write your own code to read the data, note that in the header file you can find the dimensions of the scan and the voxel spacing. In the raw file the values for each voxel are stored consecutively with index running first over x, then y, then z. The voxel-to-world matrix is also available in this header file.

The voxel type for T2-weighted images is SHORT (16 bit signed). The voxel type for the reference standard image is CHAR (8 bit signed). The reference standard image only contains the values 1 for prostate and 0 for background.


![img](./images/prostate.png)


#### [ACDC dataset](https://acdc.creatis.insa-lyon.fr/description/databases.html)

This set consists of 100 cine magneticresonance (MR) exams covering well defined pathologies:  dilated cardiomyopathy, hypertrophiccardiomyopathy, myocardial infarction with altered left ventricular ejection fraction and abnormalright ventricle.  It also included normal subjects.  The exams were acquired in breath-hold with aretrospective or prospective gating and a SSFP sequence in 2-chambers, 4-chambers and in short-axisorientations. A series of short-axis slices cover the LV from the base to the apex, with a thickness of5 to 8 mm and an inter-slice gap of 5 mm. The spatial resolution goes from 0.83 to 1.75 mm2/pixel

![img](./images/acdc-mr0.png)


### x-rays

#### [MURA](https://stanfordmlgroup.github.io/competitions/mura/)

![](images/mura.png)

#### [ChestX-ray8](http://openaccess.thecvf.com/content_cvpr_2017/papers/Wang_ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.pdf)

![](images/chestxray8.png)

### CT scans

#### [KITS](https://kits19.grand-challenge.org)

![](images/KITS2019.jpg)

![](images/KITS2019-3d.png)

### Endoscope/Dermatoscope

#### [EAD2019](https://ead2019.grand-challenge.org/)
![](images/EAD2019.jpg)

#### [ISIC2019](https://challenge2019.isic-archive.com/)
![](images/ISIC2019.jpg)




### 


## 2. [Medical Image File Formats](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3948928/)

Image file format is often a confusing aspect for someone wishing to process medical images.

### Basic concepts: pixel depth, photometric interpretation, metadata, and pixel data

What the numerical value of the pixel expresses depends on the imaging modality, the acquisition protocol, the reconstruction, and eventually, the post-processing.

#### pixel depth: the number of bits used to encode the information of each pixel

16bit: 0 to 65535
16bit: −32,768 to 32,767

Image data may also be real numbers: single precision 32-bit and the double precision 64-bit


#### photometric interpretation: specifies how the pixel data should be interpreted for the correct image display as a monochrome or color image

- samples per pixel or number of channels to determine monochrome or color 

- Clinical radiological images, like x-ray computed tomography (CT) and magnetic resonance (MR) images have a gray scale photometric interpretation.

- Nuclear medicine images, like positron emission tomography (PET) and single photo emission tomography (SPECT), are typically displayed with a color map or color palette. In this case, each pixel of the image is associated with a color in a predefined color map (only used for visualization). also single channel. (pseudo-color).

- Ultrasound images are typically stored employing R-G-B color model, 24-bits pixel depth, true color.

- Doppler ultrasound, use color to encode blood flow direction (and velocity) to show additional functional information onto a gray scale anatomical image as colored overlays, as in the case of fMRI activation sites, to simultaneously display functional and anatomical images as in the PET/CT or PET/MRI, and sometimes in place of gray tones to highlight signal differences.

#### Metadata: information that describe the images

In any file format, there is always information associated with the image beyond the pixel data, called as metadata, typically stored at the beginning of the file as a header and contains at least the image matrix dimensions, the spatial resolution, the pixel depth, and the photometric interpretation. The software uses it to recognize and correctly open an image in a supported file format.

In the case of medical images, images coming from diagnostic modalities typically have information about how the image was produced. MRI: parameters related to the pulse sequence used, timing information, flip angle, number of acquisitions. PET: have information about radiopharmaceutical injected and the weight of the patient. These data allows software to on-the-fly covert pixel values in standardized uptake values (SUV). 

Post-processing file formats have a terser metadata section that essentially describes the pixel data. 


#### Pixel data: 

![](images/medicalimagefileformat.png)

- radiological images like CT and MR and also modern nuclear medicine modalities, like PET and SPECT, store 16 bits for each pixel as integers.
- float data type is frequent in any post-processing pipeline
- may also be of complex type even if this data type is not common and can be bypassed by storing the real and imaginary parts as separate images: MRI store acquired data before the reconstruction (the so called k-space) or after the reconstruction if you choose to save both magnitude and phase image.
- little endian or big endian
- may also be compressed to reduce requirements for storage and transmission, lossless (reversible) or lossy (irreversible). In medical image, lossy tech 's usage is controversial, because it is not clear under which conditions the reading of the images and/or the quantitative post-processing procedures are not influenced by information loss.


### File formats

- intended to standardize the images generated by diagnostic modalities, e.g, Dicom.
- facilitate and strengthen post-processing analysis, e.g, Analyze, Nifti and Minc.


- a single file contains both metadata and image data, with the metadata stored at the beginning of the file: Dicom, Minc, and Nifti file formats.
- stores the metadata in one file and the image data in a second one: Analyze file format: .hdr and .img / Metaimage: .mhd and .raw


#### Analyze

old but widespread：

.hdr (metadata, 348 bytes, is described as a structure in the C programming language) and .img

#### Neuroimaging Informatics Technology Initiative (Nifti)
- Compared with Analyze： Image orientation with the intend to avoid the left-right ambiguity in brain study. support unsigned 16bit: .nii, 352 bytes header.
- a double way to store the orientation of the image volume in the space. rotation + translation to be used to map voxel coordinates to the scanner frame of reference, encoded using a matrix. affine. spatial normalization task is common in brain functional image analysis.

- Nifti-2: dimension of an image matrix supports a 64-bit integer instead of a 16-bit as in the Nifti-1 to manage larger data set. header: 544 bytes.



#### Digital Imaging and Communications in Medicine (Dicom)

Dicom standard is the backbone of every medical imaging department, is not only a file format but also a network communication protocol.

the header contains the most complete description of the entire procedure used to generate the image ever conceived in terms of acquisition protocol and scanning parameters. also patient information such as name, gender, age, weight, and height. The Dicom header is modality-dependent and varies in size.

Dicom can only store pixel values as integers. supports compressed image data through a mechanism that allow a non-Dicom-formatted document to be encapsulated in a Dicom: JPEG, run-lenght encoding (RLE), JPEG-LS, JPEG-2000, MPEG2/MPEG4 and Deflated. JPEG-XR.



Find more -> [https://itk.org/Wiki/ITK/File_Formats](https://itk.org/Wiki/ITK/File_Formats)