# Problem
- we would like to construct a complex object step-by-step with lots of possible variations but shared overall structure
- we don't want to write an initialisation function with a bunch of parameters and if statements

**Example.** ResNet looks slightly different between ImageNet and CIFAR-10. There are three key changes:
 - the first convolution looks different (`3x3` for CIFAR and `7x7` for ImageNet)
 - for ImageNet we need max pooling at the start
 - the classifier has a different number of classes

We could write this into the constructor:

```python
class ResNet(nn.Module):
  def __init__(self, variant):
    ...
    if variant == 'ImageNet':
      self.conv1 = ...

    ## normal resnet definition

    if variant == 'ImageNet':
      self.classifier = ...
```

This is bad for a few reasons:
1. it's hard to keep track of all the modifications since they are not in one place
2. if we add more datasets it will become spaghetti code very quickly

One solution is to have a ResNet class with the very core features, and an individual subclass per possible combination:

```python
class ResNet(nn.Module):
  ...

class ResNetCIFAR(ResNet):
  ...

class ResNetImageNet(ResNet):
  ...
```

and so on. If we make more modifications, this will result a lot of subclasses.

So to summarise, we can either have:
- a giant initialisation function that covers all options
- individual initialisation functions for each option
