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
  encrypted_message = [MORSE_CODE_DICT[letter] for letter in message]
  return ' '.join(encrypted_message)

def main():
  user_input = input('Please enter your input: ').upper()
  if user_input[0].isalnum():
    output = encrypt(user_input)
  else:
    output = decrypt(user_input)

  print(output)

if __name__ == "__main__":
  main()
    
#TEST = AYAM BEBEK
#TEST = .- -.-- .- -- / -... . -... . -.-
