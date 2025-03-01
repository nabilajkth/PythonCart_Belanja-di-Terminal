[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Ln5MGAF6)
# Graded Challenge 2

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Conditionals, Loops, dan Functions._

---

## Assignment Instructions

*Graded Challenge 2* dikerjakan dalam format ***Python script (.py)*** dengen beberapa **kriteria wajib** di bawah ini:

1. *Project* dinyatakan selesai dan diterima untuk dinilai jika script dapat dijalankan dengan baik di prompt maupun terminal.

2. Pada tugas Graded Challenge 2, akan diminta untuk membuat:
  - **satu file .py** yang berisikan full program sesuai dengan instruksi soal.
  - satu file gambar screenshot running program dan hasil running.

3. **Tidak diperkenankan** membuat program dalam format jupyter notebook.

4. Masing-masing file **wajib** memberikan keterangan atau pengenalan dengan menggunakan `comment` atau `docstring` yang berisikan Judul tugas, Nama, Batch, dan penjelasan singkat tentang program yang dibuat, fitur-fitur. Contoh:
    ```py
    '''
    =================================================
    Graded Challenge 2

    Nama  : Fahmi Iman Alfarizki
    Batch : CODA-RMT-001

    Program ini dibuat untuk melakukan automatisasi pengolahan (cleaning) data text yang berguna untuk pemodelan model analisa sentimen.
    =================================================
    '''
    ```
5. Tiap class dan method/function diberikan penjelasan mengenai untuk apa class/method ini dan bagaimana alur algoritmanya dengan `docstring`

  ```py
  #Contoh:

  def f(x):
    '''
    Fungsi ini ditujukan untuk menghitung kuadrat angka yang dimasukkan pengguna dengan rumus x^2.

    Argument x merupakan inputan angka berupa bilangan real.

    Contoh penggunaan:
      y = f(2)
      print(y)
      --------
      Output: 4
    '''
    return x**2

  ```

6. **WARNING**: Plagiarisme sekecil apapun dapat terdeteksi. Tugas ini akan diuji tingkat plagiarismenya dengan software khusus.

---

## Assignment Submission

- Simpan assignment pada Graded Challenge 2 ini dengan nama `<nama-student>_app.py` (file app) dan  `<nama-student>_running program.jpg` (screenshot running program - extension bebas). Misal `fahmi-iman_app.py` dan `fahmi-iman_running program.jpg` (**Maksimal nama dua suku kata**).
- Push file Assigment yang telah dibuat ke repository Github Classroom masing-masing student.

---

## Assignment Objectives

*Graded Challenge 2* ini dibuat guna mengevaluasi konsep konsep Conditionals, Loops, dan Functions.

- Mampu menggunakan Python sequence object (list/dictionary) untuk menyimpan data.
- Mampu menerapkan conditional if pada sebuah kasus.
- Mampu menerapkan _while_ loop.
- Mampu membuat function.

---

## Assignment Instructions and Cases

**Case**

Kamu adalah seorang Python developer di perusahaan retail. Kamu diminta untuk membuat program `shopping cart` sederhana yang memungkinkan user untuk menambah, menghapus, dan melihat barang di keranjang belanja (cart) mereka. Tiap barang memiliki informasi nama barang dan harganya. User juga bisa melihat total harga belanjanya.

**Requirements**

1. Buat list atau dictionary untuk menyimpan data barang dalam keranjang belanja.

2. Buat program Shooping Cart yang berisikan fitur untuk menambah barang, menghapus barang, menghitung total belanja, dan menjalankan user-interface aplikasi. Tiap fiturnya harus dibuat dalam function.

3. Program harus berupa menu-based interface dimana user akan berinteraksi dengan shopping cart nya.

  Pilihan menu harus terdapat:
  1. Menambah Barang
  2. Hapus Barang
  3. Tampilkan Barang di Keranjang
  4. Lihat Total Belanja
  5. Exit

  Jika terdapat kesalahan input menu ataupun input nilai yang diminta maka akan muncul pesan error.

  Data yang diinput melalui menu nomor 1 disimpan ke list atau dictionary yang dibuat dan untuk penghapusan barang dari keranjang belanja menyesuaikan cara menghapus item dari list atau dictionary.

4. Gunakan `While Loop` dan `Conditional If` supaya user dapat terus berinteraksi dengan program sampai user pilih menu exit.

5. Running program `<nama-student>_app.py` di `Anaconda Prompt` atau `Terminal MacOS/Linux` serta screenshot running program dan hasilnya.


**Contoh program interface:**

```
Selamat Datang di Keranjang Belanja Toko Makmur!

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 1
Masukan nama barang: Apel
Masukan harga: 3400
Barang "Apel" berhasil dimasukkan ke keranjang.

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 1
Masukan nama barang: Jeruk
Masukan harga: 2100
Barang "Jeruk" berhasil dimasukkan ke keranjang.

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 3
Barang di Keranjang:
0. Apel - Rp 3400.00
1. Jeruk - Rp 2100.00

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: tiga
Pilihannya salah. Coba lagi ya.

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 4
Total belanja: Rp 5500.00

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Pilihan: 2
Masukan nama barang yang ingin dihapus: Apel
Barang "Apel" berhasil dihapus di keranjang belanja.

Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit

Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.

```


---

## Assignment Rubrics

|**Key Component**|**Description**|**Points**|
|---|---|---|
|Functions|Siswa mampu menerapkan function berdasarkan kasus yang ingin diselesaikan|6 pts|
|Looping|Siswa mampu menerapkan looping sesuai dengan instruksi pada soal|6 pts|
|Conditional If|Mampu menerapkan conditional if dalam suatu kasus|6 pts|
|Runs Perfectly|Kode berialan tapa ada error. Seluruh kode berfungsi dan dibuat dengan benar.|2 pts|

**Total: 20 pts**

---
## Score Reduction

Jika Student terlambat mengumpulkan dengan waktu yang ditentukan, maka Graded Challenge akan diberi poin nol.

---
