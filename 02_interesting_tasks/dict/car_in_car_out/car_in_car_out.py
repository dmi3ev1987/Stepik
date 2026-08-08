n = int(input())
cars = {}


def get_money(check_in, check_out):
    free_minutes = 120
    h_in, m_in = [int(num) for num in check_in.split(':')]
    h_out, m_out = [int(num) for num in check_out.split(':')]
    total_minutes = (h_out - h_in) * 60 + (m_out - m_in)
    if total_minutes < 0:
        total_minutes += 24 * 60
    if total_minutes <= 120:
        return 'плата не взимается'
    price_for_minute = 3
    paid_minutes = (total_minutes - free_minutes) * price_for_minute
    return '{}₽'.format(paid_minutes)


for _ in range(n):
    car_id, check_in = input().split(': ')
    cars[car_id] = check_in

m = int(input())
for _ in range(m):
    car_id, check_out = input().split(': ')
    check_in = cars[car_id]
    result = get_money(check_in, check_out)
    print(f'{car_id}: {result}')
