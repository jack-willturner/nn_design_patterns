# The Builder Pattern

> The Builder pattern suggests that you extract the object construction code out of its own class and move it to separate objects called builders.

Example:

```python
class ResNetBuilder(ABC):
  def __init__(self):
    build_stem()
    build_feature_extractor()
    build_classifier()

class ResNetImageNetBuilder(ResNetBuilder):
  def build_stem():
    ...

  def build_feature_extractor():
    ...

  def build_classifier():
    ...

```
