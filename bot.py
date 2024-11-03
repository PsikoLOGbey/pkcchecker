import random
import requests
import os  
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7219547492:AAGbldzqYtgP84qrnk7AFTbop7ldVHcmzok"

required_group = {"name": "CHAT GRUBUMUZA KATIL", "chat_id": -1001992204574, "link": "https://t.me/pkcarsivim"}
required_channel = {"name": "KANALIMIZA KATIL", "chat_id": -1002005734189, "link": "https://t.me/pkcarsivv"}

async def check_membership(context: ContextTypes.DEFAULT_TYPE, user_id, chat_id):
    try:
        member = await context.bot.get_chat_member(chat_id, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(f"Hata: {e}")
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or update.effective_user.first_name

    
    is_member_group = await check_membership(context, user_id, required_group["chat_id"])
    is_member_channel = await check_membership(context, user_id, required_channel["chat_id"])

    
    if not is_member_group or not is_member_channel:
        
        keyboard = [
            [InlineKeyboardButton("CHAT GRUBUMUZA KATIL", url=required_group["link"])],
            [InlineKeyboardButton("KANALIMIZA KATIL", url=required_channel["link"])]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        
        with open("image.jpg", "rb") as image:
            await update.message.reply_photo(
                photo=image,
                caption="Lütfen önce gerekli gruba ve kanala katılın.",
                reply_markup=reply_markup
            )
    else:
        
        await update.message.reply_text(
            f"PKC ᴄʜᴇᴄᴋᴇʀ\n"
            f"{username} Sorgu Botuna Hoş Geldin. Bu Bot, Sistemlerde Bulunan Verileri Analiz Etmene Yardımcı Olur Ve Tamamen Ücretsizdir!\n\n"
            "📮 Bu Sorguların Genel Olarak Sizlere Hitap Etmek Amacıyla Hazırlandığını Rica Ediyoruz ki Unutmayınız!\n"
            "🐱‍👤 Komutlar için /komutlar komutunu kullanın"
        )

# Ad-Soyad
async def adsoyad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if len(context.args) < 2:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /adsoyad Ad Soyad")
        return
    
    
    ad = context.args[0]
    soyad = context.args[1]

    
    url = f"https://api.tsgonline.net/tsgucretsizapi/adpro.php?auth=tsgxyunus&ad={ad}&soyad={soyad}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()  
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

    
    if api_data.get("success") and "data" in api_data:
        
        random_number = random.randint(100000, 999999)
        file_name = f"PKCChecker_{random_number}.txt"

         
        with open(file_name, "w") as file:
            for person_data in api_data["data"]:
                file.write("----- PKC Checker -----\n")
                file.write(f"ID: {person_data.get('ID')}\n")
                file.write(f"TC: {person_data.get('TC')}\n")
                file.write(f"AD: {person_data.get('AD')}\n")
                file.write(f"SOYAD: {person_data.get('SOYAD')}\n")
                file.write(f"GSM: {person_data.get('GSM')}\n")
                file.write(f"BABAADI: {person_data.get('BABAADI')}\n")
                file.write(f"BABATC: {person_data.get('BABATC')}\n")
                file.write(f"ANNEADI: {person_data.get('ANNEADI')}\n")
                file.write(f"ANNETC: {person_data.get('ANNETC')}\n")
                file.write(f"DOĞUM TARİHİ: {person_data.get('DOGUMTARIHI')}\n")
                file.write(f"ÖLÜM TARİHİ: {person_data.get('OLUMTARIHI')}\n")
                file.write(f"DOĞUM YERİ: {person_data.get('DOGUMYERI')}\n")
                file.write(f"MEMLEKET İL: {person_data.get('MEMLEKETIL')}\n")
                file.write(f"MEMLEKET İLÇE: {person_data.get('MEMLEKETILCE')}\n")
                file.write(f"MEMLEKET KÖY: {person_data.get('MEMLEKETKOY')}\n")
                file.write(f"ADRES İL: {person_data.get('ADRESIL')}\n")
                file.write(f"ADRES İLÇE: {person_data.get('ADRESILCE')}\n")
                file.write(f"AİLE SIRA NO: {person_data.get('AILESIRANO')}\n")
                file.write(f"BİREY SIRA NO: {person_data.get('BIREYSIRANO')}\n")
                file.write(f"MEDENİ HAL: {person_data.get('MEDENIHAL')}\n")
                file.write(f"CİNSİYET: {person_data.get('CINSIYET')}\n")
                file.write("----- t.me/pkcarsivv -----\n")
                file.write("\n")   
        
         
        with open(file_name, "rb") as file:
            await update.message.reply_document(InputFile(file), filename=file_name)

         
        os.remove(file_name)   
    else:
        await update.message.reply_text("Geçerli bir veri bulunamadı.")

 
async def adsoyadil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /adsoyadil Ad Soyad İl")
        return

    ad = context.args[0]
    soyad = context.args[1]
    il = context.args[2]

    url = f"https://api.tsgonline.net/tsgucretsizapi/adpro.php?auth=tsgxyunus&ad={ad}&soyad={soyad}&il={il}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

    if api_data.get("success") and "data" in api_data:
        random_number = random.randint(100000, 999999)
        file_name = f"PKCChecker_{random_number}.txt"

        with open(file_name, "w") as file:
            for person_data in api_data["data"]:
                file.write("----- PKC Checker -----\n")
                file.write(f"ID: {person_data.get('ID')}\n")
                file.write(f"TC: {person_data.get('TC')}\n")
                file.write(f"AD: {person_data.get('AD')}\n")
                file.write(f"SOYAD: {person_data.get('SOYAD')}\n")
                file.write(f"GSM: {person_data.get('GSM')}\n")
                file.write(f"BABAADI: {person_data.get('BABAADI')}\n")
                file.write(f"BABATC: {person_data.get('BABATC')}\n")
                file.write(f"ANNEADI: {person_data.get('ANNEADI')}\n")
                file.write(f"ANNETC: {person_data.get('ANNETC')}\n")
                file.write(f"DOĞUM TARİHİ: {person_data.get('DOGUMTARIHI')}\n")
                file.write(f"ÖLÜM TARİHİ: {person_data.get('OLUMTARIHI')}\n")
                file.write(f"DOĞUM YERİ: {person_data.get('DOGUMYERI')}\n")
                file.write(f"MEMLEKET İL: {person_data.get('MEMLEKETIL')}\n")
                file.write(f"MEMLEKET İLÇE: {person_data.get('MEMLEKETILCE')}\n")
                file.write(f"MEMLEKET KÖY: {person_data.get('MEMLEKETKOY')}\n")
                file.write(f"ADRES İL: {person_data.get('ADRESIL')}\n")
                file.write(f"ADRES İLÇE: {person_data.get('ADRESILCE')}\n")
                file.write(f"AİLE SIRA NO: {person_data.get('AILESIRANO')}\n")
                file.write(f"BİREY SIRA NO: {person_data.get('BIREYSIRANO')}\n")
                file.write(f"MEDENİ HAL: {person_data.get('MEDENIHAL')}\n")
                file.write(f"CİNSİYET: {person_data.get('CINSIYET')}\n")
                file.write("----- @pkcarsivv -----\n")
                file.write("\n")

        with open(file_name, "rb") as file:
            await update.message.reply_document(InputFile(file), filename=file_name)

        os.remove(file_name)
    else:
        await update.message.reply_text("Geçerli bir veri bulunamadı.")


# TCPRO
async def tcpro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if len(context.args) != 1:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /tcpro 11hanelitc")
        return
    
     
    tc = context.args[0]

     
    url = f"https://api.tsgonline.net/tsgucretsizapi/adpro.php?auth=tsgxyunus&tc={tc}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()   
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

     
    if api_data.get("success") and "data" in api_data:
        results = api_data["data"]
        response_text = "\n".join([
            f"----- PKC CHECKER -----\n\n"
            f"ID: {item.get('ID')}\n"
            f"TC: {item.get('TC')}\n"
            f"AD: {item.get('AD')}\n"
            f"SOYAD: {item.get('SOYAD')}\n"
            f"GSM: {item.get('GSM')}\n"
            f"BABAADI: {item.get('BABAADI')}\n"
            f"BABATC: {item.get('BABATC')}\n"
            f"ANNEADI: {item.get('ANNEADI')}\n"
            f"ANNETC: {item.get('ANNETC')}\n"
            f"DOĞUM TARİHİ: {item.get('DOGUMTARIHI')}\n"
            f"ÖLÜM TARİHİ: {item.get('OLUMTARIHI')}\n"
            f"DOĞUM YERİ: {item.get('DOGUMYERI')}\n"
            f"MEMLEKET İL: {item.get('MEMLEKETIL')}\n"
            f"MEMLEKET İLÇE: {item.get('MEMLEKETILCE')}\n"
            f"MEMLEKET KÖY: {item.get('MEMLEKETKOY')}\n"
            f"ADRES İL: {item.get('ADRESIL')}\n"
            f"ADRES İLÇE: {item.get('ADRESILCE')}\n"
            f"AİLE SIRA NO: {item.get('AILESIRANO')}\n"
            f"BİREY SIRA NO: {item.get('BIREYSIRANO')}\n"
            f"MEDENİ HAL: {item.get('MEDENIHAL')}\n"
            f"CİNSİYET: {item.get('CINSIYET')}\n"
            f"----- t.me/pkcarsivv -----\n"
            for item in results
        ])
        await update.message.reply_text(response_text)
    else:
        await update.message.reply_text("Geçerli bir veri bulunamadı.")

# Aile
async def aile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /aile 11hanelitc")
        return

    tc = context.args[0]

    url = f"https://api.tsgonline.net/tsgucretsizapi/aile.php?tc={tc}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

    if api_data.get("success") and "data" in api_data:
        random_number = random.randint(100000, 999999)
        file_name = f"Aile_Sorgulama_{random_number}.txt"

        with open(file_name, "w") as file:
            for family_member in api_data["data"]:
                file.write("----- PKC CHECKER -----\n")
                file.write(f"ID: {family_member.get('ID')}\n")
                file.write(f"TC: {family_member.get('TC')}\n")
                file.write(f"AD: {family_member.get('AD')}\n")
                file.write(f"SOYAD: {family_member.get('SOYAD')}\n")
                file.write(f"GSM: {family_member.get('GSM')}\n")
                file.write(f"BABAADI: {family_member.get('BABAADI')}\n")
                file.write(f"BABATC: {family_member.get('BABATC')}\n")
                file.write(f"ANNEADI: {family_member.get('ANNEADI')}\n")
                file.write(f"ANNETC: {family_member.get('ANNETC')}\n")
                file.write(f"DOĞUM TARİHİ: {family_member.get('DOGUMTARIHI')}\n")
                file.write(f"ÖLÜM TARİHİ: {family_member.get('OLUMTARIHI')}\n")
                file.write(f"DOĞUM YERİ: {family_member.get('DOGUMYERI')}\n")
                file.write(f"MEMLEKET İL: {family_member.get('MEMLEKETIL')}\n")
                file.write(f"MEMLEKET İLÇE: {family_member.get('MEMLEKETILCE')}\n")
                file.write(f"MEMLEKET KÖY: {family_member.get('MEMLEKETKOY')}\n")
                file.write(f"ADRES İL: {family_member.get('ADRESIL')}\n")
                file.write(f"ADRES İLÇE: {family_member.get('ADRESILCE')}\n")
                file.write(f"AİLE SIRA NO: {family_member.get('AILESIRANO')}\n")
                file.write(f"BİREY SIRA NO: {family_member.get('BIREYSIRANO')}\n")
                file.write(f"MEDENİ HAL: {family_member.get('MEDENIHAL')}\n")
                file.write(f"CİNSİYET: {family_member.get('CINSIYET')}\n")
                file.write("----- t.me/pkcarsivv -----\n")
                file.write("\n")

        with open(file_name, "rb") as file:
            await update.message.reply_document(InputFile(file), filename=file_name)

        os.remove(file_name)
    else:
        await update.message.reply_text("Geçerli bir veri bulunamadı.")

# Sulale
async def sulale(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /sulale 11hanelitc")
        return

    tc = context.args[0]

    url = f"https://api.tsgonline.net/tsgucretsizapi/sulale.php?tc={tc}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

    if api_data.get("success") and "data" in api_data:
        random_number = random.randint(100000, 999999)
        file_name = f"PKCCHECKER_{random_number}.txt"

        with open(file_name, "w") as file:
            for family_member in api_data["data"]:
                file.write("----- PKC CHECKER -----\n")
                file.write(f"ID: {family_member.get('ID')}\n")
                file.write(f"TC: {family_member.get('TC')}\n")
                file.write(f"AD: {family_member.get('AD')}\n")
                file.write(f"SOYAD: {family_member.get('SOYAD')}\n")
                file.write(f"GSM: {family_member.get('GSM')}\n")
                file.write(f"BABAADI: {family_member.get('BABAADI')}\n")
                file.write(f"BABATC: {family_member.get('BABATC')}\n")
                file.write(f"ANNEADI: {family_member.get('ANNEADI')}\n")
                file.write(f"ANNETC: {family_member.get('ANNETC')}\n")
                file.write(f"DOĞUM TARİHİ: {family_member.get('DOGUMTARIHI')}\n")
                file.write(f"ÖLÜM TARİHİ: {family_member.get('OLUMTARIHI')}\n")
                file.write(f"DOĞUM YERİ: {family_member.get('DOGUMYERI')}\n")
                file.write(f"MEMLEKET İL: {family_member.get('MEMLEKETIL')}\n")
                file.write(f"MEMLEKET İLÇE: {family_member.get('MEMLEKETILCE')}\n")
                file.write(f"MEMLEKET KÖY: {family_member.get('MEMLEKETKOY')}\n")
                file.write(f"ADRES İL: {family_member.get('ADRESIL')}\n")
                file.write(f"ADRES İLÇE: {family_member.get('ADRESILCE')}\n")
                file.write(f"AİLE SIRA NO: {family_member.get('AILESIRANO')}\n")
                file.write(f"BİREY SIRA NO: {family_member.get('BIREYSIRANO')}\n")
                file.write(f"MEDENİ HAL: {family_member.get('MEDENIHAL')}\n")
                file.write(f"CİNSİYET: {family_member.get('CINSIYET')}\n")
                file.write("----- t.me/pkcarsivv -----\n")
                file.write("\n")

        with open(file_name, "rb") as file:
            await update.message.reply_document(InputFile(file), filename=file_name)

        os.remove(file_name)
    else:
        await update.message.reply_text("Geçerli bir veri bulunamadı.")

    # Adres 
async def adres(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /adres 11hanelitc")
        return

    tc = context.args[0]

    url = f"https://api.tsgonline.net/tsgucretsizapi/adres.php?tc={tc}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

    if api_data.get("success") and "data" in api_data:
        adres_bilgileri = api_data["data"]
        mesaj = (
            f"----- PKC CHECKER -----\n"
            f"TC: {adres_bilgileri.get('TC')}\n"
            f"ADSOYAD: {adres_bilgileri.get('ADSOYAD')}\n"
            f"DOĞUM YERİ: {adres_bilgileri.get('DOGUMYERI')}\n"
            f"VERGİ NO: {adres_bilgileri.get('VERGINO')}\n"
            f"ADRES: {adres_bilgileri.get('ADRES')}\n"
            f"----- t.me/pkcarsivv -----\n"
        )
        await update.message.reply_text(mesaj)
    else:
        await update.message.reply_text("Geçerli bir veri bulunamadı.")

# Apartman 
async def apartman(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /apartman 11hanelitc")
        return

    tc = context.args[0]

    url = f"https://api.tsgonline.net/tsgucretsizapi/apartman.php?tc={tc}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

    if api_data.get("success") and "data" in api_data:
        apartman_bilgileri = api_data["data"]
        
         
        txt_metin = f"----- PKC CHECKER -----\n" \
                    f"TC: {apartman_bilgileri.get('TC')}\n" \
                    f"ADSOYAD: {apartman_bilgileri.get('ADSOYAD')}\n" \
                    f"DOĞUM YERİ: {apartman_bilgileri.get('DOGUMYERI')}\n" \
                    f"VERGİ NO: {apartman_bilgileri.get('VERGINO')}\n" \
                    f"ADRES: {apartman_bilgileri.get('ADRES')}\n" \
                    f"TSG: {apartman_bilgileri.get('tsg')}\n" \
                    f"\nApartmandakiler:\n"

        for sakin in apartman_bilgileri.get('Apartmandakiler', []):
            txt_metin += (f"TC: {sakin.get('TC')}\n"
                           f"ADSOYAD: {sakin.get('ADSOYAD')}\n"
                           f"DOĞUM YERİ: {sakin.get('DOGUMYERI')}\n"
                           f"VERGİ NO: {sakin.get('VERGINO')}\n"
                           f"ADRES: {sakin.get('ADRES')}\n\n")

         
        file_path = "PKCCHECKER_Apartman.txt"
        with open(file_path, "w", encoding='utf-8') as file:
            file.write(txt_metin)

         
        with open(file_path, "rb") as file:
            await update.message.reply_document(file)

         
        os.remove(file_path)

    else:
        await update.message.reply_text("Geçerli bir veri bulunamadı.")

# GSM TC 
async def gsmtc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /gsmtc 10hanelitelefonnumarasi")
        return

    gsm = context.args[0]

    url = f"https://api.tsgonline.net/tsgucretsizapi/gsmtc.php?gsm={gsm}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

    if api_data.get("success") and "data" in api_data:
        gsmtc_bilgileri = api_data["data"]

         
        mesaj = "GSM TC Bilgileri:\n"
        for veri in gsmtc_bilgileri:
            mesaj += (f"----- PKC CHECKER -----\n"
                      f"ID: {veri.get('ID')}\n"
                      f"TC: {veri.get('TC')}\n"
                      f"GSM: {veri.get('GSM')}\n\n")

        await update.message.reply_text(mesaj.strip())
    else:
        await update.message.reply_text("Geçerli bir veri bulunamadı.")

# TC GSM 
async def tcgsm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /tcgsm 11hanelitc")
        return

    tc = context.args[0]

    url = f"https://api.tsgonline.net/tsgucretsizapi/tcgsm.php?tc={tc}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

    if api_data.get("success") and "data" in api_data:
        tcgsm_bilgileri = api_data["data"]

         
        mesaj = "TC GSM Bilgileri:\n"
        for veri in tcgsm_bilgileri:
            mesaj += (f"----- PKC CHECKER -----\n"
                      f"ID: {veri.get('ID')}\n"
                      f"TC: {veri.get('TC')}\n"
                      f"GSM: {veri.get('GSM')}\n\n")

        await update.message.reply_text(mesaj.strip())
    else:
        await update.message.reply_text("Geçerli bir veri bulunamadı.")

# IP  
async def ip_sorgula(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("Lütfen komutu şu formatta kullanın: /ip ip_adresi")
        return

    ip_adresi = context.args[0]
    
    url = f"https://ipapi.co/{ip_adresi}/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        await update.message.reply_text("API isteğinde bir hata oluştu.")
        print(f"Hata: {e}")
        return

    if api_data.get("ip"):
        mesaj = (
            f"----- PKC CHECKER -----\n"
            f"IP Bilgileri:\n"
            f"IP: {api_data.get('ip')}\n"
            f"Ağ: {api_data.get('network')}\n"
            f"Versiyon: {api_data.get('version')}\n"
            f"Şehir: {api_data.get('city')}\n"
            f"Region: {api_data.get('region')}\n"
            f"Ülke: {api_data.get('country_name')} ({api_data.get('country_code')})\n"
            f"Zaman Dilimi: {api_data.get('timezone')}\n"
            f"Enlem: {api_data.get('latitude')}\n"
            f"Boylam: {api_data.get('longitude')}\n"
            f"Nüfus: {api_data.get('country_population')}\n"
            f"Örgüt: {api_data.get('org')}\n"
        )
        await update.message.reply_text(mesaj.strip())
    else:
        await update.message.reply_text("Geçerli bir IP adresi bulunamadı.")



 
async def komutlar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    komut_listesi = (
        "📜 *Kullanılabilir Komutlar:*\n\n"
        "/start - Botu başlatır ve ana mesaja yönlendirir.\n"
        "/komutlar - Tüm mevcut komutların listesini gösterir.\n"
        "/adsoyad AD SOYAD - Kişinin ad soyadından sorgular.\n"
        "/adsoyadil AD SOYAD İL - Kişinin ad soyad ilinden sorgular.\n"
        "/tcpro TC - Kişinin tcsinden sorgular.\n"
        "/aile TC - Kişinin tcsinden ailesini sorgular.\n"
        "/sulale TC - Kişinin tcsinden sulalesini sorgular.\n"
        "/adres TC - Kişinin tcsinden adresini sorgular.\n"
        "/apartman TC - Kişinin tcsinden aparmanında bulunan kişileri sorgular.\n"
        "/gsmtc GSM - Kişinin telefon numarasından tcsini sorgular.\n"
        "/tcgsm TC - Kişinin tcsinden üzerine kayıtlı telefon numaralarını sorgular.\n"
    )
    await update.message.reply_text(komut_listesi, parse_mode="Markdown")

 
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("komutlar", komutlar))
app.add_handler(CommandHandler("adsoyad", adsoyad))
app.add_handler(CommandHandler("adsoyadil", adsoyadil))
app.add_handler(CommandHandler("tcpro", tcpro))
app.add_handler(CommandHandler("aile", aile))
app.add_handler(CommandHandler("sulale", sulale))
app.add_handler(CommandHandler("adres", adres))
app.add_handler(CommandHandler("apartman", apartman))
app.add_handler(CommandHandler("gsmtc", gsmtc))
app.add_handler(CommandHandler("tcgsm", tcgsm))
app.add_handler(CommandHandler("ip", ip_sorgula))

app.run_polling()
