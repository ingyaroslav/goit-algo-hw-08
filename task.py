import heapq

def minimal_cost(cables):
    heapq.heapify(cables)  # перетворюємо список кабелів у купу

    total_cost = 0
    while len(cables) > 1:
        # беремо два найменші кабелі
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        # об'єднуємо їх та рахуємо витрати
        merged_cable = cable1 + cable2
        total_cost += merged_cable

        # додаємо об'єднаний кабель назад у купу
        heapq.heappush(cables, merged_cable)

    return total_cost

# Приклад використання:
cables = [8, 4, 6, 12]
result = minimal_cost(cables)
print("Мінімальні загальні витрати:", result)
