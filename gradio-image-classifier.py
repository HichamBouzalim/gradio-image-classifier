# --- Import libraries ---
import gradio as gr  # For creating the web interface
import torch
import requests
from PIL import Image
from torchvision import transforms

# --- Load pretrained ResNet-18 model ---
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()

# --- Load ImageNet class labels ---
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

# --- Function to predict image class ---
def classify_image(image):
    """
    Takes a PIL Image and returns top 3 predicted class labels with probabilities.
    """
    try:
        # Convert image to tensor and add batch dimension
        inp = transforms.ToTensor()(image).unsqueeze(0)
        
        # Get predictions
        with torch.no_grad():
            prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
        
        # Map labels to probabilities
        confidences = {labels[i]: float(prediction[i]) for i in range(1000)}
        
        # Sort and return top 3
        top3 = dict(sorted(confidences.items(), key=lambda item: item[1], reverse=True)[:3])
        return top3
    except Exception as e:
        return {"Error": str(e)}

# --- Create Gradio interface ---
iface = gr.Interface(
    fn=classify_image,             # Function to call when an image is uploaded
    inputs=gr.Image(type="pil"),   # Input is a PIL Image
    outputs=gr.Label(num_top_classes=3),  # Output shows top 3 labels
    title="Image Classification with ResNet-18",
    description="Upload an image to classify it using a pretrained ResNet-18 model."
)

# --- Launch Gradio app ---
iface.launch(server_name="127.0.0.1", server_port= 7860)
