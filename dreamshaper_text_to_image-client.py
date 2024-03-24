import requests
import base64

url = "http://127.0.0.1:7860"

payload = {
    "prompt": "A captivating 3D render of an anime-style betta fish, emanating an aura of regal magnificence. The betta delicately holds a tiny, radiant orb symbolizing the world within its fins. The body is a breathtaking combination of deep blue and golden hues, with a subtle shimmer that captures the light. Surrounding the betta is an otherworldly cosmic backdrop of swirling stars and galaxies, emphasizing its essential role in preserving the world. This enchanting illustration masterfully blends fantasy and anime elements, creating an ethereal and spellbinding ambiance., anime, 3d render",
    "negative_prompt": "",
    "steps": 10, #about 1 min per step for cpu
    "width": 512,
    "height": 512,
    "override_settings": {
        "sd_model_checkpoint": "dreamshaperXL_v21TurboDPMSDE"
    }
}

response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
r = response.json()

with open("text_to_img_output.png", 'wb') as f:
    f.write(base64.b64decode(r['images'][0]))
