import streamlit as st

st.set_page_config(page_title="Kalkulator Kimia", page_icon="🧪")

st.title("🧪 Kalkulator Konsentrasi Larutan")
st.markdown("**Program Studi: Analisis Kimia**")

menu = st.selectbox("Pilih jenis perhitungan:", [
    "Hitung Molaritas", 
    "Hitung Normalitas", 
    "Hitung Pengenceran", 
    "Konversi ppm / persen"
])

if menu == "Hitung Molaritas":
    st.subheader("🔹 Molaritas (mol/L)")
    massa = st.number_input("Masukkan massa zat (gram)", format="%.4f")
    mr = st.number_input("Masukkan Mr (massa molar)", format="%.4f")
    volume_ml = st.number_input("Masukkan volume larutan (mL)", format="%.2f")

    if st.button("Hitung Molaritas"):
        try:
            mol = massa / mr
            molaritas = mol / (volume_ml / 1000)
            st.success(f"Molaritas = {molaritas:.3f} mol/L")
        except:
            st.error("Pastikan semua input terisi dan bukan nol.")

elif menu == "Hitung Normalitas":
    st.subheader("🔹 Normalitas (eq/L)")
    massa = st.number_input("Masukkan massa zat (gram)", format="%.4f")
    mr = st.number_input("Masukkan Mr (massa molar)", format="%.4f")
    valensi = st.number_input("Masukkan valensi zat", format="%.0f")
    volume_ml = st.number_input("Masukkan volume larutan (mL)", format="%.2f")

    if st.button("Hitung Normalitas"):
        try:
            mol = massa / mr
            eq = mol * valensi
            normalitas = eq / (volume_ml / 1000)
            st.success(f"Normalitas = {normalitas:.3f} N")
        except:
            st.error("Input tidak valid.")

elif menu == "Hitung Pengenceran":
    st.subheader("🔹 Rumus M1V1 = M2V2")
    st.markdown("Kosongkan 1 nilai untuk dihitung")

    M1 = st.text_input("M1 (mol/L)", "")
    V1 = st.text_input("V1 (mL)", "")
    M2 = st.text_input("M2 (mol/L)", "")
    V2 = st.text_input("V2 (mL)", "")

    if st.button("Hitung Pengenceran"):
        try:
            M1 = float(M1.replace(",", ".")) if M1 else None
            V1 = float(V1.replace(",", ".")) if V1 else None
            M2 = float(M2.replace(",", ".")) if M2 else None
            V2 = float(V2.replace(",", ".")) if V2 else None

            if M1 is None:
                result = (M2 * V2) / V1
                st.success(f"M1 = {result:.3f} mol/L")
            elif V1 is None:
                result = (M2 * V2) / M1
                st.success(f"V1 = {result:.3f} mL")
            elif M2 is None:
                result = (M1 * V1) / V2
                st.success(f"M2 = {result:.3f} mol/L")
            elif V2 is None:
                result = (M1 * V1) / M2
                st.success(f"V2 = {result:.3f} mL")
            else:
                st.warning("Kosongkan salah satu nilai.")

        except:
            st.error("Input tidak valid.")

elif menu == "Konversi ppm / persen":
    st.subheader("🔹 Konversi Konsentrasi")

    opsi = st.radio("Pilih konversi:", [
        "gram/L ke ppm", 
        "ppm ke gram/L", 
        "gram/100mL ke persen", 
        "persen ke gram/100mL"
    ])

    if opsi == "gram/L ke ppm":
        gram = st.number_input("Masukkan gram/L", format="%.4f")
        if st.button("Hitung ppm"):
            ppm = gram * 1000
            st.success(f"Hasil: {ppm:.2f} ppm")

    elif opsi == "ppm ke gram/L":
        ppm = st.number_input("Masukkan ppm", format="%.2f")
        if st.button("Hitung gram/L"):
            gram = ppm / 1000
            st.success(f"Hasil: {gram:.4f} gram/L")

    elif opsi == "gram/100mL ke persen":
        gram = st.number_input("Masukkan gram per 100 mL", format="%.4f")
        if st.button("Hitung %"):
            persen = gram
            st.success(f"Hasil: {persen:.2f} %")

    elif opsi == "persen ke gram/100mL":
        persen = st.number_input("Masukkan %", format="%.2f")
        if st.button("Hitung gram/100mL"):
            gram = persen
            st.success(f"Hasil: {gram:.2f} gram/100 mL")
