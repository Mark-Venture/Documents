import re

# CONFIGURATION
INPUT_FILE = "Settings_OLD.txt"
OUTPUT_FILE = "Settings_NEW.txt"

# Channels that move backwards (Open/Closed are swapped physically) in the Donor Settings FileNotFoundError
# if no channels are reveresed,  remove the numbers, but keep the brackets []
REVERSED_CHANNELS = [1,3,4,5]

# Define your NEW calibration values here
# Format: ChannelIndex: (min, max, home, neutral)
NEW_LIMITS = {
    0:  (3968, 8000, 3968, 3968),
    1:  (4992, 8000, 4992, 7232),
    2:  (3200, 6272, 3200, 3200), # Your updated values
    3:  (3648, 7744, 3648, 6784),
    4:  (3648, 7744, 3648, 7040),
    5:  (3648, 7488, 3648, 7232),
    6:  (2688, 6976, 3392, 4352),
    7:  (1984, 7808, 1984, 7808),
    8:  (1984, 7808, 1984, 6000),
    9:  (1984, 7872, 1984, 6000),
    10: (1984, 7168, 1984, 6000),
    11: (3648, 7168, 3648, 6000),
}

def scale_value(val, old_min, old_max, new_min, new_max, is_reversed=False):
    if val == 0: return 0
    percent = (val - old_min) / (old_max - old_min) if old_max != old_min else 0
    percent = max(0, min(1, percent))
    if is_reversed:
        return int(new_max - (percent * (new_max - new_min)))
    return int(new_min + (percent * (new_max - new_min)))

def run_update():
    try:
        with open(INPUT_FILE, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        return

    # 1. Parse OLD channel limits for scaling math
    old_limits = {}
    channel_defs = re.findall(r'<Channel [^>]*>', content)
    for i, ch_tag in enumerate(channel_defs):
        c_min = re.search(r'min="(\d+)"', ch_tag)
        c_max = re.search(r'max="(\d+)"', ch_tag)
        if c_min and c_max:
            old_limits[i] = (int(c_min.group(1)), int(c_max.group(1)))

    # 2. NEW LOGIC: Update the <Channels> header section text
    def update_channel_header(match):
        full_tag = match.group(0)
        idx = update_channel_header.counter
        update_channel_header.counter += 1
        if idx in NEW_LIMITS:
            n_min, n_max, n_home, n_neut = NEW_LIMITS[idx]
            full_tag = re.sub(r'min="\d+"', f'min="{n_min}"', full_tag)
            full_tag = re.sub(r'max="\d+"', f'max="{n_max}"', full_tag)
            full_tag = re.sub(r'home="\d+"', f'home="{n_home}"', full_tag)
            full_tag = re.sub(r'neutral="\d+"', f'neutral="{n_neut}"', full_tag)
        return full_tag

    update_channel_header.counter = 0
    content = re.sub(r'<Channel [^>]*>', update_channel_header, content)

    # 3. Update the Sequence Frames
    def update_frame_data(match):
        tag = match.group(1)
        vals = match.group(2).split()
        new_vals = []
        for i, v in enumerate(vals):
            try:
                v_int = int(v)
                if i in old_limits and i in NEW_LIMITS:
                    o_min, o_max = old_limits[i]
                    n_min, n_max, _, _ = NEW_LIMITS[i]
                    new_vals.append(str(scale_value(v_int, o_min, o_max, n_min, n_max, i in REVERSED_CHANNELS)))
                else:
                    new_vals.append(v)
            except ValueError:
                new_vals.append(v)
        return f"{tag}{' '.join(new_vals)}"

    content = re.sub(r'(<Frame[^>]*>)([^<]+)', update_frame_data, content)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(content)
    print(f"Success! {OUTPUT_FILE} updated with new limits and scaled frames.")

if __name__ == "__main__":
    run_update()
