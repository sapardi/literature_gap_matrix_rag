# ANALISIS MENDALAM LITERATURE GAP MATRIX
## Penguatan Keamanan Siber Penyelenggaraan Jaminan Kesehatan Nasional (JKN) Melalui AI-Based Data Loss Prevention (DLP) dan Retrieval-Augmented Generation (RAG)

### 1. Pendahuluan dan Konteks Strategis JKN
Penyelenggaraan Jaminan Kesehatan Nasional (JKN) oleh BPJS Kesehatan mengelola data lebih dari 265 juta penduduk Indonesia, menjadikannya salah satu repository data kesehatan dan kependudukan terbesar di Asia Tenggara. Skala masif ini menjadikan infrastruktur JKN sebagai target strategis serangan siber, pencurian identitas, serta potensi kebocoran data pribadi (Protected Health Information / PHI) dan klaim medis. Integrasi Large Language Models (LLM) dan arsitektur Retrieval-Augmented Generation (RAG) dalam layanan operasional JKN (seperti chatbot layanan peserta, verifikasi klaim otomatis, dan portal faskes) menawarkan efisiensi tinggi, namun di sisi lain memperluas permukaan serangan (attack surface) secara signifikan.

### 2. Sintesis Temuan Literatur dan Kesenjangan Riset (Research Gap)
Berdasarkan analisis dari 8 literatur utama yang merepresentasikan kemutakhiran riset global (Elsevier, IEEE, Springer, arXiv, Zenodo, 2024-2026), teridentifikasi beberapa pola dan kesenjangan krusial:
- **Kerentanan pada Lapisan Retrieval & Generasi:** Studi oleh arXiv:2511.11347 dan arXiv:2605.00796 membuktikan bahwa arsitektur RAG rentan terhadap embedding inversion, prompt injection, serta kebocoran log percakapan pasien dan konfigurasi backend melalui inspeksi browser sederhana tanpa autentikasi ketat. Pada konteks JKN, kelemahan ini dapat berakibat fatal terhadap kerahasiaan rekam medis peserta.
- **Keterbatasan Mekanisme Pertahanan Eksisting:** Pendekatan Differential Privacy (DP) konvensional terbukti mendistorsi akurasi teks medis dan mengalami kehabisan anggaran privasi (privacy budget exhaustion), sementara enkripsi penuh (FHE) menimbulkan overhead komputasi yang tinggi jika tidak dioptimalkan. Pendekatan hibrida seperti SecureRAG (FHE + ABE) dan LPRAG (Adaptive Local Differential Privacy) menawarkan solusi proteksi tingkat entitas yang lebih baik.
- **Ketiadaan Lapisan DLP Cerdas pada Interaksi LLM:** Sebagian besar sistem RAG medis belum mengintegrasikan proxy Data Loss Prevention (DLP) berbasis AI multi-agen secara real-time. Riset seperti Zenodo:23618658 menunjukkan perlunya arsitektur Zero-Trust dengan Layer-1 Regex, Layer-2 Neural PII Detection, dan Layer-3 RAG Semantic Policy Auditing untuk menghentikan eksfiltrasi data secara proaktif sebelum mencapai model generatif.

### 3. Arah Riset Masa Depan (Future Work) untuk JKN
Untuk mengamankan ekosistem JKN berbasis AI, riset masa depan harus fokus pada:
1. Penerapan Zero-Trust Multi-Agent DLP Proxy yang disesuaikan dengan regulasi UU Pelindungan Data Pribadi (UU PDP) dan regulasi BPJS Kesehatan.
2. Pengembangan Kebijakan Akses Berbasis Atribut (ABAC) dan Policy-Based Access Control (PBAC) yang terintegrasi dengan OIDC dan enkripsi homomorfik untuk pencarian rekam medis peserta JKN secara terdistribusi di ribuan fasilitas kesehatan mitra (Rumah Sakit, Klinik, Puskesmas).
3. Automated Privacy and Security Benchmarking Tools yang khusus memvalidasi ketahanan chatbot layanan JKN terhadap eksfiltrasi data sensitif dan manipulasi prompt injection.
