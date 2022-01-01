# OCR

## Download dependencies

```sh
sudo apt-get update
sudo apt-get --fix-missing install libleptonica-dev libtesseract-dev tesseract-ocr-all libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev libgl-dev -y
pip3 install opencv-python pytesseract
```

## Code 

### DocOCR

```py
import cv2
import pytesseract
from PIL import Image

class DocOCR:
    def __init__(self, imagePath:str=None, image=None):
        if imagePath:
            self.imagePath:str=imagePath
            self.image=cv2.imread(imagePath)
        if image:
            self.image=image
        assert self.image is not None
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

    def ocr(self) -> str:
        return pytesseract.image_to_string(self.image)
    
```

### SceneOCR

```py
pass
```

### Output for original-image from DocOCR:

```
Is It Possible To Go Completely Paperless In A Law Office? | Above ... http://abovethelaw.com/2014/07/is-it-possible-to-go-completely-pape...

—§ Qofi2-

7

For the rest of us, it is a matter of two things: (1) convenience, and (2) efficiency/billable
hours. I know it’s weird to see efficiency and billable hours used in the same sentence.
without a negative in there somewhere, but if you have ever had three hours of time
written off for looking all over the whole office for that one document that was dropped on
the file clerk’s desk last week, you know what I’m talking about. Sometimes when you
charge by the hour, it is good to work efficiently. So, I want to discuss whether it’s possible

to go almost completely paperless and what steps we can take to get there.
Why Go Paperless?

I am mostly paperless and it’s great. I know where all of my things are and I can find them
instantly. My desk has no clutter. I don’t have to get nervous when I put client medical
records in the trash or worry about shredding. My office is not paralyzed when the toner
waste drum breaks or when the machine tells me there is a jam in tray 3, but I’m looking
there and there is no jam. I have a significantly reduced file storage area and paper/printer
supply closet. In short, my office looks like Captain Picard’s ready room, only with less
Earl Grey.

_ There are some times when you are going to have to print things on paper because you go

to trial and have to make exhibit binders, or you live in a village that does not have e-filing
for state courts yet, but we can’t fix that. Instead, I am only discussing here what we can do

-_ to get as close as possible to going paperless.

Bates Stamping the Old Way

I worked for a firm that did all of its Bates stamping by hand with printable mailing labels.

All Bates-stamped documents would have an “Original” file, the “Bates stamp” copy, and
the “Produced” copy. The Bates copy looked ridiculous because the bottom right corner
was twice as thick because of the sticker label. It made the file fan out and it would never

- stack right on the shelf.

Bates Stamping the New Way

Adobe Acrobat comes with a Bates-stamping tool:

4/6/2015 9:08 PM.
```