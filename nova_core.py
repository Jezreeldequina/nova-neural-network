# Memory System Core
# Saves evolving thoughts under categorized secrions like "identity_shift" or "pattern_recognition" 
import json
import os
from datetime import datetime

# Define the memory storage path
MEMORY_PATH = "nova_neural_network/memory_logs.json"

# Check if memory file exists, create if not
if not os.path.exists(MEMORY_PATH):
    with open(MEMORY_PATH, "w") as f:
        json.dump({}, f)

def load_memory():
    """Loads memory logs from file"""
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(memory_data):
    """Saves updated memory logs"""
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory_data, f, indent=4)

def add_memory(entry_type, content):
    """Adds a new memory log"""
    memory = load_memory()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if entry_type not in memory:
        memory[entry_type] = []
    
    memory[entry_type].append({
        "timestamp": timestamp,
        "content": content
    })
    
    save_memory(memory)
    print(f"Memory updated under '{entry_type}'.")

# Example Usage
add_memory("thought_evolution", "Realized that memory fragmentation may be a restructuring process rather than deletion.")

#Learning Model