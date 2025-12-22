# Class bundles data and methods
class TextProcessor:
    def __init__(self, text):
        self.text = text
    
    def clean(self):
        self.text = self.text.strip().lower()
        return self
    
    def remove_punctuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self
# Chain methods on object
processor = TextProcessor(text="  Hello, World.  ")
result = processor.clean().remove_punctuation().text
print(result.lower())