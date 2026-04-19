print("===== TASK 1: Backtracking (Crew Scheduling) =====")

flights = [('F1', 9, 11), ('F2', 10, 12), ('F3', 12, 14)]
crew = ['C1', 'C2']

def is_valid(schedule, crew_member, flight):
    for f in schedule.get(crew_member, []):
        # Check overlap
        if not (flight[2] <= f[1] or flight[1] >= f[2]):
            return False
    return True

def backtrack(schedule, flights):
    if not flights:
        return schedule

    flight = flights[0]

    for c in crew:
        if is_valid(schedule, c, flight):
            schedule.setdefault(c, []).append(flight)

            result = backtrack(schedule, flights[1:])
            if result:
                return result

            schedule[c].pop()

    return None

print("Backtracking Solution:", backtrack({}, flights))


print("\n===== TASK 2: Branch and Bound =====")

def branch_and_bound(flights, crew):
    best = None

    def helper(schedule, remaining):
        nonlocal best

        if not remaining:
            best = schedule.copy()
            return

        flight = remaining[0]

        for c in crew:
            if is_valid(schedule, c, flight):
                schedule.setdefault(c, []).append(flight)
                helper(schedule, remaining[1:])
                schedule[c].pop()

    helper({}, flights)
    return best

print("Branch and Bound Solution:", branch_and_bound(flights, crew))


print("\n===== TASK 3: Naive String Matching =====")

def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    count = 0

    for i in range(n - m + 1):
        for j in range(m):
            count += 1
            if text[i + j] != pattern[j]:
                break
        else:
            print("Pattern found at index", i)

    print("Total Comparisons:", count)

naive_search("ABABDABACDABABCABAB", "ABABCABAB")


print("\n===== TASK 4: Observations =====")

print("• Backtracking explores all possibilities, so it is slow for large inputs.")
print("• Branch and Bound improves performance by pruning.")
print("• Naive string matching is simple but inefficient.")


print("\n===== TASK 5: Conceptual Answers =====")

print("• Backtracking has exponential complexity.")
print("• Overlap constraint is complex to manage.")
print("• Heuristics (Greedy / AI) can improve performance.")


print("\n===== END OF ASSIGNMENT =====")