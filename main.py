import tensorflow as tf
from config import args
import os
from utils import write_spec



if args.model == 'FCN':
    from model.FullyConvNet import FCN as Model
elif args.model == 'Tiramisu':
    from model.Tiramisu import Tiramisu as Model
elif args.model == 'Densenet':
    from model.DenseNet import DenseNet as Model
elif args.model == 'CNN':
    from model.My_CNN import CNN as Model



def main(_):
    if args.mode not in ['train', 'test', 'predict']:
        print('invalid mode: ', args.mode)
        print("Please input a mode: train, test, or predict")
    else:
        model = Model(tf.Session(), args)
        if not os.path.exists(args.modeldir+args.run_name):
            os.makedirs(args.modeldir+args.run_name)
        if not os.path.exists(args.logdir+args.run_name):
            os.makedirs(args.logdir+args.run_name)
        if args.mode == 'train':
            write_spec(args)
            if args.mask:
                model.load_mask()
            model.train()
        elif args.mode == 'test':
            model.test(step_num=args.step_num)


if __name__ == '__main__':
    # configure which gpu or cpu to use
    # os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1, 2, 3'
    tf.app.run()
