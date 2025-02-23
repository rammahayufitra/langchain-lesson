# langchain-lesson

## 📝 Penjelasan Kode Lesson 1
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

## 📝 **Penjelasan Kode Lesson 2**  

Kode ini menggunakan **LangChain** dan **Ollama** untuk menjalankan model **DeepSeek-R1 (1.5B)** dalam menghasilkan sinonim dari sebuah kata dengan format yang telah ditentukan.  

### **📌 Fitur Utama**  

1. **Menggunakan `OllamaLLM`**  
   - Menghubungkan model **DeepSeek-R1 (1.5B)** dengan **LangChain**.  
   - `temperature=0.7` → Memberikan hasil yang lebih bervariasi dan kreatif.  

2. **Menggunakan `ChatPromptTemplate` untuk Template Prompt**  
   - **Pesan Sistem (`system`)** → Menentukan format respons yang diinginkan.  
   - **Pesan Pengguna (`human`)** → Berisi input yang diberikan oleh pengguna.  

3. **Membuat Rantai Pemrosesan (`chain`)**  
   - **`prompt | llm`** → Menghubungkan template prompt dengan model LLM.  
   - **`chain.invoke({"input": "happy"})`** → Meminta model untuk menghasilkan sinonim dari kata "happy".  

### **📌 Contoh Keluaran**  
Jika dijalankan, kode ini akan mencetak 10 sinonim dari kata **"happy"**, misalnya:  

```
joyful, cheerful, delighted, content, elated, ecstatic, jubilant, gleeful, satisfied, blissful
```

### **🚀 Kegunaan**  
- **Membantu pengayaan kosa kata** untuk penulisan kreatif.  
- **Dapat diperluas untuk berbagai aplikasi NLP**, seperti **chatbot** atau **alat bantu penulisan**.


