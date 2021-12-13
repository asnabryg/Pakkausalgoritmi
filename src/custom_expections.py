
class EmptyFileException(Exception):
    
    def __init__(self, message="Tyhjä tiedosto."):
        super(EmptyFileException, self).__init__(message)