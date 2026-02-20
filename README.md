# Softmax-Load-Balancer
# Dağıtık Sistemler: Softmax Load Balancer Simülasyonu

Bu proje, bir sunucu kümesine gelen istekleri **Softmax Action Selection** algoritması kullanarak optimize eden bir istemci taraflı (client-side) yük dengeleyici simülasyonudur.

## 📌 Proje Amacı
Sunucuların performanslarının zamanla değiştiği (**non-stationary distribution**) bir ortamda, toplam bekleme süresini (latency) minimize ederek toplam ödülü (reward) maksimize etmek.

## 🛠️ Kullanılan Teknolojiler & Yöntemler
- **Dil:** Python 3.x
- **IDE:** Visual Studio Code
- **Model:** GPT-4o (Agentic Kodlama Yaklaşımı ile)
- **Algoritma:** Softmax Action Selection (Numerical Stability uygulanmıştır)

## 📊 Analiz Sonuçları
Simülasyon sonuçlarına göre Softmax algoritması, klasik Round-Robin yöntemine kıyasla toplam gecikme süresinde anlamlı bir iyileşme sağlamıştır.
- **Round-Robin Toplam Gecikme:** ~4659 ms
- **Softmax Toplam Gecikme:** ~3617 ms
- **İyileşme Oranı:** %22.3

## 🚀 Çalıştırma
Projeyi yerel makinenizde çalıştırmak için:
```bash
python load_balancer.py
