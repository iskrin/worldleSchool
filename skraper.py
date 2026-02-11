import os
import requests

def downloadImages():
    targetFolder = "kraje"
    baseUrl = "https://worldplacestour.com/sites/worldplacestour/files/cshapes/"
    
    # Dodajemy nagłówek, który udaje przeglądarkę Chrome
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)
    
    print("Starting download with custom headers...")

    for i in range(253):
        fileName = f"{i}.png"
        savePath = os.path.join(targetFolder, fileName)
        fullUrl = f"{baseUrl}{fileName}"
        
        try:
            # Przekazujemy headers do metody get
            response = requests.get(fullUrl, headers=headers, timeout=10)
            
            if response.status_code == 200:
                with open(savePath, 'wb') as file:
                    file.write(response.content)
                print(f"[OK] Downloaded: {fileName}")
            else:
                print(f"[ERROR {response.status_code}] Access denied or file missing for: {fileName}")
                
        except Exception as e:
            print(f"[CRITICAL ERROR] {fileName}: {e}")

    print("\nDone.")

if __name__ == "__main__":
    downloadImages()


