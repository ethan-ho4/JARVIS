import requests
import base64

url = "http://127.0.0.1:7860/sdapi/v1/img2img"


with open(r'fishy.jpg', 'rb') as image_file:
    init_image_content = base64.b64encode(image_file.read()).decode('utf-8')


payload = {
    "prompt": "A captivating 3D render of an anime-style betta fish, emanating an aura of regal magnificence. The betta delicately holds a tiny, radiant orb symbolizing the world within its fins. The body is a breathtaking combination of deep blue and golden hues, with a subtle shimmer that captures the light. Surrounding the betta is an otherworldly cosmic backdrop of swirling stars and galaxies, emphasizing its essential role in preserving the world. This enchanting illustration masterfully blends fantasy and anime elements, creating an ethereal and spellbinding ambiance.",
    "negative_prompt": "",
    "steps": 12,
    "width": 512,
    "height": 512,
    "init_images": [init_image_content],
    "override_settings": {
       "sd_model_checkpoint": "dreamshaperXL_v21TurboDPMSDE"
    },
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    r = response.json()
    

    for idx, img_b64 in enumerate(r['images']):
        with open(f"img_to_img_output{idx}.png", 'wb') as f:
            f.write(base64.b64decode(img_b64))
        print(f"Image {idx} saved successfully.")
else:
    print("Failed to generate images:", response.status_code, response.text)
