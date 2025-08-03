# Jettpass_local
## In English (short) 
**Jettpass** is a local, offline password manager with encryption and GUI.  
It works on Windows 10 and Linux Mint (tested). 

### Features:
- Store encrypted password entries
- Add, edit, delete, search entries
- AES-GCM encryption for passwords
- Password generator (8–50 characters)
- Change master password anytime

### Run:
```bash
cd path/to/project/
pip install -r requirements.txt
python -m views.Main_and_log_in
```
All data is stored locally in binary files.
Master password is hashed with SHA512 + salt.
Password entries are encrypted with AES-GCM.

## Українською
Щоб запустити: 
```bash
cd path/to/project/
pip install -r requirements.txt
python -m views.Main_and_log_in
```

  Програма являє собою менеджер паролів, котрий працює локально на вашому пристрої. Додаток сумісний з Windows 10 і Linux Mint (протестовано). 
  <br></br>
 <div align="center">
  <img width="451" height="429" alt="image" src="https://github.com/user-attachments/assets/3d82dca9-9dd5-49db-951a-72e3ffd211dd" />
</div>
<br></br>
  Щоб почати використання слід спершу створити свій локальний обліковий запис в додатку. Слід ввести login та пароль. Головний пароль (Master password) має бути довжиною мінімум 15 символів, містити в собі літери англійського алфавіту у верхньому і нижньому регістрі, як мінімум 1 цифру, 1 спеціальний символ наприклад: !»;%:?*)(_+@#$^&  .
  <br></br>
<div align="center">
<img width="500" height="356" alt="image" src="https://github.com/user-attachments/assets/cc52c64a-f709-4591-92fb-8e8323df000d" /> <img width="451" height="427" alt="image" src="https://github.com/user-attachments/assets/8b740606-4dd8-49d5-880a-5695dc2843c5" />
</div>
<br></br>
Після успішного входу в свій обліковий запис можна створювати нові записи для паролів, видаляти  та редагувати наявні, шукати записи за допомогою пошукового рядку, міняти master password, генерувати надійні паролі.

Структура запису паролю:
- Alias - «псевдонім запису» щоб легко знаходити запис серед інших
- Login / email — login або електронна пошта, якої стосується пароль у записі
- Password — пароль від потрібного вам ресурсу, який ви хочете записати, щоб не забути.
<br></br>
<div align="center">
<img width="599" height="495" alt="image_2025-08-03_12-22-41" src="https://github.com/user-attachments/assets/e0649f38-981c-4df3-8ec3-339bfd61938b" /> 
</div>
<br></br>
<div align="center">
<img width="800" height="594" alt="image" src="https://github.com/user-attachments/assets/25a4177f-3ef7-447d-807e-9ccceeeb25ec" />
</div>
<br></br>
Генератор:
  Є можливість генерувати паролі довжиною від 8 до 50 символів (рекомендовано від 15-ти символів). Згенеровані паролі відповідають вимогам master password, описаним вище.
<br></br>
<div align="center">
  <img width="495" height="298" alt="image_2025-08-03_12-25-58" src="https://github.com/user-attachments/assets/2805a526-c502-4256-bd36-fa126472884a" />
</div>
<br></br>
Сховище:
  Вся інформація записується в бінарний файл з назвою [user].dump, де user — ім’я, вказане вами при створенні облікового запису в додатку. Всі записи ваших паролів зашифровані. Інформація про облікові записи (в тому числі хеш + salt) зберігається в users.jett.

Безпека:
  Для хешування головного паролю (master password) використовується sha512 — досить надійна хеш функція + випадкові salt bytes.
Для шифрування у [user].dump файлі використовується AES у режимі GCM.
