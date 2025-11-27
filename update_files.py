import re

# Read the CSS file
with open('d:/projects/clickerbots/html/css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace enemy-image-container
old_container = r'\.enemy-image-container \{[^}]+\}'
new_container = """.enemy-image-container {
    position: relative;
    width: 100%;
    aspect-ratio: 1; /* Force square container */
    flex: 1;
    min-height: 0;
    overflow: hidden;
    border-radius: 10px;
    margin-bottom: 15px;
    border: 1px solid rgba(0, 243, 255, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
}"""

css_content = re.sub(old_container, new_container, css_content, flags=re.DOTALL)

# Replace enemy-image and add card-frame and header styles
old_image = r'\.enemy-image \{[^}]+\}'
new_image_and_extras = """.enemy-image {
    width: 100%;
    height: 100%;
    object-fit: contain; /* Maintain aspect ratio, never cut off */
    transition: filter 0.2s;
    position: relative;
    z-index: 1;
}

.card-frame {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: contain; /* Maintain aspect ratio, never cut off */
    pointer-events: none; /* Allow clicks to pass through */
    z-index: 2; /* Always on top */
}

/* Enemy Header Compact */
.enemy-header-compact {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
    flex-shrink: 0;
}

.wave-round-info {
    font-size: 0.7rem;
    color: var(--primary-color);
    font-weight: bold;
    text-shadow: 0 0 10px var(--primary-color);
}

.enemy-name-compact {
    font-size: 1.1rem;
    font-weight: 900;
    color: var(--secondary-color);
    text-shadow: 0 0 15px var(--secondary-color);
    text-transform: uppercase;
    letter-spacing: 2px;
}

.enemy-level-compact {
    font-size: 0.8rem;
    color: var(--player-color);
    font-weight: bold;
    text-shadow: 0 0 10px var(--player-color);
}"""

css_content = re.sub(old_image, new_image_and_extras, css_content, flags=re.DOTALL)

# Write back
with open('d:/projects/clickerbots/html/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# Now fix the HTML file
with open('d:/projects/clickerbots/html/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Add the card-frame after the enemy image
html_content = html_content.replace(
    '<img id="enemy-image" class="enemy-image" src="" alt="Enemy Robot">',
    '<img id="enemy-image" class="enemy-image" src="" alt="Enemy Robot">\n                        <img src="assets/card frame.png" class="card-frame" alt="Card Frame">'
)

with open('d:/projects/clickerbots/html/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Files updated successfully!")
