import resnet_cifar as cifar_models
import resnet_imagenet as imagenet_models


def ResNetFactory(version="cifar"):

    models = {"cifar": cifar_models.ResNet18(), "imagenet": imagenet_models.ResNet18()}

    return models[version]
