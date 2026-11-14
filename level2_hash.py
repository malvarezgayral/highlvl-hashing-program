USERNAME = "manuel"
SEED = 0x1234          # constante de 16 bits (param_2)


def rotar_izq_3(valor16, n=3):
    """Equivale a FUN_14000149c: rotacion a la izquierda de n bits (16 bits).
    El programa original calcula en 32 bits, asi que el resultado puede
    tener mas de 16 bits; quien llama lo recorta despues."""
    valor16 &= 0xFFFF
    n &= 0xF
    return (valor16 >> ((0x10 - n) & 0x1F)) | (valor16 << n)


def hash16(texto, semilla):
    """Equivale a FUN_1400019b1."""
    local_a = semilla & 0xFFFF
    print(f"Semilla inicial: 0x{local_a:04X}\n")

    for i, byte in enumerate(texto.encode("utf-8")):   # (byte)param_1[i]
        print(f"--- Iteracion {i + 1}: caracter '{chr(byte)}' ---")
        print(f"ASCII decimal        : {byte}")
        print(f"ASCII hex (16 bits)  : 0x{byte:04X}")

        xor = local_a ^ byte
        print(f"local_a ^ caracter   : 0x{local_a:04X} ^ 0x{byte:04X} = 0x{xor:04X}")

        # En C: int * int de 32 bits (-0x61c9 = 0xFFFF9E37 en complemento a 2)
        producto32 = (xor * -0x61C9) & 0xFFFFFFFF
        print(f"Producto (32 bits)   : 0x{xor:04X} * -0x61C9 = 0x{producto32:08X}")

        recortado = producto32 & 0xFFFF       # conversion implicita a ushort
        print(f"Recorte a 16 bits    : 0x{recortado:04X}")

        rotado32 = rotar_izq_3(recortado, 3)
        print(f"Rotacion 3 bits (32) : 0x{rotado32:05X}")

        local_a = rotado32 & 0xFFFF           # local_a = (ushort)uVar1
        print(f"local_a (16 bits)    : 0x{local_a:04X}\n")

    return local_a


if __name__ == "__main__":
    resultado = hash16(USERNAME, SEED)
    print(f"RESULTADO FINAL: 0x{resultado:04X}")
