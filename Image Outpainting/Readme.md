### **Description**

This project explores the use of deep generative models, specifically **Generative Adversarial Networks (GANs)**, to perform image outpainting. The goal is to extrapolate the content of an image beyond its original boundaries, a task that is more challenging than inpainting due to the lack of surrounding contextual pixels.

---
### **Project Goal**

The primary objective is to develop a robust neural network architecture that can accurately predict and generate realistic outward content for a given input image. The proposed model aims to improve upon existing methods by producing more consistent and higher-quality results, particularly at the image boundaries.

---
### **Proposed Architecture**

The model is a GAN-based system featuring two main components:

- **Generator**: This network is responsible for creating the outpainted image. It utilizes **dense blocks** to efficiently understand complex image features and a series of convolutional and deconvolutional layers to reconstruct the image. The use of dense blocks helps to enhance the quality of the generated output.

- **Discriminator**: This component is designed to distinguish between real and generated images. The model uses a **dual discriminator** approach, consisting of a **Global Discriminator** that analyzes the entire image and a **Local Discriminator** that focuses specifically on the boundary between the original and outpainted parts. This dual approach helps to eliminate low-quality, obviously fake hallucinations.

---

### **Software/Tools**

The following tools are required to run the project:

- **Keras**: A Python-based neural-network library for fast experimentation.
- **TensorFlow**: An open-source software library for machine learning applications.
- **PyTorch**: An open-source machine learning library primarily used for computer vision and natural language processing.
- **Google Colab**: A cloud-based Jupyter notebook environment providing free access to GPUs and TPUs.

---
### **Datasets**

The model was trained and evaluated on two datasets:

1. **Landscapes dataset**: Contains about 4300 images scraped from Flickr, presenting a challenge for the model due to the variety of content.
2. **Cat2dog dataset**: Includes 871 cat and 1364 dog images with dimensions of 178×218, which is a recognized benchmark for both inpainting and outpainting tasks.