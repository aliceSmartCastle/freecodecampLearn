def encrypt_literal(origin_iteral: str, encrypt_addition: int = 5, to_secret: bool = True):

    if not isinstance(encrypt_addition, int):
        return "the encrypt addition must be integer"
    if encrypt_addition < 1 or encrypt_addition > 25:
        return "the encrypt addition must be between 1 and 25"
    if not to_secret:
        encrypt_addition = -encrypt_addition
    alphabet = ''.join([chr(i) for i in range(97, 123)])
    cut_alphabet = alphabet[encrypt_addition:] + alphabet[0:encrypt_addition]
    using_mapping = ''.maketrans(alphabet.upper() + alphabet, cut_alphabet.upper() + cut_alphabet)
    return origin_iteral.translate(using_mapping)


def encrypt(text: str, offset: int = 5) -> str:
    return encrypt_literal(origin_iteral=text, encrypt_addition=offset)


def decrypt(text: str, offset:int = 5 ) -> str:
    return encrypt_literal(origin_iteral=text, encrypt_addition=offset, to_secret=False)


if __name__ == "__main__":
    print(encrypt(text="Python is awesome language !"))
