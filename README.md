# projetos_menores-py

## Codification.
### Caesar cipher (cifra_cesar.py)
Automates the encoding of Caesar cipher texts

#### How to use?
  ```python
  var = main(text="Hello! How you doing?", key=1, dir=True, up=True)
  ```

#### Parameters:
1. text (str):
  Text to encode.

2. key (int):
  Encoding key. Tells how many letters will be skipped at encoding time.

  Default: 1

  Example:
  ```python
  print(main(text="Hello", key=1))
  ```
  Output:
  ```text
  Ifmmp
  ```

  Because after "H", come "I"; after "e" come "f"; after "l" come "m" and after "o" come "p".

3. dir (bool):
  Is the direction in which the cipher will be applied.
  True is left to right and False is right to left.

  Default = True

  Example:
  ```python
  print(main(text="Hello", key=1, dir=True))
  ```
  
  Output:
  ```text
  Ifmmp
  ```

  But, if dir=False:
  ```python
  print(main(text="Hello", key=1, dir=False))
  ```

  Output:
  ```text
  Gdkkn
  ```

  Because before "H" is "G"; before "e" is "d"; before "l" is "k" and before "o" is "n".

4. up (bool):
  Says whether the code has capital letters or not.

  Default = True

  Example:
  ```python
  print(main(text="Hello Peter. How you doing?", key=1, dir=True, up=True))
  ```

  Output:
  ```text
  Ifmmp Qfufs. Ipx zpv epjoh?
  ```

  But, if up=False:
  ```python
  print(main(text="Hello Peter. How you doing?", key=1, dir=True, up=False))
  ```

  Output:
  ```text
  ifmmp qfufs. ipx zpv epjoh?
  ```

#### Return
The function main() always return a encode text (str).
Then, you can print this:
```python
print(main(...))
```

Or you can make a variable with this:
```python
text = "Hello World"
encode_text = main(text=text, ...)
```
