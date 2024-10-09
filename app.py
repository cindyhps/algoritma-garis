import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from algoritma import bruteforce, dda, bresenham

# Fungsi untuk menampilkan grafik kartesius
def plot_graph(points, title):
    fig, ax = plt.subplots()
    ax.plot(*zip(*points), marker='o')
    ax.set_title(title)
    ax.set_xlim([min(p[0] for p in points)-1, max(p[0] for p in points)+1])
    ax.set_ylim([min(p[1] for p in points)-1, max(p[1] for p in points)+1])
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    st.pyplot(fig)

# Judul web
st.title("Visualisasi Algoritma Garis")

# Input form
with st.form("input_form"):
    x1 = st.number_input("X1", value=0, step=1)
    y1 = st.number_input("Y1", value=0, step=1)
    x2 = st.number_input("X2", value=10, step=1)
    y2 = st.number_input("Y2", value=10, step=1)
    algorithm = st.selectbox("Pilih Algoritma", ('Brute Force', 'DDA', 'Bresenham'))
    submit = st.form_submit_button("Submit")

# Reset button
if st.button("Reset"):
    st.experimental_rerun()

# Jika form disubmit
if submit:
    points, iter_count, iter_steps = [], 0, []
    
    # Pemilihan algoritma
    if algorithm == 'Brute Force':
        points, iter_count, iter_steps = bruteforce.brute_force(x1, y1, x2, y2)
    elif algorithm == 'DDA':
        points, iter_count, iter_steps = dda.dda(x1, y1, x2, y2)
    elif algorithm == 'Bresenham':
        points, iter_count, iter_steps = bresenham.bresenham(x1, y1, x2, y2)
    
    # Menampilkan Grafik Kartesius
    if points:
        st.subheader(f"Hasil Algoritma {algorithm}")
        plot_graph(points, f"{algorithm} Line Generation")
    else:
        st.error("Tidak ada titik yang dihasilkan oleh algoritma. Pastikan koordinat yang dimasukkan valid.")
    
    # Menampilkan jumlah iterasi
    st.write(f"Total Iterasi: {iter_count}")
    
    # Menyimpan hasil iterasi ke file Excel
    df = pd.DataFrame(iter_steps, columns=['Step', 'X', 'Y'])
    filename = f"{algorithm}_iterasi.xlsx"
    df.to_excel(filename, index=False)
    st.write(f"Detail Iterasi disimpan ke file: {filename}")
    st.download_button(label="Download File Excel", data=open(filename, 'rb').read(), file_name=filename)

   
