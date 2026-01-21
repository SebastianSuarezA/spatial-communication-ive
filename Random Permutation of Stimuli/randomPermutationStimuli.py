import random
import csv
import os

# Set a seed for reproducibility (optional)
random.seed(2026)

# Original stimuli
stimuli = [f"N_Stimuli{i}" for i in range(1, 17)]

# Create a folder for results if it doesn't exist
os.makedirs("results", exist_ok=True)

# Open CSV file for writing
with open("results/participant_orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    
    # Write header
    header = ["Participant"] + [f"Order_{i}" for i in range(1, 17)]
    writer.writerow(header)
    
    # Generate random permutation for each participant
    for participant in range(1, 17):
        # Random permutation of positions
        positions = list(range(1, 17))
        random.shuffle(positions)
        
        # Assign randomized position to each stimulus
        labeled_stimuli = [f"{pos}_{stim}" for pos, stim in zip(positions, stimuli)]
        
        # Sort by the randomized position (prefix)
        ordered_stimuli = sorted(labeled_stimuli, key=lambda x: int(x.split("_")[0]))
        
        # Write to CSV: participant number + ordered stimuli
        writer.writerow([f"Participant_{participant}"] + ordered_stimuli)

print("Randomized participant orders saved to 'results/participant_orders.csv'.")
