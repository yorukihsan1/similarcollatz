def collatz_variation(start):
    """
    Belirttiğiniz kurallara göre Collatz benzeri diziyi oluşturur.
    Kurallar:
    1. Tek sayı ise: x = x / 2 + 0.5
    2. Çift sayı ise: x = 3x + 1
    """
    sequence = []
    current = start
    visited = set()

    while current not in visited:  # Döngü kontrolü
        sequence.append(current)
        visited.add(current)

        if current % 2 == 1:  # Tek sayı
            current = current / 2 + 0.5
        else:  # Çift sayı
            current = 3 * current + 1

    # Döngüyü belirleme
    cycle_start = sequence.index(current)
    cycle = sequence[cycle_start:]

    return sequence, cycle


# Kullanıcıdan değer alma
try:
    start_value = int(input("Başlangıç sayısını girin: "))
    if start_value <= 0:
        print("Lütfen pozitif bir tam sayı girin.")
    else:
        seq, cyc = collatz_variation(start_value)
        print(f"\nBaşlangıç sayısı: {start_value}")
        print(f"Dizi: {seq}")
        print(f"Döngü: {cyc}")
except ValueError:
    print("Lütfen geçerli bir tam sayı girin!")
