from viewer import Viewer
from model import Model

class Controller:
    """
    методы для взаимодействия между моделью и вьювером
    """
    def __init__(self,filename:str):
        self.viewer = Viewer()
        self.model = Model(filename)

