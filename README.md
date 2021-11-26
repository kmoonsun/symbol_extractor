# symbol_extractor
Extract the function name(symbol) from c/c++ source codes

It uses the AST of clang 6.0.0.

Parse function names from the result of 'clang -Xclang -ast-dump'.

```sh
python3 symbol_extractor.py
```
