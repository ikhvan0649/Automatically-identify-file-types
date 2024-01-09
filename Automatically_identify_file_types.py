import magic

# Jalankan fungsi 'detect_from_filename' untuk mengidentifikasi jenis file berdasarkan nama file
mime_type = magic.detect_from_filename('/content/drive/MyDrive/python/Untitled.txt')
print(f"Jenis file: {mime_type}")
