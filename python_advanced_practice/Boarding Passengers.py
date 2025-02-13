def boarding_passengers(ship_cap, *passenger_group):
    groups = {}
    for passengers, group in passenger_group:
        if ship_cap >= passengers:
            if group not in groups:
                groups[group] = 0
            groups[group] += passengers
            ship_cap -= passengers
        if ship_cap == 0:
            break

    sorted_groups = sorted(groups.items(), key=lambda x: (-x[1], x[0]))

    boarding_details = "Boarding details by benefit plan:\n"

    for key, value in sorted_groups:
        boarding_details += f"## {key}: {value} guests\n"
    total_boarded = sum(groups.values())
    total_passengers = sum (group1[0] for group1 in passenger_group)
    if total_boarded == total_passengers:
        boarding_details += "All passengers are successfully boarded!"
    elif ship_cap == 0:
        boarding_details += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        boarding_details += f"Partial boarding completed. Available capacity: {ship_cap}."
    return boarding_details


#print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
#print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))