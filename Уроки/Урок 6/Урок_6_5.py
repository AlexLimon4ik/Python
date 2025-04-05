class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built"
    
def check_material(amount, limit):
    if amount > limit:
        return 'enough material'
    else:
        raise BuildingError(amount)

materials = 123
check_material(materials, 300)