# uft-8
import torch
from densenet import densenet169
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import cv2


def default_loader(path):
    image = Image.open(path).convert('RGB')
    image = np.array(image)
    img_height, img_width, channels = image.shape
    square_len = max(img_height, img_width)
    if channels > 1:
        image = np.pad(image, \
            (((square_len-img_height)//2, square_len-img_height-(square_len-img_height)//2), \
            (((square_len-img_width)//2, square_len-img_width-(square_len-img_width)//2)), \
            (0,0)), 'reflect')
    else:
        image = np.pad(image, \
            (((square_len-img_height)//2, square_len-img_height-(square_len-img_height)//2), \
            (((square_len-img_width)//2, square_len-img_width-(square_len-img_width)//2))), 'reflect')
    image = Image.fromarray(image).convert('RGB') # Ensure it is square
    return image

def show_cam_on_image(img, mask, save_dir="cam.png"):
    
    mask = mask - np.min(mask)
    mask = mask / np.max(mask)

    mask = cv2.resize(mask, (img.shape[1],img.shape[0]))
    heatmap = cv2.applyColorMap(np.uint8(255*mask), cv2.COLORMAP_JET)
    heatmap = np.float32(heatmap) / 255
    cam = heatmap + np.float32(img)
    cam = cam / np.max(cam)
    cv2.imwrite(save_dir, np.uint8(255 * cam))

if __name__ == "__main__":
    img_dir = "image2.png"
    input_shapes=(3,320,320)
    model = densenet169(input_shapes=input_shapes, num_classes=1)

    model.load_state_dict(torch.load('model.pth', map_location='cpu'))
    model.cuda()
    model.eval()

    _transform = transforms.Compose([
            transforms.Resize((320,320)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
    
    img = default_loader(img_dir)
    img = _transform(img).unsqueeze(0).cuda()
    cls_score, cam, grad_cams = model(img)
    print(cls_score)

    img = cv2.imread(img_dir, 1)
    

    cam = cam.cpu().squeeze().data.numpy()
    grad_cams = [grad_cam.cpu().squeeze().data.numpy() for grad_cam in grad_cams]

    img = np.float32(img) / 255
    show_cam_on_image(img, cam, save_dir=img_dir.split(".")[0]+"_cam.png")
    for i, grad_cam in enumerate(grad_cams):
        show_cam_on_image(img, grad_cam, save_dir=img_dir.split(".")[0]+"_grad_cam{}.png".format(i))

