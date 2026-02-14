
import time

previous_positions = {}

def estimate_speed(object_id, current_position):
    if object_id not in previous_positions:
        previous_positions[object_id] = (current_position, time.time())
        return 0

    prev_position, prev_time = previous_positions[object_id]
    current_time = time.time()

    distance = abs(current_position - prev_position)
    time_diff = current_time - prev_time

    previous_positions[object_id] = (current_position, current_time)

    if time_diff == 0:
        return 0

    return distance / time_diff
