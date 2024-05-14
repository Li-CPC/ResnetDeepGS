from train_CV import train
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', type=str, default='./小麦2000/SVR_FS/')
    parser.add_argument('--batch_size', '-bs', type=int, default=32, help='Training batchszie, default: 32.')
    parser.add_argument('--epoch_nums', '-epoch', type=int, default=200, help='Training epochs, default: 200.')
    parser.add_argument('--learn_rate', '-lr', type=float, default=0.001, help='The second omics file name.')
    parser.add_argument('--k_folds', '-kf', type=int, default=5, help='folds of cross validation')
    parser.add_argument('--seed', '-seed', type=int, default=42, help='random seed')
    args = parser.parse_args()
    train(file_path=args.path,batch_size=args.batch_size,epoch_nums=args.epoch_nums,learn_rate=args.learn_rate,k_folds=args.k_folds,seed=args.seed)