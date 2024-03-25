# Port Scanner

Bu basit bir port tarayıcıdır. Belirtilen bir hedef IP adresine TCP portlarını taramak için kullanılır.

## Kullanım

1. Python kurulu cihazda `pip3 install -r requirements.txt` komutunu çalıştırın. Bu işlem`pyfiglet`, `socket` ve `datetime` kütüphanelerini yükleyecektir.
2. Terminalde `python port_scanner.py` komutunu çalıştırın.
3. Hedef IP adresini girin.
4. Port taraması başlayacak ve açık olan portlar listelenecektir.

## Nasıl Çalışır?

- Kullanıcıdan hedef IP adresi alınır.
- Belirtilen aralıktaki (1-1024) TCP portları tarar.
- Her port için bir soket oluşturur ve bağlantı denemesi yapar.
- Eğer bağlantı başarılıysa, o portun açık olduğunu ve hangi servisin çalıştığını belirtir.
- İşlem kullanıcı Ctrl+C ile kesilene kadar devam eder.

## Notlar

- Dikkat: Bu program sadece izin verilen sistemlerde ve ağlarda kullanılmalıdır. Aksi takdirde yasal sorunlara yol açabilir.
- Eğer herhangi bir hata alırsanız, programı yeniden başlatmayı deneyin veya hedefin erişilebilir olduğundan emin olun.
- Geliştirme ve geri bildirimler için iletişime geçebilirsiniz: [GitHub - Port Scanner](https://github.com/kutaykoca/port-scanner)