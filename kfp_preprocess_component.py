from kfp import dsl
import kfp




def preprocess_op():
    return dsl.ContainerOp(
        name = 'Preprocess Data',
        image = 'samyumobi99/rp:latest',
        arguments = [],
        file_outputs = {
            'x_train': '/app/xtrain.npyy',
            'x_test' : '/app/xtest.npy',
            'y_train': '/app/ytrain.npy',
            'y_test': '/app/ytest.npy'
        }
    )



