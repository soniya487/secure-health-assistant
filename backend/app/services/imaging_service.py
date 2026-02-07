from PIL import Image
import io, torch, torchvision.transforms as T
from torchvision import models

# load small model (cpu-friendly) for demo
_model = None
_transform = T.Compose([T.Resize((224,224)), T.ToTensor(), T.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])])
try:
    _model = models.resnet18(pretrained=True)
    _model.eval()
except Exception as e:
    _model = None

def infer_image(image_bytes: bytes):
    if _model is None:
        return {"error":"model not available"}
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    x = _transform(img).unsqueeze(0)
    with torch.no_grad():
        out = _model(x)
        probs = torch.nn.functional.softmax(out, dim=1)
    topk = torch.topk(probs, k=3)
    return {"top_indices": topk.indices.tolist(), "top_values": topk.values.tolist()}
