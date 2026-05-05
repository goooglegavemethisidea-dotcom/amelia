print("hello world")
def analyze_scores(scores):
    lowest = min(scores)
    highest = max(scores)
    total = 0 
    for score in scores :
        total += score
    average = total / len(scores)
    return lowest, highest, average
scores = [45, 67, 82, 90, 39,79]
lowest, highest, average = analyze_scores(scores)
print("Lowest :", lowest)
print("highest:", highest)
print("Average:", average)
def analyze_scores(scores):
    lowest = min(scores)
    highest = max(scores)
    
    total = 0
    passed = 0
    
    for score in scores:
        total += score
        if score >= 50:
            passed += 1
    
    avg = total / len(scores)
    
    return lowest, highest, avg, passed
owest, highest, avg, passed = analyze_scores(scores)

print("Lowest:", lowest)
print("Highest:", highest)
print("Average:", avg)
print("Passed:", passed)
def analyze_scores(scores):
    return {
        "lowest": min(scores),
        "highest": max(scores),
        "average": sum(scores) / len(scores),
        "passed": sum(1 for s in scores if s >= 50)
    }
result = analyze_scores(scores)

print(result["lowest"])
print(result["highest"])
print(result["average"])
print(result["passed"])
numbers = [12, -3, 7, 0, 25, -8, 14, 7, 19, -1]

positives = []
odds = []

# Step 1: filter positives and odds
for n in numbers:
    if n > 0:
        positives.append(n)
    if n % 2 != 0:
        odds.append(n)

# Step 2: squares of positive numbers
squares = []
for n in positives:
    squares.append(n ** 2)

# Step 3: sort positives in descending order
positives.sort(reverse=True)

# Step 4: second largest positive number
second_largest = positives[1]

# Step 5: print results
print("Positive numbers:", positives)
print("Odd numbers:", odds)
print("Squares of positives:", squares)
print("Second largest positive:", second_largest)
'stronger version'
print("\nRanking:")
for rank, value in enumerate(positives, start=1):
    print(f"Rank {rank}: {value}")

students = [
    {"name": "Alice", "track": "Python", "score": 85},
    {"name": "Bob", "track": "JavaScript", "score": 92},
    {"name": "Charlie", "track": "Python", "score": 78},
    {"name": "Diana", "track": "Python", "score": 95},
    {"name": "Eve", "track": "JavaScript", "score": 88}
]

# 1. Names of Python track students
print("Python track students:")
for student in students:
    if student["track"] == "Python":
        print(student["name"])


# 2. Average score
total = 0
for student in students:
    total += student["score"]

avg = total / len(students)
print("\nAverage score:", avg)


# 3. Student with highest score
top_name = students[0]["name"]
top_score = students[0]["score"]

for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_name = student["name"]

print("\nTop student:", top_name)


# 4. Count students per track
track_count = {}

for student in students:
    track = student["track"]
    if track in track_count:
        track_count[track] += 1
    else:
        track_count[track] = 1

print("\nTrack count:", track_count)
def top_student(students):
    best = students[0]
    
    for student in students:
        if student["score"] > best["score"]:
            best = student
    
    return best["name"], best["score"]
name, score = top_student(students)
print("\nBest student:", name, score)
word = "programming"

count = {}

for ch in word:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print("Frequency dictionary:", count)
