from collections import deque

# Input
suggested_links = deque(map(int, input().split()))  # FIFO
featured_articles = list(map(int, input().split()))  # LIFO
target_value = int(input())

# Final Feed Collection
final_feed = []

# Processing elements
while suggested_links and featured_articles:
    fifo = suggested_links.popleft()
    lifo = featured_articles.pop()

    if fifo > lifo:
        remainder = fifo % lifo
        final_feed.append(-remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)
    elif lifo > fifo:
        remainder = lifo % fifo
        final_feed.append(remainder)
        if remainder != 0:
            featured_articles.append(remainder * 2)
    else:
        final_feed.append(0)

# Calculate total engagement value
total_engagement = sum(final_feed)

# Output results
print(f"Final Feed: {', '.join(map(str, final_feed))}")
if total_engagement >= target_value:
    print(f"Goal achieved! Engagement Value: {total_engagement}")
else:
    print(f"Goal not achieved! Short by: {target_value - total_engagement}")