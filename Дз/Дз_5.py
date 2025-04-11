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

print("Fore.GREEN:", Fore.GREEN + "Green") # Робить текст зеленим
print(Style.RESET_ALL)

print("Fore.RED:", Fore.RED + "Red") # Робить текст червоним
print(Style.RESET_ALL)

print("Fore.BLUE:", Fore.BLUE + "Blue") # Робить текст синім
print(Style.RESET_ALL)

print("Style.BLUE:", Style.BRIGHT, "Bright") # Робить текст жирним
print(Style.RESET_ALL)

print("Back.GREEN:", Back.GREEN, "Back is Green", Style.RESET_ALL) # Робить зелений фон до тексту 
print(Style.RESET_ALL)

print("Back.RED:", Back.RED, "Back is Red", Style.RESET_ALL) # Робить червоний фон до тексту  
print(Style.RESET_ALL)

print("Back.BLUE:", Back.BLUE, "Back is Blue", Style.RESET_ALL) # Робить синій фон до тексту 
print(Style.RESET_ALL)

print("Style.RESET_ALL:", Style.RESET_ALL, "Reset") # Повертає все як було 
print(Style.RESET_ALL)

