
import streamlit as st

st.set_page_config(
    page_title="HobiKu | Smart Hobby Finder",
    page_icon="✨",
    layout="wide"
)

# =========================
# DESAIN HALAMAN
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --orange-50: #fff7ed;
    --orange-100: #ffedd5;
    --orange-200: #fed7aa;
    --orange-300: #fdba74;
    --orange-400: #fb923c;
    --orange-500: #f97316;
    --orange-600: #ea580c;
    --orange-700: #c2410c;
    --orange-800: #9a3412;
    --orange-900: #7c2d12;
}

.stApp {
    background:
        radial-gradient(circle at 5% 5%, #ffedd5 0, transparent 28%),
        radial-gradient(circle at 95% 10%, #fed7aa 0, transparent 25%),
        #fffaf5;
    font-family: 'DM Sans', sans-serif;
    color: var(--orange-900);
}

.block-container {
    max-width: 1150px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p, label {
    font-family: 'DM Sans', sans-serif;
}

.hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(125deg, #9a3412 0%, #c2410c 45%, #f97316 100%);
    padding: 2.5rem;
    border-radius: 28px;
    color: white;
    margin-bottom: 1.8rem;
    box-shadow: 0 16px 36px #c2410c25;
}

.hero:after {
    content: "✦";
    position: absolute;
    right: 35px;
    top: 10px;
    font-size: 8rem;
    color: #ffffff12;
    transform: rotate(12deg);
}

.eyebrow {
    display: inline-block;
    border: 1px solid #ffffff65;
    background: #ffffff20;
    border-radius: 30px;
    padding: 7px 13px;
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: 1px;
}

.hero h1 {
    color: white !important;
    font-family: 'Manrope', sans-serif;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800;
    line-height: 1.2;
    margin: 17px 0 12px;
    max-width: 750px;
}

.hero p {
    color: #fff7ed !important;
    max-width: 700px;
    line-height: 1.8;
    font-size: 1rem;
    margin-bottom: 18px;
}

.hero-chip {
    display: inline-block;
    padding: 8px 12px;
    margin: 3px 5px 0 0;
    border-radius: 11px;
    background: #ffffff20;
    border: 1px solid #ffffff25;
    color: white;
    font-size: .82rem;
}

.section-title {
    color: var(--orange-900);
    font-family: 'Manrope', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #9a6a50;
    margin-bottom: 1.1rem;
    line-height: 1.6;
}

.panel-label {
    color: var(--orange-700);
    font-weight: 800;
    font-size: .78rem;
    letter-spacing: .8px;
    margin: 1rem 0 .7rem;
}

div[data-testid="stCheckbox"] {
    background: #fffaf5;
    border: 1px solid #ffdfc2;
    border-radius: 13px;
    padding: 9px 11px;
    margin-bottom: 7px;
    transition: all .2s ease;
}

div[data-testid="stCheckbox"]:hover {
    background: var(--orange-50);
    border-color: var(--orange-400);
}

div[data-testid="stCheckbox"] label {
    color: var(--orange-900);
}

div[data-testid="stNumberInput"] input {
    border-radius: 12px;
}

div[data-testid="stRadio"] label {
    color: var(--orange-900);
}

.stButton > button,
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(100deg, #c2410c, #f97316);
    color: white;
    border: 0;
    border-radius: 13px;
    padding: .8rem 1rem;
    font-weight: 800;
    box-shadow: 0 8px 20px #c2410c25;
    transition: all .2s ease;
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] button:hover {
    color: white;
    border: 0;
    background: linear-gradient(100deg, #9a3412, #ea580c);
    transform: translateY(-1px);
}

div[data-testid="stForm"] {
    background: white;
    border: 1px solid #f5d6bd;
    border-radius: 22px;
    padding: 1.3rem;
    box-shadow: 0 8px 28px #9a34120a;
}

.metric-card {
    background: white;
    border: 1px solid #f5d6bd;
    border-radius: 18px;
    padding: 1.1rem;
    box-shadow: 0 7px 22px #9a34120a;
    min-height: 125px;
}

.metric-icon {
    font-size: 1.5rem;
}

.metric-value {
    color: var(--orange-800);
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
    font-size: 1.45rem;
    margin-top: 5px;
    overflow-wrap: anywhere;
}

.metric-label {
    color: #9a6a50;
    font-size: .82rem;
    margin-top: 3px;
}

.activity-card {
    background: white;
    border: 1px solid #f5d6bd;
    border-radius: 21px;
    padding: 1.25rem;
    min-height: 245px;
    margin-bottom: 1rem;
    box-shadow: 0 8px 24px #9a34120a;
    transition: all .2s ease;
}

.activity-card:hover {
    border-color: var(--orange-400);
    box-shadow: 0 12px 28px #c2410c12;
    transform: translateY(-2px);
}

.activity-top {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 14px;
}

.activity-icon {
    min-width: 52px;
    height: 52px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #fff7ed, #fed7aa);
    border: 1px solid #ffdfc2;
    border-radius: 16px;
    font-size: 1.7rem;
}

.activity-category {
    color: var(--orange-600);
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: .7px;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.activity-name {
    color: var(--orange-900);
    font-family: 'Manrope', sans-serif;
    font-size: 1rem;
    font-weight: 800;
    line-height: 1.4;
}

.activity-description {
    color: #8b6957;
    font-size: .88rem;
    line-height: 1.7;
    min-height: 48px;
}

.chips {
    margin: 13px 0;
}

.chip {
    display: inline-block;
    background: var(--orange-50);
    border: 1px solid #ffdfc2;
    color: var(--orange-800);
    border-radius: 9px;
    padding: 6px 9px;
    margin: 2px 3px 2px 0;
    font-size: .75rem;
    font-weight: 700;
}

.activity-reason {
    border-top: 1px solid #fbe4d2;
    padding-top: 12px;
    color: #8b6957;
    font-size: .83rem;
    line-height: 1.7;
}

.activity-reason strong {
    color: var(--orange-700);
}

.empty-state {
    text-align: center;
    background: white;
    border: 1px dashed #fdba74;
    border-radius: 23px;
    padding: 2.4rem 1.2rem;
    box-shadow: 0 8px 24px #9a341208;
}

.empty-icon {
    font-size: 2.8rem;
    margin-bottom: 8px;
}

.empty-state h3 {
    color: var(--orange-800);
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
}

.empty-state p {
    color: #9a6a50;
    line-height: 1.7;
}

div[data-testid="stAlert"] {
    border-radius: 13px;
}

div[data-testid="stExpander"] {
    border: 1px solid #f5d6bd;
    border-radius: 13px;
    background: white;
}

.footer {
    text-align: center;
    color: #b08972;
    border-top: 1px solid #f5d6bd;
    padding-top: 1.2rem;
    margin-top: 2.2rem;
    font-size: .8rem;
    line-height: 1.8;
}

hr {
    border-color: #f5d6bd;
}
</style>
""", unsafe_allow_html=True)


# =========================
# DATA DAN ATURAN AKTIVITAS
# Tetap 15 aktivitas dan 13 fasilitas
# =========================
AKTIVITAS = [
    {
        "nama": "Membaca Buku",
        "ikon": "📚",
        "kategori": "Santai dan Literasi",
        "deskripsi": "Baca novel, buku pengetahuan, atau e-book untuk menambah wawasan.",
        "waktu": 15, "biaya": 0,
        "lokasi": ["Di dalam ruangan"],
        "fasilitas": ["buku"],
        "alasan": "Waktu minimal 15 menit, lokasi dalam ruangan, dan tersedia buku atau e-book."
    },
    {
        "nama": "Menggambar atau Sketsa",
        "ikon": "🎨",
        "kategori": "Kreativitas",
        "deskripsi": "Tuangkan ide melalui gambar, ilustrasi, atau latihan sketsa.",
        "waktu": 20, "biaya": 5000,
        "lokasi": ["Di dalam ruangan"],
        "fasilitas": ["alat_gambar"],
        "alasan": "Waktu minimal 20 menit, alat gambar tersedia, dan anggaran minimal Rp5.000."
    },
    {
        "nama": "Menulis Jurnal atau Cerita",
        "ikon": "✍️",
        "kategori": "Kreativitas",
        "deskripsi": "Catat pengalaman harian, ide, atau cerita pendek.",
        "waktu": 15, "biaya": 0,
        "lokasi": ["Di dalam ruangan"],
        "fasilitas": ["alat_tulis"],
        "alasan": "Waktu minimal 15 menit dan tersedia buku catatan atau alat tulis."
    },
    {
        "nama": "Merajut",
        "ikon": "🧶",
        "kategori": "Kerajinan",
        "deskripsi": "Buat kerajinan kecil sambil melatih ketelitian dan kesabaran.",
        "waktu": 30, "biaya": 15000,
        "lokasi": ["Di dalam ruangan"],
        "fasilitas": ["benang_rajut"],
        "alasan": "Waktu minimal 30 menit, perlengkapan rajut tersedia, dan anggaran minimal Rp15.000."
    },
    {
        "nama": "Memasak Menu Sederhana",
        "ikon": "🍳",
        "kategori": "Kuliner",
        "deskripsi": "Coba resep sederhana dan pelajari teknik dasar memasak.",
        "waktu": 30, "biaya": 10000,
        "lokasi": ["Di dalam ruangan"],
        "fasilitas": ["masak"],
        "alasan": "Waktu minimal 30 menit, perlengkapan dapur tersedia, dan anggaran minimal Rp10.000."
    },
    {
        "nama": "Tantangan Puzzle atau Teka-Teki",
        "ikon": "🧩",
        "kategori": "Logika dan Tantangan",
        "deskripsi": "Asah logika dengan puzzle, teka-teki angka, sudoku, atau permainan asah otak.",
        "waktu": 15, "biaya": 0,
        "lokasi": ["Di dalam ruangan"],
        "fasilitas": ["alat_tulis"],
        "alasan": "Waktu minimal 15 menit, lokasi dalam ruangan, dan tersedia alat tulis untuk mencatat jawaban. Puzzle digital juga dapat digunakan."
    },
    {
        "nama": "Bersepeda Santai",
        "ikon": "🚴",
        "kategori": "Aktivitas Fisik",
        "deskripsi": "Jelajahi lingkungan sekitar sambil menikmati udara luar.",
        "waktu": 30, "biaya": 0,
        "lokasi": ["Di luar ruangan"],
        "fasilitas": ["sepeda"],
        "alasan": "Waktu minimal 30 menit, lokasi luar ruangan, dan sepeda tersedia."
    },
    {
        "nama": "Jogging atau Jalan Cepat",
        "ikon": "🏃",
        "kategori": "Aktivitas Fisik",
        "deskripsi": "Lakukan aktivitas ringan di luar ruangan sesuai kemampuan.",
        "waktu": 20, "biaya": 0,
        "lokasi": ["Di luar ruangan"],
        "fasilitas": ["sepatu_lari"],
        "alasan": "Waktu minimal 20 menit, lokasi luar ruangan, dan perlengkapan olahraga tersedia."
    },
    {
        "nama": "Yoga atau Peregangan",
        "ikon": "🧘",
        "kategori": "Relaksasi",
        "deskripsi": "Lakukan peregangan sederhana untuk membantu tubuh terasa rileks.",
        "waktu": 20, "biaya": 0,
        "lokasi": ["Di dalam ruangan"],
        "fasilitas": ["matras_yoga"],
        "alasan": "Waktu minimal 20 menit, lokasi dalam ruangan, dan matras yoga tersedia."
    },
    {
        "nama": "Meditasi dan Latihan Pernapasan",
        "ikon": "🌿",
        "kategori": "Relaksasi",
        "deskripsi": "Luangkan waktu untuk duduk tenang dan berlatih pernapasan teratur.",
        "waktu": 10, "biaya": 0,
        "lokasi": ["Di dalam ruangan"],
        "fasilitas": [],
        "alasan": "Waktu minimal 10 menit dan tidak memerlukan perlengkapan khusus."
    },
    {
        "nama": "Podcast atau Audiobook",
        "ikon": "🎧",
        "kategori": "Audio dan Belajar",
        "deskripsi": "Dengarkan cerita, diskusi, atau materi pengetahuan sesuai minat.",
        "waktu": 20, "biaya": 0,
        "lokasi": ["Di dalam ruangan", "Di luar ruangan"],
        "fasilitas": ["earphone"],
        "alasan": "Waktu minimal 20 menit dan tersedia earphone atau headset."
    },
    {
        "nama": "Belajar Bahasa Asing Online",
        "ikon": "🌐",
        "kategori": "Pengembangan Diri",
        "deskripsi": "Pelajari kosakata dan latihan bahasa melalui sumber digital.",
        "waktu": 15, "biaya": 0,
        "lokasi": ["Di dalam ruangan"],
        "fasilitas": ["laptop"],
        "alasan": "Waktu minimal 15 menit, lokasi dalam ruangan, dan perangkat digital tersedia."
    },
    {
        "nama": "Merawat Tanaman",
        "ikon": "🪴",
        "kategori": "Alam dan Lingkungan",
        "deskripsi": "Siram tanaman, rapikan daun, atau rawat tanaman dalam pot.",
        "waktu": 20, "biaya": 5000,
        "lokasi": ["Di luar ruangan"],
        "fasilitas": ["tanaman"],
        "alasan": "Waktu minimal 20 menit, lokasi luar ruangan, tanaman tersedia, dan anggaran minimal Rp5.000."
    },
    {
        "nama": "Fotografi dengan Ponsel",
        "ikon": "📸",
        "kategori": "Kreativitas",
        "deskripsi": "Latih komposisi foto dengan menangkap objek di sekitar.",
        "waktu": 15, "biaya": 0,
        "lokasi": ["Di dalam ruangan", "Di luar ruangan"],
        "fasilitas": ["kamera"],
        "alasan": "Waktu minimal 15 menit dan tersedia kamera atau ponsel berkamera."
    },
    {
        "nama": "Dance Challenge",
        "ikon": "💃",
        "kategori": "Musik dan Gerak",
        "deskripsi": "Coba koreografi pendek dari lagu favorit atau buat gerakan sendiri untuk bersenang-senang.",
        "waktu": 15, "biaya": 0,
        "lokasi": ["Di dalam ruangan", "Di luar ruangan"],
        "fasilitas": ["earphone"],
        "alasan": "Waktu minimal 15 menit dan tersedia earphone untuk mendengarkan musik. Pastikan ruang gerak aman dan cukup luas."
    }
]

NAMA_FASILITAS = {
    "buku": "Buku / Novel / E-Book",
    "alat_gambar": "Alat gambar / sketsa",
    "alat_tulis": "Buku catatan / alat tulis",
    "masak": "Perlengkapan memasak / dapur",
    "benang_rajut": "Benang rajut dan jarum",
    "matras_yoga": "Matras yoga / alas olahraga",
    "tanaman": "Tanaman / alat berkebun",
    "kamera": "Kamera / ponsel berkamera",
    "sepeda": "Sepeda dan perlengkapan keselamatan",
    "sepatu_lari": "Sepatu lari / pakaian olahraga",
    "earphone": "Earphone / headset",
    "laptop": "Laptop / komputer / tablet"
}


# =========================
# FUNGSI SISTEM BERBASIS ATURAN
# =========================
def periksa_aturan(aktivitas, waktu, anggaran, lokasi, fasilitas):
    """
    Aturan produksi:
    IF waktu mencukupi
    AND anggaran mencukupi
    AND lokasi sesuai
    AND fasilitas wajib tersedia
    THEN rekomendasikan aktivitas.
    """
    kondisi_waktu = waktu >= aktivitas["waktu"]
    kondisi_anggaran = anggaran >= aktivitas["biaya"]
    kondisi_lokasi = lokasi in aktivitas["lokasi"]

    kondisi_fasilitas = all(
        fasilitas.get(nama, False)
        for nama in aktivitas["fasilitas"]
    )

    return (
        kondisi_waktu
        and kondisi_anggaran
        and kondisi_lokasi
        and kondisi_fasilitas
    )


def rupiah(nilai):
    return "Rp" + f"{nilai:,.0f}".replace(",", ".")


# =========================
# HEADER UTAMA
# =========================
st.markdown("""
<div class="hero">
    <span class="eyebrow">✦ SMART HOBBY FINDER</span>
    <h1>Waktu luangmu, petualangan barumu.</h1>
    <p>
        Bingung mau melakukan apa saat punya waktu luang?
        Temukan ide aktivitas yang sesuai dengan waktu, anggaran, lokasi,
        dan fasilitas yang kamu miliki. Pilih kondisimu, lalu biarkan
        HobiKu mencarikan rekomendasi berdasarkan aturan IF–THEN.
    </p>
    <span class="hero-chip">⏱️ Atur waktumu</span>
    <span class="hero-chip">💰 Sesuaikan anggaran</span>
    <span class="hero-chip">📍 Pilih lokasi</span>
    <span class="hero-chip">✨ Temukan ide baru</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">01 · Kenali kondisimu</div>
<div class="section-subtitle">
Isi informasi berikut sesuai kondisi yang kamu miliki agar rekomendasi lebih relevan.
</div>
""", unsafe_allow_html=True)


# =========================
# FORM INPUT
# =========================
with st.form("form_rekomendasi"):
    st.markdown(
        '<div class="panel-label">⏳ WAKTU DAN ANGGARAN</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        waktu = st.number_input(
            "Waktu luang (menit)",
            min_value=0,
            max_value=1440,
            value=30,
            step=5,
            help="Masukkan waktu yang tersedia untuk melakukan aktivitas."
        )

    with c2:
        anggaran = st.number_input(
            "Anggaran tersedia (rupiah)",
            min_value=0,
            max_value=10000000,
            value=0,
            step=5000,
            help="Masukkan jumlah uang yang bersedia kamu gunakan."
        )

    st.markdown(
        '<div class="panel-label">📍 LOKASI AKTIVITAS</div>',
        unsafe_allow_html=True
    )

    lokasi = st.radio(
        "Kamu ingin beraktivitas di mana?",
        ["Di dalam ruangan", "Di luar ruangan"],
        horizontal=True
    )

    st.markdown(
        '<div class="panel-label">🎒 FASILITAS YANG TERSEDIA</div>',
        unsafe_allow_html=True
    )
    st.caption(
        "Centang fasilitas yang kamu miliki. Pilih beberapa jika diperlukan."
    )

    opsi = [
        ("buku", "📚 Buku / E-Book"),
        ("alat_gambar", "🎨 Alat gambar"),
        ("alat_tulis", "✍️ Alat tulis"),
        ("masak", "🍳 Perlengkapan memasak"),
        ("benang_rajut", "🧶 Benang dan jarum rajut"),
        ("matras_yoga", "🧘 Matras yoga"),
        ("tanaman", "🪴 Tanaman / alat berkebun"),
        ("kamera", "📸 Kamera / ponsel berkamera"),
        ("sepeda", "🚴 Sepeda dan perlengkapan keselamatan"),
        ("sepatu_lari", "🏃 Perlengkapan olahraga"),
        ("earphone", "🎧 Earphone / headset"),
        ("laptop", "💻 Laptop / komputer / tablet"),
        ("alat_gambar", "🧩 Kertas atau alat untuk puzzle")
    ]

    fasilitas = {}
    kolom_a, kolom_b = st.columns(2)

    for i, (kunci, label) in enumerate(opsi):
        kolom = kolom_a if i % 2 == 0 else kolom_b
        with kolom:
            nilai = st.checkbox(label, key=f"check_{i}_{kunci}")
            fasilitas[kunci] = fasilitas.get(kunci, False) or nilai

    st.write("")
    cari = st.form_submit_button(
        "✨ Temukan Hobi yang Cocok",
        use_container_width=True
    )


# =========================
# HASIL REKOMENDASI
# =========================
if cari:
    hasil = [
        aktivitas
        for aktivitas in AKTIVITAS
        if periksa_aturan(aktivitas, waktu, anggaran, lokasi, fasilitas)
    ]

    st.write("")
    st.markdown("""
    <div class="section-title">02 · Rekomendasi untukmu</div>
    <div class="section-subtitle">
    Berikut aktivitas yang memenuhi kondisi dan aturan pada sistem.
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">✨</div>
            <div class="metric-value">{len(hasil)}</div>
            <div class="metric-label">Aktivitas yang cocok</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">⏱️</div>
            <div class="metric-value">{waktu} menit</div>
            <div class="metric-label">Waktu tersedia</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">🪙</div>
            <div class="metric-value">{rupiah(anggaran)}</div>
            <div class="metric-label">Anggaran tersedia</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    if hasil:
        st.success(
            f"HobiKu menemukan {len(hasil)} aktivitas yang sesuai dengan kondisimu!"
        )

        for i in range(0, len(hasil), 2):
            kolom_hasil = st.columns(2, gap="medium")

            for kolom, aktivitas in zip(kolom_hasil, hasil[i:i + 2]):
                fasilitas_perlu = (
                    ", ".join(
                        NAMA_FASILITAS.get(f, f)
                        for f in aktivitas["fasilitas"]
                    )
                    if aktivitas["fasilitas"]
                    else "Tidak memerlukan fasilitas khusus"
                )

                with kolom:
                    st.markdown(f"""
                    <div class="activity-card">
                        <div class="activity-top">
                            <div class="activity-icon">{aktivitas["ikon"]}</div>
                            <div>
                                <div class="activity-category">{aktivitas["kategori"]}</div>
                                <div class="activity-name">{aktivitas["nama"]}</div>
                            </div>
                        </div>
                        <div class="activity-description">
                            {aktivitas["deskripsi"]}
                        </div>
                        <div class="chips">
                            <span class="chip">⏱️ Minimal {aktivitas["waktu"]} menit</span>
                            <span class="chip">💰 {rupiah(aktivitas["biaya"])}</span>
                        </div>
                        <div class="activity-reason">
                            <strong>Mengapa cocok?</strong><br>
                            {aktivitas["alasan"]}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    with st.expander("🔎 Lihat pemeriksaan aturan"):
                        st.write(
                            f"**Waktu:** {waktu} ≥ {aktivitas['waktu']} menit — "
                            f"{'Terpenuhi' if waktu >= aktivitas['waktu'] else 'Tidak terpenuhi'}"
                        )
                        st.write(
                            f"**Anggaran:** {rupiah(anggaran)} ≥ "
                            f"{rupiah(aktivitas['biaya'])} — "
                            f"{'Terpenuhi' if anggaran >= aktivitas['biaya'] else 'Tidak terpenuhi'}"
                        )
                        st.write(
                            f"**Lokasi:** {lokasi} — "
                            f"{'Sesuai' if lokasi in aktivitas['lokasi'] else 'Tidak sesuai'}"
                        )
                        st.write(f"**Fasilitas wajib:** {fasilitas_perlu}")

                        semua_fasilitas_ada = all(
                            fasilitas.get(f, False)
                            for f in aktivitas["fasilitas"]
                        )

                        st.write(
                            f"**Pemeriksaan fasilitas:** "
                            f"{'Terpenuhi' if semua_fasilitas_ada else 'Tidak terpenuhi'}"
                        )

                        st.code(
                            f"IF waktu >= {aktivitas['waktu']}\n"
                            f"AND anggaran >= {aktivitas['biaya']}\n"
                            f"AND lokasi sesuai\n"
                            f"AND fasilitas wajib tersedia\n"
                            f"THEN rekomendasikan '{aktivitas['nama']}'",
                            language="text"
                        )

    else:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">🔍</div>
            <h3>Belum ada hobi yang cocok</h3>
            <p>
                Jangan menyerah! Coba tambah waktu luang atau anggaran,
                ubah lokasi, atau centang fasilitas lain yang tersedia.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🧠 Bagaimana HobiKu mengambil keputusan?"):
        st.write(
            "HobiKu menggunakan aturan produksi IF–THEN. Setiap aktivitas "
            "memiliki persyaratan berupa waktu minimal, biaya perkiraan, "
            "lokasi, dan fasilitas. Aktivitas hanya direkomendasikan jika "
            "semua persyaratan yang ditentukan terpenuhi."
        )
        st.code(
            "IF waktu >= waktu_minimal\n"
            "AND anggaran >= biaya_minimal\n"
            "AND lokasi sesuai\n"
            "AND fasilitas wajib tersedia\n"
            "THEN aktivitas direkomendasikan",
            language="text"
        )
        st.caption(
            "Nilai waktu dan biaya adalah perkiraan untuk keperluan proyek, "
            "bukan harga atau durasi yang berlaku untuk semua orang."
        )

else:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">🍊</div>
        <h3>Siap mencoba sesuatu yang baru?</h3>
        <p>
            Isi waktu luang, anggaran, lokasi, dan fasilitas yang tersedia.
            Tekan tombol di atas untuk menemukan aktivitas yang sesuai denganmu.
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    HobiKu · Smart Hobby Finder<br>
    Sistem Rekomendasi Aktivitas Berbasis Aturan Produksi IF–THEN<br>
    15 pilihan aktivitas · 13 pilihan fasilitas
</div>
""", unsafe_allow_html=True)
