import warnings

warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('always', ImportWarning)

warnings.warn("Warnings, no code here", SyntaxWarning)
warnings.warn("Warnings, module not import", ImportWarning)