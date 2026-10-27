import os
import sys
import urllib.request

def download_models():
    os.makedirs('models', exist_ok=True)
    
    best_model_path = 'models/EffNetB0_512_16.h5'
    best_model_url = 'https://github.com/Josh-robins/Cassava-Leaf-Disease-Classification/raw/refs/heads/main/model/EffNetB0_512_16.h5'
    
    if os.path.exists(best_model_path):
        print(f"Best Model already exists at '{best_model_path}' ({os.path.getsize(best_model_path)/1e6:.1f} MB)")
    else:
        print("Downloading Best Model (EffNetB0_512_16.h5) from GitHub repository...")
        try:
            urllib.request.urlretrieve(best_model_url, best_model_path)
            print(f"Best Model downloaded successfully ({os.path.getsize(best_model_path)/1e6:.1f} MB)!")
        except Exception as e:
            print(f"Could not download directly from GitHub URL: {e}")
            print("Downloading from Google Drive folder...")
            try:
                import gdown
                folder_url = "https://drive.google.com/drive/folders/1cf4gfic9o6tdzJcYa1N7S9y7AH79alZT"
                gdown.download_folder(folder_url, output="models", quiet=False)
            except ImportError:
                print("Install gdown to download from Google Drive: pip install gdown")

if __name__ == '__main__':
    download_models()
