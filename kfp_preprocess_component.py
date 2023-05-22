from kfp import dsl
import kfp




def preprocess_op():
    return dsl.ContainerOp(
        name = 'Preprocess Data',
        image = 'samyumobi99/rp:latest',
        arguments = [],
        file_outputs = {
            'x_train': '/app/x_train.npy',
            'x_test' : '/app/x_test.npy',
            'y_train': '/app/y_train.npy',
            'y_test': '/app/y_test.npy'
        }
    )



