def pin_extractor(poems:list[str]) ->list[str]:
    secret_codes = []
    for a_poem in poems:
        secret_code = ''
        lines = a_poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

if __name__ =="__main__":


  poem = """Stars and the moon
  shine in the sky
  white and
  until the end of the night"""

  poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
  poem3 = 'There\nonce\nwas\na\ndragon'
  for num,i in  enumerate(pin_extractor ([poem,poem2,poem3])):
   print(f"hidden secret digit {i} of the {num} poem.")
