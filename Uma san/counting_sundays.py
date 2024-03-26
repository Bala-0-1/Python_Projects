def zeller_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    q = day
    m = month
    K = year % 100
    J = year // 100
    f = q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    day_of_week = f % 7
    return (day_of_week + 6) % 7

sundays_on_first_of_month = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if zeller_congruence(1, month, year) == 1:
            sundays_on_first_of_month += 1
