import pyrebase
firebaseConfig = {
    "apiKey": "AIzaSyBMiUhMCko3iKYzne7jJKaTlitSkzqI-Vg",
    "authDomain": "victor-bes-2020.firebaseapp.com",
    "databaseURL": "https://victor-bes-2020.firebaseio.com",
    "projectId": "victor-bes-2020",
    "storageBucket": "victor-bes-2020.appspot.com",
    "messagingSenderId": "820366940655",
    "appId": "1:820366940655:web:89036ccd5f851e884efe1a",
    "measurementId": "G-WD173L9R9P"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu usuário: ")
password = input("Digite sua senha: ")
loginStatus = auth.sign_in_with_email_and_password(user, password)
print("Sucesso:", loginStatus)
info = auth.get_account_info(loginStatus['idToken'])
print(info)
