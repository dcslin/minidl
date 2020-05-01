class Model:
    def __init__(self):
        self.data = []
        print("model inited")


class Operator:
    def __init__(self):
        print("operator init")


class IdentityOp(Operator):
    def __init__(self):
        super().__init__()
        print("identity op init")


class Tensor():
    def __init__(self):
        print("tensor init")
