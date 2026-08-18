import urllib.request
import hashlib
import json
import os
import yaml
from datetime import datetime

sources = {
    "ehman_30th": "http://www.bigear.org/Wow30th/wow30th.htm",
    "mendez_2024": "https://arxiv.org/pdf/2408.08513.pdf",
    "mendez_2025": "https://arxiv.org/pdf/2508.10657.pdf",
    "kipping_gray_2022": "https://arxiv.org/pdf/2206.08374.pdf",
    "sheikh_2021": "https://arxiv.org/pdf/2011.08976.pdf",
    "paris_davies_2017": "https://arxiv.org/pdf/1706.03259.pdf",
    "benford_2010b": "https://arxiv.org/pdf/0810.3964.pdf",
    "perez_2022": "https://iopscience.iop.org/article/10.3847/2515-5172/ac9408/pdf",
    "lingam_2023": "https://iopscience.iop.org/article/10.3847/1538-4357/acaca0/pdf",
    "sheikh_2020": "https://arxiv.org/pdf/1908.02683.pdf"
}

cache_dir = r"f:\Research_WoW!\data\sources_cache"
os.makedirs(cache_dir, exist_ok=True)
manifest_path = os.path.join(cache_dir, "sources_manifest.yaml")

manifest = {}
if os.path.exists(manifest_path):
    with open(manifest_path, "r") as f:
        manifest = yaml.safe_load(f) or {}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Research/1.0'}

for name, url in sources.items():
    ext = ".pdf" if url.endswith(".pdf") else ".htm"
    filepath = os.path.join(cache_dir, f"{name}{ext}")
    
    print(f"Downloading {name} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read()
        
        with open(filepath, "wb") as f:
            f.write(content)
            
        file_hash = hashlib.sha256(content).hexdigest()
        manifest[name] = {
            "url": url,
            "filename": f"{name}{ext}",
            "fetch_date": datetime.utcnow().isoformat() + "Z",
            "sha256": file_hash,
            "status": "CACHED"
        }
    except Exception as e:
        print(f"Failed {name}: {e}")
        manifest[name] = {
            "url": url,
            "status": f"FAILED: {str(e)}"
        }

with open(manifest_path, "w") as f:
    yaml.dump(manifest, f, default_flow_style=False)

print("Done. Manifest updated.")
