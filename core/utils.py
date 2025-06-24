import requests
import base64
from django.conf import settings
from django.core.files.base import ContentFile
from django.utils.text import slugify

API_KEY = "AIzaSyC0rt22hLfHN6iUCTVkIkYpfbnol5R67-0"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict?key={API_KEY}"

def generate_ai_image(prompt: str):

    if not prompt:
        return None
    
    if not API_KEY:
        print("AVISO: A chave de API do Google AI (GOOGLE_AI_API_KEY) não está configurada em settings.py.")
        return None

    payload = {
        "instances": [
            {"prompt": f"professional blog post header image, digital art, cinematic lighting, --ar 16:9, --no text, --no writing, {prompt}"}
        ],
        "parameters": {
            "sampleCount": 1
        }
    }

    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(API_URL, json=payload, timeout=45)
        response.raise_for_status()
        
        result = response.json()

        if "predictions" in result and result["predictions"]:
            image_b64 = result["predictions"][0]["bytesBase64Encoded"]
            image_bytes = base64.b64decode(image_b64)
            
            file_name = f"ai_generated_{slugify(prompt[:50])}.png"
            
            return ContentFile(image_bytes, name=file_name)
        else:
            print(f"ERRO: A resposta da API não continha uma imagem válida. Resposta: {result}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"ERRO: Falha na comunicação com a API de geração de imagem: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"ERRO: A estrutura da resposta da API mudou ou está inesperada: {e}")
        return None

def generate_prompt_from_content(content: str):
    if not content:
        return "tecnologia e dados em um ambiente corporativo"
    return ' '.join(content.split()[:15])

