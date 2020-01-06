class Module(object):
    """Base module interface.
    classes that implement this interface must provide
    a run function"""
    def run(self, **args):
        return NotImplementedError
