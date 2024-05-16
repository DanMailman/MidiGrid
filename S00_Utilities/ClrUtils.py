def get_contrastive_text_color(rgb):
    """Get contrastive text color."""
    luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255
    return '#FFFFFF' if luminance < 0.5 else '#000000'
def GetHexStr(rgb):
    """Return hexadecimal string of the RGB."""
    r, g, b = rgb  # Unpack the RGB tuple
    return f'#{r:02x}{g:02x}{b:02x}'
def HexStrToRGB(sHex):
    """Return RGB tuple from a hexadecimal string."""
    # Remove '#' from the hexadecimal string
    sHex = sHex.lstrip('#')
    # Convert hex values to integers
    r = int(sHex[0:2], 16)
    g = int(sHex[2:4], 16)
    b = int(sHex[4:6], 16)
    return (r, g, b)