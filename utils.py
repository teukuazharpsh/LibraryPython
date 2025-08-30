def konversi_suhu(nilai, dari, ke):
    # Normalisasi input jadi huruf kecil
    dari = dari.lower()
    ke = ke.lower()

    # Validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan harus 'C', 'F', atau 'K'."

    # Validasi nilai suhu
    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."

    # Jika satuan sama -> return langsung
    if dari == ke:
        return nilai

    # Konversi suhu
    hasil = None
    if dari == "c":  # dari Celsius
        if ke == "f":
            hasil = (nilai * 9/5) + 32
        elif ke == "k":
            hasil = nilai + 273.15

    elif dari == "f":  # dari Fahrenheit
        if ke == "c":
            hasil = (nilai - 32) * 5/9
        elif ke == "k":
            hasil = (nilai - 32) * 5/9 + 273.15

    elif dari == "k":  # dari Kelvin
        if ke == "c":
            hasil = nilai - 273.15
        elif ke == "f":
            hasil = (nilai - 273.15) * 9/5 + 32

    return hasil
