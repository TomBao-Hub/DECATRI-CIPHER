# DecaTri Cipher

> A small experimental cipher made for fun, learning, and cryptography experiments.

**DecaTri** is a custom cipher that encodes text into groups of three digits.

## How does it work?

DecaTri uses the 10 digits from `0` to `9` to create **120 unique combinations of 3 different digits**.

Each character is assigned to one of these combinations.

For example:

```text
a → 037
b → 581
c → 246
...
```

Before being written to the ciphertext, the three digits can be shuffled:

```text
037 → 703
581 → 815
246 → 624
```

During decryption, the digits are sorted again to recover the original code.

The character mapping is randomly generated and stored in a key file.

## Features

* 3-digit cipher codes
* Random character-to-code mapping
* Digit order can be shuffled
* Optional fake/noise codes
* Supports uppercase letters
* Supports spaces and common punctuation
* Custom key file
* Simple Python implementation

## Example

Plaintext:

```key
BaoTom
```

```text
Hello! My name is BaoTom.
```

DecaTri:

```text
772 372 150 113 306 080 798 166 798 659 608 424 460 237 316 907 640 626 243 248 163 991 603 766 640 238 856 640 372 439 842 659 327 624 569 544 361 665 286
```
or
```
772372150113306080798166798659608424460237316907640626243248163991603766640238856640372439842659327624569544361665286 
```

The exact ciphertext depends on the generated key and random digit shuffling.

## Important

DecaTri is an **experimental and educational cipher**.

It is **not intended to provide modern cryptographic security** and should not be used to protect sensitive information.

The project is mainly for learning, experimentation, and having fun with cryptography.

## License

DecaTri is released under the **MIT License**.

Feel free to study, modify, fork, and experiment with the code.
