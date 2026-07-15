# FREEZING_POINT = 0
# BOILING_POINT = 100
#
#
# def water_state(temperature):
#     if temperature <= FREEZING_POINT:
#         return 'Solid'
#     elif FREEZING_POINT < temperature < BOILING_POINT:
#         return 'Liquid'
#     else:
#         return 'Gas'

def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 15 <= temperature <= 25:
        return "Warm"
    elif temperature <15:
        return "Cold"
foo(15)

print(foo)


