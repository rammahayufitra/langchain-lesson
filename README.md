# langchain-lesson

<b>lesson 1.py</b> <br>
Kode ini menggunakan LangChain dengan model DeepSeek-R1 (1.5B) yang dijalankan melalui Ollama untuk memproses teks.

OllamaLLM digunakan untuk menghubungkan model LLM lokal dengan LangChain dan mengatur beberapa parameter salah satunya adalah temperature. <br>
temperature digunakan untuk mengontrol kreativitas respons model yang memiliki rentang nilai <br>
Nilai rendah (misal: 0.1 - 0.3) → Jawaban lebih deterministik dan fokus. <br>
Nilai tinggi (misal: 0.7 - 1.0) → Jawaban lebih kreatif dan bervariasi. <br>
sedangkan untuk mendapatkan response dari model LLM ada tigae metode yang perbedaannya dijelaskan pada tabel dibawah

🔥 **Perbedaan Utama**
| Metode          | Input                | Output                   | Kapan Digunakan? |
|----------------|--------------------|-------------------------|------------------|
| `invoke()`    | Satu prompt        | Satu string             | Pertanyaan tunggal |
| `batch()`     | Daftar prompt      | Daftar string           | Memproses banyak prompt sekaligus |
| `stream()`    | Satu prompt        | Generator (streaming)   | Respons panjang secara real-time |

cara menjalankan code lesson1.py <br>
$ python3 lesson1.py


