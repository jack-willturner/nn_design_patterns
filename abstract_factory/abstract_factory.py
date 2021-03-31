class Model:
    def __init__(self):
        self.num_classes = None


class ResNetCIFAR(Model):
    def __init__(self):
        self.num_classes = 10


class ResNetImageNet(Model):
    def __init__(self):
        self.num_classes = 1000


class ResNet:
    def __init__(self, factory: Type[Model] = None):
        self.factory = factory

    def get(self):
        return self.factory()


ResNet(ResNetCIFAR)
