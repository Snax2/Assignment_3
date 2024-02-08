LEVELS_DIR = "../Levels"
GRAPHICS_DIR = "../Graphics"

level_0 = {
    'Platforms': f"{LEVELS_DIR}/Level_1/Level_1_Platforms.csv",
    'Constraints': f"{LEVELS_DIR}/Level_1/Level_1_Constraints.csv",
    'Enemies': f"{LEVELS_DIR}/Level_1/Level_1_Enemies.csv",
    'Collectables': f"{LEVELS_DIR}/Level_1/Level_1_Collectables.csv",
    'Start/Stop': f"{LEVELS_DIR}/Level_1/Level_1_Start_Stop.csv",
    'Background': f"{GRAPHICS_DIR}/background.png",  # Assuming shared background
    'node_pos': (100, 700),
    'node_graphics': f"{GRAPHICS_DIR}/Level_1_Title/",
    'unlock': 1
}

level_1 = {
    'Platforms': f"{LEVELS_DIR}/Level_2/Level_2_Platforms.csv",
    'Constraints': f"{LEVELS_DIR}/Level_2/Level_2_Constraints.csv",
    'Enemies': f"{LEVELS_DIR}/Level_2/Level_2_Enemies.csv",
    'Collectables': f"{LEVELS_DIR}/Level_2/Level_2_Collectables.csv",
    'Start/Stop': f"{LEVELS_DIR}/Level_2/Level_2_Start_Stop.csv",
    'Background': f"{GRAPHICS_DIR}/Level_2_background.png",  # Or update if level-specific
    'node_pos': (280, 700),
    'node_graphics': f"{GRAPHICS_DIR}/Level_2_Title/",
    'unlock': 2
}

level_2 = {
    'Platforms': f"{LEVELS_DIR}/Level_3/Level_3_Platforms.csv",
    'Constraints': f"{LEVELS_DIR}/Level_3/Level_3_Constraints.csv",
    'Enemies': f"{LEVELS_DIR}/Level_3/Level_3_Enemies.csv",
    'Collectables': f"{LEVELS_DIR}/Level_3/Level_3_Collectables.csv",
    'Start/Stop': f"{LEVELS_DIR}/Level_3/Level_3_Start_Stop.csv",
    'Background': f"{GRAPHICS_DIR}/snow_background.jpg",  # Or update if level-specific
    'node_pos': (460, 700),
    'node_graphics': f"{GRAPHICS_DIR}/Level_3_Title/",
    'unlock': 3
}

level_3 = {
    'Platforms': f"{LEVELS_DIR}/Level_4/Level_4_Platforms.csv",
    'Constraints': f"{LEVELS_DIR}/Level_4/Level_4_Constraints.csv",
    'Enemies': f"{LEVELS_DIR}/Level_4/Level_4_Enemies.csv",
    'Collectables': f"{LEVELS_DIR}/Level_4/Level_4_Collectables.csv",
    'Start/Stop': f"{LEVELS_DIR}/Level_4/Level_4_Start_Stop.csv",
    'Background': f"{GRAPHICS_DIR}/lava_background.jpg",
    'node_pos': (650, 700),
    'node_graphics': f"{GRAPHICS_DIR}/Level_4_Title/",
    'unlock': 3
}

# Define a dictionary containing all levels
levels = {
	0: level_0,
	1: level_1,
	2: level_2,
	3: level_3,}

