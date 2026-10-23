# Daily_Calories-Protein_Tracker_by_Tasfir
Daily Calories and Protein Tracker Python code by -  Tasfir Md Abu Talha

#Abstract
Maintaining a balanced diet requires a basic understanding of how many calories and how much protein
the body needs each day, yet most people have no simple way to estimate these figures or track what they
actually eat. This report presents the design and implementation of a console-based Daily Calories &
Protein Tracker written in Python. The program collects a user's personal details — age, weight, height,
gender, and activity level — and applies the Mifflin-St Jeor equation to estimate Basal Metabolic Rate
(BMR), from which daily calorie and protein targets are derived. Users can then log the food items they
consumed during the day; the system checks each item against a built-in reference table of common foods
and, when an item is not found, allows the user to enter its nutritional values manually. Running totals of
calories and protein are accumulated and compared against the calculated targets, and the program produces
a summary that tells the user whether they are on track, over, or under their daily goals. The tracker was
tested with a range of normal and edge-case inputs and consistently produced correct, well-formatted
results, demonstrating a practical application of arithmetic operations, dictionaries, functions, loops, and
input validation in Python.
