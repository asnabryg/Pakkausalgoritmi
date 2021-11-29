

def bits_to_bytes(bits):
    """Muuttaa bittiesityksen tavuiksi.

    Args:
        bits (str): bittiesitys

    Returns:
        bytearray: tavut
    """
    byte_array = bytearray()
    # lisää bittien alkuu extra tavu, joka kertoo extra bittien määrän
    bits = get_additional_bits(bits) + bits
    for i in range(0, len(bits), 8):
        byte = (bits[i:i+8])
        byte_array.append(int(byte, 2))
    return bytes(byte_array)


def get_additional_bits(bits):
    """Laskee extra bitit bittiesityksen alkuun,
        jotta bittiesitys on oikean kokoinen.

    Args:
        bits (str): bittiesitys

    Returns:
        str: extra bittienmäärä bitteinä + extra bitit
    """
    count = 8 - (len(bits) % 8)
    count_in_bits = "{0:08b}".format(count)
    print(count_in_bits + count * "0")
    return count_in_bits + count * "0"


def bytes_to_bits(in_bytes):
    """Muuttaa tavut bittiesitykseksi.

    Args:
        in_bytes (bytes): tavut

    Returns:
        str: bittiesitys merkkijonona
    """

    bits = ""
    for byte in in_bytes:
        bits += bin(byte)[2:].rjust(8, "0")

    return bits
