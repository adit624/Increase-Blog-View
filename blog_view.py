import os
import time
# Cek apakah requests sudah diinstal
try:
    import requests
except ImportError:
    print("Modul 'requests' belum diinstal. Menginstal sekarang...")
    os.system("pip install requests")
    import requests  # Import requests setelah menginstal

# Cek apakah fake_useragent sudah diinstal
try:
    from fake_useragent import UserAgent
except ImportError:
    print("Modul 'fake_useragent' belum diinstal. Menginstal sekarang...")
    os.system("pip install fake_useragent")
    from fake_useragent import UserAgent  # Import UserAgent setelah menginstal
#credit
text = '''

 ___________
< Bjorki199 >
 -----------			       /\      /
        \   ^__^  #github             /  \/\  /
         \  (oo)\_______           /\/      \/
            (__)\       )\/\      /    view
                ||----w |   \  /\/  blog  pov :v
                ||     ||    \/
==============="Made By Bjorki199"================
'''
print(text)
#deklarasi-input
blog_url = input("Masukkan url konten blog: ")
jumlah_permintaan = int(input("Masukkan jumlah view: "))
delay_waktu = int(input("Masukkan delay waktu: "))
user_agent = UserAgent()

for i in range(jumlah_permintaan):
    try:
        headers = {'User-Agent': user_agent.random}
        response = requests.get(blog_url, headers=headers)
        print(f"Permintaan ke-{i+1} berhasil dikirim dengan User Agent: {headers['User-Agent']}")
    except requests.exceptions.RequestException as e:
        print(f"Permintaan ke-{i+1} gagal: {e}")

    time.sleep(delay_waktu)
