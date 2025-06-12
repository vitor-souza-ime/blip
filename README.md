# 📷 Caption Generation with BLIP (Bootstrapped Language Image Pretraining)

This project uses the **BLIP (Bootstrapped Language Image Pretraining)** model by Salesforce to automatically generate captions for images provided via URLs. The model is based on a Transformer architecture and is designed for vision-language understanding tasks.

## ✨ Features

* Automatically generates descriptive captions for images.
* Supports multiple image URLs.
* Handles download or processing errors gracefully.

## 🧰 Technologies & Libraries Used

* [Python 3.8+](https://www.python.org/)
* [PyTorch](https://pytorch.org/)
* [Transformers (HuggingFace)](https://huggingface.co/docs/transformers/)
* [BLIP - Salesforce](https://huggingface.co/Salesforce/blip-image-captioning-base)
* [Pillow (PIL)](https://python-pillow.org/)
* [Requests](https://pypi.org/project/requests/)

## 📦 Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/blip-caption-generator.git
cd blip-caption-generator
pip install torch transformers pillow requests
```

## 🚀 How to Use

Run the main script to generate captions for a list of images:

```bash
python generate_captions.py
```

The script will:

1. Download images from the specified URLs.
2. Use the BLIP model to generate a caption for each image.
3. Print the generated caption to the terminal.

### 📝 Example Output

```
[Image 1] Generated caption: a multimeter with a digital screen and multiple buttons

[Image 2] Generated caption: an electrical control panel with wires and components

[Image 3] Generated caption: a piece of industrial machinery

...
```

## 🛠️ Project Structure

```
blip-caption-generator/
│
├── generate_captions.py     # Main script
├── README.md                # This file
```

## ⚠️ Notes

* Make sure all URLs are valid and accessible.
* Some URLs may fail to load properly, especially if they are thumbnails or involve HTTPS redirection.

## 📄 License

This project uses public models and is licensed under the [MIT License](LICENSE).

---

