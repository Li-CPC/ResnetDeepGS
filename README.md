# ResnetDeepGS
The format of the dataset directory is as follows:
--wheat
  --trait1
  --trait2
  --trait3
Run the model
python run.py --path=./小麦2000/FS --batch_size=32 --epoch_nums=200 --learn_rate=0.001 --k_folds=5 --seed=42
