import colorama
from colorama import Fore, Back, Style

print("\nІнтроспекція colorama:\n")
for _ in dir(colorama):
   print(_)

print("\nІнтроспекція colorama, Fore:\n")
for _ in dir(Fore):
   print(_)

print("\nІнтроспекція colorama, Back:\n")
for _ in dir(Back):
   print(_)

print("\nІнтроспекція colorama, Style:\n")
for _ in dir(Style):
   print(_)


print("\nНайцікавіші команди це:\n ")

print("Fore.GREEN:", Fore.GREEN + "Green")
print(Style.RESET_ALL)

print("Fore.RED:", Fore.RED + "Red")
print(Style.RESET_ALL)

print("Fore.BLUE:", Fore.BLUE + "Blue")
print(Style.RESET_ALL)

print("Style.BLUE:", Style.BRIGHT, "Bright")
print(Style.RESET_ALL)

print("Back.GREEN:", Back.GREEN, "Back is Green", Style.RESET_ALL)
print(Style.RESET_ALL)

print("Back.RED:", Back.RED, "Back is Red", Style.RESET_ALL)
print(Style.RESET_ALL)

print("Back.BLUE:", Back.BLUE, "Back is Blue", Style.RESET_ALL)
print(Style.RESET_ALL)

print("Style.RESET_ALL:", Style.RESET_ALL, "Reset")
print(Style.RESET_ALL)

