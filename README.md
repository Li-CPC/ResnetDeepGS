# ResnetDeepGS
The format of the dataset directory is as follows:

**--wheat**

​		**--trait1**

​				**--pheno.csv**

​				**--RFE_1000.csv**

​		**--trait2**

​				**--pheno.csv**

​				**--RFE_1000.csv**

​		**--trait3**

​				**--pheno.csv**

​				**--RFE_1000.csv**

Run the model
`python run.py -p=./wheat/FS/ -bs=32 -epoch=200 -lr=0.001 -kf=5 -seed=42`

-path	dataset path

-bs	batchsize

-epoch	epoch numbers\

-lr	learn rate

-kf	k_folds

-seed	random seed

