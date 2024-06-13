import random


def format_time(seconds):
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400

    days, remaining_seconds = divmod(seconds, SECONDS_IN_DAY)
    hours, remaining_seconds = divmod(remaining_seconds, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remaining_seconds, SECONDS_IN_MINUTE)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not 11 <= days % 100 <= 14:
        day_word = "дні"
    else:
        day_word = "днів"

    time_str = f"{days} {day_word}, {hours:02}:{minutes:02}:{seconds:02}"

    return time_str


random_numbers = [random.randint(0, 8640000) for _ in range(10)]
for num in random_numbers:
    print(f"{num} -> {format_time(num)}")
