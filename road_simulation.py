"""
road_simulation.py
Full Self Driving Simulation mode in Kigali: ALU Rwanda to Convention Center

Your job: complete TODO 1 to TODO 10 below (replace each pass).
Do NOT edit engine.py, index.html or transit_program.py.
Run with:   python road_simulation.py or python3 road_simulation.py
"""

SEGMENT_M = 100
ZEBRA_WAIT = 15
ACCELERATION = 5
BRAKING = 20
START_NAME = "ALU Rwanda"
END_NAME = "Convention Center"

# Each item in the road list is ONE segment of road.
road = [
    "60", "road", "road", "road", "zebra", "road", "road",
    "80", "road", "road", "road", "road", "road", "road",
    "bus", "road", "road", "bus", "road", "road", "road",
    "60", "road", "road", "road", "road", "80", "road",
    "road", "zebra", "road", "road", "road", "road",
]

# ==================== PART 1: CHECK THE SIGN ====================

# TODO 1: Return True only if sign is text AND is "bus", "zebra"
# or a number from 20 to 100 written as text (e.g. "80").
def is_valid_sign(sign):
    if not isinstance(sign, str):
        return False
    if sign == "bus" or sign == "zebra":
        return True
    if sign.isdigit() and 20 <= int(sign) <= 100:
        return True
    return False


# TODO 2: Return "bus", "zebra", "speed" (a number) or "road".
def get_sign_type(sign):
    if sign == "bus":
        return "bus"
    if sign == "zebra":
        return "zebra"
    if sign.isdigit():
        return "speed"
    return "road"


# ==================== PART 2: TAKE ACTION ====================

# TODO 3: If the sign is a speed sign, return its number, else current_limit.
def get_speed_limit(sign, current_limit):
    if sign.isdigit():
        return int(sign)
    return current_limit


# TODO 4: Return 0 while stop_timer is above 0, otherwise the limit.
def get_target_speed(limit, stop_timer):
    if stop_timer > 0:
        return 0
    return limit


# TODO 5: Move speed ONE step towards target and return it.
# Below target: add ACCELERATION (never go above target).
# Above target: subtract BRAKING (never go below target).
def adjust_speed(speed, target):
    if speed < target:
        return min(speed + ACCELERATION, target)
    if speed > target:
        return max(speed - BRAKING, target)
    return speed


# TODO 6: Use a loop. Return (speed_signs, zebras, buses).
def count_signs(road_list):
    speed = 0
    zebra = 0
    bus = 0
    for sign in road_list:
        if sign == "zebra":
            zebra += 1
        elif sign == "bus":
            bus += 1
        elif sign.isdigit():
            speed += 1
    return speed, zebra, bus


# ==================== PART 3: SAFE INPUT AND JOURNEY ====================

# TODO 7: Keep asking until the user types a whole number from low to high.
# Use try/except for text that is not a number.
def ask_for_number(question, low, high):
    while True:
        try:
            value = int(input(question))
            if low <= value <= high:
                return value
            print("Number out of range. Try again.")
        except ValueError:
            print("That is not a whole number. Try again.")


# TODO 8: Insert sign at position. Return False if position is invalid.
# Otherwise insert and return True.
def insert_sign(road_list, sign, position):
    if not is_valid_sign(sign):
        return False
    if position < 0 or position > len(road_list):
        return False
    road_list.insert(position, sign)
    return True


# TODO 9: Replace the sign at index with a new sign. Valid index is
# from 0 to len(road_list) - 1. Otherwise replace it and return True.
def replace_sign(road_list, sign, index):
    if not is_valid_sign(sign):
        return False
    if index < 0 or index > len(road_list) - 1:
        return False
    road_list[index] = sign
    return True


# TODO 10: Summarise the journey. Use a loop to count signs passed
# (every segment that is not "road"). Return four values:
# (signs_passed, length_m, START_NAME, END_NAME)
# length_m is the number of segments times SEGMENT_M.
def get_journey_summary(road_list):
    signs_passed = 0
    for sign in road_list:
        if sign != "road":
            signs_passed += 1
    length_m = len(road_list) * SEGMENT_M
    return signs_passed, length_m, START_NAME, END_NAME


if __name__ == "__main__":
    import sys
    import transit_program
    transit_program.run(sys.modules[__name__])
