from cryptography.fernet import Fernet


key = b'13SkL31jRAq9Qujdt2Pyfy4-ma1YPc2Tmp7NMi-2qtY='
token = b'gAAAAABk_1S2kDTDVPL2T9Up85MoGRHQK2XomfLIr9ImOhIACha9FghjMcq3hf3ddGjdaTd6X49DjJ1GK6qZAS_4c4UwT_3fs9XEYtW0ki19aO05_j45vyEB7sLtd7I0aS_7kKWcHrgw'


def my_token():
    return decrypt_text(token, key)


# Расшифровываем текст с помощью ключа
def decrypt_text(encrypted_text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text
