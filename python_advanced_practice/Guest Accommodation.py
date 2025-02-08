def accommodate(*args, **kwargs):

    accommodations = {}
    homeless = 0
    rooms = sorted(kwargs.items(), key=lambda r: (r[1], r[0]))
    for curr_group in args:
        done = False
        for curr_room, curr_room_cap in rooms:
            if curr_group <= curr_room_cap:
                room_num = curr_room.split("_")[1]
                if room_num not in accommodations:
                    accommodations[room_num] = curr_group
                    rooms.remove((curr_room, curr_room_cap))
                    done = True
                    break
        if not done:
            homeless += curr_group

    if accommodations:
        result = [f"A total of {len(accommodations)} accommodations were completed!"]
        for room_num in sorted(accommodations.keys()):
            result.append(f"<Room {room_num} accommodates {accommodations[room_num]} guests>")
    else:
        result = ["No accommodations were completed!"]
    if homeless > 0:
        result.append(f"Guests with no accommodation: {homeless}")
    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")

    return "\n".join(result).strip()

print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))