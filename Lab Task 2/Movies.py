movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

add_more = input("Do you want to add more movies? (yes/no): ").lower()
if add_more == "yes":
    n = int(input("How many movies you want to add? "))
    for i in range(n):
        name = input("Enter movie name: ")
        budget = int(input("Enter budget: "))
        movies.append((name, budget))

total_budget = 0
for movie in movies:
    total_budget = total_budget + movie[1]

average_budget = total_budget / len(movies)
print("\nAverage budget of movies is:", average_budget)

count = 0
print("\nMovies with budget higher than average:")
for movie in movies:
    if movie[1] > average_budget:
        extra = movie[1] - average_budget
        print(movie[0], "has a budget", extra, "more than average")
        count = count + 1

print("\nNumber of movies with higher than average budget:", count)
