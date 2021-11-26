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
```
[
	{
		"folder": [
			{
				"version": "file_name",
				"name": "interface.c",
				"symbols": [
					"_IO_getc",
					"getline",
					"popen"
					"_IO_vfscanf",
					"fdopen",
					"printf",
					"pclose",
          ...
```
