
from datetime import datetime, timedelta
def calculate_dream_duration(dream_segments):
    total_duration = timedelta()

    # Iterate through each dream segment
    for segment in dream_segments:
        # Split the segment into start and end times
        start_time, end_time = segment.split('-')

        # Convert start and end times to datetime objects
        start_datetime = datetime.strptime(start_time, '%H:%M')
        end_datetime = datetime.strptime(end_time, '%H:%M')

        # Calculate the duration of the segment
        segment_duration = end_datetime - start_datetime

        # Add the segment duration to the total duration
        total_duration += segment_duration

    # Convert total duration to "HH:MM" format
    total_hours, remainder = divmod(total_duration.seconds, 3600)
    total_minutes = remainder // 60

    # Format the result as a string
    return f"{total_hours:02d}:{total_minutes:02d}"

# Example usage:
dream_segments = ["21:30-22:15", "23:00-23:45", "00:15-01:00"]
dream_duration = calculate_dream_duration(dream_segments)
print(dream_duration)  # This will print "02:30" for the example segments.

