## Instalasi

- Download atau melakukan git clone terhadap file github yang ada
    ```
    git clone https://github.com/MichaelKuswanto/Library-Chatbot.git
    ```

- Masuk ke dalam project yang sudah di download atau di gitclone

- Buka terminal lalu melakukan instalasi requirements (disarankan menggunakan virtual environment)
    ```
    pip install -r requirements.txt
    ```

- Jika direktori "models" kosong maka anda bisa melakukan rasa train dan rasa train nlu, jika ada maka langkah ini adalah langkah opsional
    ```
    rasa train
    rasa train nlu
    ```

## Pemakaian

- Buka aplikasi ngrok dan lakukan login dan autentikasi

- Setelah itu ketik ngrok http 5005 untuk mendapatkan link forwarding
    ```
    ngrok http 5005
    ```

- Copy link forwarding tersebut untuk di paste dalam kode file credentials.yml
    ```
    webhook_url: "<ngrok link>/webhooks/telegram/webhook"
    ```

- Ketik rasa run actions di satu terminal untuk mengaktifkan cutom actions (virtual environment disarankan)
    ```
    rasa run actions
    ```

- setelah selesai/berjalan buka terminal baru (virtual environment disarankan) lalu ketik
    ```
    rasa run
    ```

- setelah selesai/berjalan maka anda bisa bercakap dengan chatbot melalui link telegram dibawah ini:
    ```
    t.me/nrp043739_bot
    ```



## License

Project ini mengambil template dari https://github.com/shamspias/The-Rasa-Answer-Machine-GPT3.git
