from morse import MORSE_CODE_DICT

def decrypt(morse_codes):
  separated_morse_codes = morse_codes.split()
  decrypted_message = [get_key(i) if i != '/' else ' ' for i in separated_morse_codes]
  return ''.join(decrypted_message)

def get_key(morse_code):
  for key, value in MORSE_CODE_DICT.items():
    if value == morse_code:
      return key
  return None

def encrypt(message):
  encrypted_message = [MORSE_CODE_DICT[letter] if letter in MORSE_CODE_DICT else '?' for letter in message]
  return ' '.join(encrypted_message)
  

def main():
  user_input = input('Please enter your input: ').upper()
  if any(True if i.isalnum() else False for i in list(user_input)):
    output = encrypt(user_input)
    print(f'Encrypted = {output}')
  else:
    output = decrypt(user_input)
    print(f'Decrypted = {output}')


if __name__ == "__main__":
  main()

