hours = 2
minutes_in_hour = 60 * (hours // 2)
second_in_minute = (minutes_in_hour // 60) * 60
seconds = minutes_in_hour * second_in_minute * hours

print(f"2 hour(s) is {seconds} seconds.")