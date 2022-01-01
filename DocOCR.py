import pytesseract
from PIL import Image

class DocOCR:
    def __init__(self, imagePath: str):
        self.imagePath: str = imagePath

    def ocr(self) -> str:
        return pytesseract.image_to_string(Image.open(self.imagePath))
    
if __name__ == "__main__":
    print(DocOCR('original-image.png').ocr())