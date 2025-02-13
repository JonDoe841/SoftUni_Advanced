from collections import deque

package_weight = deque(map(int, input().split()))
cap_couriers = deque(map(int, input().split()))

total_delivered = 0

while package_weight and cap_couriers:
    package = package_weight[-1]
    courier = cap_couriers.popleft()

    if courier >= package:
        total_delivered += package
        package_weight.pop()

        courier -= 2 * package
        if courier > 0:
            cap_couriers.append(courier)
    else:
        total_delivered += courier
        package_weight[-1] -= courier

print(f"Total weight: {total_delivered} kg")

if not package_weight and not cap_couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif package_weight and not cap_couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, package_weight))}")
elif cap_couriers and not package_weight:
    print(f"Couriers are still on duty: {', '.join(map(str, cap_couriers))} but there are no more packages to deliver.")