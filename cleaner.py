import os
from PIL import Image

def fillAllVisibleWithGreen():
    sourceFolder = "kraje"
    outputFolder = "kraje_pure_green"
    
    # Kolor #009f00 w formacie RGBA
    targetGreen = (0, 159, 0, 255)
    
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    files = [f for f in os.listdir(sourceFolder) if f.endswith(".png")]
    print(f"Processing {len(files)} files - filling all visible pixels...")

    for fileName in files:
        filePath = os.path.join(sourceFolder, fileName)
        savePath = os.path.join(outputFolder, fileName)

        try:
            img = Image.open(filePath).convert("RGBA")
            pixels = img.getdata()

            newPixels = []

            for p in pixels:
                # p[3] to kanał Alpha (przezroczystość)
                # Jeśli piksel nie jest w pełni przezroczysty, zamień go na zielony
                if p[3] > 0:
                    newPixels.append(targetGreen)
                else:
                    # Jeśli jest przezroczysty, zostaw go bez zmian
                    newPixels.append(p)

            img.putdata(newPixels)
            img.save(savePath, "PNG")
            print(f"[OK] {fileName} - green fill applied")

        except Exception as e:
            print(f"[ERROR] {fileName}: {e}")

    print(f"\nGotowe! Wszystkie kształty są teraz jednolicie zielone (#009f00).")

if __name__ == "__main__":
    fillAllVisibleWithGreen()