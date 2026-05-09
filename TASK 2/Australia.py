# Task 2(a): Australia Map Coloring (Full Names)
def is_valid(region, color, assignment, adjacency):
    """Check if the color assignment is consistent with neighbors."""
    for neighbor in adjacency.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack_coloring(regions, colors, assignment, adjacency):
    """Backtracking algorithm to find a valid coloring."""
    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment, adjacency):
            assignment[region] = color
            result = backtrack_coloring(regions, colors, assignment, adjacency)
            if result:
                return result
            del assignment[region]
    return None

# Define Australia Data with Full Names
regions_au = [
    'Western Australia', 
    'Northern Territory', 
    'South Australia', 
    'Queensland', 
    'New South Wales', 
    'Victoria', 
    'Tasmania'
]
colors_au = ['Red', 'Green', 'Blue']

adjacency_au = {
    'Western Australia': ['Northern Territory', 'South Australia'],
    'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
    'Victoria': ['South Australia', 'New South Wales'],
    'Tasmania': [] 
}

solution_au = backtrack_coloring(regions_au, colors_au, {}, adjacency_au)

print("Australia Coloring Solution:")
for region, color in solution_au.items():
    print(f"{region}: {color}")
