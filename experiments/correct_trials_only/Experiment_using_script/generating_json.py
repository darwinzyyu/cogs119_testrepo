#!/usr/bin/env python
# coding: utf-8

# # Novel condition image pairing only

# In[1]:


import os
import json
import random

# Define path for NOVEL condition
root_path = os.getcwd()
novel_path = os.path.join(root_path, 'Stimuli', 'Novel pairs (tested)')

# Function to get image pairs for the NOVEL condition with flexible matching
def get_image_pairs_novel(condition_path):
    pairs = []
    
    # Get all .jpg files, excluding 'Thumbs.db'
    files = sorted([f for f in os.listdir(condition_path) if f.lower().endswith('.jpg') and not f.startswith('Thumbs.db')])
    
    # Debug: Print the list of files found
    print(f"Files found in {condition_path}: {files}")
    
    # Group files based on the first three characters to create pairs
    grouped_files = {}
    for f in files:
        base = f[:3]  # Base identifier (e.g., 'n01')
        if base not in grouped_files:
            grouped_files[base] = []
        grouped_files[base].append(f)
    
    # Debug: Show grouped files by base name
    print(f"Grouped files by base name (first three characters): {grouped_files}")
    
    # Identify valid pairs with explicit check for 'a' and 'b'
    for base, file_list in grouped_files.items():
        a_file = next((f for f in file_list if 'a' in f[3:]), None)
        b_file = next((f for f in file_list if 'b' in f[3:]), None)
        if a_file and b_file:
            pairs.append({
                'image1': os.path.join('Stimuli', 'Novel pairs (tested)', a_file),
                'image2': os.path.join('Stimuli', 'Novel pairs (tested)', b_file)
            })
            
            # Debug: Log successful pairing
            print(f"Pair found: {a_file} and {b_file}")
    
    # Print initial total pairs found
    initial_pair_count = len(pairs)
    print(f"Total pairs initially found for NOVEL condition: {initial_pair_count}")
    
    # Limit to 50 pairs if more are found
    final_pairs = random.sample(pairs, min(50, initial_pair_count))
    print(f"Total pairs selected for NOVEL condition (limited to 50): {len(final_pairs)}")

    return final_pairs

# Get NOVEL pairs & prepare JSON structure
novel_pairs = get_image_pairs_novel(novel_path)
json_data = [{'condition': 'NOVEL', 'image1': pair['image1'], 'image2': pair['image2']} for pair in novel_pairs]

# Output JSON file
with open('novel_pairs.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print('Successfully generated novel_pairs.json with pairs for the NOVEL condition.')


# # Novel, Exemplar, and State image pairing

# In[2]:


# Define root path for 'Stimuli' directory 
root_path = os.getcwd()

# Define conditions & their paths
conditions = {
    "EXEMPLAR": os.path.join(root_path, 'Stimuli', 'EXEMPLAR'),
    "STATE": os.path.join(root_path, 'Stimuli', 'STATE'),
    "NOVEL": os.path.join(root_path, 'Stimuli', 'Novel pairs (tested)')
}

# Function to get image pairs for EXEMPLAR and STATE
def get_image_pairs_exemplar_state(condition_path, condition_name):
    pairs = []
    subdirs = ['USED', 'UNUSED', 'UNUSED-the rest of them']
    for subdir in subdirs:
        subdir_path = os.path.join(condition_path, subdir)
        if os.path.exists(subdir_path):
            
            # Get all image files in subdirectory, excluding 'Thumbs.db'
            files = [f for f in os.listdir(subdir_path) if f.lower().endswith('.jpg') and not f.startswith('Thumbs.db')]
            files.sort()  # Ensure pairs are sequentially organized
            base_names = {}
            for f in files:
                base = f[:-5]
                if base not in base_names:
                    base_names[base] = []
                base_names[base].append(os.path.join('Stimuli', condition_name, subdir, f))
            for images in base_names.values():
                if len(images) == 2:
                    pairs.append({'image1': images[0], 'image2': images[1]})
    
    # Print initial total pairs found
    initial_pair_count = len(pairs)
    print(f"Total pairs initially found for {condition_name} condition: {initial_pair_count}")

    # Limit to 50 pairs if more are found
    final_pairs = random.sample(pairs, min(50, initial_pair_count))
    print(f"Total pairs selected for {condition_name} condition (limited to 50): {len(final_pairs)}")

    return final_pairs

# Function to get image pairs for NOVEL condition with flexible matching
def get_image_pairs_novel(condition_path):
    pairs = []
    
    # Get all .jpg files, excluding 'Thumbs.db'
    files = sorted([f for f in os.listdir(condition_path) if f.lower().endswith('.jpg') and not f.startswith('Thumbs.db')])
    
    # Group files based on the first three characters to create pairs
    grouped_files = {}
    for f in files:
        base = f[:3]  # Base identifier (e.g., 'n01')
        if base not in grouped_files:
            grouped_files[base] = []
        grouped_files[base].append(f)
    
    # Identify valid pairs with explicit check for 'a' and 'b'
    for base, file_list in grouped_files.items():
        a_file = next((f for f in file_list if 'a' in f[3:]), None)
        b_file = next((f for f in file_list if 'b' in f[3:]), None)
        if a_file and b_file:
            pairs.append({
                'image1': os.path.join('Stimuli', 'Novel pairs (tested)', a_file),
                'image2': os.path.join('Stimuli', 'Novel pairs (tested)', b_file)
            })
            # Debug: Log successful pairing
            print(f"Pair found: {a_file} and {b_file}")
    
    # Print initial total pairs found
    initial_pair_count = len(pairs)
    print(f"Total pairs initially found for NOVEL condition: {initial_pair_count}")
    
    # Limit to 50 pairs if more are found
    final_pairs = random.sample(pairs, min(50, initial_pair_count))
    print(f"Total pairs selected for NOVEL condition (limited to 50): {len(final_pairs)}")

    return final_pairs

# Collect & sample image pairs for each condition
all_pairs = {
    'EXEMPLAR': get_image_pairs_exemplar_state(conditions['EXEMPLAR'], 'EXEMPLAR'),
    'STATE': get_image_pairs_exemplar_state(conditions['STATE'], 'STATE'),
    'NOVEL': get_image_pairs_novel(conditions['NOVEL'])
}

# Preparing JSON structure
json_data = []
for condition, pairs in all_pairs.items():
    for pair in pairs:
        json_data.append({
            'condition': condition,
            'image1': pair['image1'],
            'image2': pair['image2']
        })

# Output JSON file
with open('stimuli_pairs.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print('Generated stimuli_pairs.json with pairs for each condition.')


# In[ ]:




