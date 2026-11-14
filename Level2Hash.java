import java.nio.charset.StandardCharsets;

public class Level2Hash {

    static final String USERNAME = "manuel";
    static final int SEED = 0x1234;   // constante de 16 bits (param_2)


    static int rotarIzq(int valor16, int n) {
        valor16 &= 0xFFFF;
        n &= 0xF;
        return (valor16 >>> ((0x10 - n) & 0x1F)) | (valor16 << n);
    }

    /** Equivale a FUN_1400019b1. */
    static int hash16(String texto, int semilla) {
        int localA = semilla & 0xFFFF;
        System.out.printf("Semilla inicial: 0x%04X%n%n", localA);

        byte[] bytes = texto.getBytes(StandardCharsets.UTF_8);
        for (int i = 0; i < bytes.length; i++) {
            int b = bytes[i] & 0xFF;                      // (byte)param_1[i]
            System.out.printf("--- Iteracion %d: caracter '%c' ---%n", i + 1, (char) b);
            System.out.printf("ASCII decimal        : %d%n", b);
            System.out.printf("ASCII hex (16 bits)  : 0x%04X%n", b);

            int xor = localA ^ b;

            int producto32 = xor * -0x61C9;               // int de 32 bits

            int recortado = producto32 & 0xFFFF;          // convierto implicito a ushort

            int rotado32 = rotarIzq(recortado, 3);

            localA = rotado32 & 0xFFFF;                   // local_a = (ushort)uVar1
            System.out.printf("resultado parcial para local_a (16 bits)    : 0x%04X%n%n", localA);
        }
        return localA;
    }

    public static void main(String[] args) {
        int resultado = hash16(USERNAME, SEED);
        System.out.printf("RESULTADO FINAL: 0x%04X%n", resultado);
    }
}
