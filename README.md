# symbol_extractor
Extract the function name(symbol) from c/c++ source codes

It uses the AST of clang 6.0.0.

Parse function names from the result of ```clang -Xclang -ast-dump``` provided by clang.

## Running
```sh
python3 symbol_extractor.py [folder]
```

## Result
The result is stored in ```symbol.json```
![image](https://user-images.githubusercontent.com/48425176/143532611-db74d1db-1f59-483e-ac89-87dc62328b65.png)
