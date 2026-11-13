# Lab 1: FSD on Kigali Roads

**Student:** Vicky (GitHub: Hillario94)
**Course:** Introduction to Python Programming and Databases, BSE Year 1 Trimester 2

## What this project does
A Full Self Driving simulation of a Tesla driving from ALU Rwanda to the Convention Center in Kigali. The road is a Python list. Each item is a sign: a speed limit, "zebra", "bus" or "road". The program reads the road, controls the car's speed and lane, and a web page shows the journey.

## Files
- `road_simulation.py`: my work (the 10 functions)
- `engine.py`, `transit_program.py`, `index.html`: provided files, not edited
- `analyze_log.sh`: shell script that summarises the log

## How to run
```bash
python3 road_simulation.py
```
1. Enter your driver name.
2. Use the road editor menu, then choose 5 (Start driving).
3. Open http://127.0.0.1:8008 in a browser.
4. Press Enter in the terminal to start the car.

To analyse the log (run the simulation at least once first):
```bash
bash analyze_log.sh
bash analyze_log.sh other_file.log
```

## The 10 functions
1. `is_valid_sign`: accepts only "bus", "zebra", or a number from 20 to 100 written as text.
2. `get_sign_type`: returns "bus", "zebra", "speed" or "road".
3. `get_speed_limit`: returns the sign's number, or keeps the current limit.
4. `get_target_speed`: returns 0 while stopped at a zebra, otherwise the limit.
5. `adjust_speed`: moves speed one step toward the target (+5 up, -20 down, never overshooting).
6. `count_signs`: loops through the road and counts speed signs, zebras and buses.
7. `ask_for_number`: keeps asking until the input is a whole number in range (try/except).
8. `insert_sign`: inserts a sign at a position, with bounds checking.
9. `replace_sign`: replaces a sign at an index, with bounds checking.
10. `get_journey_summary`: counts signs passed, works out road length, returns the start and end names.

## Shell script
`analyze_log.sh` reads `transit_session.log` (or a file given as the first argument). It prints an error and exits with code 1 if the file is missing. It reports the number of sessions, zebra crossing stops, lane changes, and the latest driver and top speed.
