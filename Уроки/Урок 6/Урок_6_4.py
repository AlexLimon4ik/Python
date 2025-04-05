def checker(var1):
    if type(var1) != str:
        raise TypeError(f"Вибачте, функція не працює з {type(var1)}, нам потрібен рядок(str)")
    else:
        return var1
    
first_var = 123
checker(first_var)