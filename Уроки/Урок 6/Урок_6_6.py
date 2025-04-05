import warnings

warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('always', ImportWarning)

warnings.warn("Warnings, no code here", SyntaxWarning)


try:
    warnings.warn("Warnings, module not import", ImportWarning)
except:
    print("Warning processed")

    {"name": 123,}