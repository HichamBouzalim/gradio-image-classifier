# 🖼️ Image Classification with ResNet-18

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.13-red?logo=pytorch\&logoColor=white)](https://pytorch.org/)
[![Gradio](https://img.shields.io/badge/Gradio-3.0-orange?logo=gradio\&logoColor=white)](https://gradio.app/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🚀 Project Overview

This project is a **web-based image classification app** that uses a **pretrained ResNet-18 model** from PyTorch to identify objects in images. Users can upload an image and get the **top 3 predicted labels** with their probabilities.

The app is designed to be **simple, fast, and easy to use**.

---

## 🛠️ Features

* **Pretrained ResNet-18 Model** from PyTorch for accurate predictions.
* **Top 3 Predictions** with probabilities.
* **Gradio Web Interface** for a clean and interactive experience.
* **Supports Any Image** in common formats like JPEG, PNG.
* **Easy to Run Locally** or deploy on a server.

---

## 📦 Requirements

* Python 3.8 or higher
* PyTorch
* Torchvision
* Gradio
* Pillow
* Requests

Install dependencies with:

```bash
pip install torch torchvision gradio pillow requests
```

---

## ⚡ Usage

1. **Clone the repository**

```bash
git clone https://github.com/hichambouzalim/gradio-image-classifier.git
cd gradio-image-classifier
```

2. **Run the application**

```bash
python app.py
```

3. **Open the web interface** in your browser at:

```
http://0.0.0.0:7860
```

4. **Upload an image** and view the top 3 predicted labels.

---

## 🧩 How It Works

1. **Load Model**
   The ResNet-18 model is loaded from PyTorch Hub:

```python
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()
```

2. **Fetch ImageNet Labels**
   Class labels are downloaded from a public URL:

```python
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")
```

3. **Classify Image**
   The uploaded image is transformed to a tensor and passed through the model. Top 3 predictions are returned with probabilities.

---

## 🖼️ Example

Upload an image like this:

![Example](example_image.png)

Predictions returned might look like:

```json
{
  "Labrador_retriever": 0.85,
  "Golden_retriever": 0.10,
  "Flat-coated_retriever": 0.03
}
```

---

## 🖥️ Technology Stack

| Technology                                                                              | Purpose                            |
| --------------------------------------------------------------------------------------- | ---------------------------------- |
| ![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python\&logoColor=white)   | Core programming language          |
| ![PyTorch](https://img.shields.io/badge/PyTorch-1.13-red?logo=pytorch\&logoColor=white) | Deep learning framework            |
| ![Gradio](https://img.shields.io/badge/Gradio-3.0-orange?logo=gradio\&logoColor=white)  | Web interface for user interaction |
| ![Pillow](https://img.shields.io/badge/Pillow-9.0-yellow?logo=python\&logoColor=white)  | Image processing                   |
| ![Requests](https://img.shields.io/badge/Requests-2.31-lightgrey)                       | Fetch ImageNet labels              |

---

## 📜 License

This project is licensed under the **MIT License**.
See [LICENSE](LICENSE) for details.

---

## 👤 Author

**Hicham Bouzalim**

* GitHub: [hichambouzalim](https://github.com/hichambouzalim)
* Email: [bouzalimhicham11@gmail.com](mailto:bouzalimhicham11@gmail.com)

---

## 🔗 Live Demo (Optional)

You can run the app locally using Gradio or deploy it online for a live demo.
