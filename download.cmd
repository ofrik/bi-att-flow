
set DATA_DIR=data
mkdir %DATA_DIR%

set SQUAD_DIR=%DATA_DIR%/squad
mkdir %SQUAD_DIR%
wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json -O %SQUAD_DIR%/train-v1.1.json
wget https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json -O %SQUAD_DIR%/dev-v1.1.json




set GLOVE_DIR=%DATA_DIR%/glove
mkdir %GLOVE_DIR%
wget http://nlp.stanford.edu/data/glove.6B.zip -O %GLOVE_DIR%/glove.6B.zip
