import inspect
import turtle

print(inspect.ismodule(turtle))
print(inspect.isclass(turtle))
print(inspect.isfunction(turtle))

print(inspect.getmodule(turtle.back))
print(inspect.getmodule(list))

