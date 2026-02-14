#!/usr/bin/env python3
"""
Script to rotate the 'currentlyLearning' field in README.md weekly
"""

import re
from datetime import datetime

# List of learning goals to rotate through
LEARNING_GOALS = [
    "Advanced Flutter animations & custom UI components",
    "Native Android development with Jetpack Compose",
    "Mobile app performance optimization & scalability",
    "AI/ML integration in mobile apps 🤖",
    "Clean architecture & design patterns 🏗️",
    "Cloud functions & advanced Firebase features",
    "State management patterns & app architecture",
    "iOS development with Swift"
]

def get_current_week_index():
    """Calculate which learning goal to use based on week number"""
    # Get the ISO week number of the year
    week_number = datetime.now().isocalendar()[1]
    # Rotate through the learning goals
    return week_number % len(LEARNING_GOALS)

def update_readme():
    """Update the currentlyLearning field in README.md"""
    readme_path = 'README.md'
    
    # Read the current README
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Get the current learning goal
    current_index = get_current_week_index()
    new_learning = LEARNING_GOALS[current_index]
    
    # Pattern to match the currentlyLearning line
    pattern = r'(currentlyLearning:\s*")[^"]*(")'
    replacement = f'\\1{new_learning}\\2'
    
    # Replace the learning goal
    updated_content = re.sub(pattern, replacement, content)
    
    # Write back to README
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"✅ Updated learning goal to: {new_learning}")
    print(f"📅 Week index: {current_index + 1}/{len(LEARNING_GOALS)}")

if __name__ == "__main__":
    update_readme()
