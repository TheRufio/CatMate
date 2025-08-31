from .models import Rarity

RARITY_COLORS = {
    Rarity.COMMON: "#9d9d9d",      # grey
    Rarity.UNCOMMON: "#1eff00",    # green
    Rarity.RARE: "#0070dd",        # blue
    Rarity.EPIC: "#a335ee",        # purple
    Rarity.LEGENDARY: "#ff8000",   # orange
    Rarity.MYTHIC: "#ff1493",      # pink
    Rarity.EXOTIC: "#00ffff",      # cyan
    Rarity.DIVINE: "#ffd700",      # gold
    Rarity.CELESTIAL: "#e6e6fa",   # light violet
    Rarity.UNIQUE: "#ff4500",      # red-orange
}