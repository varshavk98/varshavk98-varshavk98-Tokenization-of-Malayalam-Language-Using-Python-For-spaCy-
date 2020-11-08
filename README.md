# varshavk98-varshavk98-Tokenization-of-Malayalam-Language-Using-Python-For-spaCy-

IMPLEMENTATION

1.0 Inorder to implement spacy in Malayalam:

   1. Create dataset for Malayalam like stopwords, lexical attributes (stopwords.py, lex_attrs.py).
    
   2. Create a file init.py which contains Malayalam class definition and import all the necessary files to implement nlp.
    
   3. Create a file examples.py which contains set of Malayalam sentences.
    
   4. Cythonize all the 4 files. After cythonization we will get a copy of all files in .so format.
    
   5. pycache contains copy of files like stopwords,lexical attributes, examples, init in pyc format.
    
   6. Execute examples.py.
    
   7. Import Malayalam language package in jupyter notebook to do tokenization.

1.1 Stopwords Stopwords are the Malayalam words which does not add much meaning to a sentence. They can safely be ignored without sacrificing the meaning of the sentence. For example, the words like the, he, have etc.

1.2 Lexical Attributes spaCy includes a collection of functions that can identify whether a token has some specific attributes. For example, it is a URL!

1.3 _init _.py Python defines two types of packages, regular packages and namespace packages. Regular packages are traditional packages as they existed in Python 3.2 and earlier. A regular package is typically implemented as a directory containing an init.py file. When a regular package is imported, this init.py file is implicitly executed, and the objects it defines are bound to names in the package’s namespace. The init.py file can contain the same Python code that any other module can contain, and Python will add some additional attributes to the module when it is imported.

1.4 Cython Cython is an optimising static compiler for both the python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as Python itself.

1.5 pycache When you run a program in python, the interpreter compiles it to bytecode first (this is an oversimplification) and stores it in the pycache folder. If you look in there you will find a bunch of files sharing the names of the .py files in your project's folder, only their extensions will be either .pyc or .pyo. These are bytecode-compiled and optimized bytecode-compiled versions of your program's files, respectively.
