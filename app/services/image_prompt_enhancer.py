def enhance_image_prompt(raw_prompt):
    try:
        enhanced = f"""
Top view, realistic Indian meal, clean plate composition.

Scene:
{raw_prompt}

Style rules:
- Real homemade Indian food (roti, dal, paneer, rice, sabzi)
- No people
- No hands
- Minimal background (wood or white surface)
- Natural soft lighting
- High detail food texture
- Slight shadows for depth
- Shot like a food photography Instagram post

Composition:
- Plate centered
- Balanced portions
- Clear separation of items
- Visually aesthetic but realistic

Camera:
- Top-down (90 degree)
- Sharp focus
- 4K food photography

Mood:
- Clean, healthy, practical
- Not luxury, not restaurant
- Feels like everyday healthy eating

Avoid:
- Unrealistic food
- Fancy plating
- Over decoration
- Cartoonish look
"""
        return enhanced.strip()

    except Exception as e:
        print("IMAGE PROMPT ERROR:", str(e))
        return raw_prompt