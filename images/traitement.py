from PIL import Image
import numpy as np

# Palette ambre 16 niveaux (R, G, B)
amber_palette = [
    (0x00, 0x00, 0x00), (0x20, 0x0B, 0x00), (0x40, 0x17, 0x00), (0x60, 0x22, 0x00),
    (0x80, 0x30, 0x00), (0x99, 0x44, 0x00), (0xB2, 0x59, 0x00), (0xCB, 0x6D, 0x00),
    (0xE4, 0x82, 0x00), (0xF0, 0x98, 0x00), (0xF6, 0xA7, 0x00), (0xFB, 0xB6, 0x00),
    (0xFF, 0xC5, 0x00), (0xFF, 0xD0, 0x40), (0xFF, 0xD9, 0x80), (0xFF, 0xB0, 0x00)
]

# Paramètres ajustables
gamma_global = 0.90
contrast_global = 0.88  # +10 %

def apply_gamma_and_contrast(input_array: np.ndarray, gamma_value: float, contrast_value: float) -> np.ndarray:
    norm = input_array / 255.0
    gamma_corrected = np.power(norm, 1.0 / gamma_value)
    contrasted = (gamma_corrected - 0.5) * contrast_value + 0.5
    contrasted = np.clip(contrasted, 0, 1)
    return (contrasted * 255).astype(np.uint8)

def distribute_error(work_array: np.ndarray, x: int, y: int, error: float) -> None:
    height, width = work_array.shape
    if x + 1 < width:
        work_array[y, x + 1] += error * 7 / 16
    if y + 1 < height:
        if x > 0:
            work_array[y + 1, x - 1] += error * 3 / 16
        work_array[y + 1, x] += error * 5 / 16
        if x + 1 < width:
            work_array[y + 1, x + 1] += error * 1 / 16

def floyd_steinberg_dithering(input_array: np.ndarray, levels: int = 16) -> np.ndarray:
    work_array = input_array.astype(float)
    height, width = work_array.shape
    for y in range(height):
        for x in range(width):
            old_pixel = float(work_array[y, x])
            new_pixel = round(old_pixel * (levels - 1) / 255) * (255 / (levels - 1))
            quant_error = old_pixel - new_pixel
            work_array[y, x] = new_pixel
            distribute_error(work_array, x, y, quant_error)
    return np.clip(work_array, 0, 255).astype(np.uint8)

# --- Processus principal ---

# Charger l'image source en niveaux de gris
img = Image.open("Exemples/img101.bmp").convert("L").resize((640, 480))
image_array = np.array(img)

# Appliquer gamma et contraste
adjusted_array = apply_gamma_and_contrast(image_array, gamma_global, contrast_global)

# Appliquer dithering Floyd-Steinberg
dithered_array = floyd_steinberg_dithering(adjusted_array, levels=16)

# Quantifier en 16 niveaux (0 à 15)
quantized_array = ((dithered_array / 255) * 15).astype(np.uint8)

# Créer l'image en mode palette ('P')
pal_img = Image.fromarray(quantized_array).convert("P")

# Construire la palette complète 256*3 en remplissant avec des zéros
flat_palette = sum(amber_palette, ())
palette_full = flat_palette + (0,) * (768 - len(flat_palette))
pal_img.putpalette(palette_full)

# Sauvegarder le résultat
pal_img.save("images/img101_converted_amber_dithered.bmp")

print("✅ Conversion terminée avec gamma, contraste et dithering Floyd-Steinberg !")